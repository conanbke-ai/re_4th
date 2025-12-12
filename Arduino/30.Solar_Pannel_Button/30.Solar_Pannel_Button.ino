// 태양광 패널 가상 에너지 게임 정답 코드

// 아날로그 입력 핀 (태양광 패널, 조도센서, 가변저항 등)
const int PANEL_PIN = A0;   // 태양광 패널 입력
// 판매 버튼 핀 (내부 풀업 사용)
const int SW_PIN    = 2;    // 판매 버튼 (INPUT_PULLUP)

// 가상 에너지 저장소
long energy = 0;

// 총 판매량
long totalSale = 0;

// 판매 단위(원하는 만큼 설정 가능)
const long SELL_UNIT = 100;    // 100 단위 판매

// 충전 스케일 조정 (전압이 클수록 더 빨리 charging)
// 전압이 5V일 때 +50씩 적립
const int MAX_CHARGE_RATE = 50;

void setup() {
  Serial.begin(9600);
  // 버튼은 INPUT_PULLUP: 기본 HIGH, 눌렸을 때 LOW
  pinMode(SW_PIN, INPUT_PULLUP);

  Serial.println("== 태양광 에너지 판매 시작 ==");
}

void loop() {

  // ───────────────────────────────────
  // 1. 태양광 패널 전압 읽기 (0~5V)
  // ───────────────────────────────────
  int   raw     = analogRead(PANEL_PIN);        // 0 ~ 1023
  float voltage = (raw * 5.0) / 1023.0;         // 0.0 ~ 5.0V

  // ───────────────────────────────────
  // 2. 전압 기반 충전 공식
  //    gain = (전압비율) × (최대충전량)
  // ───────────────────────────────────
  int gain = (voltage / 5.0) * MAX_CHARGE_RATE;

  if (gain > 0) {        // 0보다 클 때만 적립
    energy += gain;      // 가상 에너지 누적
  }

  // ───────────────────────────────────
  // 3. 버튼 눌림 감지 (엣지 검출)
  //    - prev : 이전 버튼 상태
  //    - curr : 현재 버튼 상태
  //    - HIGH → LOW 으로 바뀌는 순간에만 “판매” 수행
  // ───────────────────────────────────
  static bool prev = HIGH;                // 처음에는 HIGH(안 눌린 상태)
  bool curr = digitalRead(SW_PIN);        // 현재 버튼 상태 읽기

  if (prev == HIGH && curr == LOW) {      // 막 눌린 시점
    Serial.println("=== 판매 요청 발생 ===");

    if (energy >= SELL_UNIT) {            // 에너지가 충분하면
      energy -= SELL_UNIT;                // 판매 단위만큼 차감
      totalSale += SELL_UNIT;             // 누적 판매량
      Serial.print("★ 판매 성공 | 판매량: ");
      Serial.print(SELL_UNIT);
      Serial.print(" | 남은 에너지: ");
      Serial.print(energy);
      Serial.print(" | 총 에너지 판매량: ");
      Serial.println(totalSale);
    } else {                              // 에너지 부족
      Serial.print("※ 판매 실패 | 이유: 에너지가 부족합니다 | 현재 에너지: ");
      Serial.println(energy);
    }
  }
  // 다음 loop에서 비교할 수 있도록 현재 상태를 prev에 저장
  prev = curr;

  // ───────────────────────────────────
  // 4. 현재 상태 출력 (모니터링용)
  // ───────────────────────────────────
  Serial.print("전압: ");
  Serial.print(voltage);
  Serial.print("V | 적립량: ");
  Serial.print(gain);
  Serial.print(" | 현재 에너지: ");
  Serial.println(energy);

  delay(250);   // 0.5초마다 한 번씩 상태 출력
}
