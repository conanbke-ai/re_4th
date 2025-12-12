/*
  MPU6050(가속도 + 자이로 센서) I2C 통신 예제

  - I2C(Wire 라이브러리)를 사용해 MPU6050의
    가속도(XYZ), 자이로(XYZ), 내부 온도 값을 읽어서
    시리얼 모니터에 출력하는 코드입니다.
*/

#include <Wire.h>  // 아두이노 I2C 통신 표준 라이브러리

// MPU6050 I2C 통신 주소 (보통 AD0 핀을 GND에 연결하면 0x68)
const int MPU = 0x68;

/*
  - int16_t : 16비트 정수형 타입 (-32768 ~ 32767)
  - AcX, AcY, AcZ : XYZ축의 가속도(raw 값)
  - Tmp          : 센서 내부 온도(raw 값, 공식으로 섭씨로 변환)
  - GyX, GyY, GyZ : XYZ축의 자이로스코프(raw 값)

  ※ 한 줄에 묶어서 선언해도 되고:
    int16_t AcX, AcY, AcZ, Tmp, GyX, GyY, GyZ;
    이렇게 나눠서 선언해도 동작은 동일함.
*/
int16_t AcX, AcY, AcZ;
int16_t Tmp;
int16_t GyX, GyY, GyZ;

void setup() {
  Serial.begin(9600);        // 시리얼 모니터 통신 시작 (9600bps)

  Wire.begin();              // 아두이노 I2C 통신 기능 활성화(마스터 모드)

  // ── MPU6050 슬립 모드 해제 (전원 관리 레지스터 설정) ──
  /*
    Wire.beginTransmission(MPU);
      → I2C 통신을 시작하고, 통신할 장치 주소(0x68)를 지정

    Wire.write(0x6B);
      → 전원 관리 레지스터(PWR_MGMT_1)를 선택

    Wire.write(0);
      → 해당 레지스터(0x6B)에 0을 써서 sleep 모드 해제

    Wire.endTransmission(true);
      → I2C 통신을 끝내면서(Stop 조건) 지금까지 보낸 값들을 실제로 장치에 전송
  */
  Wire.beginTransmission(MPU);  // MPU6050과 통신 시작
  Wire.write(0x6B);             // 전원 관리 레지스터(PWR_MGMT_1) 선택
  Wire.write(0);                // sleep 비트(비트6)를 0으로 → 슬립 해제
  Wire.endTransmission(true);   // I2C 통신 종료 + 명령 전송 완료
}

void loop() {
  // ── 1. 읽기 시작할 레지스터 주소 지정 ──
  /*
    Wire.write(0x3B);

    0x3B 레지스터(ACCEL_XOUT_H)를 "시작점"으로 지정하면,
    그 뒤로 아래 순서대로 2바이트씩 데이터가 쭉 이어서 들어온다.

      0x3B: ACCEL_XOUT_H
      0x3C: ACCEL_XOUT_L
      0x3D: ACCEL_YOUT_H
      0x3E: ACCEL_YOUT_L
      0x3F: ACCEL_ZOUT_H
      0x40: ACCEL_ZOUT_L
      0x41: TEMP_OUT_H
      0x42: TEMP_OUT_L
      0x43: GYRO_XOUT_H
      0x44: GYRO_XOUT_L
      0x45: GYRO_YOUT_H
      0x46: GYRO_YOUT_L
      0x47: GYRO_ZOUT_H
      0x48: GYRO_ZOUT_L

    → 즉, "0x3B부터 14바이트를 읽겠다" 라고 해두고
      Wire.read()를 순서대로 호출하면
      가속도 XYZ, 온도, 자이로 XYZ 값을 차례대로 읽을 수 있음.
  */
  Wire.beginTransmission(MPU);
  Wire.write(0x3B);            // 0x3B 레지스터(ACCEL_XOUT_H)를 시작점으로 지정
  Wire.endTransmission(false); // STOP 없이(repeated start) 연결 유지

  // ── 2. 센서 데이터 14바이트 읽기 요청 ──
  /*
    Wire.requestFrom(장치주소, 읽을바이트수, 끝나면 STOP 여부);

    여기서는
    - MPU(0x68) 주소를 가진 I2C 장치로부터
    - 14바이트를 읽어오고
    - 다 읽었다면 통신을 종료(true)

    라는 의미.

    ※ 왜 14바이트인가?
      - 가속도 X, Y, Z (각 2바이트) → 6바이트
      - 온도 (2바이트)             → 2바이트
      - 자이로 X, Y, Z (각 2바이트) → 6바이트
      총 6 + 2 + 6 = 14바이트
  */
  Wire.requestFrom(MPU, 14, true);

  /*
    MPU6050의 각 센서 값(가속도/자이로/온도)은
    1개 값이 16비트(2바이트, signed int)로 전송된다.

    - I2C는 한 번에 1바이트(8비트)씩만 전송 가능하므로
      Wire.read()를 두 번 호출해서
      상위 바이트(high)와 하위 바이트(low)를 각각 읽어야 한다.

    - 두 바이트를 하나의 16비트 값으로 합칠 때 사용하는 연산:

      <<  : 비트를 왼쪽으로 이동시키는 시프트 연산
            x << n  → x의 비트를 왼쪽으로 n비트 이동,
                     오른쪽 빈 자리는 0으로 채움

      |   : 비트 OR 연산자
            (상위 바이트와 하위 바이트를 합쳐 하나의 값으로 조립할 때 사용)

    예)
      high = Wire.read();      // 상위 8비트
      low  = Wire.read();      // 하위 8비트
      value = (high << 8) | low;
        → high를 왼쪽으로 8비트 옮겨 상위 8비트를 만들고,
          low를 OR 연산으로 합쳐 16비트 값 완성
  */

  // 가속도 X, Y, Z
  AcX = (Wire.read() << 8) | Wire.read();  // 가속도 X축
  AcY = (Wire.read() << 8) | Wire.read();  // 가속도 Y축
  AcZ = (Wire.read() << 8) | Wire.read();  // 가속도 Z축

  // 온도(raw)
  Tmp = (Wire.read() << 8) | Wire.read();  // 센서 내부 온도(raw)

  // 자이로 X, Y, Z
  GyX = (Wire.read() << 8) | Wire.read();  // 자이로 X축
  GyY = (Wire.read() << 8) | Wire.read();  // 자이로 Y축
  GyZ = (Wire.read() << 8) | Wire.read();  // 자이로 Z축

  /*
    Wire.write(0x3B); 로 "0x3B 레지스터부터 읽겠다"라고 지정했기 때문에,
    Wire.read()를 호출할 때마다 순서대로

      AcX, AcY, AcZ, Tmp, GyX, GyY, GyZ

    의 상위/하위 바이트가 들어온다.
    → 시작 레지스터와 읽을 바이트 수(14)를 정확히 맞추면
      값이 섞이거나 순서가 틀어질 일이 없다.
  */

  // 내부 온도(raw -> 섭씨) 변환: 데이터시트 공식
  //   섭씨 온도(°C) = Tmp / 340.0 + 36.53
  float tempC = Tmp / 340.0 + 36.53;

  // ── 3. 시리얼 모니터에 값 출력 ──
  Serial.print("AcX = "); Serial.print(AcX);
  Serial.print(" | AcY = "); Serial.print(AcY);
  Serial.print(" | AcZ = "); Serial.print(AcZ);

  Serial.print(" | Tmp(raw) = "); Serial.print(Tmp);
  Serial.print(" | Tmp(C) = "); Serial.print(tempC);

  Serial.print(" | GyX = "); Serial.print(GyX);
  Serial.print(" | GyY = "); Serial.print(GyY);
  Serial.print(" | GyZ = "); Serial.println(GyZ);

  // 약 0.33초(1초에 3번) 간격으로 측정값 출력
  delay(333);
}
