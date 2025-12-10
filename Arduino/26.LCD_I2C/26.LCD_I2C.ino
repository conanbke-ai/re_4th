/*

배선:
    VCC → 5V
    GND → GND
    SDA → A4
    SCL → A5

  I2C 방식 16x2 LCD 예제

  - LiquidCrystal_I2C 라이브러리를 사용해서
    I2C(2선) 방식 16x2 문자 LCD에 문자열을 출력하는 기본 코드입니다.
  - 1행에는 "Hello, World!"
    2행에는 "Posco X Codingon"을 출력한 뒤,
    잠시 후 화면을 지우는 동작을 반복합니다.
*/

#include <LiquidCrystal_I2C.h>  // I2C LCD 제어 라이브러리 포함

/*
  LiquidCrystal_I2C lcd(주소, 칸 수, 줄 수);

  - 0x27 : I2C LCD 모듈의 주소 (모듈에 따라 0x3F인 경우도 있음)
  - 16   : 한 줄에 들어가는 문자 수 (16칸 LCD)
  - 2    : 줄 수 (2줄 LCD)
*/
LiquidCrystal_I2C lcd(0x27, 16, 2);
// LiquidCrystal_I2C lcd(0x3F, 16, 2);

void setup() {
  // LCD 초기화 (I2C 통신 시작 + LCD 내부 설정)
  lcd.init();

  // LCD 백라이트(뒷불) 켜기
  // (모듈에 따라 자동으로 켜지기도 하지만, 확실히 켜주기 위해 사용)
  lcd.backlight();
}

void loop() {
  /*
    setCursor(열, 행);

    - 열(column) : 0 ~ 15 (16칸이므로 0이 첫 번째 칸)
    - 행(row)    : 0 ~ 1  (2줄이므로 0이 첫 번째 줄)
  */

  // ── 첫 번째 줄(0행) 0번째 칸에 "Hello, World!" 출력 ──
  lcd.setCursor(0, 0);               // 커서를 (열 0, 행 0) 위치로 이동
  lcd.print("Hello, World!");        // 문자열 출력
  delay(1000);                       // 1초 동안 그대로 표시

  // ── 두 번째 줄(1행) 0번째 칸에 "Posco X Codingon" 출력 ──
  lcd.setCursor(0, 1);               // 커서를 (열 0, 행 1) 위치로 이동
  lcd.print("Posco X Codingon");     // 문자열 출력
  delay(1000);                       // 1초 동안 그대로 표시

  // ── LCD 화면 전체 지우기 ──
  lcd.clear();                       // 전체 화면 클리어(커서는 (0,0)으로 돌아감)
  delay(1000);                       // 화면 지운 상태로 1초 대기

  lcd.setCursor(0, 0);               // 커서를 (열 0, 행 0) 위치로 이동
  lcd.print("Hello, I'm");        // 문자열 출력
  delay(1000);  

  lcd.setCursor(0, 1);               // 커서를 (열 0, 행 1) 위치로 이동
  lcd.print("Bae Kyung Eun");     // 문자열 출력
  delay(1000);   

  lcd.clear();
  delay(1000);


  // 그 다음 loop()가 다시 실행되면서
  // 위의 과정(1행 출력 → 2행 출력 → 화면 지우기)을 계속 반복
}
