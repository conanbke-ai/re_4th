# wifi_server.py
# pip install flask flask-cors

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 다른 출처(브라우저 / ESP 등)에서 접근 허용

@app.get("/data")
def get_data():
    """
    ESP-01(아두이노)에서
      GET /data?temperature=25&humidity=60
    이런 식으로 요청하면 여기로 들어옵니다.
    """
    params = dict(request.args)  # 쿼리스트링을 dict로 변환
    print("[GET /data] params =", params)

    # 여기서 DB 저장, 파일 기록, 추가 처리 등 원하는 걸 하면 됨
    # 예: temp = float(params.get("temperature", 0))
    #     hum  = float(params.get("humidity", 0))

    return jsonify(ok=True, received=params)


if __name__ == "__main__":
    # 0.0.0.0:5000 으로 서버 오픈
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
        use_reloader=False,
        threaded=False,
    )
