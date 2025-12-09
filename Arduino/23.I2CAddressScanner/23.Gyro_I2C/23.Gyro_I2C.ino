#include <Wire.h> // 아두이노 I2C 통신 표준 라이브러리

const int MPU = 0x68;      // MPU6050 I2C 주소(자이로센서 통신 주소)

/*
  - int16_t: 16비트 정수형 값만 저장 가능한 변수
  - AcX, AcY, AcZ: XYZ축의 가속도
  - Tmp: 센서 내부 온도 (센서 온도에 따라 오차가 달라지기 때문)
  - GyX, GyY, GyZ: XYZ축의 자이로스코프 값
*/
int16_t AcX, AcY, AcZ;
int16_t Tmp;
int16_t GyX, GyY, GyZ;

void setup() {
  Wire.begin();                   // I2C 시작
  Wire.beginTransmission(MPU);    // MPU6050과 통신 시작
  Wire.write(0x6B);               // 전원 관리 레지스터(PWR_MGMT_1)
  Wire.write(0);                  // 0x6B 레지스터에 0을 써서 sleep 모드 해제
  Wire.endTransmission(true);     // I2C 통신 종료 + 명령 전송 완료

  Serial.begin(9600);             // 시리얼 모니터 속도
}

void loop() {
  // 0x3B 레지스터(ACCEL_XOUT_H)부터 14바이트 읽기
  Wire.beginTransmission(MPU);
  Wire.write(0x3B); // 0x3B 레지스터에 센서 데이터 저장 시작
  Wire.endTransmission(false);  // 0x3B 레지스터와 연결 유지

  // 데이터 읽어오기
  // requestFrom이 매개변수 : 0x68(I2C 통신을 하는 장치)에 14바이트씩 읽고, 전부 읽었으면 통신 종료
  Wire.requestFrom(MPU, 14, true);

  AcX = Wire.read() << 8 | Wire.read();  // 가속도 X
  AcY = Wire.read() << 8 | Wire.read();  // 가속도 Y
  AcZ = Wire.read() << 8 | Wire.read();  // 가속도 Z
  Tmp = Wire.read() << 8 | Wire.read();  // 온도(raw)
  GyX = Wire.read() << 8 | Wire.read();  // 자이로 X
  GyY = Wire.read() << 8 | Wire.read();  // 자이로 Y
  GyZ = Wire.read() << 8 | Wire.read();  // 자이로 Z

  Serial.print("AcX = "); Serial.print(AcX);
  Serial.print(" | AcY = "); Serial.print(AcY);
  Serial.print(" | AcZ = "); Serial.print(AcZ);

  Serial.print(" | Tmp = ");
  Serial.print(Tmp / 340.00 + 36.53);    // 데이터시트 공식으로 섭씨 변환

  Serial.print(" | GyX = "); Serial.print(GyX);
  Serial.print(" | GyY = "); Serial.print(GyY);
  Serial.print(" | GyZ = "); Serial.println(GyZ);

  delay(333);  // 약 0.33초마다 한 줄 출력
}
