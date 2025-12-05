int LEDS[] = {10, 11, 12};
int count = 3;

void turnLed() {

  for(int i = 0; i < count; i ++) {
    digitalWrite(LEDS[i], HIGH);
    delay(500);
    digitalWrite(LEDS[i], LOW);
    delay(500);
  }
}

void setup() {
  // put your setup code here, to run once:
  for(int i = 0; i < count; i ++) {
      pinMode(LEDS[i], OUTPUT);
    }
}

void loop() {
  // put your main code here, to run repeatedly:

  turnLed();
}
