#define GAS_A A0
#define GAS_D 8

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("히터 가열");
  delay(1000);

}

void loop() {
  // put your main code here, to run repeatedly:

  float sensorValue = analogRead(GAS_A);
  float sensorDValue = digitalRead(GAS_D);

  Serial.print("센서 아날로그: ");
  Serial.print(sensorValue);

  if(sensorValue > 300) {
    Serial.print(" | ※ 연기 감지!!!");
    Serial.println("");
  }

  Serial.print(" | 센서 디지털: ");
  Serial.print(sensorDValue);
  Serial.println("");

  delay(1000);
}
