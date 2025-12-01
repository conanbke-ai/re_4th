// === OpenWeather API 키 & Flask API 베이스 ===
const API_KEY  = "048e02bd86129621273156bd69dbcd80";
const API_BASE = "http://127.0.0.1:5000"; // Flask 서버 주소

// 헬퍼
const $ = (sel) => document.querySelector(sel);

// DOM 요소들
const input           = $("#city-input");
const searchBtn       = $("#search-btn");
const suggestionsList = $("#city-suggestions");
const currentBtn      = $("#current-btn");
const unitToggleBtn   = $("#unit-toggle");

const loadingBox = $("#loading");
const errorBox   = $("#error");
const weatherBox = $("#weather");

// 표시 영역
const cityNameEl   = $("#city-name");
const regionNameEl = $("#region-name");
const iconEl       = $("#weather-icon");
const tempEl       = $("#temp");
const descEl       = $("#description");
const feelsLikeEl  = $("#feels-like");
const humidityEl   = $("#humidity");
const windEl       = $("#wind");
const pressureEl   = $("#pressure");

// 상태값
let currentWeatherData = null;     // 마지막 날씨 데이터 (항상 metric)
let currentUnit        = "metric"; // 'metric' | 'imperial'
let currentLocation    = null;     // { lat, lon }
let cityList           = [];       // Flask(cities.json)에서 가져오는 도시 리스트

// =========================
//  1. (백업용) 기본 도시 리스트 (Flask 실패 시만 사용)
// =========================
const defaultCityList = [
  // === 한국 주요 도시 ===
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

  // === 일본 ===
  { "name": "Tokyo",       "country": "JP", "lat": 35.6895, "lon": 139.6917 },
  { "name": "Osaka",       "country": "JP", "lat": 34.6937, "lon": 135.5023 },
  { "name": "Yokohama",    "country": "JP", "lat": 35.4437, "lon": 139.6380 },
  { "name": "Nagoya",      "country": "JP", "lat": 35.1815, "lon": 136.9066 },
  { "name": "Sapporo",     "country": "JP", "lat": 43.0621, "lon": 141.3544 },
  { "name": "Fukuoka",     "country": "JP", "lat": 33.5904, "lon": 130.4017 },

  // === 중국/홍콩/대만 ===
  { "name": "Beijing",     "country": "CN", "lat": 39.9042, "lon": 116.4074 },
  { "name": "Shanghai",    "country": "CN", "lat": 31.2304, "lon": 121.4737 },
  { "name": "Guangzhou",   "country": "CN", "lat": 23.1291, "lon": 113.2644 },
  { "name": "Shenzhen",    "country": "CN", "lat": 22.5431, "lon": 114.0579 },
  { "name": "Hong Kong",   "country": "HK", "lat": 22.3193, "lon": 114.1694 },
  { "name": "Taipei",      "country": "TW", "lat": 25.0330, "lon": 121.5654 },

  // === 동남아 ===
  { "name": "Singapore",   "country": "SG", "lat": 1.3521,  "lon": 103.8198 },
  { "name": "Bangkok",     "country": "TH", "lat": 13.7563, "lon": 100.5018 },
  { "name": "Kuala Lumpur","country": "MY", "lat": 3.1390,  "lon": 101.6869 },
  { "name": "Hanoi",       "country": "VN", "lat": 21.0278, "lon": 105.8342 },
  { "name": "Ho Chi Minh City", "country": "VN", "lat": 10.8231, "lon": 106.6297 },
  { "name": "Manila",      "country": "PH", "lat": 14.5995, "lon": 120.9842 },
  { "name": "Jakarta",     "country": "ID", "lat": -6.2088, "lon": 106.8456 },

  // === 인도 ===
  { "name": "Delhi",       "country": "IN", "lat": 28.6139, "lon": 77.2090 },
  { "name": "Mumbai",      "country": "IN", "lat": 19.0760, "lon": 72.8777 },
  { "name": "Bangalore",   "country": "IN", "lat": 12.9716, "lon": 77.5946 },

  // === 중동/서아시아 ===
  { "name": "Dubai",       "country": "AE", "lat": 25.2048, "lon": 55.2708 },
  { "name": "Riyadh",      "country": "SA", "lat": 24.7136, "lon": 46.6753 },
  { "name": "Istanbul",    "country": "TR", "lat": 41.0082, "lon": 28.9784 },
  { "name": "Tehran",      "country": "IR", "lat": 35.6892, "lon": 51.3890 },

  // === 아프리카 ===
  { "name": "Cairo",       "country": "EG", "lat": 30.0444, "lon": 31.2357 },
  { "name": "Lagos",       "country": "NG", "lat": 6.5244,  "lon": 3.3792 },
  { "name": "Nairobi",     "country": "KE", "lat": -1.2921, "lon": 36.8219 },
  { "name": "Johannesburg","country": "ZA", "lat": -26.2041, "lon": 28.0473 },
  { "name": "Cape Town",   "country": "ZA", "lat": -33.9249, "lon": 18.4241 },

  // === 유럽 ===
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

  // === 북미 ===
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

  // === 남미 ===
  { "name": "São Paulo",   "country": "BR", "lat": -23.5558, "lon": -46.6396 },
  { "name": "Rio de Janeiro","country": "BR", "lat": -22.9068, "lon": -43.1729 },
  { "name": "Buenos Aires","country": "AR", "lat": -34.6037, "lon": -58.3816 },
  { "name": "Lima",        "country": "PE", "lat": -12.0464, "lon": -77.0428 },
  { "name": "Santiago",    "country": "CL", "lat": -33.4489, "lon": -70.6693 },

  // === 오세아니아 ===
  { "name": "Sydney",      "country": "AU", "lat": -33.8688, "lon": 151.2093 },
  { "name": "Melbourne",   "country": "AU", "lat": -37.8136, "lon": 144.9631 },
  { "name": "Brisbane",    "country": "AU", "lat": -27.4698, "lon": 153.0251 },
  { "name": "Perth",       "country": "AU", "lat": -31.9523, "lon": 115.8613 },
  { "name": "Auckland",    "country": "NZ", "lat": -36.8485, "lon": 174.7633 }
];

// =========================
//  2. Flask에서 도시 리스트 초기화
// =========================
async function initCityList() {
  try {
    const res = await fetch(`${API_BASE}/cities`);
    if (!res.ok) throw new Error("도시 리스트 로드 실패");

    const data = await res.json();
    if (Array.isArray(data) && data.length > 0) {
      cityList = data;
      console.log("✅ Flask에서 cities 로드, 개수:", cityList.length);
    } else {
      console.warn("Flask cities 비어있음, 기본 리스트 사용");
      cityList = defaultCityList.slice();
    }
  } catch (err) {
    console.warn("Flask 연동 실패, 기본 리스트 사용:", err.message);
    cityList = defaultCityList.slice();
  }
}
initCityList();

// =========================
//  3. 공통 UI 함수
// =========================
function showLoading(show) {
  if (!loadingBox) return;
  loadingBox.classList.toggle("hidden", !show);
}

function showWeather(show) {
  if (!weatherBox) return;
  weatherBox.classList.toggle("hidden", !show);
}

function showError(msg) {
  if (!errorBox) return;
  if (!msg) {
    errorBox.textContent = "";
    errorBox.classList.add("hidden");
  } else {
    errorBox.textContent = msg;
    errorBox.classList.remove("hidden");
  }
}

// 배경 테마 적용
function applyTheme(mainWeather) {
  if (!mainWeather) return;
  const body = document.body;
  body.classList.remove(
    "theme-clear",
    "theme-clouds",
    "theme-rain",
    "theme-snow",
    "theme-thunder"
  );

  const type = mainWeather.toLowerCase();
  if (type.includes("clear")) {
    body.classList.add("theme-clear");
  } else if (type.includes("cloud")) {
    body.classList.add("theme-clouds");
  } else if (type.includes("rain") || type.includes("drizzle")) {
    body.classList.add("theme-rain");
  } else if (type.includes("snow")) {
    body.classList.add("theme-snow");
  } else if (type.includes("thunder")) {
    body.classList.add("theme-thunder");
  }
}

// =========================
//  4. 도시 리스트 유틸
// =========================
function makeCityKey(c) {
  return `${(c.name || "").toLowerCase()}|${(c.country || "").toLowerCase()}`;
}

function addCityToList(name, country, lat, lon) {
  if (!name || typeof lat !== "number" || typeof lon !== "number") return;

  const newCity = { name, country: country || "", lat, lon };
  const key = makeCityKey(newCity);

  const exists = cityList.some((c) => makeCityKey(c) === key);
  if (exists) return;

  cityList.push(newCity);
  console.log("📌 cityList에 새 도시 추가:", name, country);

  // Flask 서버에도 저장 (cities.json 업데이트)
  fetch(`${API_BASE}/cities`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(newCity)
  })
    .then((res) => res.json())
    .then((data) => {
      console.log("서버 저장 결과:", data);
    })
    .catch((err) => {
      console.warn("서버에 도시 저장 실패:", err);
    });
}

function addCityToListFromWeatherData(data) {
  if (!data || !data.name || !data.sys || !data.coord) return;
  addCityToList(data.name, data.sys.country, data.coord.lat, data.coord.lon);
}

// =========================
//  5. Geocoding API 유틸 (추천 + 검색용)
// =========================
async function fetchGeocodeCities(query, limit = 5) {
  const trimmed = (query || "").trim();
  if (!trimmed) return [];

  const url =
    `https://api.openweathermap.org/geo/1.0/direct` +
    `?q=${encodeURIComponent(trimmed)}` +
    `&limit=${limit}` +
    `&appid=${API_KEY}`;

  const res = await fetch(url);
  if (!res.ok) throw new Error("Geocoding API 에러");

  const data = await res.json(); // [{name, country, lat, lon, ...}, ...]
  if (!Array.isArray(data) || data.length === 0) return [];

  return data
    .filter((item) => item && item.name && typeof item.lat === "number" && typeof item.lon === "number")
    .map((item) => ({
      name: item.name,
      country: item.country || "",
      lat: item.lat,
      lon: item.lon
    }));
}

// =========================
//  6. 날씨 조회
// =========================
async function fetchWeatherByCity(city) {
  const trimmed = (city || "").trim();
  if (!trimmed) {
    showError("도시 이름을 입력해주세요.");
    showWeather(false);
    return;
  }

  showLoading(true);
  showError("");
  showWeather(false);

  try {
    const url =
      `https://api.openweathermap.org/data/2.5/weather?q=${encodeURIComponent(trimmed)}` +
      `&appid=${API_KEY}&units=metric&lang=kr`;

    const res = await fetch(url);
    if (!res.ok) {
      if (res.status === 404) throw new Error("해당 도시를 찾을 수 없습니다.");
      throw new Error("날씨 정보를 가져오는 중 오류가 발생했습니다.");
    }

    const data = await res.json();
    currentWeatherData = data;
    currentUnit = "metric";
    if (unitToggleBtn) unitToggleBtn.textContent = "단위: °C";

    addCityToListFromWeatherData(data);
    renderWeather();
  } catch (err) {
    showError(err.message);
  } finally {
    showLoading(false);
  }
}

async function fetchWeatherByCoords(lat, lon) {
  showLoading(true);
  showError("");
  showWeather(false);

  try {
    const url =
      `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}` +
      `&appid=${API_KEY}&units=metric&lang=kr`;
    const res = await fetch(url);
    if (!res.ok) throw new Error("현재 위치 날씨를 불러오지 못했습니다.");

    const data = await res.json();
    currentWeatherData = data;
    currentUnit = "metric";
    if (unitToggleBtn) unitToggleBtn.textContent = "단위: °C";

    addCityToListFromWeatherData(data);
    renderWeather();
  } catch (err) {
    showError(err.message);
  } finally {
    showLoading(false);
  }
}

function toFahrenheit(tempC) {
  return tempC * 1.8 + 32;
}

function renderWeather() {
  if (!currentWeatherData) return;

  const data = currentWeatherData;

  if (cityNameEl)   cityNameEl.textContent   = data.name;
  if (regionNameEl) regionNameEl.textContent = data.sys.country;

  const mainWeather = data.weather[0].main;
  const description = data.weather[0].description;
  const iconCode    = data.weather[0].icon;

  const tempC  = data.main.temp;
  const feelsC = data.main.feels_like;

  let tempDisplay, feelsDisplay, unitLabel;

  if (currentUnit === "metric") {
    tempDisplay  = Math.round(tempC);
    feelsDisplay = Math.round(feelsC);
    unitLabel    = "°C";
  } else {
    tempDisplay  = Math.round(toFahrenheit(tempC));
    feelsDisplay = Math.round(toFahrenheit(feelsC));
    unitLabel    = "°F";
  }

  if (tempEl)      tempEl.textContent      = `${tempDisplay} ${unitLabel}`;
  if (descEl)      descEl.textContent      = description;
  if (feelsLikeEl) feelsLikeEl.textContent = `${feelsDisplay} ${unitLabel}`;
  if (humidityEl)  humidityEl.textContent  = data.main.humidity;
  if (windEl)      windEl.textContent      = data.wind.speed;
  if (pressureEl)  pressureEl.textContent  = data.main.pressure;

  if (iconEl) {
    iconEl.src = `https://openweathermap.org/img/wn/${iconCode}@2x.png`;
    iconEl.alt = description;
  }

  applyTheme(mainWeather);
  showWeather(true);
}

// =========================
//  7. 추천용 유틸 (cities + 위치)
// =========================
function clearSuggestions() {
  if (!suggestionsList) return;
  suggestionsList.innerHTML = "";
  suggestionsList.style.display = "none";
}

function highlightMatch(label, query) {
  const q = query.trim();
  if (!q) return label;

  const lowerLabel = label.toLowerCase();
  const lowerQ     = q.toLowerCase();
  const idx        = lowerLabel.indexOf(lowerQ);

  if (idx === -1) return label;

  const end    = idx + lowerQ.length;
  const before = label.slice(0, idx);
  const match  = label.slice(idx, end);
  const after  = label.slice(end);

  return `${before}<span class="suggestion-highlight">${match}</span>${after}`;
}

function levenshtein(a, b) {
  const m = a.length;
  const n = b.length;
  const dp = Array.from({ length: m + 1 }, () =>
    new Array(n + 1).fill(0)
  );

  for (let i = 0; i <= m; i++) dp[i][0] = i;
  for (let j = 0; j <= n; j++) dp[0][j] = j;

  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      const cost = a[i - 1] === b[j - 1] ? 0 : 1;
      dp[i][j] = Math.min(
        dp[i - 1][j] + 1,
        dp[i][j - 1] + 1,
        dp[i - 1][j - 1] + cost
      );
    }
  }
  return dp[m][n];
}

function distanceKm(lat1, lon1, lat2, lon2) {
  const R = 6371;
  const toRad = (deg) => (deg * Math.PI) / 180;

  const dLat = toRad(lat2 - lat1);
  const dLon = toRad(lon2 - lon1);
  const a =
    Math.sin(dLat / 2) * Math.sin(dLat / 2) +
    Math.cos(toRad(lat1)) *
      Math.cos(toRad(lat2)) *
      Math.sin(dLon / 2) *
      Math.sin(dLon / 2);

  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  return R * c;
}

// 이름이 query와 얼마나 잘 맞는지 점수화 (낮을수록 더 잘 맞음)
function scoreNameForQuery(name, query) {
  const ln = (name || "").toLowerCase();
  const lq = (query || "").toLowerCase();

  if (!ln || !lq) return 9999;

  // 완전 일치 최우선
  if (ln === lq) return -100;

  // 시작 부분 일치 (예: "seo" → "seoul")
  if (ln.startsWith(lq)) return -80;

  // substring 포함 (예: "gree" → "Greece")
  if (ln.includes(lq)) {
    const lenDiff = Math.abs(ln.length - lq.length);
    return -50 + lenDiff;
  }

  // 그 외에는 Levenshtein 거리 기반
  const dist = levenshtein(lq, ln);
  return dist;
}

// cities.json 리스트 기반 문자열 + 오타 보정 추천
function getCitySuggestionsFromList(query, limit = 10) {
  const trimmed = query.trim();
  const lowerQ  = trimmed.toLowerCase();

  if (!trimmed || cityList.length === 0) return [];

  const scored = cityList.map((c) => {
    const name      = c.name || "";
    const lowerName = name.toLowerCase();

    const idxSub = lowerName.indexOf(lowerQ);
    const hasSub = idxSub !== -1;

    const dist = levenshtein(lowerQ, lowerName);
    let score = dist;

    if (lowerName === lowerQ) {
      score -= 5; // 완전 일치
    } else if (idxSub === 0) {
      score -= 3; // 앞부분 substring
    } else if (hasSub) {
      score -= 1; // 중간 substring
    }

    let geoDist = null;
    if (
      currentLocation &&
      typeof c.lat === "number" &&
      typeof c.lon === "number"
    ) {
      geoDist = distanceKm(
        currentLocation.lat,
        currentLocation.lon,
        c.lat,
        c.lon
      );
    }

    return { city: c, score, geoDist };
  });

  scored.sort((a, b) => {
    if (a.score !== b.score) return a.score - b.score;
    const dA = typeof a.geoDist === "number" ? a.geoDist : Infinity;
    const dB = typeof b.geoDist === "number" ? b.geoDist : Infinity;
    return dA - dB;
  });

  return scored.slice(0, limit).map((x) => x.city);
}

// 현재 위치 기준으로 가까운 도시 추천
function getNearbyCitySuggestions(limit = 5) {
  if (!currentLocation || cityList.length === 0) return [];

  const scored = cityList.map((c) => {
    if (typeof c.lat !== "number" || typeof c.lon !== "number") {
      return { city: c, dist: Infinity };
    }
    const d = distanceKm(
      currentLocation.lat,
      currentLocation.lon,
      c.lat,
      c.lon
    );
    return { city: c, dist: d };
  });

  scored.sort((a, b) => a.dist - b.dist);
  return scored.slice(0, limit).map((x) => x.city);
}

// =========================
//  8. 추천 리스트 업데이트
// =========================
let suggestionRequestId = 0;
const MAX_SUGGESTIONS = 10;

async function updateSuggestionsList(query) {
  if (!suggestionsList) return;
  clearSuggestions();

  const trimmed = query.trim();
  if (!trimmed) return;

  const lowerQ = trimmed.toLowerCase();
  const myRequestId = ++suggestionRequestId;

  // 0. "입력값 그대로 검색" 항목
  const keywordLi = document.createElement("li");
  keywordLi.innerHTML = `<span class="history-label">"${trimmed}" 그대로 검색</span>`;
  keywordLi.style.cursor = "pointer";
  keywordLi.style.fontSize = "0.9rem";
  keywordLi.addEventListener("click", () => {
    if (input) input.value = trimmed;
    clearSuggestions();
    searchByCityName(trimmed);
  });
  suggestionsList.appendChild(keywordLi);

  // 1. Geocoding 결과
  let geoCities = [];
  try {
    geoCities = await fetchGeocodeCities(trimmed, 5);
    geoCities.forEach((c) => addCityToList(c.name, c.country, c.lat, c.lon));
  } catch (e) {
    console.warn("Geocoding 추천 실패:", e.message);
  }

  if (myRequestId !== suggestionRequestId) return;

  // 2. cities.json 기반 후보
  const listCities = getCitySuggestionsFromList(trimmed, 10);

  // 3. 위치 기반 후보
  const nearbyCities = getNearbyCitySuggestions(10);

  // 4. 세 그룹을 하나의 후보 풀로 합치고 중복 제거
  const candidateMap = new Map();
  function pushCandidates(arr) {
    arr.forEach((c) => {
      if (!c || !c.name) return;
      const key = makeCityKey(c);
      if (candidateMap.has(key)) return;
      candidateMap.set(key, { city: c });
    });
  }

  pushCandidates(geoCities);
  pushCandidates(listCities);
  pushCandidates(nearbyCities);

  const all = Array.from(candidateMap.values());

  // 5. 이름 기준 그룹 나누기
  const exactPrefix = [];
  const substring   = [];
  const others      = [];

  all.forEach((item) => {
    const nameLower = (item.city.name || "").toLowerCase();
    if (nameLower === lowerQ || nameLower.startsWith(lowerQ)) {
      exactPrefix.push(item);
    } else if (nameLower.includes(lowerQ)) {
      substring.push(item);
    } else {
      others.push(item);
    }
  });

  // 6. others 정렬 (문자열 + 거리)
  others.sort((a, b) => {
    const sa = scoreNameForQuery(a.city.name, trimmed);
    const sb = scoreNameForQuery(b.city.name, trimmed);
    if (sa !== sb) return sa - sb;

    const dA = (currentLocation && typeof a.city.lat === "number" && typeof a.city.lon === "number")
      ? distanceKm(currentLocation.lat, currentLocation.lon, a.city.lat, a.city.lon)
      : Infinity;
    const dB = (currentLocation && typeof b.city.lat === "number" && typeof b.city.lon === "number")
      ? distanceKm(currentLocation.lat, currentLocation.lon, b.city.lat, b.city.lon)
      : Infinity;

    return dA - dB;
  });

  // 7. 전체 추천 순서: exact/prefix → substring → others
  const ordered = [...exactPrefix, ...substring, ...others]
    .slice(0, MAX_SUGGESTIONS);

  // 8. DOM에 뿌리기
  ordered.forEach((item) => {
    const c = item.city;
    const label = `${c.name}, ${c.country || ""}`.trim();

    const li = document.createElement("li");
    li.innerHTML = highlightMatch(label, trimmed);
    li.style.cursor = "pointer";
    li.style.fontSize = "0.9rem";

    li.addEventListener("click", () => {
      if (input) input.value = c.name;
      clearSuggestions();
      fetchWeatherByCoords(c.lat, c.lon);
    });

    suggestionsList.appendChild(li);
  });

  suggestionsList.style.display = "block";
}

// =========================
//  9. 검색 실행
// =========================
async function searchByCityName(query) {
  const raw = (query || "").trim();
  if (!raw) {
    showError("도시 이름을 입력해주세요.");
    showWeather(false);
    return;
  }

  showError("");
  clearSuggestions();

  try {
    // 1) Geocoding 후보 중 가장 문자열상 가까운 도시
    const geoCities = await fetchGeocodeCities(raw, 5);

    if (geoCities.length > 0) {
      geoCities.sort(
        (a, b) => scoreNameForQuery(a.name, raw) - scoreNameForQuery(b.name, raw)
      );
      const best = geoCities[0];
      if (input) input.value = best.name;
      addCityToList(best.name, best.country, best.lat, best.lon);
      await fetchWeatherByCoords(best.lat, best.lon);
      return;
    }

    // 2) cities.json 기반 후보 중 가장 가까운 도시
    const listCities = getCitySuggestionsFromList(raw, 5);
    if (listCities.length > 0) {
      listCities.sort(
        (a, b) => scoreNameForQuery(a.name, raw) - scoreNameForQuery(b.name, raw)
      );
      const best = listCities[0];
      if (input) input.value = best.name;
      await fetchWeatherByCoords(best.lat, best.lon);
      return;
    }

    // 3) 그래도 없으면 입력값 그대로 OpenWeather에 날리기
    await fetchWeatherByCity(raw);
  } catch (err) {
    console.error(err);
    showError(err.message || "도시를 찾는 중 오류가 발생했습니다.");
  }
}

// =========================
// 10. 이벤트 등록
// =========================
let typingTimer;
const TYPING_DELAY = 250;

if (input) {
  input.addEventListener("input", () => {
    const q = input.value;
    clearTimeout(typingTimer);

    if (!q.trim()) {
      clearSuggestions();
      return;
    }

    typingTimer = setTimeout(() => {
      updateSuggestionsList(q);
    }, TYPING_DELAY);
  });

  input.addEventListener("blur", () => {
    setTimeout(clearSuggestions, 150);
  });

  input.addEventListener("keyup", (e) => {
    if (e.key === "Enter") {
      const city = input.value;
      searchByCityName(city);
    }
  });
}

if (searchBtn) {
  searchBtn.addEventListener("click", () => {
    const city = input ? input.value : "";
    searchByCityName(city);
  });
}

if (currentBtn) {
  currentBtn.addEventListener("click", () => {
    if (!navigator.geolocation) {
      showError("이 브라우저에서는 위치 정보를 지원하지 않습니다.");
      return;
    }

    showError("");
    navigator.geolocation.getCurrentPosition(
      (pos) => {
        const { latitude, longitude } = pos.coords;
        currentLocation = { lat: latitude, lon: longitude };
        fetchWeatherByCoords(latitude, longitude);
      },
      () => {
        showError("위치 권한을 허용해야 현재 위치 날씨를 볼 수 있습니다.");
      }
    );
  });
}

if (unitToggleBtn) {
  unitToggleBtn.addEventListener("click", () => {
    if (!currentWeatherData) return;

    currentUnit = currentUnit === "metric" ? "imperial" : "metric";
    unitToggleBtn.textContent =
      currentUnit === "metric" ? "단위: °C" : "단위: °F";
    renderWeather();
  });
}
