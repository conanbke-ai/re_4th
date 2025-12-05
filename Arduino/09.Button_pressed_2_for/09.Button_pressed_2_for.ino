int BTN[] = {1, 2};
int count = 2;

void setup() {
  Serial.begin(9600);
  for(int i = 0; i < count; i++) {
    pinMode(BTN[i], INPUT_PULLUP);
  }

}

void loop() {
  for(int i = 0; i < count; i++) {
    int BTNState = digitalRead(BTN[i]);
    Serial.println(BTNState);
  }
}