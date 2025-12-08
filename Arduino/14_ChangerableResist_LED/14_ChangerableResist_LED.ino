// 가변 저항 모듈을 사용해도 저항을 사용 하는 이유 = 1023 byte로 출력 시, LED가 탈 수 있기 때문에 보호하기 위함

const int LED_PIN = 10;
// delay를 없애 반응성을 더 좋게 개선
const unsigned long INTERVAL = 100;
unsigned long prevMillis = 0;

void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  
  unsigned long now = millis();

  if (now - prevMillis >= INTERVAL) {
    prevMillis = now;

    int sensor = analogRead(A0);
    byte pwm = sensor >> 2; // pwm = map(sensor, 0, 1023, 0, 255);
                            // map() 내장함수 : 입력값(0~1023)을 출력값(0~255)로 변환

    Serial.println(sensor);
    analogWrite(LED_PIN, pwm);
  }

  // 여기서 다른 작업들(버튼 체크, 센서 추가 등) 계속 가능
}
