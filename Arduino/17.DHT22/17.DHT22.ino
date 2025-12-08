#include "DHT.h"

#define DTHPIN 2
#define DHTTYPE DHT22

DHT myDHT(DTHPIN, DHTTYPE);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  myDHT.begin();

}

void loop() {
  // put your main code here, to run repeatedly:
  delay(2000);
  float h = myDHT.readHumidity();
  float c = myDHT.readTemperature();
  float f = myDHT.readTemperature(true);

  if (isnan(h) || isnan(c) || isnan(f)) {
    Serial.println("측정을 실패하였습니다.");
    return;
  }

  Serial.println();
  Serial.println("습도: " + String(h) + "% \n섭씨: " + String(c) + "°C \n화씨: " + String(f) + "°F");
  Serial.println();

}
