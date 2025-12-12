#include <SoftwareSerial.h>

SoftwareSerial esp(2, 3);   // D2 = RX, D3 = TX

// ─────────────────────────────────────
//  PC <-> Arduino 시리얼 + 디버그 출력
// ─────────────────────────────────────
void debugln(const String &msg) {
  Serial.println(msg);
}

// ESP로 명령 전송 + 응답에서 expected 문자열이 나올 때까지 대기
bool sendAT(const String &cmd, const String &expected, unsigned long timeout) {
  while (esp.available()) esp.read();  // 기존 버퍼 비우기

  debugln(">>> " + cmd);
  esp.print(cmd);

  unsigned long start = millis();
  String resp;

  while (millis() - start < timeout) {
    while (esp.available()) {
      char c = esp.read();
      resp += c;
      Serial.write(c);   // ESP가 보낸 내용 그대로 시리얼 모니터에 출력
      if (resp.indexOf(expected) != -1) {
        debugln("\n[OK] expected found: " + expected);
        return true;
      }
    }
  }

  debugln("\n[WARN] timeout, last resp:");
  debugln(resp);
  return false;
}

void setup() {
  Serial.begin(9600);      // PC <-> Arduino
  esp.begin(9600);       // Arduino <-> ESP-01 (AT 펌웨어 보레이트)

  debugln("=== ESP WiFi Auto Connect Demo ===");

  delay(2000); // ESP 부팅 대기

  // 1) 테스트: AT
  sendAT("AT\r\n", "OK", 2000);

  // 2) Station 모드 설정
  sendAT("AT+CWMODE=1\r\n", "OK", 3000);

  // 3) 원하는 AP에 접속 (SSID, PASSWORD 직접 넣기)
  //    예: AT+CWJAP="MyWiFi","mypassword"
  // ESP8655의 경우, 2.4GHz만 호환 가능(일반적인 5GHz의 와이파이 연결 불가) 
  sendAT("AT+CWJAP=\"spreatics_eungam_cctv\",\"spreatics*\"\r\n", "OK", 15000);

  // 4) IP 확인
  sendAT("AT+CIFSR\r\n", "OK", 3000);

  // debugln("=== WiFi init sequence finished ===");
}

void loop() {
  // 여기부터는:
  // - 주기적으로 서버에 HTTP GET/POST 날리거나
  // - PC에서 명령을 받아 ESP를 통해 웹으로 보내는 등
  // 원하는 로직을 설계하면 됩니다.
}
