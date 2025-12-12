#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// =======================================================
//  LCD & 하드웨어 설정
// =======================================================

// I2C LCD 주소(보통 0x27 또는 0x3F), 16x2 LCD 사용
LiquidCrystal_I2C lcd(0x27, 16, 2);

// 사용자 정의 문자 번호 (0~7 사용 가능)
const byte CHAR_DINO = 0;   // 공룡 캐릭터
const byte CHAR_TREE = 1;   // 나무(장애물) 캐릭터

// 핀 설정
const int PIN_BUTTON_JUMP = 2;   // 점프 버튼
const int LED_RED         = 13;  // 보드 내장 LED(또는 외부 LED)

// LCD 컬럼 개수
const int LCD_COLS = 16;

// =======================================================
//  게임용 상태 변수
// =======================================================

// 게임이 진행 중인지 여부
bool isPlaying = false;

// 공룡이 땅에 있는지 여부
bool isDinoOnGround = true;

// 현재 점수
long score = 0;

// 점프 버튼이 "현재 계속 눌려 있는지" 상태
bool jumpButtonLatched = false;

// 버튼이 눌리기 시작한 시각 (밀리초 단위)
unsigned long jumpPressStartTime = 0;

// =======================================================
//  사용자 정의 문자 패턴 (공룡, 나무)
// =======================================================

// 공룡 캐릭터 (8행 x 5열 비트맵)
byte dinoBitmap[8] =
{
  B00000,
  B00111,
  B00101,
  B10111,
  B11100,
  B11111,
  B01101,
  B01100
};

// 나무 캐릭터 (장애물)
byte treeBitmap[8] =
{
  B00011,
  B11011,
  B11011,
  B11011,
  B11011,
  B11111,
  B01110,
  B01110
};

// =======================================================
//  함수 선언부
// =======================================================
void showReadyScreen();
void waitForStartButton();
void resetGameState();
void playOneRound();
void handleGameOver();
void drawTree(int col);
void updateDinoPosition();
void putDinoOnGround();
void putDinoInAir();

// =======================================================
//  setup() : 초기 1회 실행
// =======================================================
void setup() {
  // 시리얼 통신 초기화 (모니터에서 값 확인용)
  Serial.begin(9600);
  Serial.println("=== DINO RUN LCD GAME ===");
  Serial.println("Press button to start game...");

  // I2C 통신 시작
  Wire.begin();

  // LCD 초기화
  lcd.init();
  lcd.backlight();

  // 사용자 정의 문자 등록
  lcd.createChar(CHAR_DINO, dinoBitmap);
  lcd.createChar(CHAR_TREE, treeBitmap);

  // 버튼, LED 핀 모드 설정
  pinMode(PIN_BUTTON_JUMP, INPUT_PULLUP);  // 내부 풀업 사용 (LOW = 눌림)
  pinMode(LED_RED, OUTPUT);
  digitalWrite(LED_RED, LOW);             // 시작 시 LED OFF

  // 첫 화면: 준비 화면 출력
  showReadyScreen();
}

// =======================================================
//  loop() : 메인 루프
//  - "대기 → 게임 플레이 → 게임 오버 → 대기" 흐름 관리
// =======================================================
void loop() {
  if (!isPlaying) {
    // 1) 준비 화면 출력
    showReadyScreen();
    // 2) 시작 버튼 대기
    waitForStartButton();
    // 3) 게임 상태 초기화
    resetGameState();
    // 4) 게임 시작
    isPlaying = true;

    Serial.println("=== GAME START ===");
  } else {
    // 한 라운드(나무들이 한 번 지나가는 사이클)를 플레이
    playOneRound();
    // playOneRound() 안에서 충돌/롱프레스가 발생하면
    // handleGameOver() + isPlaying = false 가 설정됨
  }
}

// =======================================================
//  준비 화면 출력
// =======================================================
void showReadyScreen() {
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("DINO RUN LCD");
  lcd.setCursor(0, 1);
  lcd.print("Press Btn to Go");
}

// =======================================================
//  시작 버튼 대기
//  - 점프 버튼이 한 번 눌릴 때까지 기다렸다가 반환
// =======================================================
void waitForStartButton() {
  while (true) {
    int btn = digitalRead(PIN_BUTTON_JUMP);

    // 풀업이므로 LOW = 눌림
    if (btn == LOW) {
      delay(20); // 간단 디바운스
      if (digitalRead(PIN_BUTTON_JUMP) == LOW) {
        // 버튼이 실제로 눌린 상태 유지 확인
        while (digitalRead(PIN_BUTTON_JUMP) == LOW) {
          // 버튼에서 손을 뗄 때까지 대기
        }
        break;
      }
    }
  }
}

// =======================================================
//  게임 상태 초기화
// =======================================================
void resetGameState() {
  score = 0;
  isDinoOnGround = true;
  jumpButtonLatched = false;
  jumpPressStartTime = 0;
  digitalWrite(LED_RED, LOW);  // LED도 OFF로 초기화
  lcd.clear();
}

// =======================================================
//  한 라운드 플레이
//  - 나무 3개를 오른쪽에서 왼쪽으로 이동
//  - 공룡과의 충돌 여부 체크
//  - 버튼 롱프레스(2초 이상)도 여기서 감지
// =======================================================
void playOneRound() {
  lcd.clear();

  // 버튼이 공중에서 몇 번 읽혔는지 (점수 패널티용)
  int buttonPressedTimesInAir = 0;

  // 나무 사이 간격(난수 사용)
  // secondOffset 을 2~4로 줄여서 "촘촘한 || 패턴"도 나오게 함
  int secondOffset = random(2, 5);   // 첫 번째와 두 번째 나무 사이 (2~4칸)
  int thirdOffset  = random(4, 9);   // 두 번째와 세 번째 나무 사이 (4~8칸)

  int firstTreeCol = LCD_COLS;       // 첫 번째 나무 시작 위치 (오른쪽 밖)
  int stopCol = -(secondOffset + thirdOffset);  // 마지막 나무 지나간 뒤 멈추는 지점

  for (int col = firstTreeCol; col >= stopCol; col--) {
    // -----------------------------
    // 1) 바닥 줄 전체를 매 프레임 지움
    //    → 이전 나무가 캐릭터 뒤에 남는 버그 방지
    // -----------------------------
    lcd.setCursor(0, 1);
    lcd.print("                ");  // 16칸 공백으로 바닥 초기화

    // -----------------------------
    // 2) 상단 오른쪽에 점수 표시
    // -----------------------------
    lcd.setCursor(10, 0);
    lcd.print("    ");        // 이전 점수 지우기
    lcd.setCursor(10, 0);
    lcd.print(score);

    // -----------------------------
    // 3) 공룡 위치 업데이트
    //    - 점프 버튼 상태에 따라 공중/지상 이동
    //    - 2초 이상 누르고 있으면 여기서 게임 오버
    // -----------------------------
    updateDinoPosition();

    // updateDinoPosition() 내에서 롱프레스로 게임 오버가 발생하면
    // isPlaying 이 false 로 바뀌므로 이 라운드 종료
    if (!isPlaying) {
      break;
    }

    // -----------------------------
    // 4) 나무 위치 계산 및 출력
    // -----------------------------
    int secondTreeCol = col + secondOffset;
    int thirdTreeCol  = secondTreeCol + thirdOffset;

    drawTree(col);
    drawTree(secondTreeCol);
    drawTree(thirdTreeCol);

    // -----------------------------
    // 5) 충돌 체크 (공룡이 땅에 있을 때만)
    // -----------------------------
    if (isDinoOnGround) {
      // 공룡(1,1)에 나무가 걸리면 충돌
      if (col == 1 || secondTreeCol == 1 || thirdTreeCol == 1) {
        handleGameOver();
        isPlaying = false;
        break;        // for 루프 탈출
      }
      // 땅에 떨어지면 공중에서의 버튼 카운트 초기화
      buttonPressedTimesInAir = 0;
    } else {
      // 너무 오래 공중에 있으면 점수 페널티 (원 코드 로직 유지)
      if (buttonPressedTimesInAir > 2) {
        score -= 3;
      }
      buttonPressedTimesInAir++;
    }

    // -----------------------------
    // 6) 프레임마다 점수 증가 + 시리얼 출력
    // -----------------------------
    score++;
    Serial.print("Score: ");
    Serial.println(score);

    delay(200);  // 나무 이동 속도 (200ms당 1칸 이동)
  }
}

// =======================================================
//  게임 오버 처리
//  - LCD에 GAME OVER와 SCORE 표시
//  - 시리얼 모니터에 FINAL SCORE 출력
// =======================================================
void handleGameOver() {
  lcd.clear();

  lcd.setCursor(0, 0);
  lcd.print("  GAME  OVER  ");

  lcd.setCursor(0, 1);
  lcd.print("SCORE: ");
  lcd.print(score);

  // 게임 오버 시 LED도 OFF
  digitalWrite(LED_RED, LOW);

  // 시리얼 모니터에 최종 점수 출력
  Serial.println("=== GAME OVER ===");
  Serial.print("FINAL SCORE: ");
  Serial.println(score);

  // 다음 게임을 위해 점수 초기화
  score = 0;

  delay(2000);
}

// =======================================================
//  나무(장애물) 출력
//  - col 위치가 화면 안에 있을 때만 출력
//  - 바닥 줄은 매 프레임 지우기 때문에
//    여기서는 나무만 찍어주면 됨
// =======================================================
void drawTree(int col) {
  // 화면 밖(왼쪽/오른쪽)인 경우는 그리지 않음
  if (col < 0 || col >= LCD_COLS) {
    return;
  }

  lcd.setCursor(col, 1);  // 두 번째 줄(바닥)
  lcd.write(CHAR_TREE);   // 나무 출력
}

// =======================================================
//  공룡 위치 업데이트
//  - 버튼 상태에 따라 공룡을 땅 또는 공중에 두는 역할
//  - 버튼을 2초 이상 계속 누르고 있으면 게임 오버
// =======================================================
void updateDinoPosition() {
  int buttonState = digitalRead(PIN_BUTTON_JUMP);
  unsigned long now = millis();

  if (buttonState == LOW) {
    // 버튼이 눌린 상태

    if (!jumpButtonLatched) {
      // 방금 눌리기 시작한 순간
      jumpButtonLatched = true;
      jumpPressStartTime = now;  // 눌린 시각 기록
    } else {
      // 이미 누르고 있던 상태 → 누른 시간 누적 확인
      if (now - jumpPressStartTime >= 2000 && isPlaying) {
        // 2초 이상 계속 누르고 있으면 게임 오버 처리
        handleGameOver();
        isPlaying = false;  // 현재 라운드/게임 종료
        return;             // 더 이상 공룡 위치 갱신 안 함
      }
    }

    // 버튼이 눌린 동안에는 항상 공중 상태(점프)
    putDinoInAir();

  } else {
    // 버튼이 눌려 있지 않은 상태 → 지상 상태
    jumpButtonLatched = false;
    jumpPressStartTime = 0;
    putDinoOnGround();
  }
}

// =======================================================
//  공룡을 땅에 두는 함수
//  - LCD (x=1, y=1)에 공룡, 위칸은 공백
//  - 이때 LED는 OFF
// =======================================================
void putDinoOnGround() {
  lcd.setCursor(1, 1);
  lcd.write(CHAR_DINO);   // 바닥에 공룡

  lcd.setCursor(1, 0);
  lcd.print(" ");         // 위 칸 지우기

  isDinoOnGround = true;

  // 땅에 있을 때는 LED OFF
  digitalWrite(LED_RED, LOW);
  Serial.println("DINO: GROUND, LED OFF");
}

// =======================================================
//  공룡을 공중에 두는 함수
//  - LCD (x=1, y=0)에 공룡, 아래칸은 공백
//  - "점프 중" 상태이므로 LED를 ON
// =======================================================
void putDinoInAir() {
  lcd.setCursor(1, 0);
  lcd.write(CHAR_DINO);   // 위 줄에 공룡

  lcd.setCursor(1, 1);
  lcd.print(" ");         // 아래 칸 지우기

  isDinoOnGround = false;

  // 점프(공중 상태)일 때 LED ON
  digitalWrite(LED_RED, HIGH);
  Serial.println("DINO: AIR, LED ON");
}
