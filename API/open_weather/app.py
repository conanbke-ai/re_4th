# pip install flask flask-cors

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
# 모든 origin에서 /cities API 접근 허용 (VSCode Live Server 등)
CORS(app)

CITIES_FILE = "cities.json"

# 기본 도시 리스트 (파일 없을 때 초기값으로 사용)
DEFAULT_CITIES = [
  # === 한국 주요 도시 ===
  { "name": "Seoul",       "country": "KR", "lat": 37.5665, "lon": 126.9780 },
  { "name": "Busan",       "country": "KR", "lat": 35.1796, "lon": 129.0756 },
  { "name": "Incheon",     "country": "KR", "lat": 37.4563, "lon": 126.7052 },
  { "name": "Daegu",       "country": "KR", "lat": 35.8722, "lon": 128.6025 },
  { "name": "Daejeon",     "country": "KR", "lat": 36.3504, "lon": 127.3845 },
  { "name": "Gwangju",     "country": "KR", "lat": 35.1595, "lon": 126.8526 },
  { "name": "Ulsan",       "country": "KR", "lat": 35.5384, "lon": 129.3114 },
  { "name": "Sejong",      "country": "KR", "lat": 36.4800, "lon": 127.2890 },

  { "name": "Suwon",       "country": "KR", "lat": 37.2636, "lon": 127.0286 },
  { "name": "Yongin",      "country": "KR", "lat": 37.2411, "lon": 127.1776 },
  { "name": "Goyang",      "country": "KR", "lat": 37.6584, "lon": 126.8320 },
  { "name": "Seongnam",    "country": "KR", "lat": 37.4200, "lon": 127.1260 },
  { "name": "Anyang",      "country": "KR", "lat": 37.3943, "lon": 126.9568 },
  { "name": "Bucheon",     "country": "KR", "lat": 37.5034, "lon": 126.7660 },
  { "name": "Hwaseong",    "country": "KR", "lat": 37.1996, "lon": 126.8313 },
  { "name": "Namyangju",   "country": "KR", "lat": 37.6360, "lon": 127.2140 },
  { "name": "Pyeongtaek",  "country": "KR", "lat": 36.9907, "lon": 127.0850 },
  { "name": "Gimpo",       "country": "KR", "lat": 37.6176, "lon": 126.7148 },
  { "name": "Gwangmyeong", "country": "KR", "lat": 37.4787, "lon": 126.8644 },
  { "name": "Siheung",     "country": "KR", "lat": 37.3800, "lon": 126.8020 },

  { "name": "Jeju-si",     "country": "KR", "lat": 33.4996, "lon": 126.5312 },
  { "name": "Cheongju",    "country": "KR", "lat": 36.6424, "lon": 127.4890 },
  { "name": "Chuncheon",   "country": "KR", "lat": 37.8813, "lon": 127.7298 },
  { "name": "Wonju",       "country": "KR", "lat": 37.3417, "lon": 127.9202 },
  { "name": "Gangneung",   "country": "KR", "lat": 37.7519, "lon": 128.8761 },
  { "name": "Jeonju",      "country": "KR", "lat": 35.8460, "lon": 127.1297 },
  { "name": "Mokpo",       "country": "KR", "lat": 34.8118, "lon": 126.3922 },
  { "name": "Pohang",      "country": "KR", "lat": 36.0190, "lon": 129.3435 },
  { "name": "Gumi",        "country": "KR", "lat": 36.1195, "lon": 128.3446 },
  { "name": "Changwon",    "country": "KR", "lat": 35.2280, "lon": 128.6810 },
  { "name": "Jinju",       "country": "KR", "lat": 35.1799, "lon": 128.1076 },

  # === 일본 ===
  { "name": "Tokyo",       "country": "JP", "lat": 35.6895, "lon": 139.6917 },
  { "name": "Osaka",       "country": "JP", "lat": 34.6937, "lon": 135.5023 },
  { "name": "Yokohama",    "country": "JP", "lat": 35.4437, "lon": 139.6380 },
  { "name": "Nagoya",      "country": "JP", "lat": 35.1815, "lon": 136.9066 },
  { "name": "Sapporo",     "country": "JP", "lat": 43.0621, "lon": 141.3544 },
  { "name": "Fukuoka",     "country": "JP", "lat": 33.5904, "lon": 130.4017 },

  # === 중국/홍콩/대만 ===
  { "name": "Beijing",     "country": "CN", "lat": 39.9042, "lon": 116.4074 },
  { "name": "Shanghai",    "country": "CN", "lat": 31.2304, "lon": 121.4737 },
  { "name": "Guangzhou",   "country": "CN", "lat": 23.1291, "lon": 113.2644 },
  { "name": "Shenzhen",    "country": "CN", "lat": 22.5431, "lon": 114.0579 },
  { "name": "Hong Kong",   "country": "HK", "lat": 22.3193, "lon": 114.1694 },
  { "name": "Taipei",      "country": "TW", "lat": 25.0330, "lon": 121.5654 },

  # === 동남아 ===
  { "name": "Singapore",   "country": "SG", "lat": 1.3521,  "lon": 103.8198 },
  { "name": "Bangkok",     "country": "TH", "lat": 13.7563, "lon": 100.5018 },
  { "name": "Kuala Lumpur","country": "MY", "lat": 3.1390,  "lon": 101.6869 },
  { "name": "Hanoi",       "country": "VN", "lat": 21.0278, "lon": 105.8342 },
  { "name": "Ho Chi Minh City", "country": "VN", "lat": 10.8231, "lon": 106.6297 },
  { "name": "Manila",      "country": "PH", "lat": 14.5995, "lon": 120.9842 },
  { "name": "Jakarta",     "country": "ID", "lat": -6.2088, "lon": 106.8456 },

  # === 인도 ===
  { "name": "Delhi",       "country": "IN", "lat": 28.6139, "lon": 77.2090 },
  { "name": "Mumbai",      "country": "IN", "lat": 19.0760, "lon": 72.8777 },
  { "name": "Bangalore",   "country": "IN", "lat": 12.9716, "lon": 77.5946 },

  # === 중동/서아시아 ===
  { "name": "Dubai",       "country": "AE", "lat": 25.2048, "lon": 55.2708 },
  { "name": "Riyadh",      "country": "SA", "lat": 24.7136, "lon": 46.6753 },
  { "name": "Istanbul",    "country": "TR", "lat": 41.0082, "lon": 28.9784 },
  { "name": "Tehran",      "country": "IR", "lat": 35.6892, "lon": 51.3890 },

  # === 아프리카 ===
  { "name": "Cairo",       "country": "EG", "lat": 30.0444, "lon": 31.2357 },
  { "name": "Lagos",       "country": "NG", "lat": 6.5244,  "lon": 3.3792 },
  { "name": "Nairobi",     "country": "KE", "lat": -1.2921, "lon": 36.8219 },
  { "name": "Johannesburg","country": "ZA", "lat": -26.2041, "lon": 28.0473 },
  { "name": "Cape Town",   "country": "ZA", "lat": -33.9249, "lon": 18.4241 },

  # === 유럽 ===
  { "name": "London",      "country": "GB", "lat": 51.5074, "lon": -0.1278 },
  { "name": "Paris",       "country": "FR", "lat": 48.8566, "lon": 2.3522 },
  { "name": "Berlin",      "country": "DE", "lat": 52.5200, "lon": 13.4050 },
  { "name": "Rome",        "country": "IT", "lat": 41.9028, "lon": 12.4964 },
  { "name": "Madrid",      "country": "ES", "lat": 40.4168, "lon": -3.7038 },
  { "name": "Barcelona",   "country": "ES", "lat": 41.3851, "lon": 2.1734 },
  { "name": "Amsterdam",   "country": "NL", "lat": 52.3676, "lon": 4.9041 },
  { "name": "Brussels",    "country": "BE", "lat": 50.8503, "lon": 4.3517 },
  { "name": "Vienna",      "country": "AT", "lat": 48.2082, "lon": 16.3738 },
  { "name": "Prague",      "country": "CZ", "lat": 50.0755, "lon": 14.4378 },
  { "name": "Warsaw",      "country": "PL", "lat": 52.2297, "lon": 21.0122 },
  { "name": "Moscow",      "country": "RU", "lat": 55.7558, "lon": 37.6173 },

  # === 북미 ===
  { "name": "New York",    "country": "US", "lat": 40.7128, "lon": -74.0060 },
  { "name": "Los Angeles", "country": "US", "lat": 34.0522, "lon": -118.2437 },
  { "name": "Chicago",     "country": "US", "lat": 41.8781, "lon": -87.6298 },
  { "name": "San Francisco","country": "US","lat": 37.7749, "lon": -122.4194 },
  { "name": "Houston",     "country": "US", "lat": 29.7604, "lon": -95.3698 },
  { "name": "Seattle",     "country": "US", "lat": 47.6062, "lon": -122.3321 },

  { "name": "Toronto",     "country": "CA", "lat": 43.6532, "lon": -79.3832 },
  { "name": "Vancouver",   "country": "CA", "lat": 49.2827, "lon": -123.1207 },
  { "name": "Montreal",    "country": "CA", "lat": 45.5017, "lon": -73.5673 },

  { "name": "Mexico City", "country": "MX", "lat": 19.4326, "lon": -99.1332 },

  # === 남미 ===
  { "name": "São Paulo",   "country": "BR", "lat": -23.5558, "lon": -46.6396 },
  { "name": "Rio de Janeiro","country": "BR", "lat": -22.9068, "lon": -43.1729 },
  { "name": "Buenos Aires","country": "AR", "lat": -34.6037, "lon": -58.3816 },
  { "name": "Lima",        "country": "PE", "lat": -12.0464, "lon": -77.0428 },
  { "name": "Santiago",    "country": "CL", "lat": -33.4489, "lon": -70.6693 },

  # === 오세아니아 ===
  { "name": "Sydney",      "country": "AU", "lat": -33.8688, "lon": 151.2093 },
  { "name": "Melbourne",   "country": "AU", "lat": -37.8136, "lon": 144.9631 },
  { "name": "Brisbane",    "country": "AU", "lat": -27.4698, "lon": 153.0251 },
  { "name": "Perth",       "country": "AU", "lat": -31.9523, "lon": 115.8613 },
  { "name": "Auckland",    "country": "NZ", "lat": -36.8485, "lon": 174.7633 },
]


def load_cities():
    """cities.json을 읽어오고, 없으면 기본 리스트로 생성."""
    if os.path.exists(CITIES_FILE):
        try:
            with open(CITIES_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    return data
        except Exception as e:
            print("Error reading cities.json:", e)

    # 파일이 없거나 깨진 경우 → 기본 리스트 사용 + 파일로 저장
    cities = DEFAULT_CITIES.copy()
    save_cities(cities)
    return cities


def save_cities(cities):
    """도시 리스트를 cities.json에 저장."""
    with open(CITIES_FILE, "w", encoding="utf-8") as f:
        json.dump(cities, f, ensure_ascii=False, indent=2)


def make_key(city):
    name = (city.get("name") or "").lower()
    country = (city.get("country") or "").lower()
    return f"{name}|{country}"


@app.route("/")
def index():
    return "Weather cities API is running."


@app.route("/cities", methods=["GET"])
def get_cities():
    """전체 도시 리스트 반환."""
    cities = load_cities()
    return jsonify(cities)


@app.route("/cities", methods=["POST"])
def add_city():
    """
    도시 추가
    body: { "name": "...", "country": "...", "lat": 37.xxx, "lon": 127.xxx }
    """
    data = request.get_json(force=True) or {}

    name = data.get("name")
    country = data.get("country") or ""
    lat = data.get("lat")
    lon = data.get("lon")

    if name is None or lat is None or lon is None:
        return jsonify({"error": "name, lat, lon은 필수입니다."}), 400

    cities = load_cities()
    new_city = {"name": name, "country": country, "lat": lat, "lon": lon}
    new_key = make_key(new_city)

    for c in cities:
        if make_key(c) == new_key:
            # 이미 있는 도시면 그대로 반환
            return jsonify({"status": "exists", "city": c})

    cities.append(new_city)
    save_cities(cities)
    return jsonify({"status": "added", "city": new_city})


if __name__ == "__main__":
    # http://127.0.0.1:5000
    app.run(debug=True, port=5000)
