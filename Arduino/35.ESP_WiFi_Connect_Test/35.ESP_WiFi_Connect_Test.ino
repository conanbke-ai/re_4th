#include <SoftwareSerial.h>

// D2 = Arduino RX(ESP TX), D3 = Arduino TX(ESP RX) 라고 가정
// 실질적으로 TX 가 D2연결, RX가 D3 연결
SoftwareSerial myESP(2, 3);

// 테스트할 보레이트 후보들
const long BAUD_CANDIDATES[] = {
  9600,
  19200,
  38400,
  57600,
  115200
};
const int NUM_BAUDS = sizeof(BAUD_CANDIDATES) / sizeof(BAUD_CANDIDATES[0]);

bool testOneBaud(long baud) {
  // SoftwareSerial 보레이트 설정
  myESP.begin(baud);
  delay(200);  // 설정 안정화 대기

  // 이전에 남아있던 ESP 수신 버퍼 비우기
  while (myESP.available()) {
    myESP.read();
  }

  Serial.println();
  Serial.print(F("[TEST] Trying baud "));
  Serial.println(baud);

  // ESP에게 "AT\r\n" 명령 전송
  myESP.print("AT\r\n");
  Serial.println(F("[SEND] AT"));

  // 일정 시간 동안 ESP 응답 수집
  unsigned long start = millis();
  String resp;

  while (millis() - start < 1500) {  // 최대 1.5초 대기
    while (myESP.available()) {
      char c = (char)myESP.read();
      resp += c;
      Serial.write(c);  // 모니터에도 그대로 출력
    }
  }

  Serial.println();
  Serial.print(F("[RESP] "));
  Serial.println(resp);

  // 응답 안에 "OK"가 포함되어 있으면 보레이트 일치로 판단
  if (resp.indexOf("OK") != -1) {
    Serial.print(F("[FOUND] 'OK' at baud "));
    Serial.println(baud);
    return true;
  }

  return false;
}

void setup() {
  Serial.begin(9600);    // PC <-> Arduino
  Serial.println(F("=== ESP8266 AT Baud Scan ==="));
  Serial.println(F("This will try several baud rates and look for 'OK'."));
  Serial.println();
}

void loop() {
  for (int i = 0; i < NUM_BAUDS; i++) {
    long baud = BAUD_CANDIDATES[i];
    if (testOneBaud(baud)) {
      Serial.println(F("=== Scan finished. Use this baud for myESP.begin() ==="));
      while (true) {
        // 여기서 멈춤
      }
    }
    delay(1000);  // 다음 보레이트 테스트 전에 잠시 대기
  }

  Serial.println(F("[WARN] No 'OK' found with any baud. Restarting scan..."));
  delay(3000);
}
