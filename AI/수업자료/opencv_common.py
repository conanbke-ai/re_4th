# -*- coding: utf-8 -*-
"""
================================================================================
공용 유틸(Utilities) 모음

이 파일은 OpenCV 학습/실습 코드(여러 .py 파일)에서 공통으로 사용하는 기능을 담습니다.

- 목표
  1) 예제 코드의 "핵심 로직"을 보기 좋게 유지
  2) 파일/카메라 입력, 윈도우 표시, 안전한 종료 등 반복되는 코드 제거
  3) 실습 환경(윈도우/맥/리눅스, 웹캠 유무, 이미지 파일 유무)에 따라
     예제가 "깨지지 않도록" 방어적 코딩(Defensive Coding) 제공

- 참고
  * 이 프로젝트는 사용자가 업로드한 OpenCV 강의 PDF(기초/영상처리기초/심화/객체탐지/OCR)를
    대주제별로 분할 정리한 학습용 스크립트입니다.
  * 일부 슬라이드는 이미지(스크린샷) 형태로 삽입된 코드/설명이 있어 텍스트 추출이 제한적일 수 있습니다.
    그런 경우에는 OpenCV의 표준 사용 패턴을 기반으로 동일 개념을 재현 가능한 예제로 구성했습니다.

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
# [개념] OpenCV / NumPy 임포트
# -----------------------------------------------------------------------------
# - OpenCV는 "cv2" 패키지 이름으로 제공됩니다.
# - NumPy는 이미지(행렬) 데이터를 다루는 데 사실상 표준 라이브러리입니다.
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
# [개념] 예외/환경 체크 유틸
# =============================================================================
def require_cv2() -> Any:
    """cv2가 임포트되지 않았을 때 친절한 오류를 발생시킵니다."""
    if cv2 is None:
        raise RuntimeError(
            "OpenCV(cv2) 임포트 실패.\n"
            "1) pip install opencv-python\n"
            "2) (GUI 환경) OS/권한/원격환경에서 imshow가 안 될 수 있음\n"
            f"원인: {_CV2_IMPORT_ERROR}"
        )
    return cv2


def require_np() -> Any:
    """numpy가 임포트되지 않았을 때 친절한 오류를 발생시킵니다."""
    if np is None:
        raise RuntimeError(
            "NumPy(np) 임포트 실패.\n"
            "pip install numpy\n"
            f"원인: {_NP_IMPORT_ERROR}"
        )
    return np


def is_camera_source(src: str) -> bool:
    """문자열 입력이 카메라 인덱스인지(예: '0', '1') 판별."""
    return src.isdigit()


def parse_source_to_capture_arg(src: str) -> Any:
    """--source 인자(문자열)를 VideoCapture에 넣을 수 있는 형태로 변환."""
    return int(src) if is_camera_source(src) else src


# =============================================================================
# [개념] 안전한 imshow / waitKey 패턴
# -----------------------------------------------------------------------------
# OpenCV GUI는 환경에 따라 동작이 다릅니다.
# - 로컬 PC: 대부분 정상
# - 원격 서버/WSL/일부 IDE: GUI가 뜨지 않거나 프리징될 수 있음
#
# 따라서 예제에서는:
# - 창 크기 조절 가능한 WINDOW_NORMAL 옵션 제공
# - 키 입력(q/ESC)으로 종료하는 패턴을 표준화
# =============================================================================
def safe_named_window(winname: str, resizable: bool = True) -> None:
    cv = require_cv2()
    flags = cv.WINDOW_NORMAL if resizable else cv.WINDOW_AUTOSIZE
    cv.namedWindow(winname, flags)


def safe_imshow(winname: str, img: Any, resizable: bool = True, wait: int = 1) -> int:
    """imshow + waitKey를 한 번에 수행하고, 누른 키 코드를 반환합니다."""
    cv = require_cv2()
    safe_named_window(winname, resizable=resizable)
    cv.imshow(winname, img)
    return cv.waitKey(wait) & 0xFF


def close_all_windows() -> None:
    """모든 OpenCV 창 닫기."""
    cv = require_cv2()
    try:
        cv.destroyAllWindows()
    except Exception:
        # 일부 환경에서 destroyAllWindows가 예외를 던지기도 함
        pass


def close_window(winname: str) -> None:
    """특정 창 닫기."""
    cv = require_cv2()
    try:
        cv.destroyWindow(winname)
    except Exception:
        pass


# =============================================================================
# [개념] 이미지 생성(실습용 더미 데이터)
# -----------------------------------------------------------------------------
# PDF(기초 파트)에는 "빈 화면 만들기/일부 영역 색칠/색상 변경" 등이 포함됩니다.
# 실습 환경에서 샘플 이미지가 없어도 동일 개념을 체험하도록,
# 아래 함수로 테스트 이미지를 생성할 수 있습니다.
# =============================================================================
def make_blank(width: int = 640, height: int = 480, color_bgr: Tuple[int, int, int] = (0, 0, 0)) -> Any:
    np_ = require_np()
    img = np_.zeros((height, width, 3), dtype=np_.uint8)
    img[:] = color_bgr
    return img


def make_random_noise(width: int = 640, height: int = 480) -> Any:
    np_ = require_np()
    img = np_.random.randint(0, 256, (height, width, 3), dtype=np_.uint8)
    return img


def make_gradient(width: int = 640, height: int = 480, direction: str = "horizontal",
                  start_bgr: Tuple[int, int, int] = (0, 0, 0),
                  end_bgr: Tuple[int, int, int] = (255, 255, 255)) -> Any:
    """
    direction:
      - 'horizontal': 좌→우 그라데이션
      - 'vertical'  : 상→하 그라데이션
    """
    np_ = require_np()
    if direction not in ("horizontal", "vertical"):
        raise ValueError("direction must be 'horizontal' or 'vertical'")

    start = np_.array(start_bgr, dtype=np_.float32)
    end = np_.array(end_bgr, dtype=np_.float32)

    if direction == "horizontal":
        t = np_.linspace(0.0, 1.0, width, dtype=np_.float32)
        line = (start[None, :] * (1 - t[:, None]) + end[None, :] * t[:, None])  # (W,3)
        img = np_.tile(line[None, :, :], (height, 1, 1))
    else:
        t = np_.linspace(0.0, 1.0, height, dtype=np_.float32)
        col = (start[None, :] * (1 - t[:, None]) + end[None, :] * t[:, None])  # (H,3)
        img = np_.tile(col[:, None, :], (1, width, 1))

    return np_.clip(img, 0, 255).astype(np_.uint8)


def bgr_to_rgb(img: Any) -> Any:
    cv = require_cv2()
    return cv.cvtColor(img, cv.COLOR_BGR2RGB)


def bgr_to_gray(img: Any) -> Any:
    cv = require_cv2()
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# =============================================================================
# [개념] 샘플 이미지 자동 탐색
# -----------------------------------------------------------------------------
# 사용자의 폴더가 다음과 같이 구성되어 있을 수 있습니다:
#   AI/
#     Images/
#     Videos/
# 예제에서 --image 또는 --source를 생략해도 동작하도록,
# 현재 스크립트 기준으로 주변 폴더에서 이미지/영상 파일을 찾아 사용합니다.
# =============================================================================
_IMAGE_EXTS = (".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff", ".webp")
_VIDEO_EXTS = (".mp4", ".avi", ".mov", ".mkv", ".wmv", ".webm")


def find_first_file(root: str, exts: Tuple[str, ...]) -> Optional[str]:
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            if fn.lower().endswith(exts):
                return os.path.join(dirpath, fn)
    return None


def auto_find_image(start_dir: str = ".") -> Optional[str]:
    # 우선순위: ./Images -> ./images -> 현재 폴더 전체
    for cand in ["Images", "images", "AI/Images", "ai/Images", "ai/images"]:
        p = os.path.join(start_dir, cand)
        if os.path.isdir(p):
            f = find_first_file(p, _IMAGE_EXTS)
            if f:
                return f
    return find_first_file(start_dir, _IMAGE_EXTS)


def auto_find_video(start_dir: str = ".") -> Optional[str]:
    for cand in ["Videos", "videos", "AI/Videos", "ai/Videos", "ai/videos"]:
        p = os.path.join(start_dir, cand)
        if os.path.isdir(p):
            f = find_first_file(p, _VIDEO_EXTS)
            if f:
                return f
    return find_first_file(start_dir, _VIDEO_EXTS)


# =============================================================================
# [개념] CLI(Demo Runner) 공용 파서
# =============================================================================
@dataclass
class Demo:
    key: str
    title: str
    fn: Callable[..., None]


def build_cli_parser(title: str) -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=title)
    p.add_argument("--list", action="store_true", help="데모 목록 출력")
    p.add_argument("--demo", type=str, default="", help="실행할 데모 key (예: 01, 02, draw_line, ...)")
    p.add_argument("--image", type=str, default="", help="입력 이미지 경로(선택)")
    p.add_argument("--source", type=str, default="", help="비디오 소스(파일 경로 또는 카메라 인덱스 '0')")
    p.add_argument("--save", type=str, default="", help="결과 저장 경로(선택)")
    return p


def run_demos(demos: List[Demo], args: argparse.Namespace) -> None:
    if args.list or not args.demo:
        print("\n[Demo List]")
        for d in demos:
            print(f"  - {d.key}: {d.title}")
        print("\n예) python <file>.py --demo 01")
        return

    lookup: Dict[str, Demo] = {d.key: d for d in demos}
    if args.demo not in lookup:
        print(f"[ERROR] demo '{args.demo}' not found. --list로 확인하세요.")
        return

    # 실행
    lookup[args.demo].fn(args)


# =============================================================================
# [개념] 자주 쓰는 "종료 키" 패턴
# =============================================================================
def is_exit_key(key: int) -> bool:
    """q 또는 ESC 입력이면 종료."""
    return key in (ord('q'), 27)


def wait_until_exit(winname: str = "result", resizable: bool = True) -> None:
    """창을 띄운 뒤, q/ESC 누를 때까지 대기."""
    cv = require_cv2()
    while True:
        key = cv.waitKey(20) & 0xFF
        if is_exit_key(key):
            break
    close_window(winname)


if __name__ == "__main__":  # pragma: no cover
    # 공용 모듈은 단독 실행을 권장하지 않습니다.
    print("This is a helper module. Run topic scripts like 02_opencv_basics.py, 03_image_processing_basics.py, ...")
