int LED_PIN = 3;
int DELAY = 10;

void setup() {
  // put your setup code here, to run once:

  pinMode(LED_PIN, OUTPUT);

  // 시리얼 통신 : 글자, 숫자, 데이터 값을 주고 받는 통신
  // Serial : 시리얼 통신을 담당하는 객체
  // .begin() : 시리얼 객체에 내장된 메서드
  Serial.begin(9600);  // COM7 과 같은 연결된 아두이노 객체와 시리얼 통신을 9600 의 속도로 시작
}

void loop() {
  // put your main code here, to run repeatedly:

  for(int brightness = 0; brightness < 255; brightness++) {
    analogWrite(LED_PIN, brightness);
    delay(DELAY);
    Serial.println(brightness); // .println(): 시리얼 모니터링 출력하는 함수
                                // 통신상태를 확인하거나 디버깅용
  }

}
