#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN  10    // MFRC522의 SDA(SS) 연결 핀
#define RST_PIN 9   // MFRC522의 RST 연결 핀

// 실제 배선
// MFRC522 SDA  → D10
// MFRC522 SCK  → D13
// MFRC522 MOSI → D11
// MFRC522 MISO → D12
// MFRC522 RST  → D9
// MFRC522 3.3V → 3.3V
// MFRC522 GND  → GND

MFRC522 mfrc(SS_PIN, RST_PIN);

void setup() {
  Serial.begin(9600);
  Serial.println("=== RFID 카드 테스트 시작 ===");

  SPI.begin();
  Serial.println("step 1: SPI.begin OK");

  mfrc.PCD_Init();
  Serial.println("step 2: PCD_Init OK");

  mfrc.PCD_DumpVersionToSerial();
  Serial.println("step 3: DumpVersionToSerial OK");

  Serial.println("카드를 안테나 위에 올려두거나, 가까이 대 보세요.");
  Serial.println("==============================================");
}

void loop() {
  // Serial.println("loop start");   // ★ loop 들어왔는지 확인
  delay(200);                     // 너무 빨리 도는 것 방지용

  // Serial.println("call IsNewCardPresent()");
  bool hasNewCard = mfrc.PICC_IsNewCardPresent();
  // Serial.println("after IsNewCardPresent()");   // ★ 여기까지 오면 멈추지 않은 것

  if (!hasNewCard) {
    // Serial.println("No new card.");
    delay(500);
    return;
  }
  Serial.println(">> 새 카드 감지됨!");

  // Serial.println("call ReadCardSerial()");
  bool canRead = mfrc.PICC_ReadCardSerial();
  // Serial.println("after ReadCardSerial()");     // ★ 여기까지 오면 UID 읽기까지 무한루프는 아님

  if (!canRead) {
    Serial.println("!! 카드 감지됨, 하지만 UID 읽기 실패");
    delay(500);
    return;
  }

  // UID 출력
  Serial.print("Card UID: ");
  for (byte i = 0; i < mfrc.uid.size; i++) {
    if (mfrc.uid.uidByte[i] < 0x10) Serial.print("0");
    Serial.print(mfrc.uid.uidByte[i], HEX);
    Serial.print(" ");
  }
  Serial.println();

  MFRC522::PICC_Type piccType = mfrc.PICC_GetType(mfrc.uid.sak);
  Serial.print("PICC type: ");
  Serial.println(mfrc.PICC_GetTypeName(piccType));

  mfrc.PICC_HaltA();
  mfrc.PCD_StopCrypto1();

  Serial.println("---- 카드 처리 완료, 다음 카드 대기 ----");
  delay(500);
}

