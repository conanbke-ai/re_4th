// 매개변수화
// 함수에는 매개변수를 사용하여 더 확정성있는 함수를 선언할 수 있음
// 제어할 LED 핀 번호 배열
int LEDS[] = {10, 11, 12};
const int count = 3;
const int DELAY_TIME = 500;  // ms 단위

// 1개 LED를 ON → OFF까지 처리하는 "매개변수화된 함수"
void blinkLed(int pin, int onTime, int offTime) {
  digitalWrite(pin, HIGH);   // 켜기
  delay(onTime);

  digitalWrite(pin, LOW);    // 끄기
  delay(offTime);
}

// LED 배열을 순서대로 돌면서, 각 LED를 ON → OFF까지 실행
void runSequence(int onTime, int offTime) {
  for (int i = 0; i < count; i++) {
    blinkLed(LEDS[i], onTime, offTime);
  }
}

void setup() {
  for (int i = 0; i < count; i++) {
    pinMode(LEDS[i], OUTPUT);
  }
}

void loop() {
  // 전체 시퀀스 반복
  runSequence(DELAY_TIME, DELAY_TIME);
}
