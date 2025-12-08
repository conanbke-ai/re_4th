
// 초음파 센서를 통해 물체까지의 거리 계

#define TRIG 8
#define ECHO 9

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  // 초음파를 출력하는 핀
  pinMode(TRIG, OUTPUT);
  // 초음파를 수신받는 핀
  pinMode(ECHO, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

  // TRIG 핀이 10ms(1000㎕) 동안 HIGH 신호를 보냄
  digitalWrite(TRIG, HIGH);
  delay(10);
  digitalWrite(TRIG, LOW);

  // pulseIn : 마이크로초 단위(㎕, 10^-6)
  // duration은 왕복 시간이 저장됨(초음파가 나갔다가 되돌아오기까지의 시간)
  // ECHO 와 연결된 핀에서 입력을 시간으로 받
  float duration = pulseIn(ECHO, HIGH);
  float distance = ((34000*duration)/1000000)/2;

  Serial.print("distance: " + String(distance));
  Serial.println("cm");
  delay(100);
}
