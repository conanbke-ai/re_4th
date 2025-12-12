#include <SoftwareSerial.h>

// 흐름 정리

/*
  1. setup()
    - AT: ESP 살아있는지 확인
    - AT+CWMODE=1: Wifi 동작 모드 설정
    - AT+CWJAP="ssid","password": 와이파이 공유기 접속
    - AT+CIPMUX=0: 안정적인 통신을 위해 한 번에 하나의 연결만 하도록 제한
*/

/*
  2. loop()
    - 5초마다 sendDataToServer(25, 60) 실행
    - sendDataToServer()
      - AT+CIPSTART="TCP","서버IP",포트: TCP 열기
      - 온도와 습도에 해단 HTTP 요청 문자열 생성
      - AT+CIPSEND=길이: 해당 길이만큼 HTTP 요청
      - > 나올 때까지 기다리면서 HTTP GET 요청 전송
      - AT+CIPCLOSE로 연결 종료
*/

/*
  3. senCommand()
    - 공통 유틸 함수
    - 명령 문자열과 \r\n(종료용 빈 문자열) 전송
    - ESP 응답을 읽어 시리얼 모니터에 출력
    - 응답 안에 원하는 문자열 나오면 성공
    - timeout 까지 안나오면 실패
*/

// ────────────────────────────────────────────────
// 1. ESP-01(ESP8266)과 통신할 SoftwareSerial 포트 설정
//    - D2 : Arduino가 데이터를 "받는" 핀 (ESP-01의 TX에 연결)
//    - D3 : Arduino가 데이터를 "보내는" 핀 (ESP-01의 RX에 연결)
//    - 실제 배선:
//        ESP-01 TX  -> 아두이노 D2
//        ESP-01 RX  <- 아두이노 D3  (5V → 3.3V 레벨 변환 권장)
// ────────────────────────────────────────────────
SoftwareSerial esp8266(2, 3);

// ────────────────────────────────────────────────
// 2. 접속할 WiFi AP 정보
//    - 반드시 자신이 사용하는 공유기의 SSID / 비밀번호로 수정할 것
// ────────────────────────────────────────────────
// const char* ssid     = "spreatics_eungam_cctv";        // WiFi SSID (슬라이드 예시)
// const char* password = "sperateics*";  // WiFi PASSWORD (슬라이드 예시)

const char* ssid     = "Galaxy_A90";        // WiFi SSID (슬라이드 예시)
const char* password = "19941207";  // WiFi PASSWORD (슬라이드 예시)

// ────────────────────────────────────────────────
// 3. Flask 서버가 실행 중인 PC의 IP 주소와 포트 번호
//    - Windows의 cmd 창에서 ipconfig 입력 후 IPv4 주소를 확인해서
//      아래 server 값에 넣어야 한다.
//    - port 는 Flask 코드(app.run)에서 지정한 포트 번호와 동일하게.
// ────────────────────────────────────────────────
// const char* server = "192.168.1.138";  // 예시 IP, 반드시 본인 PC IPv4로 변경
const char* server = "10.119.92.28";
const int   port   = 5000;               // Flask 서버 포트 (예: 5000)

// ────────────────────────────────────────────────
// 4. 공통 유틸리티 함수: AT 명령을 ESP-01에게 보내고
//    응답에 특정 문자열(expect)이 포함되면 true, 아니면 false 반환
//
//    - bool: 반환값으로 응답을 잘 했는지 확인
//    - cmd      : ESP로 보낼 AT 명령 문자열 ("AT", "AT+CWMODE=1" 등)
//    - expect   : 응답에서 기대하는 문자열 (기본값 "OK")
//                 예) "WIFI GOT IP", "CONNECT", ">" 등
//    - timeout  : 최대 대기 시간 (밀리초 단위)
// ────────────────────────────────────────────────

bool sendCommand(const String& cmd, const char* expect = "OK",
                 unsigned long timeout = 5000) {

  // 4-1. ESP-01로 AT 명령 전송
  //      예: "AT", "AT+CWMODE=1" ...
  esp8266.print(cmd);

  // 4-2. AT 명령 끝에는 항상 CRLF(\r\n)를 붙여야 한다.
  //      시리얼 모니터에서 "Both NL & CR" 옵션과 동일한 역할.
  esp8266.print("\r\n");

  // 4-3. 현재 시간을 기록해서, timeout ms 동안만 응답을 기다리기 위한 기준값
  unsigned long start = millis();

  // 4-4. ESP로부터 받은 전체 응답을 저장할 버퍼
  String buf;

  // 4-5. timeout이 지나기 전까지 루프를 돌면서 데이터를 계속 읽는다.
  while (millis() - start < timeout) {
    // 4-5-1. ESP가 보낸 데이터가 있으면 모두 읽어서 buf에 추가
    while (esp8266.available()) {
      char c = (char)esp8266.read();  // 1바이트 읽기
      buf += c;                       // 문자열 버퍼에 누적
      Serial.write(c);               // 동시에 PC 시리얼 모니터에도 그대로 출력
    }

    // 4-5-2. 응답 문자열 buf 안에 기대하는 문자열(expect)이 포함되어 있으면 성공
    //        예) buf 안에 "OK" 가 포함되면 true 반환
    if (expect && buf.indexOf(expect) != -1) {
      return true;           // 기대 문자열을 찾았으므로 성공 처리
    }
  }

  // 4-6. 여기까지 왔다는 것은 timeout ms 동안 기대하는 문자열을 못 찾았다는 뜻
  Serial.println(F("\n[sendCommand] timeout"));
  Serial.print(F("Last response: "));
  Serial.println(buf);       // 마지막으로 받은 전체 응답을 출력해서 디버깅에 사용
  return false;              // 실패
}

// ────────────────────────────────────────────────
// 5. setup()
//    - 아두이노가 켜질 때 한 번만 실행되는 초기화 코드
//    - PC와 ESP-01의 시리얼 속도를 맞추고, WiFi 접속을 수행한다.
// ────────────────────────────────────────────────
void setup() {
  // 5-1. PC ↔ Arduino 시리얼 통신 시작
  //      시리얼 모니터 보레이트도 9600으로 맞춰야 한다.
  Serial.begin(9600);

  // 5-2. Arduino ↔ ESP-01 시리얼 통신 시작
  //      이 보드(ESP-01)의 AT 펌웨어가 115200bps 인 것으로 확인되었으므로 115200 사용
  esp8266.begin(9600);

  Serial.println(F("\n=== ESP8266 WiFi + Flask Demo ==="));

  // 5-3. ESP-01이 부팅을 끝내고 응답 준비를 할 수 있도록 약간 기다림
  delay(2000);

  // ── (1) AT 통신 테스트 ─────────────────────────
  // "AT" 명령에 "OK"가 돌아오면
  // - 배선 OK
  // - 보레이트 OK
  // - ESP-01 전원/부팅 OK
  sendCommand("AT", "OK", 2000);

  // ── (2) WiFi 모드 설정 ─────────────────────────
  // AT+CWMODE=1 : Station 모드(일반적인 WiFi 클라이언트 모드)
  sendCommand("AT+CWMODE=1", "OK", 2000);

  // ── (3) AP(공유기)에 접속 ──────────────────────
  // AT+CWJAP="ssid","password"
  {
    // String 을 사용해 "AT+CWJAP=\"SSID\",\"PASSWORD\"" 형식으로 조합
    String cmd = String("AT+CWJAP=\"") + ssid + "\",\"" + password + "\"";

    // 연결에 성공하면 응답에 "WIFI GOT IP" 문자열이 포함된다.
    // (네트워크에서 IP를 할당받았다는 의미)
    sendCommand(cmd, "WIFI GOT IP", 20000);  // WiFi 연결은 오래 걸릴 수 있어서 timeout을 20초로 설정
  }

  // ── (4) TCP 단일 연결 모드 설정 ─────────────────
  // AT+CIPMUX=0 : 다중 연결(MUX) 모드가 아닌, 단일 연결 모드
  //               HTTP 요청을 하나씩 보낼 때 사용하기 편함
  sendCommand("AT+CIPMUX=0", "OK", 2000);

  Serial.println(F("=== WiFi init done ==="));
}

// ────────────────────────────────────────────────
// 6. loop()
//    - setup() 이후 무한히 반복되는 부분
//    - 여기서는 예제로 temp/hum 값을 조금씩 바꾸면서
//      주기적으로 Flask 서버에 GET 요청을 보내는 역할만 수행.
// ────────────────────────────────────────────────
void loop() {
  // 6-1. static 변수: 함수가 다시 호출되어도 값이 유지된다.
  //     temp/hum 을 계속 누적해서 바꾸기 위해 static 사용.
  static int temp = 25;
  static int hum  = 60;

  // 6-2. 예제용 데이터 생성
  //     - 실제 센서를 연결하면 이 부분을 센서값 읽는 코드로 교체하면 된다.
  temp = (temp + 1) % 40;   // 0~39 범위를 반복 (온도)
  hum  = (hum + 2) % 100;   // 0~99 범위를 반복 (습도)

  // 6-3. 위에서 만든 temp/hum 값을 Flask 서버로 전송
  sendDataToServer(temp, hum);

  // 6-4. 5초 기다린 후 다음 전송
  delay(5000);
}

// ────────────────────────────────────────────────
 // 7. 실제로 Flask 서버(/data)에 GET 요청을 보내는 함수
//    - 예) GET /data?temperature=25&humidity=60 HTTP/1.1
// ────────────────────────────────────────────────
void sendDataToServer(int temp, int hum) {
  // 7-1. 요청 URL(쿼리스트링)을 문자열로 생성
  //      최종적으로 "/data?temperature=25&humidity=60" 형태가 된다.
  String url = String("/data?temperature=") + String(temp) +
               "&humidity=" + String(hum);

  // 7-2. Flask 서버(IP: server, Port: port)에 TCP 연결 요청
  //      AT+CIPSTART="TCP","192.168.200.100",5000
  String cmd = String("AT+CIPSTART=\"TCP\",\"") + server + "\"," + port;

  //      "CONNECT" 라는 응답이 오면 TCP 연결 성공
  if (!sendCommand(cmd, "CONNECT", 5000)) {
    Serial.println(F("[sendDataToServer] TCP connect failed"));
    return;   // 연결 실패 시 함수 종료
  }

  // 7-3. HTTP GET 요청 전체 문자열 만들기
  //      HTTP/1.1 프로토콜 형식에 맞게 헤더까지 구성해야 한다.
  String req;
  req  = "GET " + url + " HTTP/1.1\r\n";                         // 요청 라인
  req += "Host: " + String(server) + ":" + String(port) + "\r\n"; // Host 헤더
  req += "Connection: close\r\n\r\n";                            // 연결 종료 옵션 + 빈 줄(헤더 종료)

  // 7-4. 먼저 보낼 데이터 길이를 ESP에 알려준다.
  //      AT+CIPSEND=요청길이
  cmd = String("AT+CIPSEND=") + req.length();

  //      ESP 응답에서 '>' 프롬프트가 나오면 "이제 데이터를 보내도 좋다"는 의미
  if (!sendCommand(cmd, ">", 3000)) {
    Serial.println(F("[sendDataToServer] CIPSEND '>' not received"));
    return;  // '>'를 못 받으면 실제 HTTP 요청을 보내지 않고 종료
  }

  // 7-5. 실제 HTTP 요청 문자열 전송
  esp8266.print(req);
  Serial.println(F("[sendDataToServer] HTTP request sent"));

  // 7-6. 서버(Flask)에서 오는 응답을 5초 동안 읽어서 resp에 저장
  unsigned long start = millis();
  String resp;
  while (millis() - start < 5000) {
    while (esp8266.available()) {
      char c = (char)esp8266.read();
      resp += c;           // 응답을 문자열로 누적
      Serial.write(c);     // 동시에 시리얼 모니터에도 표시
    }
  }

  Serial.println(F("\n[sendDataToServer] Response received (truncated):"));
  Serial.println(resp);    // 응답 전체(또는 일부)를 한 번 더 출력

  // 7-7. HTTP 통신이 끝났으므로 TCP 소켓을 닫는다.
  //      AT+CIPCLOSE
  sendCommand("AT+CIPCLOSE", "OK", 2000);
  Serial.println(F("[sendDataToServer] connection closed\n"));
}
