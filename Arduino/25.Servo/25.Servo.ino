#include <Servo.h>

Servo servo;  // Servo.h 라이브러리에 내장된 Servo 클래스로 서보 모터를 제어하기 위한 servo 객체 생성

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  servo.attach(8); // attach를 통해 pin 호
}

void loop() {
  // put your main code here, to run repeatedly:
  // 각도 0~180도 사이 1도씩 증가
  // 모터 내부 문제 발생 시, 중간에 초기화될 수 있음
  for(int angle = 0; angle <= 180; angle++) {
    servo.write(angle);
    Serial.print("angle: ");
    Serial.print(angle);
    Serial.println("");
    delay(100);
  }
}
