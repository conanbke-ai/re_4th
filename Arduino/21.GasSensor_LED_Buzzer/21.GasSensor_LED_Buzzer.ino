// 연기 감지 시, LED ON + FIEZO ON

#define GAS_A A0
#define GAS_D 8
#define LED 2
#define FIEZO 3

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("히터 가열");
  delay(1000);

  pinMode(LED, OUTPUT);
  pinMode(FIEZO, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:

  float sensorValue = analogRead(GAS_A);
  float sensorDValue = digitalRead(GAS_D);

  Serial.print("센서 아날로그: ");
  Serial.print(sensorValue);
  Serial.print(" | 센서 디지털: ");
  Serial.print(sensorDValue);
  Serial.println("");
  delay(1000);

  if(sensorValue > 300 || sensorDValue == 0) {
    Serial.print(" | ※ 연기 감지!!! |");
    Serial.println("");

    digitalWrite(LED, HIGH);
    digitalWrite(FIEZO, HIGH);
    
  } else {
    digitalWrite(LED, LOW);
    digitalWrite(FIEZO, LOW);
  }
}
