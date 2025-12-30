# -*- coding: utf-8 -*-
"""
AI/Open_CV/9.실습3.py

OpenCV / NumPy 필터 실습 모음 (실습 1~3)
- 실습1: 커스텀 커널 만들기(기본)
- 실습2: 블러 효과 비교(응용)
- 실습3: 샤프닝 강도 조절(응용) (+ 슬라이더 선택)

================================================================================
[저장 규칙(요청 반영)]
- 결과물(이미지)은 기본적으로 "ouput" 디렉토리에 저장합니다.
  ※ 디렉토리명은 요청하신 그대로 "ouput" 입니다(일반적으로는 output이 흔함).
- outdir는 "현재 작업 디렉토리(CWD)"가 아니라 "이 스크립트가 있는 폴더" 기준으로 생성합니다.
  -> 예: ./AI/Open_CV/9.실습3.py 위치에서 ./AI/Open_CV/ouput/ 아래로 저장

================================================================================
[요구사항]
- Python 3.x
- pip install opencv-python numpy

================================================================================
[실행 방법]
1) 목록 보기
   python ./AI/Open_CV/9.실습3.py --list

2) 특정 실습 실행
   python ./AI/Open_CV/9.실습3.py --task ex1
   python ./AI/Open_CV/9.실습3.py --task ex2
   python ./AI/Open_CV/9.실습3.py --task ex3

3) 출력 폴더 변경(선택)
   python ./AI/Open_CV/9.실습3.py --task ex1 --outdir ouput

4) (선택) ex3 샤프닝 슬라이더 모드 활성화
   python ./AI/Open_CV/9.실습3.py --task ex3 --slider

================================================================================
[주의]
- cv2.imshow()는 GUI 환경(로컬 PC)에서 정상 동작합니다.
  (주피터/서버/헤드리스 환경에서는 창이 안 뜰 수 있음)
- 이 스크립트는 imshow 실패 시 자동으로 파일 저장으로 대체하도록 설계했습니다.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional

import cv2
import numpy as np


# =============================================================================
# 공통 유틸리티 (저장 경로/표시 안전장치)
# =============================================================================

def script_dir() -> Path:
    """
    현재 스크립트(9.실습3.py)가 존재하는 폴더 경로를 반환합니다.

    왜 필요한가?
    - 파이썬은 실행 위치(CWD)에 따라 상대경로가 달라질 수 있습니다.
    - 실습 결과 파일을 항상 "스크립트 폴더 기준"으로 저장하려면 __file__ 기반이 가장 안전합니다.

    Returns
    -------
    Path
        이 스크립트가 있는 폴더의 절대 경로
    """
    return Path(__file__).resolve().parent


def ensure_outdir(outdir: Path) -> Path:
    """
    결과 저장 폴더(outdir)를 생성(없으면 생성)하고 Path를 반환합니다.

    Parameters
    ----------
    outdir : Path
        생성할 디렉토리 경로

    Returns
    -------
    Path
        실제 존재하게 된 디렉토리 경로
    """
    outdir.mkdir(parents=True, exist_ok=True)
    return outdir


def safe_imshow(winname: str, img: np.ndarray, out_fallback_path: Optional[Path] = None, wait: int = 0) -> None:
    """
    GUI 환경이면 cv2.imshow로 표시하고, GUI가 없으면 파일 저장으로 대체합니다.

    Parameters
    ----------
    winname : str
        창 제목
    img : np.ndarray
        표시할 이미지(BGR 또는 grayscale)
    out_fallback_path : Optional[Path]
        imshow 실패 시 저장할 파일 경로
    wait : int
        cv2.waitKey 대기(ms). 0이면 키 입력까지 대기
    """
    try:
        cv2.imshow(winname, img)
        cv2.waitKey(wait)
        cv2.destroyWindow(winname)
    except cv2.error as e:
        print(f"[WARN] cv2.imshow 실패(헤드리스/GUI 미지원 가능): {e}")
        if out_fallback_path is not None:
            cv2.imwrite(str(out_fallback_path), img)
            print(f"[INFO] 대체 저장 완료: {out_fallback_path}")


def bgr_note() -> None:
    """OpenCV의 색상 채널 순서가 BGR임을 안내합니다."""
    print("[NOTE] OpenCV 색상 채널 순서: BGR (Blue, Green, Red)")


# =============================================================================
# 내부 유틸 (실습 이미지 생성/라벨/그리드)
# =============================================================================

def make_random_color_image(h: int = 480, w: int = 640, seed: int = 42) -> np.ndarray:
    """
    실습용 랜덤 컬러 이미지를 생성합니다.

    왜 랜덤 이미지를 사용하나?
    - 실습에서 "랜덤 이미지에 적용" 요구
    - 별도 샘플 파일 없이 즉시 실행 가능
    - 블러/샤프닝 효과를 다양한 패턴에서 관찰 가능

    Parameters
    ----------
    h, w : int
        생성할 이미지 높이/너비
    seed : int
        랜덤 시드(재현 가능)

    Returns
    -------
    np.ndarray
        (h, w, 3) uint8 BGR 이미지
    """
    rng = np.random.default_rng(seed)
    return rng.integers(0, 256, size=(h, w, 3), dtype=np.uint8)


def put_label_ascii(img: np.ndarray, label: str, xy=(12, 30)) -> np.ndarray:
    """
    비교용으로 이미지 좌상단에 라벨(영문/숫자)을 붙입니다.

    주의:
    - OpenCV 기본 폰트는 한글 미지원 -> 라벨은 영문으로 처리합니다.

    Parameters
    ----------
    img : np.ndarray
        대상 이미지(BGR)
    label : str
        라벨 텍스트(영문 권장)
    xy : tuple
        텍스트 시작 좌표

    Returns
    -------
    np.ndarray
        라벨이 포함된 이미지(BGR)
    """
    out = img.copy()
    cv2.putText(out, label, xy, cv2.FONT_HERSHEY_SIMPLEX, 0.85, (255, 255, 255), 2, cv2.LINE_AA)
    return out


def grid_3x3(images: list[np.ndarray], cell_h: int, cell_w: int, pad: int = 8) -> np.ndarray:
    """
    9장의 이미지를 3x3 그리드로 합칩니다.

    Parameters
    ----------
    images : list[np.ndarray]
        길이 9인 이미지 리스트
    cell_h, cell_w : int
        각 셀의 목표 높이/너비
    pad : int
        셀 간 여백(px)

    Returns
    -------
    np.ndarray
        3x3 그리드 이미지(BGR)
    """
    if len(images) != 9:
        raise ValueError("3x3 그리드는 이미지 9장이 필요합니다.")

    canvas_h = 3 * cell_h + 4 * pad
    canvas_w = 3 * cell_w + 4 * pad
    canvas = np.zeros((canvas_h, canvas_w, 3), dtype=np.uint8)

    idx = 0
    for r in range(3):
        for c in range(3):
            y0 = pad + r * (cell_h + pad)
            x0 = pad + c * (cell_w + pad)

            cell = images[idx]
            if cell.shape[:2] != (cell_h, cell_w):
                cell = cv2.resize(cell, (cell_w, cell_h), interpolation=cv2.INTER_AREA)

            canvas[y0:y0 + cell_h, x0:x0 + cell_w] = cell
            idx += 1

    return canvas


# =============================================================================
# 실습 1: 커스텀 커널 만들기(기본)
# =============================================================================

def ex1_custom_kernel(outdir: Path) -> None:
    """
    실습1: 커스텀 커널 만들기(기본)  [task: ex1]

    요구사항
    - 자신만의 3x3 커널을 만들어 이미지에 적용
    - "중앙 가중치가 높은 커널" 생성
    - 랜덤 이미지에 적용
    - 원본과 결과 비교

    핵심 개념 정리
    1) 커널(kernel, filter)란?
       - 주변 픽셀을 어떤 비율로 섞어서 새로운 픽셀 값을 만들지 정의하는 '가중치 행렬'입니다.
       - 3x3 커널이면, 한 픽셀 주변 8개 + 자기 자신(중앙)을 섞어 결과 픽셀을 만듭니다.

    2) 중앙 가중치가 높은 커널
       - 중앙 픽셀(현재 픽셀)의 비율이 크고, 주변 픽셀 비율은 작음
       - 결과가 원본을 크게 유지하면서 주변 정보를 살짝 반영한 형태

    3) 커널 합(sum) 정규화(normalization)
       - 커널 합이 1이면 밝기(에너지)가 급격히 변하는 것을 줄입니다.
       - 실습에서는 합이 1이 되도록 설계하거나, 필요하면 나눠서 정규화합니다.

    출력 파일
    - ouput/ex1_custom_kernel_original.png
    - ouput/ex1_custom_kernel_filtered.png
    - ouput/ex1_custom_kernel_compare.png
    """
    bgr_note()

    img = make_random_color_image(480, 640, seed=101)

    # 중앙 가중치가 큰 커널 예시
    # - 중앙 0.60
    # - 주변 8칸 각 0.05
    # - 총합 1.00 (밝기 변화가 과도하지 않음)
    kernel = np.array(
        [[0.05, 0.05, 0.05],
         [0.05, 0.60, 0.05],
         [0.05, 0.05, 0.05]],
        dtype=np.float32
    )

    # filter2D: 커널을 이용해 컨볼루션 수행
    filtered = cv2.filter2D(img, ddepth=-1, kernel=kernel)

    out_orig = outdir / "ex1_custom_kernel_original.png"
    out_filt = outdir / "ex1_custom_kernel_filtered.png"
    out_cmp = outdir / "ex1_custom_kernel_compare.png"

    cv2.imwrite(str(out_orig), img)
    cv2.imwrite(str(out_filt), filtered)

    left = put_label_ascii(img, "Original")
    right = put_label_ascii(filtered, "Custom kernel (center-high)")
    compare = np.hstack([left, right])
    cv2.imwrite(str(out_cmp), compare)

    print(f"[OK] 저장: {out_orig}")
    print(f"[OK] 저장: {out_filt}")
    print(f"[OK] 저장: {out_cmp}")

    safe_imshow("ex1 - compare", compare, out_fallback_path=out_cmp, wait=0)


# =============================================================================
# 실습 2: 블러 효과 비교(응용)
# =============================================================================

def ex2_blur_compare(outdir: Path) -> None:
    """
    실습2: 블러 효과 비교(응용)  [task: ex2]

    요구사항
    - 같은 이미지에 서로 다른 블러 필터를 적용하고 비교
      * 평균 블러: cv2.blur()
      * 가우시안 블러: cv2.GaussianBlur()
      * 미디언 블러: cv2.medianBlur()
    - 커널 크기: (3, 7, 15)
    - 3x3 그리드로 결과 비교

    블러 종류 개념 요약
    1) 평균 블러(Mean Blur, Box Filter)
       - 주변 픽셀의 평균값으로 대체
       - 빠르고 단순하지만 경계도 함께 뭉개짐

    2) 가우시안 블러(Gaussian Blur)
       - 중심에 더 큰 가중치를 주는 "정규분포(가우시안)" 기반 평균
       - 평균 블러보다 자연스럽고 노이즈 제거에 자주 사용

    3) 미디언 블러(Median Blur)
       - 주변 픽셀의 "중앙값(median)"으로 대체
       - 소금-후추(salt & pepper) 노이즈 제거에 특히 강함
       - 다만 계산 비용이 상대적으로 큼

    그리드 배치(권장)
    - 1행: Mean k=3,7,15
    - 2행: Gaussian k=3,7,15
    - 3행: Median k=3,7,15

    출력 파일
    - ouput/ex2_blur_grid.png
    """
    bgr_note()

    img = make_random_color_image(480, 640, seed=202)
    ksizes = [3, 7, 15]

    cells: list[np.ndarray] = []

    # 1행: Mean
    for k in ksizes:
        out = cv2.blur(img, (k, k))
        cells.append(put_label_ascii(out, f"Mean k={k}"))

    # 2행: Gaussian
    for k in ksizes:
        out = cv2.GaussianBlur(img, (k, k), sigmaX=0)
        cells.append(put_label_ascii(out, f"Gaussian k={k}"))

    # 3행: Median (ksize는 홀수여야 함)
    for k in ksizes:
        out = cv2.medianBlur(img, k)
        cells.append(put_label_ascii(out, f"Median k={k}"))

    grid = grid_3x3(cells, cell_h=260, cell_w=360, pad=10)

    out_path = outdir / "ex2_blur_grid.png"
    cv2.imwrite(str(out_path), grid)
    print(f"[OK] 저장: {out_path}")

    safe_imshow("ex2 - blur grid", grid, out_fallback_path=out_path, wait=0)


# =============================================================================
# 실습 3: 샤프닝 강도 조절(응용)
# =============================================================================

def sharpen_kernel(center: float) -> np.ndarray:
    """
    샤프닝 커널을 생성합니다. (중앙값을 조절하여 강도 조절)

    기본 형태(가장 널리 쓰는 3x3 샤프닝 커널 중 하나)
        [ 0, -1,  0]
        [-1,  c, -1]
        [ 0, -1,  0]

    커널 합(sum) = c - 4
    - c=5이면 합이 1 → 밝기 보존에 유리(대표적인 기본 샤프닝)
    - c가 커질수록 샤프닝이 강해짐

    정규화(normalization)
    - 합이 1이 되도록 (c-4)로 나눠 밝기 변화가 과도하지 않게 합니다.

    Parameters
    ----------
    center : float
        중앙값(c). 4보다 커야 정규화 가능

    Returns
    -------
    np.ndarray
        (3,3) float32 정규화 커널
    """
    if center <= 4:
        center = 5.0

    k = np.array(
        [[0, -1, 0],
         [-1, center, -1],
         [0, -1, 0]],
        dtype=np.float32
    )
    s = center - 4.0
    return k / s


def sharpen_kernel(center: float) -> np.ndarray:
    """
    "중앙값(center)"을 조절 가능한 샤프닝 커널(3x3)을 생성한다.

    가장 널리 쓰이는 형태 중 하나:
        [ 0, -1,  0]
        [-1,  c, -1]
        [ 0, -1,  0]

    이 커널의 합(sum)은 (c - 4).
    - c=5이면 합이 1 -> 평균 밝기 변화가 비교적 적고, 기본 샤프닝으로 자주 사용됨
    - c가 커질수록 중앙 픽셀을 더 강하게 강조 -> 샤프닝(엣지 강조) 강도가 증가

    정규화(normalization)
    - 커널 합이 1이 되게 (c-4)로 나누어 밝기 변화(전체적으로 너무 밝아지거나 어두워짐)를 줄인다.
    - 단, c=4이면 합이 0이 되어 정규화 불가 -> 최소 5로 보정한다.

    Parameters
    ----------
    center : float
        중앙값 c. (권장: 5 이상)

    Returns
    -------
    np.ndarray
        float32 (3,3) 커널
    """
    if center <= 4:
        # 안전장치: 정규화 분모가 0이 되지 않게 보정
        center = 5.0

    k = np.array(
        [[0, -1, 0],
         [-1, center, -1],
         [0, -1, 0]],
        dtype=np.float32
    )

    # 합이 1이 되도록 정규화(밝기 유지에 유리)
    denom = center - 4.0
    k = k / denom
    return k


# =============================================================================
# 3) 실습 3 본체: 약/중/강 저장 + (선택) 슬라이더 + "2행 비교 레이아웃" 저장
# =============================================================================

def ex3_sharpen_strength(outdir: Path, slider: bool = False) -> None:
    """
    (실습 3) 샤프닝 강도 조절(약/중/강 + 선택 슬라이더)

    이 함수가 보장하는 것
    - GUI가 되든 안 되든 아래 출력 파일은 항상 생성된다:
        ex3_sharpen_weak.png
        ex3_sharpen_mid.png
        ex3_sharpen_strong.png
        ex3_sharpen_compare_2rows.png
        ex3_sharpen_compare_2rows_fit.png

    compare 레이아웃(요청 반영: strong가 "절대 안 잘리게")
    - 1행: ORIGINAL | WEAK | MID
    - 2행: STRONG  | (blank) | (blank)
    -> 가로가 지나치게 길어지는 문제를 피하고,
       대부분의 이미지 뷰어에서 스크롤 없이 확인 가능.

    Parameters
    ----------
    outdir : Path
        결과 저장 폴더
    slider : bool
        True이면 트랙바(슬라이더) UI를 띄워 강도를 실시간 조절
        (단, GUI 환경에서만 가능. 실패 시 자동으로 preview grid로 대체 저장)
    """
    outdir.mkdir(parents=True, exist_ok=True)

    # -------------------------------------------------------------------------
    # (A) 입력 이미지 준비
    # -------------------------------------------------------------------------
    img = make_random_color_image(480, 640, seed=303)

    # -------------------------------------------------------------------------
    # (B) 약/중/강 3단계 샤프닝 적용
    #     - weak  : center=5  (가장 기본)
    #     - mid   : center=9
    #     - strong: center=13 (강하게)
    # -------------------------------------------------------------------------
    levels = {
        "weak": 5.0,
        "mid": 9.0,
        "strong": 13.0,
    }

    results: dict[str, np.ndarray] = {}

    for name, c in levels.items():
        k = sharpen_kernel(c)
        # filter2D: 커널 컨볼루션
        out = cv2.filter2D(img, ddepth=-1, kernel=k)
        results[name] = out

        out_path = outdir / f"ex3_sharpen_{name}.png"
        cv2.imwrite(str(out_path), out)
        print(f"[OK] 저장: {out_path} (center={c})")

    # -------------------------------------------------------------------------
    # (C) strong가 안 보이는 문제를 원천 차단:
    #     "2행 레이아웃" 비교 이미지 생성 및 저장
    # -------------------------------------------------------------------------
    orig_l = put_label_ascii(img, "ORIGINAL")
    weak_l = put_label_ascii(results["weak"], "WEAK c=5")
    mid_l = put_label_ascii(results["mid"], "MID  c=9")
    strong_l = put_label_ascii(results["strong"], "STRONG c=13")

    # 셀 크기 통일(혹시라도 입력/결과 크기가 달라지는 상황 대비)
    cell_h, cell_w = orig_l.shape[:2]

    def _resize_to_cell(x: np.ndarray) -> np.ndarray:
        if x.shape[:2] == (cell_h, cell_w):
            return x
        return cv2.resize(x, (cell_w, cell_h), interpolation=cv2.INTER_AREA)

    orig_l = _resize_to_cell(orig_l)
    weak_l = _resize_to_cell(weak_l)
    mid_l = _resize_to_cell(mid_l)
    strong_l = _resize_to_cell(strong_l)

    # 빈칸 셀(검정) 2개
    blank = np.zeros((cell_h, cell_w, 3), dtype=np.uint8)
    blank = put_label_ascii(blank, "(blank)")

    row1 = cv2.hconcat([orig_l, weak_l, mid_l])
    row2 = cv2.hconcat([strong_l, blank, blank])
    compare_2rows = cv2.vconcat([row1, row2])

    out_cmp_full = outdir / "ex3_sharpen_compare_2rows.png"
    cv2.imwrite(str(out_cmp_full), compare_2rows)
    print(f"[OK] 저장: {out_cmp_full}")

    # -------------------------------------------------------------------------
    # (D) "한 화면에 들어오게" 축소본도 추가 저장
    #     - 일부 뷰어(VSCode 등)에서 큰 이미지를 일부만 보여주는 경우가 있어
    #       fit 파일을 같이 만들어주면 확인이 매우 쉬움.
    # -------------------------------------------------------------------------
    target_w = 1200
    H, W = compare_2rows.shape[:2]
    scale = target_w / float(W)
    target_h = max(1, int(H * scale))
    compare_fit = cv2.resize(compare_2rows, (target_w, target_h), interpolation=cv2.INTER_AREA)

    out_cmp_fit = outdir / "ex3_sharpen_compare_2rows_fit.png"
    cv2.imwrite(str(out_cmp_fit), compare_fit)
    print(f"[OK] 저장: {out_cmp_fit}")

    # 표시 시도(실패해도 이미 저장 완료)
    safe_imshow("ex3 - compare (2rows fit)", compare_fit, out_fallback_path=out_cmp_fit, wait=0)

    # -------------------------------------------------------------------------
    # (E) (선택) 슬라이더 모드: center 값을 실시간 조절
    #     - GUI 미지원이면 예외 -> 자동으로 preview grid 저장(대체)
    # -------------------------------------------------------------------------
    if not slider:
        print("[INFO] 슬라이더를 사용하려면: ex3_sharpen_strength(outdir, slider=True)")
        return

    win = "ex3 - slider (q=quit, s=save)"
    saved_path = outdir / "ex3_sharpen_slider_saved.png"

    try:
        cv2.namedWindow(win, cv2.WINDOW_NORMAL)

        # 0~200 -> center = 5.0 + v/10.0 => 5.0~25.0
        cv2.createTrackbar("strength", win, 0, 200, lambda v: None)
        print("[INFO] 슬라이더 모드: q=종료, s=저장 (center=5.0~25.0)")

        while True:
            v = cv2.getTrackbarPos("strength", win)
            center = 5.0 + (v / 10.0)

            k = sharpen_kernel(center)
            out = cv2.filter2D(img, ddepth=-1, kernel=k)

            view = put_label_ascii(out, f"center={center:.1f}")
            cv2.imshow(win, view)

            key = cv2.waitKey(10) & 0xFF

            if key == ord("q"):
                break

            if key == ord("s"):
                cv2.imwrite(str(saved_path), out)
                print(f"[OK] 저장: {saved_path} (center={center:.1f})")

        # 종료 정리
        try:
            cv2.destroyWindow(win)
        except cv2.error:
            cv2.destroyAllWindows()

    except cv2.error as e:
        # GUI 미지원(헤드리스)에서 흔히 발생
        print(f"[WARN] 슬라이더 모드 실행 불가(GUI 미지원 가능): {e}")
        print("[INFO] 대체로 '슬라이더 느낌'의 미리보기 그리드(3x3)를 저장합니다.")

        # center 값을 여러 개 찍어서 "강도 스윕" 결과를 한 장에 모아 저장
        centers = [5, 7, 9, 11, 13, 15, 17, 19, 21]  # 9개(3x3)
        cells: list[np.ndarray] = []

        for c in centers:
            k = sharpen_kernel(float(c))
            out = cv2.filter2D(img, ddepth=-1, kernel=k)
            cells.append(put_label_ascii(out, f"c={c}"))

        # 3x3 그리드 생성(이 함수 파일 밖에서 쓰려면 아래 간단 구현 포함)
        preview = grid_3x3(cells, cell_h=260, cell_w=360, pad=10)

        out_preview = outdir / "ex3_sharpen_slider_preview_grid.png"
        cv2.imwrite(str(out_preview), preview)
        print(f"[OK] 저장: {out_preview}")


# =============================================================================
# 4) (슬라이더 GUI 불가 시) 미리보기 그리드 생성 함수
# =============================================================================

def grid_3x3(images: list[np.ndarray], cell_h: int, cell_w: int, pad: int = 10) -> np.ndarray:
    """
    9장의 이미지를 3x3로 배치하는 그리드 생성기.

    slider가 안 되는 환경에서도 "강도 스윕" 결과를 한 번에 확인할 수 있도록 제공한다.

    Parameters
    ----------
    images : list[np.ndarray]
        길이 9의 BGR 이미지 리스트
    cell_h, cell_w : int
        각 셀 이미지 크기
    pad : int
        셀 사이 여백

    Returns
    -------
    np.ndarray
        합성된 그리드 이미지(BGR)
    """
    if len(images) != 9:
        raise ValueError("grid_3x3는 이미지 9장이 필요합니다.")

    canvas_h = 3 * cell_h + 4 * pad
    canvas_w = 3 * cell_w + 4 * pad
    canvas = np.zeros((canvas_h, canvas_w, 3), dtype=np.uint8)

    idx = 0
    for r in range(3):
        for c in range(3):
            y0 = pad + r * (cell_h + pad)
            x0 = pad + c * (cell_w + pad)

            cell = images[idx]
            if cell.shape[:2] != (cell_h, cell_w):
                cell = cv2.resize(cell, (cell_w, cell_h), interpolation=cv2.INTER_AREA)

            canvas[y0:y0 + cell_h, x0:x0 + cell_w] = cell
            idx += 1

    return canvas

# =============================================================================
# CLI
# =============================================================================

TASKS = {
    "ex1": ("실습1: 커스텀 커널 만들기(중앙 가중치)", ex1_custom_kernel),
    "ex2": ("실습2: 블러 효과 비교(Mean/Gaussian/Median, k=3/7/15)", ex2_blur_compare),
    "ex3": ("실습3: 샤프닝 강도 조절(약/중/강 + 슬라이더 선택)", ex3_sharpen_strength),
}


def list_tasks() -> None:
    print("사용 가능한 --task 목록:")
    for k, (desc, _) in TASKS.items():
        print(f" - {k:<4} : {desc}")


def main() -> None:
    parser = argparse.ArgumentParser(description="OpenCV 필터 실습 1~3 (커널/블러/샤프닝)")
    parser.add_argument("--list", action="store_true", help="가능한 task 목록 출력")
    parser.add_argument("--task", type=str, default=None, help="실행할 task id (ex1/ex2/ex3)")
    parser.add_argument("--outdir", type=str, default="ouput", help="결과 저장 폴더(기본: ouput)")
    parser.add_argument("--slider", action="store_true", help="ex3에서 슬라이더(trackbar) 모드 사용")

    args = parser.parse_args()

    if args.list:
        list_tasks()
        return

    if args.task is None:
        list_tasks()
        print("\n예) python 9.실습3.py --task ex1")
        return

    task = args.task.strip()
    if task not in TASKS:
        print(f"[ERROR] 알 수 없는 task: {task}")
        list_tasks()
        return

    outdir = ensure_outdir(script_dir() / args.outdir)

    desc, fn = TASKS[task]
    print(f"[RUN] {task} - {desc}")

    # ex3만 시그니처가 (outdir, slider)라서 분기
    if task == "ex3":
        fn(outdir, slider=args.slider)  # type: ignore[arg-type]
    else:
        fn(outdir)


if __name__ == "__main__":
    main()
