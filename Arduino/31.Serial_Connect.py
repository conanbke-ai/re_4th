"""
아두이노 LED ON/OFF 제어 스크립트
- PC에서 '1' 또는 '0'을 입력하면 시리얼 포트를 통해 아두이노로 전송
- '1' 입력: LED ON
- '0' 입력: LED OFF
- 그 외 입력: 프로그램 종료
"""

import time
import serial  # pyserial 라이브러리 (pip install pyserial 필요)


# ===== 설정 영역 =====
PORT = "COM7"     # 아두이노가 연결된 시리얼 포트 이름 (예: COM3, COM4 등)
BAUDRATE = 9600   # 아두이노 스케치에서 설정한 보레이트와 동일해야 함
DELAY = 1.0       # LED ON/OFF 후 대기 시간(초)


def main():
    """
    아두이노와 시리얼 통신을 열고,
    사용자의 입력에 따라 '1' 또는 '0'을 아두이노로 보내는 메인 함수.
    """
    try:
        # 1. 시리얼 포트 오픈
        #    timeout: 읽기 동작 시 최대 대기 시간(여기서는 사용 안 하지만 관례적으로 많이 둠)
        print(f"[INFO] {PORT} 포트에 {BAUDRATE} 보레이트로 연결 시도 중...")
        arduino = serial.Serial(PORT, BAUDRATE, timeout=1)

        # 2. 아두이노가 리셋될 시간을 약간 기다려줌
        #    (아두이노 보드 대부분은 시리얼 연결 시 리셋이 발생)
        time.sleep(2)
        print(f"[INFO] 아두이노와 연결되었습니다. (포트: {PORT})\n")

        # 3. 사용자 안내 문구 출력
        print("'1'을 입력하면 LED ON, '0'을 입력하면 LED OFF")
        print("그 외 아무 문자열이나 입력하면 프로그램이 종료됩니다.\n")

        # 4. 무한 루프: 사용자가 종료할 때까지 반복
        while True:
            # input()으로 터미널에서 한 줄 입력 받기
            # .strip()으로 앞뒤 공백/개행 제거
            user_input = input("입력 (1=ON, 0=OFF, 기타=종료): ").strip()

            if user_input == "1":
                # 문자열을 바이너리(바이트) 형태로 인코딩해서 전송해야 함
                # 아두이노에서는 Serial.read() 혹은 Serial.readString() 등으로 수신
                sent = arduino.write(b"1")  # user_input.encode('utf-8') 로 써도 동일
                print(f"[ACTION] LED ON 명령 전송, 전송 바이트: {sent}")
                time.sleep(DELAY)

            elif user_input == "0":
                sent = arduino.write(b"0")
                print(f"[ACTION] LED OFF 명령 전송, 전송 바이트: {sent}")
                time.sleep(DELAY)

            else:
                # 1 / 0 이 아닌 다른 값이 들어오면 루프 종료 및 LED 초기화
                sent = arduino.write(b"0")
                print("[INFO] 종료 명령이 입력되어 프로그램을 종료합니다.")
                break

    except serial.SerialException as e:
        # 시리얼 포트가 없거나 사용 중일 때 발생할 수 있는 예외 처리
        print(f"[ERROR] 시리얼 포트를 열 수 없습니다: {e}")

    except KeyboardInterrupt:
        # Ctrl+C 로 강제 종료 시 친절한 메시지 출력
        print("\n[INFO] KeyboardInterrupt 감지. 프로그램을 종료합니다.")

    finally:
        # 시리얼 포트를 열었다면 안전하게 닫아줌
        # ('arduino' 변수가 생성된 경우에만 닫도록 예외 처리)
        try:
            if 'arduino' in locals() and arduino.is_open:
                arduino.close()
                print(f"[INFO] 시리얼 포트를 닫았습니다. (포트: {PORT})")
        except Exception:
            # 닫는 과정에서 문제가 생겨도 프로그램이 죽지 않도록 방어
            pass


# 이 파일을 직접 실행했을 때만 main() 실행
if __name__ == "__main__":
    main()
