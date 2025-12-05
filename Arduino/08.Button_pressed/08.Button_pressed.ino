const int buttonPin = 3;

void setup() {
  pinMode(buttonPin, INPUT);    // 외부 풀업 사용
  Serial.begin(9600);
}

void loop() {
  int raw = digitalRead(buttonPin);
  int pressed = (raw == LOW) ? 1 : 0;   // 풀업이라 LOW가 눌린 상태
  Serial.println(pressed);

}
