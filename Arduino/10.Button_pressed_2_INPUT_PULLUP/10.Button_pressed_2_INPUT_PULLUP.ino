int switch1= 1; // 택트1
int switch2= 2; // 택트2
int ledRed = 3; // LED 빨강
int ledBlue = 4; // LED 파랑

void setup() {
   Serial.begin(9600);  // 9600 속도로 시리얼 통신 시작
   pinMode(switch1, INPUT_PULLUP);
   pinMode(switch2, INPUT_PULLUP);
   pinMode(ledBlue , OUTPUT);
   pinMode(ledRed , OUTPUT);
}

void loop() 
{
  int SW1 = digitalRead(switch1); // 택트1의 상태 저장 - 기본적으로 1 출력(INPUT_PULLUP mode이기 때문) / 스위치 눌릴 시, 0 출력
  int SW2 = digitalRead(switch2); // 택트2의 상태 저장

  digitalWrite(ledRed, LOW); // OUPUT mode 이므로, 기본 상태를 LOW로 설정해야, 꺼진 상태로 됨
  digitalWrite(ledBlue, LOW); 

  // 스위치를 눌렀을 때,
  if(SW1 == LOW){
    Serial.println("Switch : RED");
    digitalWrite(ledRed, HIGH); // 스위치를 누른 상태로, LED를 킨 상태로 전환
  }
  if(SW2 == LOW){
    Serial.println("Switch : BLUE");
    digitalWrite(ledBlue, HIGH); 
  }
  delay(100);
}