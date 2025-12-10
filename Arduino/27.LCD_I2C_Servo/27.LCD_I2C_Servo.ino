/*
  가변 저항을 이용하여 서보 모터를 제어하고,
  서보 모터의 각도 값을 I2C LCD에 출력하는 예제

  - A0에 연결된 가변 저항 값(0~1023)을 읽어서
    0~180도의 각도로 변환한 뒤 서보 모터(8번 핀)에 전달한다.
  - 현재 서보 각도는 LCD(16x2)에 실시간으로 표시한다.
*/

#include <Servo.h>
#include <LiquidCrystal_I2C.h>

// ───────────────────── 상수 & 객체 선언 ─────────────────────

// 핀 번호 상수
const int POT_PIN   = A0;  // 가변 저항 가운데 핀
const int SERVO_PIN = 8;   // 서보 모터 제어 핀

// 서보 객체
Servo servo;

// I2C LCD 객체 (주소 0x27, 16x2)
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  // 시리얼 모니터 시작 (디버깅용)
  Serial.begin(9600);
  Serial.println("** 서보 모터 작동 및 LCD 출력 시작 **");

  // 서보 모터를 지정한 핀에 연결
  servo.attach(SERVO_PIN);

  // LCD 초기화 및 백라이트 켜기
  lcd.init();
  lcd.backlight();

  // LCD 초기 화면 설정
  lcd.clear();
  lcd.setCursor(0, 0);        // (열 0, 행 0)
  lcd.print("Servo Angle");      // 1행에는 고정 문구 출력
}

void loop() {
  // ───────────────── 1) 가변 저항 값 읽기 ─────────────────
  int sensor = analogRead(POT_PIN);  // 0 ~ 1023의 값
  Serial.print("Resist: ");
  Serial.print(sensor);

  // 0~1023 범위를 0~180도로 매핑
  // 일반적인 서보는 0~180도만 사용 (360도 서보면 0~360으로 바꿔도 됨)
  int angle = map(sensor, 0, 1023, 0, 180);

  // ───────────────── 2) 서보 모터에 각도 전달 ─────────────────
  servo.write(angle);  // 서보 모터에 각도 명령
  Serial.print(" | angle: ");
  Serial.println(angle);

  // ───────────────── 3) LCD에 각도 출력 ─────────────────
  // 1행(0번째 줄)은 이미 "ANGLE IS"가 고정되어 있으므로
  // 2행(1번째 줄)에 각도 값만 갱신한다.
  lcd.setCursor(0, 1);   // (열 0, 행 1)

  // 이전에 출력된 값이 더 길 경우를 대비해 한 번 지워준다.
  // 예: 이전에 "180"을 출력하고 이번에 "5"를 출력하면 "580"처럼 보일 수 있음
  lcd.print("                ");  // 16칸 전부 공백으로 지우기
  lcd.setCursor(0, 1);   // 다시 (0,1)로 이동

  lcd.print(": ");
  lcd.print(angle);      // 현재 각도 숫자 출력
  lcd.print(" deg");     // 단위(degree) 표시 (원하면 생략 가능)

  // ───────────────── 4) 약간의 지연 ─────────────────
  // 서보가 너무 자주 갱신되어 떨리는 것을 방지하고,
  // 시리얼/화면 갱신 속도를 적당히 줄이기 위한 지연
  delay(100);            // 0.1초마다 한 번씩 갱신
}
