/*
  기능 요약
  1) 주기적으로 온습도 + 가스 센서(AO/DO) 출력
  2) 가스 센서 값에 따라 RED / GREEN / BLUE LED 상태 결정
  3) 연기(위험) 상태에서, 초음파 센서로 5cm 이내 접근 시 RED LED를 0.1초 간격으로 깜빡임
  4) 연기 + 5cm 이내 + 택트 스위치 누름 → 피에조 부저는 스위치에 직접 연결되어 울림,
     아두이노는 조건 만족시 시리얼에 경고 메시지 출력
*/

// DHT 센서
#include "DHT.h"
#define DHTPIN 5
#define DHTTYPE DHT22
DHT myDHT(DHTPIN, DHTTYPE);

// 초음파 센서
#define ECHO 6
#define TRIG 7

// LED
#define LED_RED   2
#define LED_GREEN 3
#define LED_BLUE  4

// 택트 스위치 (피에조는 스위치 쪽에 직접 연결)
#define TACT_FIEZO 9 

// 가스 센서
#define GAS_A A0
#define GAS_D 8

// ── 음계 정의 (필요한 것만) ──
#define NOTE_C4  262
#define NOTE_D4  294
#define NOTE_E4  330
#define NOTE_G4  392
#define NOTE_A4  440
#define NOTE_AS4 466
#define NOTE_B4  494

#define NOTE_C5  523
#define NOTE_D5  587
#define NOTE_DS5 622
#define NOTE_E5  659
#define NOTE_GS4 415   // G#4
#define NOTE_GS5 831   // G#5 (조금 높은 느낌)

// 시간 관리용 상수
const unsigned long DHT_GAS_INTERVAL   = 2000;   // 온습도/가스 센서 읽기 주기 (ms)
const unsigned long ULTRA_INTERVAL     = 100;    // 초음파 센서 갱신 주기 (ms)
const unsigned long RED_BLINK_INTERVAL = 100;    // 빨간 LED 깜빡임 간격 (0.1초)

// 시간 저장용 변수
unsigned long lastDhtGasTime   = 0;
unsigned long lastUltraTime    = 0;
unsigned long lastBlinkToggle  = 0;

// 센서 상태 저장 변수
float  h = 0, c = 0, f = 0;
int    sensorValue = 0;      // 가스 AO
int    sensorDValue = 0;     // 가스 DO
float  distanceCm = 9999.0;  // 초음파 거리

// 상태 플래그
bool hasSmoke  = false;  // 연기 발생 (위험)
bool preSmoke  = false;  // 연기 전조 상태
bool redBlinkState = false; // 깜빡임 상태 저장

// Für Elise 메인 테마(간략) – E5 D#5 E5 D#5 E5 B4 D5 C5 A4 ...
int melody[] = {
  // 1구절
  NOTE_E5, NOTE_DS5, NOTE_E5, NOTE_DS5, NOTE_E5, NOTE_B4, NOTE_D5, NOTE_C5, NOTE_A4,
  NOTE_C4, NOTE_E4, NOTE_A4, NOTE_B4,
  NOTE_E4, NOTE_GS4, NOTE_B4, NOTE_C5,

  // 2구절 (첫 구절과 비슷하게 반복)
  NOTE_E5, NOTE_DS5, NOTE_E5, NOTE_DS5, NOTE_E5, NOTE_B4, NOTE_D5, NOTE_C5, NOTE_A4,
  NOTE_C4, NOTE_E4, NOTE_A4, NOTE_B4,
  NOTE_E4, NOTE_C5, NOTE_B4, NOTE_A4
};

// 각 음 길이 (ms 단위) – 전체 합이 대략 15초 정도 되도록 조절
int noteDurations[] = {
  // 1구절
  200, 200, 200, 200, 200, 200, 200, 200, 400,
  200, 200, 200, 400,
  200, 200, 200, 600,

  // 2구절
  200, 200, 200, 200, 200, 200, 200, 200, 400,
  200, 200, 200, 400,
  200, 200, 200, 800
};

const int NUM_NOTES = sizeof(melody) / sizeof(melody[0]);
// 음과 음 사이의 작은 쉼 (ms)
const int GAP = 50;

void playFurEliseOnce() {
  for (int i = 0; i < NUM_NOTES; i++) {
    int freq = melody[i];
    int dur  = noteDurations[i];

    tone(TACT_FIEZO, freq, dur);
    delay(dur + GAP);   // 음이 다 끝날 때까지 + 약간 쉼
  }
  noTone(TACT_FIEZO);
}

void setup() {
  Serial.begin(9600);
  myDHT.begin();
  Serial.println("센서 작동!!");

  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);

  pinMode(LED_RED, OUTPUT);
  pinMode(LED_BLUE, OUTPUT);
  pinMode(LED_GREEN, OUTPUT);

  pinMode(TACT_FIEZO, INPUT_PULLUP); // 스위치: 눌림=LOW
  pinMode(GAS_D, INPUT);             // 가스 DO 디지털 입력
}

void loop() {
  unsigned long now = millis();

  // 1) 온습도 + 가스 센서 읽기 (2초마다)
  if (now - lastDhtGasTime >= DHT_GAS_INTERVAL) {
    lastDhtGasTime = now;

    h = myDHT.readHumidity();
    c = myDHT.readTemperature();
    f = myDHT.readTemperature(true);

    sensorValue   = analogRead(GAS_A);
    sensorDValue  = digitalRead(GAS_D);

    if (isnan(h) || isnan(c) || isnan(f)) {
      Serial.println("DHT 측정을 실패하였습니다.");
    } else {
      Serial.print("* 습도: ");
      Serial.print(h);
      Serial.print("%  |  섭씨: ");
      Serial.print(c);
      Serial.print("°C  |  화씨: ");
      Serial.print(f);
      Serial.println("°F");
    }

    Serial.print("* 가스 센서 AO: ");
    Serial.print(sensorValue);
    Serial.print("  |  DO: ");
    Serial.println(sensorDValue);

    // 연기 상태 판별
    hasSmoke = (sensorValue > 600 || sensorDValue == 0);
    preSmoke = (!hasSmoke && sensorValue > 300);
  }

  // 2) 초음파 센서로 거리 측정 (0.1초마다)
  if (now - lastUltraTime >= ULTRA_INTERVAL) {
    lastUltraTime = now;

    digitalWrite(TRIG, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG, LOW);

    unsigned long duration = pulseIn(ECHO, HIGH, 30000); // 타임아웃 30ms
    if (duration == 0) {
      // 측정 실패 시 큰 값으로 처리
      distanceCm = 9999.0;
    } else {
      distanceCm = ((34000.0 * duration) / 1000000.0) / 2.0;
    }

    Serial.print("거리: ");
    Serial.print(distanceCm);
    Serial.println(" cm");
  }

  // 3) 기본 LED 상태 (RED는 아래에서 별도 처리)
  if (hasSmoke) {
    // 위험: 빨간 LED만 사용, 나머지는 꺼둔다
    digitalWrite(LED_GREEN, LOW);
    digitalWrite(LED_BLUE, LOW);
  } else if (preSmoke) {
    // 연기 조짐: GREEN ON
    digitalWrite(LED_GREEN, HIGH);
    digitalWrite(LED_BLUE, LOW);
    digitalWrite(LED_RED, LOW);
    redBlinkState = false;
  } else {
    // 안전: BLUE ON
    digitalWrite(LED_BLUE, HIGH);
    digitalWrite(LED_GREEN, LOW);
    digitalWrite(LED_RED, LOW);
    redBlinkState = false;
  }

  // 4) 빨간 LED 제어 (연기 상태일 때만)
  if (hasSmoke) {
    if (distanceCm < 5.0) {
      // 5cm 이내 접근 → 0.1초 간격으로 깜빡이기
      if (now - lastBlinkToggle >= RED_BLINK_INTERVAL) {
        lastBlinkToggle = now;
        redBlinkState = !redBlinkState;
        digitalWrite(LED_RED, redBlinkState ? HIGH : LOW);
      }
    } else {
      // 연기만 있고 사람은 멀리 → RED 계속 ON
      digitalWrite(LED_RED, HIGH);
      redBlinkState = true;
    }
  }

  // 5) 택트 스위치 + 피에조 부저 조건
  // (피에조는 스위치에 직접 연결되어 있어서, 아두이노는 스위치 눌림만 감지)
  int swState = digitalRead(TACT_FIEZO); // 눌림 = LOW (INPUT_PULLUP)

  if (hasSmoke && distanceCm < 5.0 && swState == LOW) {
    Serial.println("※ 경고: 연기 + 근접 + 스위치 눌림 → 피에조 부저 ON 상태 (하드웨어 직접 연결)");
    playFurEliseOnce();
  }
// (delay 없음, 모든 타이밍은 millis로 제어)
}
