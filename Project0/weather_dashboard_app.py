# -------------------------------
# weather_dashboard_app.py
# -------------------------------
from flask import Flask, render_template, request, redirect
import requests
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from datetime import datetime, timedelta
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

# -------------------------------
# 1. 기상청 예보 API
# -------------------------------
def get_forecast(service_key, nx, ny):
    now = datetime.now()
    base_date = now.strftime("%Y%m%d")
    hour = now.hour
    available_times = [2,5,8,11,14,17,20,23]
    base_time = None
    for h in reversed(available_times):
        if hour >= h:
            base_time = f"{h:02d}00"
            break
    if base_time is None:
        yesterday = now - timedelta(days=1)
        base_date = yesterday.strftime("%Y%m%d")
        base_time = "2300"

    url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst"
    params = {
        "serviceKey": service_key,
        "pageNo": "1",
        "numOfRows": "1000",
        "dataType": "JSON",
        "base_date": base_date,
        "base_time": base_time,
        "nx": str(nx),
        "ny": str(ny)
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    items = data["response"]["body"]["items"]["item"]

    forecast = {}
    for item in items:
        if item["category"] in ["T1H","REH","WSD","PTY","POP"]:
            t = item["fcstTime"]
            if t not in forecast:
                forecast[t] = {}
            forecast[t][item["category"]] = float(item["fcstValue"])
    return forecast

# -------------------------------
# 2. 데이터 전처리
# -------------------------------
def prepare_dataset(forecast, features=["T1H","REH","WSD","PTY","POP"], look_back=24):
    sorted_times = sorted(forecast.keys())
    data = []
    for t in sorted_times:
        row = [forecast[t].get(f, 0) for f in features]
        data.append(row)
    data = np.array(data)

    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(data)

    X = []
    for i in range(len(scaled) - look_back):
        X.append(scaled[i:i+look_back])
    return np.array(X), scaler, sorted_times[look_back:], data[look_back:]

# -------------------------------
# 3. LSTM 모델
# -------------------------------
def build_lstm(input_shape):
    model = Sequential([
        LSTM(64, activation="tanh", input_shape=input_shape),
        Dense(32, activation="relu"),
        Dense(input_shape[1])
    ])
    model.compile(optimizer="adam", loss="mse")
    return model

# -------------------------------
# 4. 알림 및 아이콘
# -------------------------------
def pty_to_icon(pty):
    mapping = {0:"☀️",1:"🌧️",2:"🌦️",3:"❄️",4:"⛈️"}
    return mapping.get(int(pty),"❓")

def generate_alerts(pred_real):
    alerts = []
    for v in pred_real:
        temp, hum, wind, pty, pop = v
        msg = ""
        if pty == 4 or pop>70:
            msg += "⚠️ 폭우/강한 강수 "
        if wind >= 8:
            msg += "💨 강풍 "
        if temp >= 35:
            msg += "🔥 폭염 "
        elif temp <= 0:
            msg += "❄️ 한파 "
        alerts.append(msg.strip())
    return alerts

# -------------------------------
# 5. 이메일 발송
# -------------------------------
def send_email(sender, password, receiver, subject, html_content):
    msg = MIMEMultipart('alternative')
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.attach(MIMEText(html_content, 'html'))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())

# -------------------------------
# 6. 웹 라우팅
# -------------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        location = request.form.get("location")
        email = request.form.get("email")
        # 좌표 변환 (예: 서울 기준 nx=60, ny=127)
        # 실제 구현 시 외부 API 또는 DB로 변환 가능
        NX, NY = 60, 127

        SERVICE_KEY = "본인의_API_KEY_입력"
        forecast = get_forecast(SERVICE_KEY, NX, NY)
        X, scaler, times, obs_real = prepare_dataset(forecast)
        model = build_lstm(X.shape[1:])
        model.fit(X, X[:,-1,:], epochs=30, batch_size=8, verbose=0)
        last_seq = X[-1].reshape(1, X.shape[1], X.shape[2])
        pred_scaled = model.predict(last_seq)
        pred_real = scaler.inverse_transform(pred_scaled)

        temps  = [v[0] for v in pred_real]
        humidity= [v[1] for v in pred_real]
        wind   = [v[2] for v in pred_real]
        ptys   = [v[3] for v in pred_real]
        pops   = [v[4] for v in pred_real]
        alerts = generate_alerts(pred_real)

        html_dashboard = render_template(
            "dashboard.html",
            times=times[:len(pred_real)],
            temps=temps,
            humidity=humidity,
            wind=wind,
            ptys=ptys,
            pops=pops,
            alerts=alerts
        )

        # 이메일 발송
        SENDER = "your_email@gmail.com"
        PASSWORD = "앱 비밀번호"
        RECEIVER = email
        send_email(SENDER, PASSWORD, RECEIVER, "📊 스마트 날씨 대시보드", html_dashboard)

        return html_dashboard
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
