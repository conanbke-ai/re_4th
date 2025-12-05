// const : 절대 상수(변경 X)
const int PIN = 8;
const int melody[] = {
  // 도, 레, 미, 파, 솔, 라, 시, 도
  262, 294, 330, 349, 392, 440, 494, 523
};
int DELAY = 500;

void setup() {
  // put your setup code here, to run once:
  for(int i = 0; i < sizeof(melody); i++) {
    tone(PIN, melody[i], 500);
    delay(DELAY);
  }
}

void loop() {
  // put your main code here, to run repeatedly:

}
