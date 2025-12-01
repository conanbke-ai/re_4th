// open_movie.js

const BASE_URL = "https://api.themoviedb.org/3";
const API_KEY = "d40653d9f45c0c0a68900733a9c2b6e7"; // 👉 여기에 본인 키 입력
const IMG_BASE = "https://image.tmdb.org/t/p";

// DOM 요소들
const searchInput = document.querySelector("#search-input");
const searchBtn = document.querySelector("#search-btn");
const suggestionsList = document.querySelector("#search-suggestions");

const movieDetailEl = document.querySelector("#movie-detail");
const searchSectionEl = document.querySelector("#search-section");
const searchListEl = document.querySelector("#search-movie-list");
const searchCountEl = document.querySelector("#search-count");

const popularListEl = document.querySelector("#popular-movie-list");

const errorBanner = document.querySelector("#error-banner");
const loadingOverlay = document.querySelector("#loading-overlay");

let suggestionTimer = null;

// 공통 fetch 함수
async function fetchJson(url, { useLoading = true } = {}) {
  if (useLoading) showLoading();
  hideError();

  try {
    const res = await fetch(url);
    if (!res.ok) {
      throw new Error(`HTTP ${res.status}`);
    }
    return await res.json();
  } catch (err) {
    console.error("API 요청 실패:", err);
    if (useLoading) {
      showError("데이터를 불러오는 중 오류가 발생했습니다. 잠시 후 다시 시도해주세요.");
    }
    return null;
  } finally {
    if (useLoading) hideLoading();
  }
}

function showError(message) {
  errorBanner.textContent = message;
  errorBanner.classList.remove("hidden");
}

function hideError() {
  errorBanner.classList.add("hidden");
}

function showLoading() {
  loadingOverlay.classList.remove("hidden");
}

function hideLoading() {
  loadingOverlay.classList.add("hidden");
}

// 이미지 URL 만들기
function getImageUrl(path, size = "w500") {
  if (!path) return "";
  return `${IMG_BASE}/${size}${path}`;
}

// =======================
// 인기 영화 불러오기
// =======================

async function loadPopularMovies() {
  const url = `${BASE_URL}/movie/popular?api_key=${API_KEY}&language=ko-KR&page=1`;
  const data = await fetchJson(url);
  if (!data || !data.results) return;
  renderMovieList(data.results, popularListEl);
}

// =======================
// 영화 검색
// =======================

async function searchMovies(query) {
  const url = `${BASE_URL}/search/movie?api_key=${API_KEY}&language=ko-KR&query=${encodeURIComponent(
    query
  )}&page=1&include_adult=false`;
  return await fetchJson(url);
}

async function handleSearch() {
  const query = searchInput.value.trim();
  if (!query) {
    alert("검색어를 입력해주세요.");
    return;
  }

  const data = await searchMovies(query);
  if (!data) return;

  const movies = data.results || [];
  renderMovieList(movies, searchListEl);
  searchListEl.classList.toggle("empty", movies.length === 0);

  if (movies.length > 0) {
    searchCountEl.textContent = `${movies.length}건`;
  } else {
    searchCountEl.textContent = "";
  }

  // 첫 검색이면 검색 섹션에 살짝 강조 느낌 주고 싶으면 여기에 클래스 추가도 가능
}

// =======================
// 영화 상세 정보
// =======================

async function loadMovieDetail(movieId) {
  const url = `${BASE_URL}/movie/${movieId}?api_key=${API_KEY}&language=ko-KR`;
  const data = await fetchJson(url);
  if (!data) return;
  renderMovieDetail(data);
}

function renderMovieDetail(movie) {
  const posterUrl = getImageUrl(movie.poster_path, "w500");

  const year = movie.release_date ? movie.release_date.slice(0, 4) : "정보 없음";
  const runtime = movie.runtime ? `${movie.runtime}분` : "정보 없음";
  const vote = movie.vote_average ? movie.vote_average.toFixed(1) : "-";
  const genres =
    movie.genres && movie.genres.length
      ? movie.genres.map((g) => g.name).join(" · ")
      : "장르 정보 없음";

  movieDetailEl.innerHTML = `
    <div class="movie-detail-layout">
      <div class="movie-detail-poster">
        ${
          posterUrl
            ? `<img src="${posterUrl}" alt="${movie.title}" />`
            : `<div class="poster-placeholder">NO IMAGE</div>`
        }
      </div>
      <div class="movie-detail-body">
        <h2 class="movie-detail-title">${movie.title || "제목 없음"}</h2>
        <p class="movie-detail-original">
          원제: ${movie.original_title || "-"}
        </p>

        <div class="movie-detail-meta">
          <span class="movie-detail-rating">${vote} / 10</span>
          <span>개봉: ${year}</span>
          <span>러닝타임: ${runtime}</span>
        </div>

        <div class="movie-detail-genres">
          장르: ${genres}
        </div>

        ${
          movie.tagline
            ? `<p class="movie-detail-tagline">“${movie.tagline}”</p>`
            : ""
        }

        <p class="movie-detail-overview">
          ${
            movie.overview
              ? movie.overview
              : "줄거리 정보가 등록되어 있지 않습니다."
          }
        </p>
      </div>
    </div>
  `;

  movieDetailEl.classList.remove("hidden");
}

// =======================
// 리스트 렌더링
// =======================

function renderMovieList(movies, containerEl) {
  containerEl.innerHTML = "";

  if (!movies || movies.length === 0) {
    return;
  }

  movies.forEach((movie) => {
    const card = document.createElement("article");
    card.className = "movie-card";
    card.dataset.id = movie.id;

    const posterUrl = getImageUrl(movie.poster_path, "w342");
    const year = movie.release_date ? movie.release_date.slice(0, 4) : "N/A";
    const vote = movie.vote_average ? movie.vote_average.toFixed(1) : "-";

    card.innerHTML = `
      <div class="movie-card-poster">
        ${
          posterUrl
            ? `<img src="${posterUrl}" alt="${movie.title}" loading="lazy" />`
            : `<div class="poster-placeholder">NO IMAGE</div>`
        }
        <div class="movie-card-vote">${vote}</div>
      </div>
      <div class="movie-card-body">
        <div class="movie-card-title">${movie.title || "제목 없음"}</div>
        <div class="movie-card-meta">
          <span>${year}</span>
          <span>${movie.original_language?.toUpperCase() || ""}</span>
        </div>
      </div>
    `;

    card.addEventListener("click", () => {
      loadMovieDetail(movie.id);
      window.scrollTo({ top: 0, behavior: "smooth" });
    });

    containerEl.appendChild(card);
  });
}

// =======================
// 자동완성 (날씨앱과 동일 스타일)
// =======================

function clearSuggestions() {
  suggestionsList.innerHTML = "";
  suggestionsList.classList.remove("visible");
}

function renderSuggestions(movies) {
  suggestionsList.innerHTML = "";

  if (!movies || movies.length === 0) {
    suggestionsList.classList.remove("visible");
    return;
  }

  movies.slice(0, 8).forEach((movie) => {
    const li = document.createElement("li");
    li.className = "suggestion-item";

    const year = movie.release_date ? movie.release_date.slice(0, 4) : "";

    li.innerHTML = `
      <span class="suggestion-title">${movie.title}</span>
      <span class="suggestion-meta">${year}</span>
    `;

    li.addEventListener("click", () => {
      searchInput.value = movie.title;
      clearSuggestions();
      // 바로 상세 정보 열기 + 검색 결과에도 반영
      loadMovieDetail(movie.id);
      handleSearch();
    });

    suggestionsList.appendChild(li);
  });

  suggestionsList.classList.add("visible");
}

function setupAutocomplete() {
  searchInput.addEventListener("input", () => {
    const query = searchInput.value.trim();

    if (suggestionTimer) clearTimeout(suggestionTimer);

    if (query.length < 2) {
      clearSuggestions();
      return;
    }

    // 디바운스: 300ms 후 검색
    suggestionTimer = setTimeout(async () => {
      const data = await searchMovies(query);
      if (!data) return;
      renderSuggestions(data.results || []);
    }, 300);
  });

  // 검색창 밖 클릭 시 자동완성 닫기
  document.addEventListener("click", (e) => {
    const isInsideSearchArea = e.target.closest(".search-area");
    if (!isInsideSearchArea) {
      clearSuggestions();
    }
  });
}

// =======================
// 이벤트 & 초기화
// =======================

function setupEvents() {
  searchBtn.addEventListener("click", () => {
    clearSuggestions();
    handleSearch();
  });

  searchInput.addEventListener("keyup", (e) => {
    if (e.key === "Enter") {
      clearSuggestions();
      handleSearch();
    }
  });
}

async function init() {
  setupEvents();
  setupAutocomplete();
  await loadPopularMovies();
}

init();
