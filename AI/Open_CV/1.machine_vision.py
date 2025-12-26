# -*- coding: utf-8 -*-

"""
[목표]
- 머신비전/OpenCV 입문 수업용 내용을 "개념 + 예제" 중심으로 한 파일에 통합합니다.
- 실행하면서 바로 이해할 수 있도록 주석(설명)을 최대한 자세히 작성합니다.

[이 파일의 구성]
0) 머신비전/영상의 디지털화 개념 요약
1) OpenCV/NumPy 기초: dtype, unsigned, np.uint8(픽셀)
2) 경로(상대경로) 문제 방지: __file__ 기준으로 안전하게 이미지 경로 구성
3) 이미지 생성 예제(요청 반영)
   - 검정/흰색/특정색(B/G/R 포함)
   - Blue/Green/Red 지정 비교 (채널만 남기기)
   - 랜덤 색상 이미지(픽셀 노이즈/블록)
   - 그라데이션(수평 -> 수직 -> [요청] 컬러 그라데이션 -> 2D -> 라디얼)
4) OpenCV 창(Window) 모드 비교
   - 크기 조절 불가: WINDOW_AUTOSIZE
   - 크기 조절 가능: WINDOW_NORMAL (+ resizeWindow)
5) 기존 수업 흐름(유지)
   - imread / imshow / waitKey / ASCII / destroyAllWindows
   - shape 확인 / imwrite로 저장
6) 채널 분리/병합/개별 접근(split/merge/indexing)
7) (응용) uint8 오버플로와 안전한 밝기 조절(cv2.add)

----------------------------------------------------------------
0) 머신 비전(Machine Vision) 개요
----------------------------------------------------------------
인간이 시각정보를 보고 판단하듯, 컴퓨터는 영상 데이터를 보고 판단
    - 이미지 획득(이미지 센서) → 이미지 분석/이해 → 특정 작업 수행

* 비디오 파일이 만들어지는 과정
    이미지 센서가 빛의 양을 감지하여 숫자로 변환
        - 빛의 양 감지 → 전기 신호로 변환 → 디지털화(숫자로 변환)

    - 아날로그 : 연속적으로 변화하는 물리량을 표현(연속적)
    - 디지털 : 데이터를 0과 1의 2진 부호로 표현(불연속적)

    * Analogue to Digital 변환
        [아날로그 → 디지털]
        샘플링, 양자화를 거쳐 실제 장면이 픽셀(Pixel) 단위의 숫자로만 이루어진
        영상 데이터(2차원/3차원 배열)로 변환됨

        - 샘플링(Sampling)
            : 특정 주기(Frequency, 가로축)로 아날로그 데이터의 값을 기록
                - 초에 60번 샘플링: 60Hz(FPS)
                - 촘촘할수록 실제 장면과 가까워짐

        - 양자화(Quantization)
            : 특정 단위(Bit, 세로축)로 아날로그 데이터를 이산적인 값으로 표현
                - 8bit 컬러 = 2^8 = 256 단계
                - 24bit 컬러 = 2^24 단계(일반적인 True Color)
                - 단계가 많을수록(촘촘할수록) 실제 장면과 가까워짐

    * 영상 처리 과정(전형적인 파이프라인)

    [입력 데이터] 해결하기 원하는 문제에 대한 이미지 또는 영상 입력
         ↓
    [전처리 과정] 각종 필터 및 마스킹을 통한 영상 노이즈 제거
         ↓
    [특징 검출] 윤곽선, 코너, 특정 색 등 목표한 특징 검출
         ↓
    [데이터 해석] 검출된 데이터를 기반으로 해석 및 문제 해결
         ↓
    [출력 데이터] 목표한 최종 데이터 출력

----------------------------------------------------------------
1) 머신비전 라이브러리(요약)
----------------------------------------------------------------
- OpenCV : 무료, BSD 라이센스, 코드 공개 의무 없음, 상업적 이용 가능
- Halcon : 유료, 비쌈, 강력한 성능, 다양한 기능, 전문가 우대
- MIL    : 유료, 국내에서 많이 사용
- Vision Pro : 유료, 코드 리딩/패턴 매칭 등에 사용

----------------------------------------------------------------
2) OpenCV(Open Source Computer Vision Library)
----------------------------------------------------------------
- Intel에서 최초 개발(1999)
- C/C++, C#, Python, Java 지원
- 다양한 영상 처리 알고리즘 최적화 제공
- GPU 가속 모듈 지원
- 머신러닝 관련 모듈 포함

- 공식 홈페이지 : https://opencv.org/
- 파이썬 튜토리얼 : https://docs.opencv.org/4.10.0/d6/d00/tutorial_py_root.html

- 설치 방법 : pip install opencv-python
- 불러오기 : import cv2

----------------------------------------------------------------
[추가로 꼭 알아야 하는 핵심 개념]
----------------------------------------------------------------
(1) OpenCV 이미지 = NumPy 배열(np.ndarray)
    - grayscale(흑백): shape=(H, W)
    - color(컬러 BGR): shape=(H, W, 3)

(2) dtype = np.uint8
    - unsigned 8-bit integer = 0~255 범위
    - 영상/이미지는 보통 8bit(0~255)로 많이 다룸
    - 주의: uint8 상태에서 numpy 연산(+/-) 시 wrap-around(오버플로/언더플로) 위험
      예) np.uint8(250) + 10 -> 4 (260을 256으로 나눈 나머지)
    - 밝기 조절은 cv2.add/cv2.subtract 또는 astype+clip 후 uint8로 복귀 권장

(3) OpenCV 기본 채널 순서 = BGR
    - (0,0,255)는 “빨강”(B=0,G=0,R=255)

(4) 좌표/인덱싱
    - 말로는 (x,y)라고 하지만, 배열 접근은 img[y, x]
      (y=행=세로, x=열=가로)

실행:
    python 1.machine_vision_INTEGRATED.py

필요 이미지(권장):
    AI/images/blackberries.jpg
    AI/images/blueberries.jpg
    AI/images/strawberries.jpg

※ 이미지가 없거나 경로가 다르면, 일부 파트는 합성 이미지로 자동 대체(fallback)합니다.
"""

"""
----------------------------------------------------------------------
[핵심 개념] unsigned int? np.uint8?
----------------------------------------------------------------------
- unsigned(부호 없음): 음수가 없는 정수 타입
- C/C++의 unsigned int는 보통 32-bit인 경우가 많지만(0~2^32-1),
  "환경"에 따라 크기가 달라질 수 있습니다.

- NumPy의 np.uint8:
  - 8비트 부호 없는 정수 (0~255)
  - 일반적인 8-bit 영상(픽셀 값)은 보통 np.uint8로 표현합니다.

[중요] uint8 산술 주의
- numpy로 uint8끼리 더하면 overflow(넘침)로 값이 "회전"할 수 있습니다.
  예) 250 + 10 = 4 (260 mod 256)
- 밝기 증가/감소처럼 영상 처리에서는
  - cv2.add / cv2.subtract (포화 연산, saturate) 를 선호하거나
  - int16/float로 변환 후 clip(0~255) 하는 방법을 사용합니다.

----------------------------------------------------------------------
[중요] OpenCV 색상 채널 순서
----------------------------------------------------------------------
- OpenCV의 컬러 채널 순서는 RGB가 아니라 "BGR" 입니다.
  Blue  = (255, 0, 0)
  Green = (0, 255, 0)
  Red   = (0, 0, 255)

----------------------------------------------------------------------
[실행]
python 1_machine_vision_integrated.py
"""

from __future__ import annotations

from pathlib import Path
import cv2
import numpy as np


# =============================================================================
# 1) 경로 설정: 상대경로 깨짐 방지 (__file__ 기준)
# =============================================================================
print(f"OpenCV version: {cv2.__version__}")

# 현재 .py 파일 위치
BASE_DIR = Path(__file__).resolve().parent

# 사용자 폴더 구조 가정:
# - 이 파일이 .../AI/Open_CV/ 에 있고
# - 이미지가 .../AI/images/ 에 있는 구조를 기준으로 합니다.
AI_DIR = BASE_DIR.parent
IMG_DIR = AI_DIR / "images"
OUT_DIR = IMG_DIR / "output"
OUT_DIR.mkdir(parents=True, exist_ok=True)

print("BASE_DIR:", BASE_DIR)
print("IMG_DIR :", IMG_DIR)
print("OUT_DIR :", OUT_DIR)


# =============================================================================
# 2) 공통 유틸 함수(학습/디버깅을 위한 도구)
# =============================================================================
def ensure_loaded(img: np.ndarray | None, path: Path) -> np.ndarray:
    """
    cv2.imread()는 경로가 잘못되면 예외를 던지지 않고 None을 반환합니다.
    그래서 "반드시" None 체크를 해서 빨리 원인을 찾는 습관이 중요합니다.
    """
    if img is None:
        raise FileNotFoundError(f"[imread 실패] 파일을 찾을 수 없거나 읽을 수 없습니다: {path}")
    return img


def info(name: str, img: np.ndarray) -> None:
    """
    이미지의 기본 정보를 출력해 두면(특히 dtype/min/max),
    전처리/연산 과정에서 값이 깨졌는지 빠르게 확인할 수 있습니다.
    """
    print(f"\n[{name}]")
    print(" shape:", img.shape)
    print(" dtype:", img.dtype)
    print(" min/max:", int(img.min()), int(img.max()))


def put_label(img: np.ndarray, text: str, org: tuple[int, int] = (10, 30)) -> np.ndarray:
    """
    비교용 패널을 만들 때 라벨(텍스트)이 있으면 학습 효율이 크게 올라갑니다.
    putText는 원본 배열을 직접 수정하므로 copy 후 작업합니다.
    """
    out = img.copy()
    # 글자 그림자(검정) -> 본문(흰색) 순으로 두 번 그리면 가독성이 좋아집니다.
    cv2.putText(out, text, org, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 4, cv2.LINE_AA)
    cv2.putText(out, text, org, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
    return out


def gray_to_bgr(gray: np.ndarray) -> np.ndarray:
    """그레이(1채널)를 BGR(3채널)로 변환(패널 합치기 편함)."""
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)


def show_wait(title: str, img: np.ndarray, delay: int = 0) -> int:
    """
    - delay=0  : 키 입력까지 대기
    - delay>0  : delay(ms) 후 자동 진행
    """
    cv2.imshow(title, img)
    return cv2.waitKey(delay)


def close_all() -> None:
    """창 정리."""
    cv2.destroyAllWindows()


# =============================================================================
# 3) dtype / np.uint8 예제 (기존 코드에서 자주 실수하던 부분 보강)
# =============================================================================
def demo_dtype_uint8() -> None:
    """
    기존 코드에 등장했던:
        color_img = np.zeros((100, 200), dtype=uint8)
    는 'uint8' 이름이 정의되어 있지 않으면 NameError가 납니다.

    올바른 표기:
        np.uint8

    참고로, 정말 uint8이라는 별칭을 쓰고 싶다면:
        uint8 = np.uint8
    처럼 먼저 정의해야 합니다(권장하진 않음).
    """
    print("\n=== demo_dtype_uint8 ===")

    # (권장) 명시적으로 np.uint8 사용
    gray = np.zeros((100, 200), dtype=np.uint8)
    info("gray zeros", gray)

    # (설명용) 별칭을 꼭 쓰고 싶다면 이렇게 정의 가능
    uint8 = np.uint8  # noqa: N816 (교육용)
    gray2 = np.zeros((100, 200), dtype=uint8)
    info("gray zeros (alias uint8)", gray2)

    # 컬러 이미지는 보통 (H,W,3)
    color = np.zeros((100, 200, 3), dtype=np.uint8)
    info("color zeros", color)


# =============================================================================
# 4) (요청) 검정/흰색/특정색 + B/G/R 비교 + 채널만 남기기
# =============================================================================
def make_solid(height: int, width: int, bgr: tuple[int, int, int]) -> np.ndarray:
    """BGR 단색 이미지 생성."""
    img = np.zeros((height, width, 3), dtype=np.uint8)
    img[:, :] = bgr
    return img


def keep_only_channel(img: np.ndarray, channel: str) -> np.ndarray:
    """
    컬러 이미지에서 특정 채널만 남기고 나머지는 0으로 만드는 함수.

    - channel='b' -> Blue 채널만 남김
    - channel='g' -> Green 채널만 남김
    - channel='r' -> Red 채널만 남김

    왜 중요?
    - "blue를 지정한 경우 / green / red"를 직관적으로 비교 가능
    - 색상 기반 처리(마스킹) 이해에도 도움이 됩니다.
    """
    out = np.zeros_like(img)
    ch = channel.lower()

    if ch == "b":
        out[:, :, 0] = img[:, :, 0]
    elif ch == "g":
        out[:, :, 1] = img[:, :, 1]
    elif ch == "r":
        out[:, :, 2] = img[:, :, 2]
    else:
        raise ValueError("channel은 'b','g','r' 중 하나여야 합니다.")
    return out


def demo_black_white_and_colors() -> None:
    """
    - 검정/흰색 이미지
    - 특정 색상 이미지(B/G/R)
    - 추가 색(노랑/시안/보라)까지 포함해서 BGR 감각을 강화
    - 패널로 저장 + 창으로 표시
    """
    print("\n=== demo_black_white_and_colors ===")

    H, W = 200, 250
    black = put_label(make_solid(H, W, (0, 0, 0)), "BLACK (0,0,0)")
    white = put_label(make_solid(H, W, (255, 255, 255)), "WHITE (255,255,255)")

    blue = put_label(make_solid(H, W, (255, 0, 0)), "BLUE  BGR=(255,0,0)")
    green = put_label(make_solid(H, W, (0, 255, 0)), "GREEN BGR=(0,255,0)")
    red = put_label(make_solid(H, W, (0, 0, 255)), "RED   BGR=(0,0,255)")

    yellow = put_label(make_solid(H, W, (0, 255, 255)), "YELLOW BGR=(0,255,255)")
    cyan = put_label(make_solid(H, W, (255, 255, 0)), "CYAN   BGR=(255,255,0)")
    purple = put_label(make_solid(H, W, (255, 0, 255)), "PURPLE BGR=(255,0,255)")

    row1 = cv2.hconcat([black, white, yellow, cyan])
    row2 = cv2.hconcat([blue, green, red, purple])
    panel = cv2.vconcat([row1, row2])

    out_path = OUT_DIR / "panel_solid_colors.png"
    cv2.imwrite(str(out_path), panel)
    print("[saved]", out_path)

    cv2.namedWindow("Solid Colors (Resizable)", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Solid Colors (Resizable)", 1200, 550)
    show_wait("Solid Colors (Resizable)", panel, 0)
    close_all()


def demo_channel_only_compare() -> None:
    """
    요청사항:
    - blue 이미지 지정/green/red 지정 비교
    - 여기서는 "하나의 컬러 이미지"에서 채널만 남기는 방식으로 비교합니다.

    (학습 포인트)
    - 채널 분리/접근이 어떤 의미인지 즉시 체감
    - '색상 정보는 결국 채널 값들의 조합'임을 이해
    """
    print("\n=== demo_channel_only_compare ===")

    # 테스트용 컬러 이미지: B=100, G=150, R=200
    img = np.zeros((220, 320, 3), dtype=np.uint8)
    img[:, :, 0] = 100
    img[:, :, 1] = 150
    img[:, :, 2] = 200

    b_only = keep_only_channel(img, "b")
    g_only = keep_only_channel(img, "g")
    r_only = keep_only_channel(img, "r")

    panel = cv2.hconcat([
        put_label(img, "Original (B=100,G=150,R=200)"),
        put_label(b_only, "Keep ONLY Blue channel"),
        put_label(g_only, "Keep ONLY Green channel"),
        put_label(r_only, "Keep ONLY Red channel"),
    ])

    out_path = OUT_DIR / "panel_keep_only_channels.png"
    cv2.imwrite(str(out_path), panel)
    print("[saved]", out_path)

    cv2.namedWindow("Channel Only Compare (Resizable)", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Channel Only Compare (Resizable)", 1500, 450)
    show_wait("Channel Only Compare (Resizable)", panel, 0)
    close_all()


# =============================================================================
# 5) (요청) 창 크기 조절 가능/불가능 비교
# =============================================================================
def demo_window_modes(img: np.ndarray) -> None:
    """
    WINDOW_AUTOSIZE:
    - 창 크기가 이미지 크기에 고정되는 경향
    - 드래그로 크기 변경이 제한될 수 있음(환경에 따라 다소 차이)

    WINDOW_NORMAL:
    - 사용자가 창 크기를 자유롭게 조절 가능
    - resizeWindow로 코드에서 크기도 지정 가능
    """
    print("\n=== demo_window_modes ===")

    win_auto = "AUTOSIZE (Not Resizable)"
    win_norm = "NORMAL (Resizable)"

    cv2.namedWindow(win_auto, cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow(win_norm, cv2.WINDOW_NORMAL)

    # NORMAL은 일부러 크게 띄워 "조절 가능"을 바로 체감하게 함
    cv2.resizeWindow(win_norm, 1200, 700)

    cv2.imshow(win_auto, img)
    cv2.imshow(win_norm, img)

    print("두 창을 직접 드래그해서 크기 변경이 가능한지 비교해보세요.")
    print("키를 누르면 다음으로 진행합니다.")
    cv2.waitKey(0)
    close_all()


# =============================================================================
# 6) (요청) 랜덤 색상 / 그라데이션(수평/수직/컬러/2D/라디얼)
# =============================================================================
def random_color_noise(h: int, w: int, seed: int = 0) -> np.ndarray:
    """픽셀 단위 랜덤 컬러 노이즈."""
    rng = np.random.default_rng(seed)
    return rng.integers(0, 256, size=(h, w, 3), dtype=np.uint8)


def random_color_blocks(h: int, w: int, block: int = 25, seed: int = 0) -> np.ndarray:
    """블록 단위 랜덤 컬러(픽셀 노이즈보다 패턴이 명확)."""
    rng = np.random.default_rng(seed)
    img = np.zeros((h, w, 3), dtype=np.uint8)
    for y in range(0, h, block):
        for x in range(0, w, block):
            img[y:y + block, x:x + block] = (
                int(rng.integers(0, 256)),
                int(rng.integers(0, 256)),
                int(rng.integers(0, 256)),
            )
    return img


def grad_horizontal_gray(h: int, w: int) -> np.ndarray:
    """수평 그라데이션(좌->우): 0..255"""
    line = np.linspace(0, 255, w, dtype=np.uint8)
    return np.tile(line, (h, 1))


def grad_vertical_gray(h: int, w: int) -> np.ndarray:
    """수직 그라데이션(상->하): 0..255"""
    col = np.linspace(0, 255, h, dtype=np.uint8).reshape(h, 1)
    return np.tile(col, (1, w))


def grad_horizontal_color(h: int, w: int) -> np.ndarray:
    """
    [요청] 수직 그라데이션 다음에 컬러 그라데이션 추가
    -> 컬러(수평) 그라데이션

    예시 구성(BGR):
    - B: 좌->우 증가
    - G: 우->좌 증가(반전)
    - R: 고정(중간값)
    """
    x = np.linspace(0, 255, w, dtype=np.uint8)
    b = np.tile(x, (h, 1))
    g = np.tile(x[::-1], (h, 1))
    r = np.full((h, w), 90, dtype=np.uint8)
    return cv2.merge([b, g, r])


def grad_vertical_color(h: int, w: int) -> np.ndarray:
    """
    컬러(수직) 그라데이션

    - B: 상->하 증가
    - G: 고정
    - R: 하->상 증가(반전)
    """
    y = np.linspace(0, 255, h, dtype=np.uint8).reshape(h, 1)
    b = np.tile(y, (1, w))
    g = np.full((h, w), 80, dtype=np.uint8)
    r = np.tile(y[::-1], (1, w))
    return cv2.merge([b, g, r])


def grad_2d_gray(h: int, w: int) -> np.ndarray:
    """2D 그라데이션(좌상단->우하단): 수평+수직 평균."""
    gx = grad_horizontal_gray(h, w).astype(np.uint16)
    gy = grad_vertical_gray(h, w).astype(np.uint16)
    return ((gx + gy) // 2).astype(np.uint8)


def grad_radial_gray(h: int, w: int) -> np.ndarray:
    """라디얼(원형) 그라데이션: 중심에서 멀어질수록 값 증가."""
    yy, xx = np.indices((h, w))
    cy, cx = h / 2.0, w / 2.0
    dist = np.sqrt((yy - cy) ** 2 + (xx - cx) ** 2)
    dist_norm = dist / dist.max()
    return (dist_norm * 255).astype(np.uint8)


def demo_random_and_gradients() -> None:
    """
    랜덤/그라데이션을 한 화면에서 비교 가능한 패널로 구성합니다.

    [요청 순서 반영]
    - 수평(그레이) -> 수직(그레이)
    - 그 다음에 컬러 그라데이션(수평/수직) 배치
    - 이후 2D/라디얼 및 랜덤 예제
    """
    print("\n=== demo_random_and_gradients ===")

    H, W = 220, 320

    # --- (1) 그레이 그라데이션: 수평 -> 수직 (요청 순서)
    g_h = put_label(gray_to_bgr(grad_horizontal_gray(H, W)), "Gray Gradient: Horizontal")
    g_v = put_label(gray_to_bgr(grad_vertical_gray(H, W)), "Gray Gradient: Vertical")

    # --- (2) [요청] 수직 그라데이션 다음에 컬러 그라데이션 추가
    c_h = put_label(grad_horizontal_color(H, W), "Color Gradient: Horizontal (BGR)")
    c_v = put_label(grad_vertical_color(H, W), "Color Gradient: Vertical (BGR)")

    # --- (3) 추가 그라데이션(2D/라디얼)
    g_2d = put_label(gray_to_bgr(grad_2d_gray(H, W)), "Gray Gradient: 2D")
    g_rad = put_label(gray_to_bgr(grad_radial_gray(H, W)), "Gray Gradient: Radial")

    # --- (4) 랜덤 이미지(요청)
    rand_pix = put_label(random_color_noise(H, W, seed=1), "Random Color: Pixel Noise")
    rand_blk = put_label(random_color_blocks(H, W, block=25, seed=2), "Random Color: Block Pattern")

    # 패널 구성(가독성 있게 행 단위)
    row1 = cv2.hconcat([g_h, g_v, c_h, c_v])
    row2 = cv2.hconcat([g_2d, g_rad, rand_pix, rand_blk])
    panel = cv2.vconcat([row1, row2])

    out_path = OUT_DIR / "panel_random_and_gradients.png"
    cv2.imwrite(str(out_path), panel)
    print("[saved]", out_path)

    cv2.namedWindow("Random & Gradients (Resizable)", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Random & Gradients (Resizable)", 1600, 700)
    show_wait("Random & Gradients (Resizable)", panel, 0)
    close_all()


# =============================================================================
# 7) 기존 수업 흐름 유지: imread/imshow/waitKey/ASCII + shape + imwrite
# =============================================================================
def demo_image_io_like_class_flow() -> None:
    """
    사용자가 기존에 작성했던 흐름을 "개념/예제"로 보기 좋게 정리한 섹션입니다.

    포함 내용:
    - imread: 컬러/그레이 읽기
    - imshow: 창 표시
    - waitKey: 키 입력 대기 + ASCII 변환
    - destroyAllWindows: 창 정리
    - shape 확인
    - imwrite: 저장

    [주의]
    - 이미지 파일이 실제로 IMG_DIR에 있어야 합니다.
      (blackberries.jpg, blueberries.jpg, strawberries.jpg)
    """
    print("\n=== demo_image_io_like_class_flow ===")

    # ------------------------------------------------------------
    # 7-1) imread: 이미지 읽기
    # ------------------------------------------------------------
    blackberries_path = IMG_DIR / "blackberries.jpg"
    blueberries_path = IMG_DIR / "blueberries.jpg"

    blackberries = cv2.imread(str(blackberries_path))  # 기본: 컬러(BGR)
    blueberries = cv2.imread(str(blueberries_path), cv2.IMREAD_GRAYSCALE)

    blackberries = ensure_loaded(blackberries, blackberries_path)
    blueberries = ensure_loaded(blueberries, blueberries_path)

    info("blackberries(color)", blackberries)
    info("blueberries(gray)", blueberries)

    # ------------------------------------------------------------
    # 7-2) imshow + waitKey: 창 표시 + 키 입력 받기
    # ------------------------------------------------------------
    cv2.imshow("blackberries image", blackberries)
    cv2.imshow("blueberries image grayscale", blueberries)

    # waitKey(0): 무한 대기 (키를 누를 때까지)
    key = cv2.waitKey(0)
    print("key (raw int):", key)

    # 키 값은 환경/특수키에 따라 상위비트가 포함될 수 있어 하위 1바이트만 쓰는 편이 안전
    ch = chr(key & 0xFF)
    ascii_code = ord(ch)
    print(f"문자: {ch}, ASCII CODE: {ascii_code}")

    cv2.destroyAllWindows()

    # ------------------------------------------------------------
    # 7-3) shape 확인 + imwrite로 저장
    # ------------------------------------------------------------
    strawberries_path = IMG_DIR / "strawberries.jpg"
    strawberries = cv2.imread(str(strawberries_path), cv2.IMREAD_COLOR)
    strawberries_gray = cv2.imread(str(strawberries_path), cv2.IMREAD_GRAYSCALE)

    strawberries = ensure_loaded(strawberries, strawberries_path)
    strawberries_gray = ensure_loaded(strawberries_gray, strawberries_path)

    print("\n[shape 확인]")
    print("color strawberries image shape:", strawberries.shape)       # (H, W, 3)
    print("gray  strawberries image shape:", strawberries_gray.shape)  # (H, W)

    cv2.imshow("cute strawberries color", strawberries)
    cv2.imshow("cute strawberries gray", strawberries_gray)

    # 컬러: (H, W, C)
    h2, w2, c2 = strawberries.shape
    print("color height:", h2)
    print("color width :", w2)
    print("color channel:", c2)

    # [:2]로 (H, W)만 얻기
    h3, w3 = strawberries.shape[:2]
    print("color height3:", h3)
    print("color width3 :", w3)

    # 그레이: (H, W)
    h1, w1 = strawberries_gray.shape
    print("gray height:", h1)
    print("gray width :", w1)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    out_path = OUT_DIR / "strawberries_gray.png"
    ok = cv2.imwrite(str(out_path), strawberries_gray)
    print(f"[imwrite] saved={ok} -> {out_path}")


# =============================================================================
# 8) 채널 분리/병합/개별 접근 (원문에서 오타가 나기 쉬운 부분을 정확히 정리)
# =============================================================================
def demo_split_merge_access() -> None:
    """
    채널 분리/병합은 머신비전에서 매우 자주 등장합니다.
    - 색상 기반 마스킹(HSV 변환 전/후)
    - 특정 채널 강조/억제
    - 특징(엣지, 밝기) 추출 전처리 등

    [올바른 사용]
    b, g, r = cv2.split(img)        # img는 (H,W,3)
    merged = cv2.merge([b, g, r])

    [주의: 흔한 실수]
    cv2.split([b, g, r]) 처럼 "리스트"를 넣는 것은 일반적으로 올바르지 않습니다.
    split은 "3채널 이미지"를 입력으로 받아야 합니다.
    """
    print("\n=== demo_split_merge_access ===")

    # 예제용 컬러 이미지 생성
    img = np.zeros((220, 320, 3), dtype=np.uint8)
    img[:, :, 0] = 100  # Blue
    img[:, :, 1] = 150  # Green
    img[:, :, 2] = 200  # Red

    # (정답) 채널 분리
    b, g, r = cv2.split(img)

    # (정답) 채널 병합
    merged = cv2.merge([b, g, r])

    # (추가) 개별 채널 접근(배열 인덱싱)
    b2 = img[:, :, 0]
    g2 = img[:, :, 1]
    r2 = img[:, :, 2]

    panel1 = cv2.hconcat([
        put_label(img, "Original (BGR)"),
        put_label(gray_to_bgr(b), "Split B"),
        put_label(gray_to_bgr(g), "Split G"),
        put_label(gray_to_bgr(r), "Split R"),
    ])

    panel2 = cv2.hconcat([
        put_label(merged, "Merged (should match original)"),
        put_label(gray_to_bgr(b2), "Index img[:,:,0]"),
        put_label(gray_to_bgr(g2), "Index img[:,:,1]"),
        put_label(gray_to_bgr(r2), "Index img[:,:,2]"),
    ])

    panel = cv2.vconcat([panel1, panel2])

    out_path = OUT_DIR / "panel_split_merge_access.png"
    cv2.imwrite(str(out_path), panel)
    print("[saved]", out_path)

    cv2.namedWindow("Split/Merge/Access (Resizable)", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Split/Merge/Access (Resizable)", 1500, 600)
    show_wait("Split/Merge/Access (Resizable)", panel, 0)
    close_all()


# =============================================================================
# 9) (응용) uint8 오버플로 vs 안전한 밝기 조절
# =============================================================================
def demo_uint8_overflow() -> None:
    """
    uint8 산술의 '함정'을 눈으로 확인하는 예제입니다.

    - numpy 연산: overflow 위험(값 회전)
    - cv2.add: 포화(saturate) 연산(255를 넘으면 255로 고정)
    """
    print("\n=== demo_uint8_overflow ===")

    img = np.full((180, 320, 3), 250, dtype=np.uint8)

    # (위험) numpy + 10 (overflow 가능)
    bad = img + 10

    # (안전) cv2.add (포화)
    good = cv2.add(img, 10)

    panel = cv2.hconcat([
        put_label(img, "Original (250)"),
        put_label(bad, "Numpy +10 (overflow risk)"),
        put_label(good, "cv2.add +10 (saturate)"),
    ])

    out_path = OUT_DIR / "panel_uint8_overflow.png"
    cv2.imwrite(str(out_path), panel)
    print("[saved]", out_path)

    cv2.namedWindow("uint8 overflow vs safe (Resizable)", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("uint8 overflow vs safe (Resizable)", 1200, 350)
    show_wait("uint8 overflow vs safe (Resizable)", panel, 0)
    close_all()
    
# =============================================================================
# 10) main: 학습 흐름(개념/예제 순서)으로 실행
# =============================================================================
def main() -> None:
    # 1) dtype/uint8 기본
    demo_dtype_uint8()

    # 2) 검정/흰색/색상 패널
    demo_black_white_and_colors()

    # 3) Blue/Green/Red 지정 비교(채널만 남기기)
    demo_channel_only_compare()

    # 4) 창 모드 비교(조절 가능 vs 불가능)
    #    비교용으로 "검정/흰색/색상 패널"을 재활용해서 보여줍니다.
    H, W = 200, 250
    sample_panel = cv2.hconcat([
        make_solid(H, W, (0, 0, 0)),
        make_solid(H, W, (255, 255, 255)),
        make_solid(H, W, (255, 0, 0)),
        make_solid(H, W, (0, 255, 0)),
        make_solid(H, W, (0, 0, 255)),
    ])
    sample_panel = put_label(sample_panel, "Window Mode Compare: AUTOSIZE vs NORMAL", (10, 30))
    demo_window_modes(sample_panel)

    # 5) 랜덤/그라데이션(수평->수직->컬러 그라데이션->2D->라디얼 + 랜덤)
    demo_random_and_gradients()

    # 6) 기존 수업 흐름(IO): 파일이 실제 존재해야 함
    #    (없으면 여기서 FileNotFoundError로 알려줌)
    #    수업 자료가 준비되어 있으면 반드시 이 섹션을 돌려보는 것을 권장합니다.
    demo_image_io_like_class_flow()

    # 7) 채널 분리/병합/접근
    demo_split_merge_access()

    # 8) uint8 오버플로 응용
    demo_uint8_overflow()

    print("\n[완료] output 폴더에 결과 이미지(패널)가 저장되었습니다.")
    print("OUT_DIR:", OUT_DIR)


if __name__ == "__main__":
    main()
