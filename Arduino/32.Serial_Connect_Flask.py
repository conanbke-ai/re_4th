# 32.Serial_Connect_Flask.py
# pip install flask flask-cors pyserial

from flask import Flask, request, jsonify, send_from_directory  # ★ send_from_directory 추가
from flask_cors import CORS
import serial
import time
import os  # ★ 파일 경로 계산용

# ===== 경로 설정 =====
# 이 파일(32.Serial_Connect_Flask.py)이 있는 폴더 경로
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ===== 시리얼 설정 =====
SERIAL_PORT = "COM7"   # 실제 아두이노 포트로 바꾸세요 (예: COM3, COM4 등)
BAUD = 9600

# 아두이노 시리얼 포트 오픈
arduino = serial.Serial(SERIAL_PORT, BAUD, timeout=1)
time.sleep(2)  # 보드 리셋 대기

# ===== Flask 앱 설정 =====
app = Flask(__name__)
CORS(app)  # 브라우저/다른 출처에서 접근 허용 (같은 포트 쓰면 사실 없어도 됨)

# 현재 LED 상태를 서버에서 기억 (on / off)
state = "off"


def send_to_arduino(byte_value: bytes) -> int:
    """
    아두이노로 1바이트 명령 전송.
    - byte_value: 예) b"1", b"0"
    - 반환값: 실제로 전송된 바이트 수
    """
    if not arduino.is_open:
        arduino.open()
    sent = arduino.write(byte_value)
    print(f"[SERIAL] write {byte_value!r} ({sent} bytes)")
    return sent


# ===== 1) 메인 페이지: 32.index.html 서빙 =====
@app.route("/")
def index():
    """
    http://127.0.0.1:8000/ 로 접속하면
    같은 폴더(BASE_DIR)에 있는 32.index.html 파일을 돌려줌.
    """
    return send_from_directory(BASE_DIR, "32.index.html")


# ===== 2) LED 제어 API (/led) =====
@app.post("/led")
def led():
    global state

    data = request.get_json(force=True, silent=True) or {}
    print(f"[DEBUG] /led request data = {data!r}")

    desired_raw = data.get("state")
    desired = (desired_raw or "").lower()

    if desired == "on":
        sent = send_to_arduino(b"1")
        state = "on"
        return jsonify({"ok": True, "state": state, "sent_bytes": sent})

    sent = send_to_arduino(b"0")
    prev_state = state
    state = "off"

    if desired == "off":
        return jsonify({"ok": True, "state": state, "sent_bytes": sent})

    return jsonify({
        "ok": False,
        "state": state,
        "prev_state": prev_state,
        "error": "state must be 'on' or 'off'",
        "raw_state": desired_raw,
        "sent_bytes": sent,
    }), 400


if __name__ == "__main__":
    try:
        # 재로딩이 두 번 돌면서 포트를 두 번 여는 걸 막기 위해 use_reloader=False
        app.run(
            host="127.0.0.1",   # 로컬 개발은 127.0.0.1 추천
            port=8000,
            debug=True,
            use_reloader=False,
            threaded=False
        )
    finally:
        # 서버 종료 시(예: Ctrl+C) 마지막으로 LED OFF 명령 한 번 더 전송 후 포트 닫기
        try:
            if arduino.is_open:
                try:
                    arduino.write(b"0")  # 안전하게 LED OFF
                    time.sleep(0.5)
                    print("[INFO] 종료 전 초기화(LED OFF) 명령 전송 완료")
                finally:
                    arduino.close()
                    print(f"[INFO] 시리얼 포트를 닫았습니다. ({SERIAL_PORT})")
        except Exception as e:
            print(f"[WARN] 종료 처리 중 오류: {e}")
