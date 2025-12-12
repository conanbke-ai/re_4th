/*
  MFRC522 RFID 리더기 + LED + 피에조 부저 예제 (조건 분기 버전)

  기능:
    - RFID 카드/태그를 안테나 위에 올리면 UID(고유번호)를 읽어서
      시리얼 모니터로 출력한다.
    - UID를 문자열로 변환해서 미리 등록해둔 카드와 비교한다.
    - 1번 카드 → 파란 LED ON + 부저 1회 울림
    - 2번 카드 → 빨간 LED ON + 부저 2회 울림
    - 그 외 카드 → “등록되지 않은 카드” 메시지 + 빨강/파랑 LED 번갈아 깜빡임

  사용 장치:
    - MFRC522 RFID 모듈
    - 빨간 LED, 파란 LED
    - 피에조 부저
*/

#include <SPI.h>
#include <MFRC522.h>

// ─────────────────────────────────────────────
// 핀 설정 (Arduino UNO 기준)
// ─────────────────────────────────────────────
#define SS_PIN    10   // RFID 모듈 SDA(SS) 핀 → D10
#define RST_PIN    9   // RFID 모듈 RST 핀 → D9

#define LED_RED    6   // 빨간 LED
#define LED_BLUE   7   // 파란 LED

#define FIEZO      2   // 피에조 부저 (+)

// MFRC522 객체 생성
MFRC522 mfrc(SS_PIN, RST_PIN);

// 읽어온 카드 UID를 문자열로 저장할 변수
String CardUuid = "";

// ─────────────────────────────────────────────
// 1번 / 2번 카드 UID (시리얼 모니터로 확인한 값 사용)
//   - 카드 1: A6 9F B9 02 → "A6:9F:B9:02"  흰색 태그
//   - 카드 2: 55 FC CD 01 → "55:FC:CD:01"  파란색 태그
// ─────────────────────────────────────────────
const String CARD1_UID = "A6:9F:B9:02";  // 1번 카드 (흰색 태그)
const String CARD2_UID = "55:FC:CD:01";  // 2번 카드 (파란색 태그)

// ─────────────────────────────────────────────
// UID를 "XX:YY:ZZ:WW" 형태의 문자열로 변환하는 함수
// 예: 0x55 0xFC 0xCD 0x01 → "55:FC:CD:01"
// ─────────────────────────────────────────────
String getCardUidString(const MFRC522::Uid &uid) {
  String uidStr = "";

  for (byte i = 0; i < uid.size; i++) {
    // 값이 0x0F 이하(한 자리 HEX)일 때 앞에 0 붙이기 (예: 0x5 → "05")
    if (uid.uidByte[i] < 0x10) uidStr += "0";

    // 16진수 형태의 문자열로 붙이기 (예: 0xA6 → "a6")
    uidStr += String(uid.uidByte[i], HEX);

    // 각 바이트 사이에 ":" 구분자 추가
    if (i < uid.size - 1) {
      uidStr += ":";
    }
  }

  // 소문자 → 대문자로 통일 ("a6:9f" → "A6:9F")
  uidStr.toUpperCase();
  return uidStr;
}

// ─────────────────────────────────────────────
// 부저를 여러 번 울리는 헬퍼 함수
//   count  : 울릴 횟수
//   freq   : 주파수(Hz) – 높을수록 높은 음
//   onTime : 한 번 울릴 때 ON 시간(ms)
//   offTime: 울리고 나서 쉬는 시간(ms)
// ─────────────────────────────────────────────
void beep(int count, unsigned int freq, unsigned int onTime, unsigned int offTime) {
  for (int i = 0; i < count; i++) {
    tone(FIEZO, freq);   // 해당 주파수로 부저 ON
    delay(onTime);       // onTime ms 동안 유지
    noTone(FIEZO);       // 부저 OFF
    delay(offTime);      // offTime ms 쉼
  }
}

// ─────────────────────────────────────────────
// 등록되지 않은 카드일 때
// 빨간 LED ↔ 파란 LED 번갈아 깜빡이게 하는 함수
//   times    : "빨강-파랑" 한 쌍을 몇 번 반복할지
//   interval : 각 색상 유지 시간(ms)
// ─────────────────────────────────────────────
void blinkAlternate(int times, unsigned int interval) {
  for (int i = 0; i < times; i++) {
    // 1) 빨간 LED ON, 파란 LED OFF
    digitalWrite(LED_RED, HIGH);
    digitalWrite(LED_BLUE, LOW);
    delay(interval);

    // 2) 빨간 LED OFF, 파란 LED ON
    digitalWrite(LED_RED, LOW);
    digitalWrite(LED_BLUE, HIGH);
    delay(interval);
  }

  // 마지막에는 둘 다 OFF 상태로 마무리
  digitalWrite(LED_RED, LOW);
  digitalWrite(LED_BLUE, LOW);
}

void setup() {
  Serial.begin(9600);

  // ── 핀 모드 설정 ──
  pinMode(LED_RED, OUTPUT);
  pinMode(LED_BLUE, OUTPUT);
  pinMode(FIEZO, OUTPUT);

  // 시작 시 LED/부저 OFF 상태로 초기화
  digitalWrite(LED_RED, LOW);
  digitalWrite(LED_BLUE, LOW);
  digitalWrite(FIEZO, LOW);

  Serial.println("=== RFID 카드 테스트 시작 ===");

  // ── SPI & MFRC522 초기화 ──
  SPI.begin();          // SPI 통신 시작
  Serial.println("step 1: SPI.begin OK");

  mfrc.PCD_Init();      // MFRC522 칩 초기화
  Serial.println("step 2: PCD_Init OK");

  // 펌웨어 버전 정보 출력 (정상 통신 확인용)
  mfrc.PCD_DumpVersionToSerial();
  Serial.println("step 3: DumpVersionToSerial OK");

  Serial.println("카드를 안테나 위에 올려두거나, 가까이 대 보세요.");
  Serial.println("==============================================");
}

void loop() {
  // 너무 빠른 폴링 방지 (조금만 천천히 돌리기)
  delay(200);

  // ─────────────────────────────────────────
  // 1) 새 카드가 있는지 확인
  //    - 카드가 없으면 return → loop 처음으로 돌아감
  // ─────────────────────────────────────────
  if (!mfrc.PICC_IsNewCardPresent()) {
    return;
  }
  Serial.println(">> 새 카드 감지됨!");

  // ─────────────────────────────────────────
  // 2) 감지된 카드의 UID 읽기
  // ─────────────────────────────────────────
  if (!mfrc.PICC_ReadCardSerial()) {
    Serial.println("!! 카드 감지됨, 하지만 UID 읽기 실패");
    delay(500);
    return;
  }
  Serial.println(">> 카드 UID 읽기 성공");

  // ─────────────────────────────────────────
  // 3) UID 바이트 값을 HEX로 출력
  //    (시리얼 모니터에서 UID 확인용)
// ─────────────────────────────────────────
  Serial.print("Card UID (HEX): ");
  for (byte i = 0; i < mfrc.uid.size; i++) {
    if (mfrc.uid.uidByte[i] < 0x10) Serial.print("0"); // 한 자리 HEX일 때 0 패딩
    Serial.print(mfrc.uid.uidByte[i], HEX);            // 16진수로 출력
    Serial.print(" ");
  }
  Serial.println();

  // ─────────────────────────────────────────
  // 4) UID를 "XX:YY:ZZ:WW" 형식의 문자열로 변환
  // ─────────────────────────────────────────
  CardUuid = getCardUidString(mfrc.uid);
  Serial.print("UID String = ");
  Serial.println(CardUuid);

  // ─────────────────────────────────────────
  // 5) 카드 타입 정보 출력 (MIFARE 1KB 등)
// ─────────────────────────────────────────
  MFRC522::PICC_Type piccType = mfrc.PICC_GetType(mfrc.uid.sak);
  Serial.print("PICC type: ");
  Serial.println(mfrc.PICC_GetTypeName(piccType));

  // ─────────────────────────────────────────
  // 6) UID에 따라 LED / 부저 동작 분기
  // ─────────────────────────────────────────
  // 모든 LED 먼저 끄고 시작 (상태 초기화)
  digitalWrite(LED_RED, LOW);
  digitalWrite(LED_BLUE, LOW);

  if (CardUuid == CARD1_UID) {
    // ■ 1번 카드: 파란 LED ON + 부저 1회 울림
    Serial.println("① 1번 카드 인식: BLUE LED ON + 부저 1회");

    digitalWrite(LED_BLUE, HIGH);   // 파란 LED 켜기
    digitalWrite(LED_RED, LOW);     // 빨간 LED 끄기

    // 부저 1회 울리기: 2kHz, 200ms ON, 150ms OFF
    beep(1, 2000, 200, 150);
  }
  else if (CardUuid == CARD2_UID) {
    // ■ 2번 카드: 빨간 LED ON + 부저 2회 울림
    Serial.println("② 2번 카드 인식: RED LED ON + 부저 2회");

    digitalWrite(LED_BLUE, LOW);    // 파란 LED 끄기
    digitalWrite(LED_RED, HIGH);    // 빨간 LED 켜기

    // 부저 2회 울리기: 1.5kHz, 200ms ON, 150ms OFF
    beep(2, 1500, 200, 150);
  }
  else {
    // ■ 등록되지 않은 카드
    Serial.println("※ 등록되지 않은 카드입니다. (RED/BLUE 번갈아 깜빡임)");

    // 빨간 LED ↔ 파란 LED 번갈아 깜빡이기
    // 예: 6번 반복, 각 색상 200ms 유지 → 총 약 2.4초 정도 깜빡
    blinkAlternate(6, 200);
  }

  // LED 상태를 유지하고 싶으면 이 부분은 빼도 됨
  // blinkAlternate()에서 이미 OFF로 마무리하긴 하지만,
  // 안전하게 한 번 더 꺼주는 초기화 코드
  delay(500);
  digitalWrite(LED_RED, LOW);
  digitalWrite(LED_BLUE, LOW);

  // ─────────────────────────────────────────
  // 7) 카드 통신 종료 (다음 카드 읽기 준비)
  // ─────────────────────────────────────────
  mfrc.PICC_HaltA();       // 현재 카드와 통신 종료
  mfrc.PCD_StopCrypto1();  // 암호화 세션 종료

  Serial.println("---- 카드 처리 완료, 다음 카드 대기 ----");
  Serial.println();
}
