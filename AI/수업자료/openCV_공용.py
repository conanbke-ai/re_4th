# -*- coding: utf-8 -*-
"""
openCV_공용.py
================================================================================
공용 유틸(Utilities) 모음  —  "학습 노트(A 버전: 설명 중심)" 에디션

이 파일은 OpenCV 학습/실습 코드(여러 .py 파일)에서 공통으로 사용하는 기능을 담습니다.

왜 "공용 유틸"을 따로 두나?
--------------------------------------------------------------------------------
OpenCV 예제를 작성하다 보면 아래 코드가 거의 매번 반복됩니다.

1) cv2 / numpy 임포트 및 설치 여부 확인
2) 이미지/비디오 입력(파일 또는 웹캠) 처리
3) imshow(창 띄우기) + waitKey(키 입력/이벤트 루프) 패턴
4) q 또는 ESC로 종료하는 표준 루프
5) --demo / --list 같은 CLI 인자 파싱 및 데모 선택 실행

학습용 스크립트는 "개념/예제"가 핵심이므로,
이런 반복 코드를 공통 모듈로 빼두면 다음 장점이 있습니다.

- 각 주제 파일이 짧고, 핵심 로직(예: threshold, blur, contour)에 집중할 수 있음
- 실습 환경(윈도우/맥/리눅스, 웹캠 유무, 샘플 이미지 유무)이 달라도
  예제가 쉽게 깨지지 않도록 방어적 코딩(Defensive Coding)을 한 곳에서 제공
- 모든 데모가 같은 UX(종료 키, 창 리사이즈, 자동 샘플 탐색)를 공유하므로 학습 피로가 줄어듦

이 버전(A)은 "학습 노트" 스타일:
--------------------------------------------------------------------------------
- 각 함수/모듈에 대해 다음을 최대한 설명합니다.
  (1) 목적(왜 필요한가)
  (2) 입력(파라미터)의 의미와 범위/제약
  (3) 반환값(있다면)
  (4) 흔한 실수/주의사항
  (5) 사용 예시(짧은 스니펫)

작성일: 2025-12-26
"""

from __future__ import annotations

import argparse
import os
import sys
import time
from dataclasses import dataclass
from typing import Optional, Tuple, List, Dict, Callable, Any

# =============================================================================
# 1) OpenCV / NumPy 임포트(설치/환경 이슈를 친절히 안내하기 위한 패턴)
# -----------------------------------------------------------------------------
# - OpenCV는 보통 "opencv-python" 패키지를 설치하면 "cv2" 이름으로 import 됩니다.
# - NumPy는 OpenCV 이미지(행렬) 데이터를 다루는 데 사실상 표준 라이브러리입니다.
# 왜 try/except 로 감싸나?
# - import 단계에서 실패하면 Python은 즉시 예외를 던지고 프로그램이 종료됩니다.
# - 학습 환경에서는 "왜 실패했는지"와 "어떻게 해결하는지"를 알려주는 것이 중요합니다.
# - 그래서 실패 원인을 변수에 저장해 두었다가, require_*() 함수에서
#   "해결 가이드 포함 메시지"로 RuntimeError를 발생시키는 방식을 사용합니다.
# =============================================================================
try:
    import cv2  # type: ignore
except Exception as e:  # pragma: no cover
    cv2 = None  # type: ignore
    _CV2_IMPORT_ERROR = e
else:
    _CV2_IMPORT_ERROR = None

try:
    import numpy as np
except Exception as e:  # pragma: no cover
    np = None  # type: ignore
    _NP_IMPORT_ERROR = e
else:
    _NP_IMPORT_ERROR = None


# =============================================================================
# 2) 예외/환경 체크 유틸(require_*)
# -----------------------------------------------------------------------------
# 목적:
# - cv2 또는 numpy가 설치되지 않았거나(또는 가상환경이 잘못 선택되었거나),
#   로딩이 실패했을 때 "친절한 안내"와 함께 즉시 종료시키기.
# 학습용으로 중요한 이유:
# - 초보자 환경에서는 가장 흔한 문제들이 "설치/가상환경/IDE 인터프리터" 이슈이므로,
#   문제를 빠르게 진단할 수 있는 메시지가 큰 도움이 됩니다.
# =============================================================================
def require_cv2() -> Any:
    """
    cv2(OpenCV)가 임포트되지 않았을 때 친절한 오류를 발생시킵니다.

    반환값
    -------
    cv2 모듈 객체

    흔한 실패 원인/해결
    -------------------
    1) 설치 안 됨:
       - pip install opencv-python

    2) 가상환경/인터프리터 불일치:
       - VSCode의 Python Interpreter가 다른 venv를 가리키는지 확인

    3) GUI(창) 문제:
       - 원격 서버/WSL/헤드리스 환경에서는 imshow가 동작하지 않을 수 있음
         (이 경우 import는 성공해도 창이 안 뜨거나 프리징되는 문제가 생길 수 있습니다.)
    """
    if cv2 is None:
        raise RuntimeError(
            "OpenCV(cv2) 임포트 실패.\n"
            "1) pip install opencv-python\n"
            "2) (GUI 환경) OS/권한/원격환경에서 imshow가 안 될 수 있음\n"
            f"원인: {_CV2_IMPORT_ERROR}"
        )
    return cv2


def require_np() -> Any:
    """
    numpy가 임포트되지 않았을 때 친절한 오류를 발생시킵니다.

    반환값
    -------
    numpy 모듈 객체

    해결
    ----
    - pip install numpy
    """
    if np is None:
        raise RuntimeError(
            "NumPy(np) 임포트 실패.\n"
            "pip install numpy\n"
            f"원인: {_NP_IMPORT_ERROR}"
        )
    return np


# =============================================================================
# 3) 비디오 입력 소스 판별(웹캠 인덱스 vs 파일 경로)
# -----------------------------------------------------------------------------
# OpenCV에서 비디오 입력은 cv2.VideoCapture(...) 로 받습니다.
# - 웹캠: cv2.VideoCapture(0)   ← 정수 인덱스
# - 파일: cv2.VideoCapture("C:/path/video.mp4")  ← 문자열 경로
# 그래서 CLI로 --source 를 받을 때는 문자열로 들어오므로,
# "숫자 문자열인지"를 보고 웹캠 인덱스로 해석할지 결정합니다.
# 주의:
# - isdigit()는 "0", "1" 같은 순수 숫자 문자열만 True 입니다.
# - " 0" (공백 포함), "-1" (음수), "0\n" 같은 형태는 False가 될 수 있습니다.
#   (학습용에서는 단순 패턴으로 두되, 필요하면 strip/try-except로 개선할 수 있습니다.)
# =============================================================================
def is_camera_source(src: str) -> bool:
    """
    문자열 입력이 카메라 인덱스인지(예: '0', '1') 판별합니다.

    입력
    ----
    src: str
        사용자가 CLI로 입력한 --source 문자열

    반환
    ----
    bool
        True면 웹캠 인덱스(정수)로 처리 가능
    """
    return src.isdigit()


def parse_source_to_capture_arg(src: str) -> Any:
    """
    --source 인자(문자열)를 cv2.VideoCapture에 넣을 수 있는 형태로 변환합니다.

    규칙
    ----
    - "0", "1" 같은 숫자 문자열이면 int로 변환하여 웹캠 인덱스로 사용
    - 그 외 문자열이면 파일 경로로 간주하여 그대로 반환

    예시
    ----
    parse_source_to_capture_arg("0")            -> 0
    parse_source_to_capture_arg("Videos/a.mp4") -> "Videos/a.mp4"
    """
    return int(src) if is_camera_source(src) else src


# =============================================================================
# 4) 안전한 imshow / waitKey 패턴
# -----------------------------------------------------------------------------
# OpenCV GUI는 환경에 따라 동작이 다릅니다.
# - 로컬 PC(Windows/Mac/Linux 데스크톱): 대부분 정상
# - 원격 서버/WSL/헤드리스: 창이 안 뜨거나, waitKey에서 멈추는 현상 가능
# - 일부 IDE(특히 원격 확장): imshow 창이 포커스를 못 받거나 입력이 안 될 수 있음
# 또한 중요한 사실:
# - cv2.imshow()는 "그리는 함수"일 뿐이고, 실제 OS 이벤트 루프가 돌기 위해서는
#   반드시 cv2.waitKey(...)가 주기적으로 호출되어야 합니다.
# 따라서 예제에서는:
# - 창 크기 조절 가능한 WINDOW_NORMAL 옵션 제공
# - 키 입력(q/ESC)으로 종료하는 패턴을 표준화
# - imshow + waitKey를 한 번에 묶어 실수 가능성을 줄임
# =============================================================================
def safe_named_window(winname: str, resizable: bool = True) -> None:
    """
    OpenCV 윈도우를 안전하게 생성합니다.

    입력
    ----
    winname: str
        창 제목/식별자
    resizable: bool (default=True)
        True  -> cv2.WINDOW_NORMAL  (사용자가 창 크기 조절 가능)
        False -> cv2.WINDOW_AUTOSIZE(이미지 크기에 맞춰 고정)

    왜 이 옵션이 중요한가?
    -----------------------
    고해상도 이미지(예: 1920x1080)를 AUTOSIZE로 띄우면 화면 밖으로 나갈 수 있습니다.
    학습/디버깅에는 resizable 창이 훨씬 편합니다.
    """
    cv = require_cv2()
    flags = cv.WINDOW_NORMAL if resizable else cv.WINDOW_AUTOSIZE
    cv.namedWindow(winname, flags)


def safe_imshow(winname: str, img: Any, resizable: bool = True, wait: int = 1) -> int:
    """
    imshow + waitKey를 한 번에 수행하고, 누른 키 코드를 반환합니다.

    입력
    ----
    winname: str
        창 이름(윈도우 핸들 역할)
    img: Any (보통 numpy.ndarray)
        OpenCV가 표시할 이미지(행렬)

        이미지 데이터의 "표준 형태"를 꼭 기억하세요:
        - 컬러(BGR): shape = (H, W, 3), dtype=uint8, 값 범위 0~255
        - 그레이:    shape = (H, W),    dtype=uint8, 값 범위 0~255

        dtype이 float인 경우(0~1 등)도 가능하지만,
        학습 초반에는 uint8을 기본으로 두는 것이 혼란을 줄입니다.
    resizable: bool
        창 크기 조절 여부
    wait: int (default=1)
        cv2.waitKey(wait)로 대기할 ms
        - wait=0  : 키 입력이 있을 때까지 무한 대기(정지)
        - wait=1~ : 이벤트 루프를 돌리며 매우 짧게 대기(실시간 루프에 적합)

    반환
    ----
    int
        사용자가 누른 키 코드(0~255로 정규화됨)

    주의
    ----
    - imshow만 호출하면 창이 "갱신되지 않을 수" 있습니다.
      최소한 waitKey(1)이라도 호출해 OS 이벤트 처리가 일어나도록 해야 합니다.
    """
    cv = require_cv2()
    safe_named_window(winname, resizable=resizable)
    cv.imshow(winname, img)
    return cv.waitKey(wait) & 0xFF


def close_all_windows() -> None:
    """
    모든 OpenCV 창을 닫습니다.

    주의
    ----
    일부 환경에서는 destroyAllWindows가 예외를 던지는 경우가 있어
    학습용 코드에서는 try/except로 감쌉니다.
    """
    cv = require_cv2()
    try:
        cv.destroyAllWindows()
    except Exception:
        # 일부 환경에서 destroyAllWindows가 예외를 던지기도 함
        pass


def close_window(winname: str) -> None:
    """
    특정 창(winname)만 닫습니다.

    입력
    ----
    winname: str
        닫을 창의 이름(생성 시 사용한 동일 문자열)
    """
    cv = require_cv2()
    try:
        cv.destroyWindow(winname)
    except Exception:
        pass


# =============================================================================
# 5) 이미지 생성(실습용 더미 데이터)
# -----------------------------------------------------------------------------
# 실습 환경에 샘플 이미지가 없는 경우에도, 아래 함수들로 테스트 이미지를 만들어
# "개념을 재현 가능한 형태"로 연습할 수 있습니다.
# 예) 블러/이진화/모폴로지 같은 기본 영상처리 실습은
#     외부 이미지가 없어도 그라데이션/도형/노이즈로 충분히 체험할 수 있습니다.
def make_blank(
    width: int = 640,
    height: int = 480,
    color_bgr: Tuple[int, int, int] = (0, 0, 0),
) -> Any:
    """
    지정한 색상(BGR)으로 채워진 빈 캔버스를 생성합니다.

    입력
    ----
    width, height: int
        생성할 이미지의 크기
    color_bgr: (B, G, R)
        0~255 범위의 정수 튜플
        - OpenCV 기본은 BGR 순서라는 점이 중요합니다.

    반환
    ----
    numpy.ndarray (H, W, 3), dtype=uint8

    사용 예시
    --------
    img = make_blank(800, 600, (20, 20, 20))
    cv2.circle(img, (400,300), 80, (0,0,255), -1)
    """
    np_ = require_np()
    img = np_.zeros((height, width, 3), dtype=np_.uint8)
    img[:] = color_bgr
    return img


def make_random_noise(width: int = 640, height: int = 480) -> Any:
    """
    랜덤 노이즈 이미지를 생성합니다.

    - 각 픽셀의 B/G/R 값이 0~255 범위에서 무작위로 선택됩니다.
    - 블러/노이즈 제거(denoise) 데모에서 원본과 혼합해 효과를 비교하기 좋습니다.

    반환
    ----
    numpy.ndarray (H, W, 3), dtype=uint8
    """
    np_ = require_np()
    img = np_.random.randint(0, 256, (height, width, 3), dtype=np_.uint8)
    return img


def make_gradient(
    width: int = 640,
    height: int = 480,
    direction: str = "horizontal",
    start_bgr: Tuple[int, int, int] = (0, 0, 0),
    end_bgr: Tuple[int, int, int] = (255, 255, 255),
) -> Any:
    """
    그라데이션(색상 점진 변화) 이미지를 생성합니다.

    입력
    ----
    direction: str
        - 'horizontal': 좌 -> 우 방향으로 색이 변함
        - 'vertical'  : 상 -> 하 방향으로 색이 변함
    start_bgr, end_bgr: (B, G, R)
        시작/끝 색상

    내부 원리(학습 포인트)
    ----------------------
    - 0~1 범위의 t를 linspace로 만들고,
      start*(1-t) + end*t 형태로 선형 보간(Linear Interpolation)을 합니다.
    - float32로 계산 후 0~255로 clip, 마지막에 uint8로 변환합니다.

    반환
    ----
    numpy.ndarray (H, W, 3), dtype=uint8
    """
    np_ = require_np()
    if direction not in ("horizontal", "vertical"):
        raise ValueError("direction must be 'horizontal' or 'vertical'")

    start = np_.array(start_bgr, dtype=np_.float32)
    end = np_.array(end_bgr, dtype=np_.float32)

    if direction == "horizontal":
        t = np_.linspace(0.0, 1.0, width, dtype=np_.float32)  # (W,)
        # (W,3): 각 x 위치마다 BGR 색상을 계산
        line = (start[None, :] * (1 - t[:, None]) + end[None, :] * t[:, None])
        # (H,W,3): 위에서 만든 1줄을 height만큼 복제
        img = np_.tile(line[None, :, :], (height, 1, 1))
    else:
        t = np_.linspace(0.0, 1.0, height, dtype=np_.float32)  # (H,)
        col = (start[None, :] * (1 - t[:, None]) + end[None, :] * t[:, None])
        img = np_.tile(col[:, None, :], (1, width, 1))

    return np_.clip(img, 0, 255).astype(np_.uint8)



def make_checkerboard(
    width: int = 500,
    height: int = 500,
    square: int = 50,
    *,
    as_bgr: bool = False,
    v0: int = 0,
    v1: int = 255,
) -> Any:
    """
    체크보드(체스판) 패턴을 생성합니다.

    왜 필요하나요?
    - 카메라 캘리브레이션(체스보드 코너 검출) 전 "패턴 이해"에 도움이 됩니다.
    - 이진화/필터링/에지 검출 등의 결과가 잘 보이는 '규칙적 테스트 이미지'로도 유용합니다.

    파라미터
    - width, height: 출력 이미지 크기(px)
    - square: 한 칸(사각형) 한 변의 길이(px)
      * 예) square=50이면 50x50 픽셀 단위로 흑/백이 번갈아 배치됩니다.
    - as_bgr: True면 (H,W) 그레이스케일이 아니라 (H,W,3) BGR 컬러로 반환합니다.
    - v0, v1: 흑/백 값(기본 0/255). 필요하면 대비를 낮출 수도 있습니다.

    반환
    - 그레이스케일: uint8, shape=(height, width)
    - BGR: uint8, shape=(height, width, 3)

    구현 아이디어(NumPy)
    - 각 픽셀이 '몇 번째 사각형'에 속하는지 계산:
        y_index = (np.arange(height) // square)
        x_index = (np.arange(width)  // square)
      두 인덱스의 합을 2로 나누면(%) 흑/백이 교차합니다.
    """
    np_ = require_np()
    cv = require_cv2()

    if square <= 0:
        raise ValueError("square는 1 이상의 정수여야 합니다.")

    # y: (H,1), x: (1,W) 형태로 만들어 브로드캐스팅을 유도합니다.
    y = (np_.arange(height, dtype=np_.int32) // square)[:, None]
    x = (np_.arange(width, dtype=np_.int32) // square)[None, :]

    board = (y + x) % 2  # 0/1 패턴
    img = (board * (v1 - v0) + v0).astype(np_.uint8)

    if as_bgr:
        img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
    return img




def bgr_to_rgb(img: Any) -> Any:
    """
    OpenCV(BGR) -> RGB 변환

    왜 필요하나?
    ------------
    - OpenCV는 기본 색상 순서가 BGR입니다.
    - 반면, PIL/Matplotlib는 기본이 RGB인 경우가 많습니다.
    - 두 라이브러리를 섞어 쓰면 색이 "뒤집혀 보이는" 문제가 자주 발생합니다.

    반환
    ----
    RGB 이미지 (numpy.ndarray)
    """
    cv = require_cv2()
    return cv.cvtColor(img, cv.COLOR_BGR2RGB)


def bgr_to_gray(img: Any) -> Any:
    """
    BGR 컬러 이미지를 그레이스케일(1채널)로 변환합니다.

    왜 그레이로 바꾸나?
    --------------------
    - threshold, Canny, 많은 특징 추출 알고리즘은 1채널 입력이 표준인 경우가 많습니다.
    - 조명/색상 정보를 제거하고 밝기 구조에 집중하는 처리에 유리합니다.

    반환
    ----
    gray 이미지 (H,W) 형태, dtype=uint8 (일반적)
    """
    cv = require_cv2()
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# =============================================================================
# 6) 샘플 이미지/비디오 자동 탐색(auto_find_*)
# -----------------------------------------------------------------------------
# 학습 폴더 구조가 사람마다 조금씩 다를 수 있습니다.
# 예:
#   AI/
#     Images/
#     Videos/
# 데모 스크립트에서 --image 또는 --source를 생략해도 동작하도록
# 주변 폴더에서 이미지/영상 파일을 찾아 "첫 번째 후보"를 반환합니다.
# 주의(학습 팁):
# - os.walk는 폴더가 매우 큰 경우 느릴 수 있습니다.
# - 학습용에서는 편의성이 중요하므로 단순 구현을 사용합니다.
# =============================================================================
_IMAGE_EXTS = (".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff", ".webp")
_VIDEO_EXTS = (".mp4", ".avi", ".mov", ".mkv", ".wmv", ".webm")


def find_first_file(root: str, exts: Tuple[str, ...]) -> Optional[str]:
    """
    root 폴더 아래를 재귀 탐색(os.walk)하여, 지정 확장자 중 첫 파일을 반환합니다.

    입력
    ----
    root: str
        탐색을 시작할 디렉터리
    exts: tuple[str, ...]
        허용 확장자 목록(소문자 기준으로 endswith 검사)

    반환
    ----
    str | None
        발견한 첫 파일의 전체 경로, 없으면 None
    """
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            if fn.lower().endswith(exts):
                return os.path.join(dirpath, fn)
    return None


def auto_find_image(start_dir: str = ".") -> Optional[str]:
    """
    start_dir 기준으로 이미지 파일을 자동 탐색합니다.

    우선순위(가정)
    --------------
    1) ./Images
    2) ./images
    3) ./AI/Images, ./ai/images 등 흔한 폴더명
    4) 그 외: start_dir 전체 재귀 탐색

    반환
    ----
    str | None
        이미지 파일 경로(첫 후보) 또는 None
    """
    # 우선순위: ./Images -> ./images -> 현재 폴더 전체
    for cand in ["Images", "images", "AI/Images", "ai/Images", "ai/images"]:
        p = os.path.join(start_dir, cand)
        if os.path.isdir(p):
            f = find_first_file(p, _IMAGE_EXTS)
            if f:
                return f
    return find_first_file(start_dir, _IMAGE_EXTS)


def auto_find_video(start_dir: str = ".") -> Optional[str]:
    """
    start_dir 기준으로 비디오 파일을 자동 탐색합니다.

    우선순위
    --------
    1) ./Videos, ./videos
    2) ./AI/Videos, ./ai/videos
    3) 그 외: start_dir 전체 재귀 탐색
    """
    for cand in ["Videos", "videos", "AI/Videos", "ai/Videos", "ai/videos"]:
        p = os.path.join(start_dir, cand)
        if os.path.isdir(p):
            f = find_first_file(p, _VIDEO_EXTS)
            if f:
                return f
    return find_first_file(start_dir, _VIDEO_EXTS)


# =============================================================================
# 7) CLI(Demo Runner) 공용 파서
# -----------------------------------------------------------------------------
# 데모 파일들은 보통 다음처럼 실행됩니다.
#   python ./AI/수업자료/14.openCV_영상처리_기초.py --list
#   python ./AI/수업자료/14.openCV_영상처리_기초.py --demo 05 --image ./Images/sample.jpg
# 이때 매 파일마다 argparse 코드를 반복 작성하면 코드가 지저분해집니다.
# 그래서 공통 파서를 만들고, 데모 목록 및 실행 로직도 표준화합니다.
# =============================================================================
@dataclass
class Demo:
    """
    데모 하나를 정의하는 데이터 구조(학습용 라우팅 테이블의 한 행)

    필드
    ----
    key: str
        실행 키(예: "01", "05")
    title: str
        --list 출력용 설명
    fn: Callable[..., None]
        실제 실행 함수. 보통 fn(args) 형태로 사용합니다.
    """
    key: str
    title: str
    fn: Callable[..., None]


def build_cli_parser(title: str) -> argparse.ArgumentParser:
    """
    데모 실행을 위한 공통 CLI 파서를 생성합니다.

    입력
    ----
    title: str
        argparse description에 들어갈 제목(설명)

    제공 인자(학습용 표준)
    ---------------------
    --list
        데모 목록을 출력합니다.
    --demo <key>
        실행할 데모 key(예: 01, 02...)
        * 학습 UX: demo를 안 주면 기본 데모(보통 '00')가 실행됩니다.
        (선택) --menu를 주면 대화형으로 선택할 수 있습니다.
    --image <path>
        이미지 기반 데모 입력 파일
        * 없으면 데모 코드가 auto_find_image / 더미 이미지 생성으로 처리 가능
    --source <path|index>
        비디오 기반 데모 입력 소스
        * "0" 같은 숫자 문자열은 웹캠 인덱스로 해석 가능(parse_source_to_capture_arg 참고)
    --save <path>
        결과 저장 경로(선택)
        * 데모 함수에서 args.save를 참고하여 이미지/영상 저장 기능을 확장할 수 있습니다.

    반환
    ----
    argparse.ArgumentParser
    """
    p = argparse.ArgumentParser(description=title)
    p.add_argument("--list", action="store_true", help="데모 목록 출력")
    p.add_argument("--menu", action="store_true", help="(대화형) 데모 선택 메뉴 표시")
    p.add_argument("--demo", type=str, default="", help="실행할 데모 key (예: 00) / 여러 개는 콤마로 지정(예: 00,03,05) / 범위 지정(예: 02-06) / all=전체 실행")
    p.add_argument("--image", type=str, default="", help="입력 이미지 경로(선택)")
    p.add_argument("--source", type=str, default="", help="비디오 소스(파일 경로 또는 카메라 인덱스 '0')")
    p.add_argument("--save", type=str, default="", help="결과 저장 경로(선택)")
    return p


def run_demos(demos: List[Demo], args: argparse.Namespace) -> None:
    """데모 목록 출력/실행 라우팅.

    --demo 문법
      - 단일: 05
      - 콤마: 00,03,05
      - 범위: 02-06  (포함)
      - 혼합: 00-03,05,07-09
      - 전체: all
      - 생략: 기본('00' 또는 첫 데모)

    참고: 각 데모는 보통 imshow 창에서 'q' 또는 ESC로 종료하도록 구성되어 있어,
    여러 데모를 연속 실행해도 데모별로 종료 후 다음으로 넘어갑니다.
    """
    if not demos:
        print('[ERROR] no demos configured.')
        return

    default_key = '00' if any(d.key == '00' for d in demos) else demos[0].key

    def _print_list() -> None:
        print()
        print('[Demo List]')
        for d in demos:
            print(f'  - {d.key}: {d.title}')
        print()
        print('Examples:')
        print('  python ./AI/수업자료/<파일명>.py                 (기본 데모 실행)')
        print('  python ./AI/수업자료/<파일명>.py --demo 00')
        print('  python ./AI/수업자료/<파일명>.py --demo 00,03,05')
        print('  python ./AI/수업자료/<파일명>.py --demo 02-06')
        print('  python ./AI/수업자료/<파일명>.py --demo 00-03,05,07-09')
        print('  python ./AI/수업자료/<파일명>.py --demo all')
        print('  python ./AI/수업자료/<파일명>.py --menu')
        print('  python ./AI/수업자료/<파일명>.py --list')

    if getattr(args, 'list', False):
        _print_list()
        return

    lookup: Dict[str, Demo] = {d.key: d for d in demos}
    demo_sel = (getattr(args, 'demo', '') or '').strip()

    # --demo 생략 시: 기본 데모
    if not demo_sel:
        demo_sel = default_key

        # 대화형 메뉴(선택): TTY에서만
        if getattr(args, 'menu', False) and bool(getattr(sys, 'stdin', None)) and sys.stdin.isatty():
            _print_list()
            try:
                user_in = input(f'Select demo (Enter={default_key}, 예: 00,03,02-06, all, q=종료): ').strip()
            except EOFError:
                user_in = ''

            if user_in.lower() in ('q', 'quit', 'exit'):
                return
            if user_in:
                demo_sel = user_in

    numeric_key_lengths = [len(k) for k in lookup.keys() if k.isdigit()]
    pad_width = max(numeric_key_lengths) if numeric_key_lengths else 0

    def _normalize_numeric(n: int) -> str:
        if pad_width > 0:
            k = str(n).zfill(pad_width)
            if k in lookup:
                return k
        k = str(n)
        if k in lookup:
            return k
        k2 = str(n).zfill(2)
        return k2 if k2 in lookup else k

    def _normalize_single_key(k: str) -> str:
        k = k.strip()
        if k in lookup:
            return k
        if k.isdigit():
            try:
                n = int(k)
            except ValueError:
                return k
            k_pad = _normalize_numeric(n)
            return k_pad if k_pad in lookup else k
        return k

    def _expand_selection(sel: str) -> List[str]:
        sel = sel.strip()
        if not sel:
            return [default_key]
        if sel.lower() == 'all':
            return ['all']

        tokens = [t.strip() for t in sel.split(',') if t.strip()]
        out: List[str] = []

        for tok in tokens:
            if tok.lower() == 'all':
                out.append('all')
                continue

            if '-' in tok:
                a, b = tok.split('-', 1)
                a = a.strip()
                b = b.strip()
                if a.isdigit() and b.isdigit():
                    start = int(a)
                    end = int(b)
                    step = 1 if start <= end else -1
                    for n in range(start, end + step, step):
                        out.append(_normalize_numeric(n))
                    continue

            out.append(_normalize_single_key(tok))

        return out

    demo_keys = _expand_selection(demo_sel)

    if any(k.lower() == 'all' for k in demo_keys):
        for d in demos:
            print()
            print(f'[RUN] {d.key} - {d.title}')
            d.fn(args)
        return

    missing = [k for k in demo_keys if k not in lookup]
    if missing:
        print(f"[ERROR] demo not found: {', '.join(missing)}. --list로 확인하세요.")
        return

    for k in demo_keys:
        d = lookup[k]
        print()
        print(f'[RUN] {d.key} - {d.title}')
        d.fn(args)


# =============================================================================
# 8) 자주 쓰는 "종료 키" 패턴
# -----------------------------------------------------------------------------
# OpenCV 실습에서 가장 흔한 사용자 경험(UX)은:
# - 창을 띄운 다음
# - q 또는 ESC로 종료
# 이 패턴을 통일하면, 여러 데모를 돌릴 때 학습자가 헷갈리지 않습니다.
def is_exit_key(key: int) -> bool:
    """
    종료 키 판단 함수

    입력
    ----
    key: int
        cv2.waitKey(...)로 받은 키 코드(대개 0~255)

    반환
    ----
    bool
        True면 종료(q 또는 ESC)

    참고
    ----
    - ord('q')는 'q'의 ASCII 코드
    - 27은 ESC 키 코드
    """
    return key in (ord('q'), 27)


def wait_until_exit(winname: str = "result", resizable: bool = True) -> None:
    """
    (이미 창이 떠 있다는 가정 하에) q/ESC가 눌릴 때까지 대기합니다.

    입력
    ----
    winname: str
        닫을 창 이름
    resizable: bool
        (현재 구현에서는 사용하지 않지만, 호출부에서 UX 통일을 위해 인자로 유지)
        - 향후 safe_named_window 등을 넣을 때를 대비한 확장 포인트로 생각할 수 있습니다.

    사용 예시
    --------
    safe_imshow("result", img, resizable=True, wait=1)
    wait_until_exit("result")

    주의
    ----
    - imshow 없이 waitKey만 반복하면 아무 창도 표시되지 않습니다.
      반드시 호출부에서 먼저 imshow를 해야 합니다.
    """
    cv = require_cv2()
    while True:
        key = cv.waitKey(20) & 0xFF
        if is_exit_key(key):
            break
    close_window(winname)


if __name__ == "__main__":  # pragma: no cover
    # 공용 모듈은 단독 실행을 권장하지 않습니다.
    print("This is a helper module. Run topic scripts like ./AI/수업자료/13.openCV_기초.py, ./AI/수업자료/14.openCV_영상처리_기초.py, ./AI/수업자료/15.openCV_영상처리_심화.py, ./AI/수업자료/16.openCV_객체탐지_OCR.py
