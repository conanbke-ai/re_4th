int LED_PIN = 3;
int DELAY = 500;

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  analogWrite(LED_PIN, 255);  // 최대 출력 5V (digitalWrite(HIGH)와 동일)
  delay(DELAY);
  analogWrite(LED_PIN, 128);  // 50% 출력 2.5V
  delay(DELAY);
  analogWrite(LED_PIN, 0);  // 최소 출력 0V (digitalWrite(LOW)와 동일)
  delay(DELAY);

}
