int LEDS[] = {10, 11, 12};
int count = 3;

void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  
  for(int i = 0; i < count; i++) {
    pinMode(LEDS[i], OUTPUT);
  }
}

// the loop function runs over and over again forever
void loop() {

  for(int i = 0; i < count; i++) {
      digitalWrite(LEDS[i], HIGH);  // turn the LED on (HIGH is the voltage level)
      delay(500);               // wait for a second
      digitalWrite(LEDS[i], LOW);   // turn the LED off by making the voltage LOW
      delay(500);  
    }

}