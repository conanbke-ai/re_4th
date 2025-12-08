// 가변 저항 모듈을 사용해도 저항을 사용 하는 이유 = 1023 byte로 출력 시, LED가 탈 수 있기 때문에 보호하기 위함

const int LED_PIN = 10;
// delay를 없애 반응성을 더 좋게 개선
const unsigned long INTERVAL = 100;
unsigned long prevMillis = 0;

void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  
  unsigned long now = millis();

  if (now - prevMillis >= INTERVAL) {
    prevMillis = now;

    int sensor = analogRead(A0);
    Serial.println(sensor);

    // 조도 센서는 빛이 강하면 저항값이 낮아짐 -> 전압(출력값)이 커짐
    // 조도 센서는 빛이 약하면 저항값이 높아짐 -> 전압(출력값)이 낮아짐
    if (sensor > 900){
      digitalWrite(LED_PIN, HIGH);
    } else {
      digitalWrite(LED_PIN, LOW);
    }
  }

}
