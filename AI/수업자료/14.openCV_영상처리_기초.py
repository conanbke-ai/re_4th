# -*- coding: utf-8 -*-
"""
14.openCV_영상처리_기초.py
================================================================================
[대주제] openCV 영상처리 기초 (그리기/텍스트/블러/이진화/트랙바)

이 파일은 업로드된 PDF:
- 12_OpenCV(2)_영상처리기초.pdf
의 대주제들을 빠짐없이 정리한 뒤,
추가 개념/응용 예제까지 확장한 학습 스크립트입니다.

실행 방식
--------------------------------------------------------------------------------
0) 기본 실행(가장 간단):
    python ./AI/수업자료/14.openCV_영상처리_기초.py

   * 기본 데모(보통 00)가 바로 실행됩니다.
   * 데모 선택 메뉴가 필요하면 --menu 옵션을 사용하세요.

1) 데모 목록 보기:
    python ./AI/수업자료/14.openCV_영상처리_기초.py --list

2) 데모 실행:
    python ./AI/수업자료/14.openCV_영상처리_기초.py --menu   # 메뉴에서 demo key 선택
    python ./AI/수업자료/14.openCV_영상처리_기초.py --demo 01
    python ./AI/수업자료/14.openCV_영상처리_기초.py --demo all   # 데모를 순서대로 전부 실행
    python ./AI/수업자료/14.openCV_영상처리_기초.py --demo 05 --image ./Images/sample.jpg

- 공통 종료 키: 'q' 또는 ESC

작성일: 2025-12-26
"""

from __future__ import annotations

import os
from typing import Any, Tuple

from openCV_공용 import (
    require_cv2, require_np,
    auto_find_image,
    make_blank, make_random_noise, make_gradient,
    bgr_to_gray,
    safe_imshow, safe_named_window, close_all_windows, close_window,
    build_cli_parser, run_demos, Demo,
    is_exit_key
)

cv2 = require_cv2()
np = require_np()


# =============================================================================
# [PDF 체크리스트] 12_OpenCV(2)_영상처리기초.pdf 대주제 → 코드 매핑
# PDF 체크리스트(슬라이드 대주제 → 코드 위치)
# --------------------------------------------------------------------
# 번호 | 슬라이드(p) | 대주제 | 코드 섹션/데모
# --------------------------------------------------------------------
# 01 | p02-02 | 영상처리기초 | demo 00 (overview)
# 02 | p03-03 | 도형 그리기 | demo 01 (draw_shapes)
# 03 | p04-04 | 선 그리기 | demo 01 (draw_shapes)
# 04 | p05-07 | 선 그리기 – 라인 타입 | demo 01 (draw_shapes)
# 05 | p08-08 | 선 그리기 | demo 01 (draw_shapes)
# 06 | p09-10 | 원 그리기 | demo 01 (draw_shapes)
# 07 | p11-12 | 타원 그리기 | demo 01 (draw_shapes)
# 08 | p13-14 | 사각형 그리기 | demo 01 (draw_shapes)
# 09 | p15-15 | 사각형과 직선이 만나는 점 | demo 02 (clipLine)
# 10 | p16-17 | 다각형 그리기(선) | demo 01 (draw_shapes)
# 11 | p18-19 | 다각형 그리기(채우기) | demo 01 (draw_shapes)
# 12 | p20-20 | 실습1. 도형 그려보기 | demo 01 (draw_shapes)
# 13 | p21-21 | 텍스트 | demo 03 (putText)
# 14 | p22-23 | 텍스트 그리기(영문) | demo 03 (putText)
# 15 | p24-25 | 텍스트 그리기(한글) | demo 03 (putText)
# 16 | p26-26 | 이미지 흐리기 | demo 04 (blur/denoise)
# 17 | p27-27 | 블러와 노이즈 제거 | demo 04 (blur/denoise)
# 18 | p28-30 | 이미지 흐리기 | demo 04 (blur/denoise)
# 19 | p31-32 | 이진화 | demo 05 (threshold+trackbar+palette)
# 20 | p33-33 | 기본 이진화 - threshold | demo 05 (threshold+trackbar+palette)
# 21 | p35-35 | 기본 이진화 - threshold | demo 05 (threshold+trackbar+palette)
# 22 | p36-40 | 트랙바 | demo 05 (threshold+trackbar+palette)
# 23 | p41-41 | 실습2-1. Threshold에 적용 | (covered)
# 24 | p42-42 | 실습2-2. 컬러 팔레트 만들기 | demo 05 (threshold+trackbar+palette)
# 25 | p43-45 | 적응형 이진화 | demo 05 (threshold+trackbar+palette)
# 26 | p46-47 | 오츠 알고리즘 | demo 05 (threshold+trackbar+palette)
# 27 | p48-48 | 감사합니다 | -
# --------------------------------------------------------------------
# =============================================================================
# 0. 입력 이미지 로드(없으면 더미 생성)
def _load_or_make_image(path: str) -> Any:
    if path and os.path.isfile(path):
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        if img is None:
            raise ValueError(f"이미지 로드 실패: {path}")
        return img

    auto = auto_find_image(".")
    if auto:
        img = cv2.imread(auto, cv2.IMREAD_COLOR)
        if img is not None:
            print(f"[INFO] auto image: {auto}")
            return img

    # 더미: 색상 그라데이션(수평) + 도형을 얹어 영상처리 효과가 보이도록 구성
    img = make_gradient(640, 420, direction="horizontal", start_bgr=(10, 10, 10), end_bgr=(240, 240, 240))
    cv2.circle(img, (180, 210), 80, (0, 0, 255), thickness=-1)
    cv2.rectangle(img, (330, 120), (600, 330), (0, 255, 0), thickness=4)
    cv2.line(img, (0, 0), (639, 419), (255, 0, 0), thickness=3)
    return img


# =============================================================================
# demo 00. 개요(영상처리 기초)
def demo_00_overview(args) -> None:
    """
    [개념]
    - "영상처리(Image Processing)"는 픽셀 배열에 다양한 연산(필터/변환)을 적용하여
      노이즈 제거, 엣지 강조, 이진화, 특징 추출 등을 수행하는 분야입니다.

    [이 파일에서 다루는 핵심]
    1) 도형/텍스트 그리기 (시각화/디버깅/오버레이)
    2) 블러(흐리기)로 노이즈 감소
    3) 이진화(threshold)로 전경/배경 분리
    4) 트랙바(trackbar)로 파라미터를 실시간 조정(실습에 매우 중요)

    [예제]
    - 더미 이미지를 띄우고 종료(q/ESC) 확인
    """
    img = _load_or_make_image(args.image)
    safe_imshow("demo00_overview (q/ESC)", img, resizable=True, wait=1)
    while True:
        if is_exit_key(cv2.waitKey(20) & 0xFF):
            break
    close_all_windows()


# =============================================================================
# demo 01. 도형 그리기(선/원/타원/사각형/다각형) + 실습1
def demo_01_draw_shapes(args) -> None:
    """
    [개념] 기본 도형 API
    - cv2.line(img, pt1, pt2, color, thickness, lineType)
    - cv2.rectangle(img, pt1, pt2, color, thickness)
    - cv2.circle(img, center, radius, color, thickness)
    - cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness)
    - cv2.polylines(img, [pts], isClosed, color, thickness)
    - cv2.fillPoly(img, [pts], color)
    - cv2.drawContours(img, contours, contourIdx, color, thickness)
    - cv2.arrowedLine(img, pt1, pt2, color, thickness)

    [라인 타입]
    - cv2.LINE_4, cv2.LINE_8, cv2.LINE_AA(안티앨리어싱)

    [실습1 대응]
    - 여러 도형을 활용해 "나만의 이미지"를 그려보기
    """
    canvas = make_blank(900, 520, color_bgr=(20, 20, 20))

    # --- 선 그리기(라인 타입 비교)
    cv2.line(canvas, (50, 60), (850, 60), (255, 255, 255), 1, cv2.LINE_4)
    cv2.putText(canvas, "LINE_4", (60, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (200, 200, 200), 2)

    cv2.line(canvas, (50, 130), (850, 130), (255, 255, 255), 1, cv2.LINE_8)
    cv2.putText(canvas, "LINE_8", (60, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (200, 200, 200), 2)

    cv2.line(canvas, (50, 200), (850, 200), (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(canvas, "LINE_AA", (60, 190), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (200, 200, 200), 2)

        # 화살표 선(arrowedLine) — 진행 방향을 표시할 때 유용
    cv2.arrowedLine(canvas, (60, 235), (260, 235), (0, 200, 255), 2, tipLength=0.25)

    # drawContours 예제:
    # - contours는 (N, 1, 2) 형태의 int32 점 배열들의 리스트
    contour = np.array([[700, 260], [820, 300], [780, 420], [660, 380]], dtype=np.int32).reshape((-1, 1, 2))
    cv2.drawContours(canvas, [contour], contourIdx=-1, color=(180, 0, 180), thickness=3)

# --- 사각형/원/타원
    cv2.rectangle(canvas, (80, 260), (330, 470), (0, 255, 0), 4)
    cv2.circle(canvas, (520, 365), 85, (0, 0, 255), -1)  # 채우기
    cv2.ellipse(canvas, (730, 365), (120, 60), 25, 0, 360, (255, 0, 0), 3)

    # --- 다각형(삼각형) + 채우기
    tri = np.array([[410, 470], [520, 260], [630, 470]], dtype=np.int32)
    cv2.polylines(canvas, [tri], True, (255, 255, 0), 3, cv2.LINE_AA)
    cv2.fillPoly(canvas, [tri], (60, 60, 0))

    safe_imshow("demo01_draw_shapes (q/ESC)", canvas, resizable=True, wait=1)
    while True:
        if is_exit_key(cv2.waitKey(20) & 0xFF):
            break
    close_all_windows()


# =============================================================================
# demo 02. 사각형과 직선이 만나는 점(clipLine)
def demo_02_clipline_intersection(args) -> None:
    """
    [개념] cv2.clipLine
    - 직선(pt1~pt2)이 사각형 rect 내부와 교차하는 구간을 계산합니다.
    - 활용:
      * 영상 밖으로 나간 선을 화면 안에서만 그리기
      * 선-사각형 교차 구간/교차점 계산(기초적 기하)

    [시그니처]
    - ok, pt1c, pt2c = cv2.clipLine(rect, pt1, pt2)
      * rect: (x, y, w, h)

    [예제]
    - 화면을 벗어나는 긴 선을 만들고, clipLine 결과로 "화면 안 선분"만 그리기
    """
    canvas = make_blank(640, 420, color_bgr=(0, 0, 0))

    rect = (80, 60, 480, 300)  # x,y,w,h
    x, y, w, h = rect
    cv2.rectangle(canvas, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 화면 밖까지 뻗는 긴 선
    pt1 = (-200, 10)
    pt2 = (900, 500)
    cv2.line(canvas, pt1, pt2, (50, 50, 50), 1, cv2.LINE_AA)  # 원래 선(회색)

    ok, c1, c2 = cv2.clipLine(rect, pt1, pt2)
    if ok:
        cv2.line(canvas, c1, c2, (0, 0, 255), 3, cv2.LINE_AA)
        cv2.circle(canvas, c1, 6, (0, 0, 255), -1)
        cv2.circle(canvas, c2, 6, (0, 0, 255), -1)
        cv2.putText(canvas, f"clipped: {c1}->{c2}", (20, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (200, 200, 200), 2)
    else:
        cv2.putText(canvas, "no intersection", (20, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    safe_imshow("demo02_clipLine (q/ESC)", canvas, resizable=True, wait=1)
    while True:
        if is_exit_key(cv2.waitKey(20) & 0xFF):
            break
    close_all_windows()


# =============================================================================
# demo 03. 텍스트 그리기(putText) + 한국어 오버레이(응용)
def demo_03_puttext_kor_eng(args) -> None:
    """
    [개념] cv2.putText
    - OpenCV 기본 putText는 한글 지원이 제한적입니다(폰트/렌더링 이슈).
    - 영어/숫자/기호 중심의 디버깅 텍스트에는 매우 유용합니다.

    [시그니처]
    - cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType)

    [응용] 한글 텍스트
    - Pillow(PIL)로 한글을 그린 뒤 NumPy 배열로 변환하는 방식이 일반적입니다.
    - PIL이 없으면 영어 텍스트만 표시하도록 fallback 처리합니다.
    """
    img = _load_or_make_image(args.image).copy()

    # 영어 텍스트(OpenCV)
    cv2.putText(img, "OpenCV putText demo", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, "1234567890 !@#$", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2, cv2.LINE_AA)

    # 한글 텍스트(PIL) - 선택적
    try:
        from PIL import ImageFont, ImageDraw, Image  # type: ignore
        # 시스템에 설치된 폰트가 다르므로, 폰트 경로는 환경에 맞게 변경 가능
        # Windows 예: C:/Windows/Fonts/malgun.ttf
        # Mac     예: /System/Library/Fonts/Supplemental/AppleGothic.ttf
        font_candidates = [
            "C:/Windows/Fonts/malgun.ttf",
            "C:/Windows/Fonts/gulim.ttc",
            "/System/Library/Fonts/Supplemental/AppleGothic.ttf",
            "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",
        ]
        font_path = next((p for p in font_candidates if os.path.isfile(p)), "")
        if not font_path:
            raise FileNotFoundError("한글 폰트를 찾지 못했습니다. font_candidates를 수정하세요.")

        pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(pil)
        font = ImageFont.truetype(font_path, 32)
        draw.text((20, 120), "한글 텍스트 예시: 영상처리 기초", font=font, fill=(255, 200, 0))
        img = cv2.cvtColor(np.array(pil), cv2.COLOR_RGB2BGR)
    except Exception as e:
        cv2.putText(img, "(Korean text skipped - install PIL & font)", (20, 140),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2, cv2.LINE_AA)
        print("[WARN] PIL/Korean text not available:", e)

    safe_imshow("demo03_putText (q/ESC)", img, resizable=True, wait=1)
    while True:
        if is_exit_key(cv2.waitKey(20) & 0xFF):
            break
    close_all_windows()


# =============================================================================
# demo 04. 흐리기(Blur) / 노이즈 제거(기초)
def demo_04_blur_denoise(args) -> None:
    """
    [개념] 블러(흐리기)는 노이즈를 줄이고, 작은 디테일을 완화하는 기본 기법입니다.

    - 평균 블러(Mean blur)
      cv2.blur(src, ksize)
    - 가우시안 블러(Gaussian blur)
      cv2.GaussianBlur(src, ksize, sigmaX)
    - 중값 블러(Median blur)
      cv2.medianBlur(src, ksize)
    - 양방향 필터(Bilateral filter): 엣지를 비교적 잘 보존
      cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace)

    [예제]
    - 노이즈가 섞인 이미지에 다양한 블러를 적용해 비교
    """
    img = _load_or_make_image(args.image)
    noise = make_random_noise(img.shape[1], img.shape[0])
    noisy = cv2.addWeighted(img, 0.75, noise, 0.25, 0)

    mean = cv2.blur(noisy, (7, 7))
    gauss = cv2.GaussianBlur(noisy, (7, 7), 1.2)
    median = cv2.medianBlur(noisy, 7)
    bilateral = cv2.bilateralFilter(noisy, d=9, sigmaColor=80, sigmaSpace=80)

    safe_imshow("demo04_noisy (q/ESC)", noisy, resizable=True, wait=1)
    safe_imshow("demo04_mean_blur (q/ESC)", mean, resizable=True, wait=1)
    safe_imshow("demo04_gaussian_blur (q/ESC)", gauss, resizable=True, wait=1)
    safe_imshow("demo04_median_blur (q/ESC)", median, resizable=True, wait=1)
    safe_imshow("demo04_bilateral (q/ESC)", bilateral, resizable=True, wait=1)

    while True:
        if is_exit_key(cv2.waitKey(20) & 0xFF):
            break
    close_all_windows()


# =============================================================================
# demo 05. 이진화(Threshold) + 트랙바 + 적응형/오츠 + 컬러 팔레트(실습2-2)
def demo_05_threshold_trackbar_palette(args) -> None:
    """
    [개념] 기본 이진화(threshold)
    - ret, dst = cv2.threshold(src, thresh, maxval, type)
      type:
        * THRESH_BINARY
        * THRESH_BINARY_INV
        * THRESH_TRUNC
        * THRESH_TOZERO
        * THRESH_TOZERO_INV

    [개념] 적응형 이진화(adaptiveThreshold)
    - 전역 임계값(thresh)이 아니라, 주변 영역 기반으로 임계값을 자동 계산
      * 조명 변화가 큰 이미지에 유리

    [개념] 오츠(Otsu) 이진화
    - cv2.threshold에서 THRESH_OTSU 플래그를 주면, 최적 임계값을 자동 산출
      (대신 thresh 인자는 무시되며, 입력은 보통 grayscale)

    [개념] 트랙바(trackbar)
    - 파라미터(thresh, blur kernel 등)를 실시간으로 조정 가능
    - 학습/튜닝 단계에서 매우 유용

    [실습 2-1/2-2 확장]
    - (A) threshold 값을 트랙바로 조절
    - (B) RGB 트랙바로 컬러 팔레트 만들기
    """
    img = _load_or_make_image(args.image)
    gray = bgr_to_gray(img)

    win = "demo05_threshold_trackbar (q/ESC)"
    safe_named_window(win, resizable=True)

    # --- 트랙바 콜백 (OpenCV 요구사항상 시그니처 고정)
    def on_change(_v: int) -> None:
        pass

    # threshold 슬라이더
    cv2.createTrackbar("thresh", win, 127, 255, on_change)
    # blur kernel 슬라이더(홀수로 만들기 위해 내부에서 처리)
    cv2.createTrackbar("blur(k)", win, 1, 25, on_change)
    # 모드 선택(0:binary, 1:inv, 2:adaptive, 3:otsu)
    cv2.createTrackbar("mode(0/1/2/3)", win, 0, 3, on_change)

    print("[KEY] q/ESC=quit  | 트랙바로 thresh/blur/mode 조절")

    while True:
        t = cv2.getTrackbarPos("thresh", win)
        k = cv2.getTrackbarPos("blur(k)", win)
        mode = cv2.getTrackbarPos("mode(0/1/2/3)", win)

        # 커널 사이즈는 홀수여야 하는 경우가 많음
        k = max(1, k)
        if k % 2 == 0:
            k += 1

        blurred = cv2.GaussianBlur(gray, (k, k), 0)

        if mode == 0:
            _, binimg = cv2.threshold(blurred, t, 255, cv2.THRESH_BINARY)
            label = f"binary t={t}, k={k}"
        elif mode == 1:
            _, binimg = cv2.threshold(blurred, t, 255, cv2.THRESH_BINARY_INV)
            label = f"binary_inv t={t}, k={k}"
        elif mode == 2:
            # blockSize는 홀수이면서 3 이상이어야 함(여기서는 k를 활용)
            block = max(3, k)
            if block % 2 == 0:
                block += 1
            binimg = cv2.adaptiveThreshold(
                blurred, 255,
                adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                thresholdType=cv2.THRESH_BINARY,
                blockSize=block,
                C=2
            )
            label = f"adaptive block={block}"
        else:
            # Otsu: threshold 값(t)은 무시됨
            _ret, binimg = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            label = f"otsu ret={_ret:.1f}"

        # 시각화: 원본(좌) + 결과(우)
        vis_left = cv2.cvtColor(blurred, cv2.COLOR_GRAY2BGR)
        vis_right = cv2.cvtColor(binimg, cv2.COLOR_GRAY2BGR)
        vis = np.hstack([vis_left, vis_right])
        cv2.putText(vis, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow(win, vis)

        key = cv2.waitKey(10) & 0xFF
        if is_exit_key(key):
            break

    close_all_windows()

    # -------------------------------------------------------------------------
    # [실습 2-2 확장] 컬러 팔레트: RGB 트랙바 3개로 색상 만들기
    # -------------------------------------------------------------------------
    win2 = "demo05_color_palette (q/ESC)"
    safe_named_window(win2, resizable=True)

    def _noop(_v: int) -> None:
        pass

    cv2.createTrackbar("B", win2, 0, 255, _noop)
    cv2.createTrackbar("G", win2, 0, 255, _noop)
    cv2.createTrackbar("R", win2, 0, 255, _noop)

    print("[KEY] q/ESC=quit  | RGB 트랙바로 팔레트 색 만들기")

    while True:
        b = cv2.getTrackbarPos("B", win2)
        g = cv2.getTrackbarPos("G", win2)
        r = cv2.getTrackbarPos("R", win2)

        palette = make_blank(640, 360, color_bgr=(b, g, r))
        cv2.putText(palette, f"BGR=({b},{g},{r})", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255-b, 255-g, 255-r), 2, cv2.LINE_AA)
        cv2.imshow(win2, palette)

        if is_exit_key(cv2.waitKey(10) & 0xFF):
            break

    close_all_windows()


# =============================================================================
# [추가 개념/응용] (PDF 외 확장)
# -----------------------------------------------------------------------------
# - 이진화/블러 다음 단계로 많이 이어지는 주제:
#   1) Morphology(침식/팽창)로 잡음 제거
#   2) Edge(Canny)로 경계 강조
#   3) Connected Components로 객체 개수 세기
# 여기서는 간단히 "침식/팽창" 맛보기 예제를 추가합니다.
def demo_06_bonus_morphology(args) -> None:
    """
    [BONUS] Morphology(침식/팽창) 미니 예제
    - 이진화 결과에서 작은 점 잡음 제거에 자주 사용됩니다.
    """
    img = _load_or_make_image(args.image)
    gray = bgr_to_gray(img)
    _ret, binimg = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    eroded = cv2.erode(binimg, kernel, iterations=1)
    dilated = cv2.dilate(binimg, kernel, iterations=1)
    opened = cv2.morphologyEx(binimg, cv2.MORPH_OPEN, kernel, iterations=1)
    closed = cv2.morphologyEx(binimg, cv2.MORPH_CLOSE, kernel, iterations=1)

    def to_bgr(x):
        return cv2.cvtColor(x, cv2.COLOR_GRAY2BGR)

    vis = np.vstack([
        np.hstack([to_bgr(binimg), to_bgr(eroded)]),
        np.hstack([to_bgr(dilated), to_bgr(opened)]),
        np.hstack([to_bgr(closed), to_bgr(gray)]),
    ])
    safe_imshow("demo06_bonus_morphology (q/ESC)", vis, resizable=True, wait=1)
    while True:
        if is_exit_key(cv2.waitKey(20) & 0xFF):
            break
    close_all_windows()



def demo_07_text_size_center_and_alpha_overlay(args: argparse.Namespace) -> None:
    """
    [활용 팁] 반투명 오버레이(addWeighted) + getTextSize로 텍스트 레이아웃(가운데 정렬)

    포함 개념(요청 사항):
    1) 원본 보존을 위해 copy() 사용
    2) 반투명(투명도) 도형/영역 만들기:
       overlay = img.copy()
       cv2.rectangle(overlay, ..., thickness=-1)
       cv2.addWeighted(overlay, alpha, img, 1-alpha, 0, dst)
    3) 텍스트 크기 계산:
       (w, h), baseline = cv2.getTextSize(text, fontFace, fontScale, thickness)
    4) 이미지 중앙에 텍스트 배치:
       x = (W - w) // 2
       y = (H + h) // 2   # putText는 '좌하단' 기준이므로 h를 더해줌
    """
    cv2 = require_cv2()
    np = require_np()

    W, H = 900, 520
    img = make_gradient(W, H, direction="horizontal", start_bgr=(20, 20, 20), end_bgr=(80, 80, 80))

    # -----------------------------
    # 1) 반투명 오버레이
    # -----------------------------
    overlay = img.copy()
    cv2.rectangle(overlay, (80, 120), (W - 80, H - 120), (0, 180, 0), -1)  # 채워진 사각형
    alpha = 0.35
    cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0, img)

    # -----------------------------
    # 2) getTextSize + 가운데 정렬
    # -----------------------------
    text = "Centered Text (getTextSize)"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.2
    thickness = 2

    (tw, th), baseline = cv2.getTextSize(text, font, font_scale, thickness)

    x = (W - tw) // 2
    y = (H + th) // 2  # putText는 좌하단 기준

    # 텍스트 배경 박스(가독성)
    pad = 10
    cv2.rectangle(img, (x - pad, y - th - pad), (x + tw + pad, y + baseline + pad), (0, 0, 0), -1)
    cv2.putText(img, text, (x, y), font, font_scale, (255, 255, 255), thickness, cv2.LINE_AA)

    # 하단 안내 텍스트
    cv2.putText(
        img,
        "Tip: putText origin is bottom-left; use (H+text_h)//2 for vertical centering.",
        (40, H - 30),
        cv2.FONT_HERSHEY_PLAIN,
        1.2,
        (255, 255, 255),
        1,
        cv2.LINE_AA,
    )

    safe_named_window("demo_07_overlay_text", resizable=True)
    cv2.imshow("demo_07_overlay_text", img)
    print("[조작] q 또는 ESC를 누르면 종료합니다.")
    while True:
        key = cv2.waitKey(20)
        if is_exit_key(key):
            break
    close_window("demo_07_overlay_text")

# =============================================================================
# [추가] 사용자 제공 예제: 색상 공간 변환 + 비트 연산/마스킹
# -----------------------------------------------------------------------------
# 아래 데모(08~09)는 사용자가 제공한 'OpenCV 기초 02~03' 예제를
# 이 파일의 데모 러너 체계에 맞춰 그대로 실행 가능하도록 편입한 것입니다.
# =============================================================================


def demo_08_color_space_conversion(args: argparse.Namespace) -> None:
    """
    OpenCV 기초 - 02. 색상 공간 변환

    이 데모에서 배울 내용:
    1) 다양한 색상 공간의 종류와 특징 이해하기
    2) BGR, HSV, Grayscale 등으로 변환하는 방법
    3) 각 색상 공간이 언제 유용한지 알아보기

    ------------------------------------------------------------
    색상 공간(Color Space)이란?
    ------------------------------------------------------------
    색상을 표현하는 방법은 여러 가지가 있습니다.
    우리가 보는 색을 컴퓨터가 이해할 수 있도록 숫자로 나타내는 방식입니다.

    왜 여러 가지 색상 공간이 필요할까?
    - 작업의 목적에 따라 적합한 색상 표현 방식이 다르기 때문!
    - 예: 특정 색의 물체를 찾을 때는 HSV가 더 쉬운 경우가 많습니다.

    ------------------------------------------------------------
    주요 색상 공간 소개
    ------------------------------------------------------------

    1) RGB/BGR (Red, Green, Blue)
    - 빛의 3원색을 섞는 방식(가산 혼합)
    - 모니터/화면에서 사용하는 표준 방식
    - ⚠️ OpenCV는 BGR 순서를 사용! (다른 라이브러리는 RGB가 흔함)
    - 값의 범위: 각 채널 0~255

    2) HSV (Hue, Saturation, Value)
    - Hue(색상): 0~179 (OpenCV 기준)
    - Saturation(채도): 0~255 (0=회색, 255=선명한 색)
    - Value(명도): 0~255 (0=검정, 255=밝음)
    - 💡 언제 사용? 특정 색상의 물체를 찾을 때 매우 유용!

    3) HLS (Hue, Lightness, Saturation)
    - HSV와 유사하지만 명도 대신 밝기(Lightness)를 사용
    - HSV와 비슷하지만 밝기 계산 방식이 조금 다릅니다.

    4) YCrCb (휘도, 색차)
    - Y: 휘도(밝기 정보)
    - Cr, Cb: 색차(색상 정보)
    - 💡 언제 사용? 동영상/JPEG 압축 등에서 자주 등장

    5) Lab (CIE L*a*b)
    - L: 밝기
    - a: 녹색~빨강 축
    - b: 파랑~노랑 축
    - 💡 언제 사용? 색상 비교, 피부색 검출 등(사람 시각과 유사한 축)

    6) Grayscale (흑백)
    - 단일 채널 (색상 정보 없음)
    - 0(검정) ~ 255(흰색)의 밝기 정보만
    - 💡 언제 사용? 처리 속도가 중요하거나 색상이 필요 없을 때
    """
    cv = require_cv2()
    np = require_np()

    # (선택) Matplotlib이 있으면 2x2로 보기 좋게 표시, 없으면 OpenCV 창으로 표시
    try:
        import matplotlib.pyplot as plt  # type: ignore
        has_mpl = True
    except Exception:
        has_mpl = False

    # ============================================================
    # 예제 1: 무지개 그라데이션 이미지 만들고 색상 공간 변환하기
    # ============================================================
    h, w = 400, 600
    img = np.zeros((h, w, 3), dtype=np.uint8)

    # 왼쪽->오른쪽으로 Hue가 0~179로 증가하도록 만들어 무지개 생성
    for i in range(w):
        hue = int(180 * i / w)  # 0~179
        hsv_pix = np.array([[[hue, 255, 255]]], dtype=np.uint8)  # (1,1,3)
        bgr_pix = cv.cvtColor(hsv_pix, cv.COLOR_HSV2BGR)
        img[:, i] = bgr_pix[0, 0]

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

    if has_mpl:
        fig, axes = plt.subplots(2, 2, figsize=(12, 6))

        # Matplotlib은 RGB 순서이므로 변환 필요
        axes[0, 0].imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
        axes[0, 0].set_title("Original (BGR)")

        axes[0, 1].imshow(gray, cmap="gray")
        axes[0, 1].set_title("Grayscale")

        axes[1, 0].imshow(hsv[:, :, 0], cmap="hsv")
        axes[1, 0].set_title("HSV - Hue Channel (색상)")

        axes[1, 1].imshow(lab[:, :, 0], cmap="gray")
        axes[1, 1].set_title("Lab - L Channel (밝기)")

        for ax in axes.flat:
            ax.axis("off")

        plt.tight_layout()
        plt.show()
    else:
        # Matplotlib이 없으면 OpenCV 창으로 기본 표시
        safe_imshow("08-1 Original (BGR)", img)
        safe_imshow("08-1 Grayscale", gray)
        safe_imshow("08-1 HSV Hue (0~179)", hsv[:, :, 0])
        safe_imshow("08-1 Lab L (밝기)", lab[:, :, 0])
        cv.waitKey(0)
        close_all_windows()

    # ============================================================
    # 예제 2: 4가지 색상 블록 만들고 다양한 색상 공간으로 변환하기
    # ============================================================
    img_bgr = np.zeros((200, 200, 3), dtype=np.uint8)
    img_bgr[:100, :100] = [255, 0, 0]    # 파란색 (BGR)
    img_bgr[:100, 100:] = [0, 255, 0]    # 초록색
    img_bgr[100:, :100] = [0, 0, 255]    # 빨간색
    img_bgr[100:, 100:] = [255, 0, 255]  # 보라색 (파랑+빨강)

    gray2 = cv.cvtColor(img_bgr, cv.COLOR_BGR2GRAY)
    rgb2 = cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB)
    hsv2 = cv.cvtColor(img_bgr, cv.COLOR_BGR2HSV)
    hls2 = cv.cvtColor(img_bgr, cv.COLOR_BGR2HLS)
    ycrcb2 = cv.cvtColor(img_bgr, cv.COLOR_BGR2YCrCb)
    lab2 = cv.cvtColor(img_bgr, cv.COLOR_BGR2LAB)

    print(f"[Demo 08] BGR 이미지 shape: {img_bgr.shape}")
    print(f"[Demo 08] Grayscale shape: {gray2.shape}")
    print(f"[Demo 08] HSV 이미지 shape: {hsv2.shape}")

    # 예제 2는 OpenCV 창으로 간단히 확인
    safe_imshow("08-2 Color Blocks (BGR)", img_bgr)
    safe_imshow("08-2 Color Blocks (Gray)", gray2)
    cv.waitKey(0)
    close_all_windows()

    # ============================================================
    # 예제 3: BGR을 Grayscale로 변환하는 원리 이해하기
    # ============================================================
    """
    BGR 이미지를 흑백으로 변환할 때, 단순 평균이 아니라 사람 시각 특성을 반영한 가중치 사용:
        Gray = 0.299 * R + 0.587 * G + 0.114 * B
    왜 Green의 비중이 가장 클까?
    - 사람의 눈은 녹색 빛에 가장 민감하기 때문
    """

    tiny = np.array([[
        [255, 0, 0],   # 파란색(B)
        [0, 255, 0],   # 초록색(G)
        [0, 0, 255],   # 빨간색(R)
    ]], dtype=np.uint8)

    gray_cv = cv.cvtColor(tiny, cv.COLOR_BGR2GRAY)

    print("[Demo 08] BGR -> Grayscale 변환 결과:")
    print(gray_cv)
    print("\n각 색상이 얼마나 밝게 변환되었는지 확인해보세요!")
    print("초록색이 가장 밝게(값이 크게) 나타날 거예요!")


def demo_09_bitwise_and_masking(args: argparse.Namespace) -> None:
    """
    OpenCV 기초 - 03. 비트 연산과 마스킹

    이 데모에서 배울 내용:
    1) 비트 연산(AND, OR, XOR, NOT)이 무엇인지
    2) 마스크를 만들고 사용하는 방법
    3) 마스크를 이용해서 이미지의 특정 부분만 선택하거나 합성하기

    ------------------------------------------------------------
    비트 연산이란?
    ------------------------------------------------------------
    - 이미지의 각 픽셀값을 0과 1(혹은 0과 255)로 생각하고 논리 연산을 수행
    - 마스크(선택 영역)를 만들 때 매우 유용

    주요 비트 연산:
    - AND: 교집합(겹치는 부분만)
    - OR : 합집합(둘 중 하나라도 포함)
    - XOR: 배타적 논리합(겹치지 않는 부분만)
    - NOT: 반전(흰색<->검은색 뒤집기)
    """
    cv = require_cv2()
    np = require_np()

    h, w = 300, 300

    # ------------------------------------------------------------
    # 1) 비트 연산 시각화: 원/사각형 마스크로 AND/OR/XOR/NOT 보기
    # ------------------------------------------------------------
    circle_mask = np.zeros((h, w), dtype=np.uint8)
    cv.circle(circle_mask, (150, 150), 100, 255, -1)  # -1: 채우기

    rect_mask = np.zeros((h, w), dtype=np.uint8)
    cv.rectangle(rect_mask, (100, 100), (200, 200), 255, -1)

    and_mask = cv.bitwise_and(circle_mask, rect_mask)
    or_mask = cv.bitwise_or(circle_mask, rect_mask)
    xor_mask = cv.bitwise_xor(circle_mask, rect_mask)
    not_mask = cv.bitwise_not(circle_mask)

    # 결과를 한 줄로 나란히 배치
    result = np.hstack([circle_mask, rect_mask, and_mask, or_mask, xor_mask, not_mask])

    safe_imshow("09-1 Bitwise Ops: circle | rect | AND | OR | XOR | NOT", result)
    print("[Demo 09] 비트 연산 결과를 확인하세요! 아무 키로 다음.")
    cv.waitKey(0)
    close_all_windows()

    # ------------------------------------------------------------
    # 2) 마스크를 이용한 이미지 합성
    # ------------------------------------------------------------
    """
    마스킹이란?
    - 이미지의 특정 부분만 선택하거나 숨기는 기술
    - 사진 배경 바꾸기, 로고/워터마크 합성 등에 자주 사용

    절차:
    1) 마스크(mask)를 만든다 (선택 영역: 255, 나머지: 0)
    2) bitwise_and로 원본에서 필요한 부분만 추출
    3) 배경(background) 생성
    4) 마스크 반전(inv_mask)으로 배경에서 필요한 부분만 추출
    5) 두 결과를 add로 합성
    """

    # 원본 이미지 생성 (파란색 계열 랜덤 이미지)
    img = np.random.randint(100, 200, (300, 300, 3), dtype=np.uint8)
    img[:, :, 0] = 200  # Blue 채널 강조

    # 원형 마스크 생성 (원 안쪽만 선택)
    mask = np.zeros((300, 300), dtype=np.uint8)
    cv.circle(mask, (150, 150), 100, 255, -1)

    # 1) 원본에서 원 부분만 추출
    masked = cv.bitwise_and(img, img, mask=mask)

    # 2) 새로운 배경 만들기 (빨간색)
    background = np.zeros_like(img)
    background[:] = [0, 0, 255]

    # 3) 마스크 반전 -> 원 바깥 부분만 선택
    inv_mask = cv.bitwise_not(mask)
    bg_part = cv.bitwise_and(background, background, mask=inv_mask)

    # 4) 합성
    composite = cv.add(masked, bg_part)

    display = np.hstack([img, masked, composite])
    safe_imshow("09-2 Masking: original | masked | composite", display)
    print("[Demo 09] 마스킹/합성 결과를 확인하세요! 아무 키로 종료.")
    cv.waitKey(0)
    close_all_windows()


def main() -> None:
    parser = build_cli_parser("Image Processing Basics (PDF2) - demos")
    args = parser.parse_args()

    demos = [
        Demo("00", "개요(영상처리 기초)", demo_00_overview),
        Demo("01", "도형 그리기(선/원/타원/사각형/다각형) + 실습1", demo_01_draw_shapes),
        Demo("02", "사각형과 직선 교차(clipLine)", demo_02_clipline_intersection),
        Demo("03", "텍스트 그리기(putText) + 한글 오버레이(응용)", demo_03_puttext_kor_eng),
        Demo("04", "블러/노이즈 제거(평균/가우시안/중값/양방향)", demo_04_blur_denoise),
        Demo("05", "이진화(threshold) + 트랙바 + adaptive/otsu + 컬러 팔레트", demo_05_threshold_trackbar_palette),
        Demo("06", "BONUS: Morphology(침식/팽창/열림/닫힘)", demo_06_bonus_morphology),
        Demo("07", "BONUS: addWeighted(반투명) + getTextSize(가운데 정렬)", demo_07_text_size_center_and_alpha_overlay),
    
        Demo("08", "Color space conversion (BGR/HSV/GRAY/Lab)", demo_08_color_space_conversion),
        Demo("09", "Bitwise ops & masking (AND/OR/XOR/NOT)", demo_09_bitwise_and_masking),
]
    run_demos(demos, args)


if __name__ == "__main__":
    main()
