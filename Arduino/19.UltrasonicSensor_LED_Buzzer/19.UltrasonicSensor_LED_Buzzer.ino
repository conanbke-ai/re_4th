// 초음파 센서에 가까운 물체 감지 시, 빨간 LED ON + 피에조 부저 경고음 ON

#define TRIG 8
#define ECHO 9
#define LED 2
#define FIEZO 3

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  pinMode(LED, OUTPUT);
  pinMode(FIEZO, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:

  // TRIG 핀이 10ms(1000㎕) 동안 HIGH 신호를 보냄
  digitalWrite(TRIG, HIGH);
  delay(10);
  digitalWrite(TRIG, LOW);

  // pulseIn : 마이크로초 단위(㎕, 10^-6)
  // duration은 왕복 시간이 저장됨(초음파가 나갔다가 되돌아오기까지의 시간)
  float duration = pulseIn(ECHO, HIGH);
  float distance = ((34000*duration)/1000000)/2;

  Serial.print("distance: " + String(distance));
  Serial.println("cm");
  delay(100);

  if (distance < 15) {
    digitalWrite(LED, HIGH);
    digitalWrite(FIEZO, HIGH);
    Serial.println("==================");
    Serial.println("LED ON | FIEZO ON");
    Serial.println("==================");
  } else {
    digitalWrite(LED, LOW);
    digitalWrite(FIEZO, LOW);
  }

}
