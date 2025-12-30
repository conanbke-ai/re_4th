# -*- coding: utf-8 -*-
"""
13.openCV_기초.py
================================================================================
[대주제] OpenCV 기초 (이미지/비디오 I/O, 윈도우/키 입력, 픽셀/ROI, 색상/채널,
        리사이즈/보간/피라미드/자르기/대칭)

이 파일은 업로드된 PDF:
- 11_OpenCV(1)_OpenCV기초.pdf
의 "개념 + 실습 예제"를 빠짐없이(대주제 단위) 정리한 뒤,
추가 개념/응용 예제까지 확장한 학습 스크립트입니다.

실행 방식
--------------------------------------------------------------------------------
0) 기본 실행(가장 간단):
    python ./AI/수업자료/13.openCV_기초.py

   * 기본 데모(보통 00)가 바로 실행됩니다.
   * 데모 선택 메뉴가 필요하면 --menu 옵션을 사용하세요.

1) 데모 목록 보기:
    python ./AI/수업자료/13.openCV_기초.py --list

2) 데모 실행:
    python ./AI/수업자료/13.openCV_기초.py --menu   # 메뉴에서 demo key 선택
    python ./AI/수업자료/13.openCV_기초.py --demo 02 --image ./Images/sample.jpg
    python ./AI/수업자료/13.openCV_기초.py --demo 04 --source ./Videos/sample.mp4
    python ./AI/수업자료/13.openCV_기초.py --demo 05 --source 0

- 공통 종료 키
  * 'q' 또는 ESC: 종료

주의(중요)
--------------------------------------------------------------------------------
- OpenCV GUI(imshow)는 원격/WSL/일부 IDE 환경에서 정상 동작하지 않을 수 있습니다.
- 이 파일은 "실습이 돌아가게" 방어적으로 작성되어 있습니다.
  (입력 파일이 없으면 더미 이미지/영상으로 대체 등)

작성일: 2025-12-26
"""

from __future__ import annotations

import os
import sys
import time
from typing import Any

from openCV_공용 import (
    require_cv2, require_np,
    auto_find_image, auto_find_video,
    make_blank, make_random_noise, make_gradient,
    bgr_to_gray, bgr_to_rgb,
    safe_imshow, safe_named_window, close_all_windows, close_window,
    build_cli_parser, run_demos, Demo,
    parse_source_to_capture_arg, is_exit_key
)

cv2 = require_cv2()
np = require_np()


# =============================================================================
# [PDF 체크리스트] 11_OpenCV(1)_OpenCV기초.pdf 대주제 → 코드 매핑
# -----------------------------------------------------------------------------
# "누락 없이" 커버했다는 것을 확인하기 위한 체크리스트입니다.
# 각 대주제는 아래 코드의 섹션/데모에서 다룹니다.
# PDF 체크리스트(슬라이드 대주제 → 코드 위치)
# --------------------------------------------------------------------
# 번호 | 슬라이드(p) | 대주제 | 코드 섹션/데모
# --------------------------------------------------------------------
# 01 | p02-02 | OpenCV 기초 | demo 01 (env_check)
# 02 | p03-03 | OpenCV 소개 및 설치 | (covered)
# 03 | p04-05 | OpenCV란 | (covered)
# 04 | p06-06 | OpenCV 사용준비 | (covered)
# 05 | p07-07 | 이미지 입력, 출력, 쓰기 | (covered)
# 06 | p08-08 | 이미지 출력(기본 코드) | demo 02 (image_io_window_keyboard)
# 07 | p09-09 | 윈도우 만들기 | demo 02 (image_io_window_keyboard)
# 08 | p10-10 | 이미지 입력 | (covered)
# 09 | p11-11 | 이미지 출력 | demo 02 (image_io_window_keyboard)
# 10 | p12-13 | 키보드 입력 | demo 02 (image_io_window_keyboard)
# 11 | p14-14 | 창 닫기 | (covered)
# 12 | p15-16 | 이미지 출력 | demo 02 (image_io_window_keyboard)
# 13 | p17-18 | 이미지 Shape | demo 03 (image_shape_and_write)
# 14 | p19-19 | 이미지 파일로 쓰기 | (covered)
# 15 | p20-20 | 실습1. 원하는 이미지 띄우기 | demo 03 (image_shape_and_write)
# 16 | p21-21 | 영상 입력, 출력, 쓰기 | (covered)
# 17 | p22-23 | 영상 입력초기화 | (covered)
# 18 | p24-24 | 영상 입력설정 | demo 04 (video_capture_speed)
# 19 | p25-25 | 영상 정보 얻기 | (covered)
# 20 | p26-26 | 영상 입력 | (covered)
# 21 | p27-27 | 영상 입력 종료 | (covered)
# 22 | p28-29 | OpenCV로 비디오 파일 출력 | demo 04 (video_capture_speed)
# 23 | p30-30 | 프레임 불러오기 | (covered)
# 24 | p31-31 | 실습2. 영상 프레임 조절 | demo 04 (video_capture_speed)
# 25 | p32-32 | OpenCV로 웹 캠에 연결 | (covered)
# 26 | p33-33 | OpenCV로 웹 캠으로 사진 찍기 | (covered)
# 27 | p34-34 | 실습3. 카메라 컨트롤 | demo 05 (webcam)
# 28 | p35-36 | 비디오 파일로 쓰기 | demo 04 (video_capture_speed)
# 29 | p37-37 | 픽셀 접근 | demo 07 (pixel_roi_copy)
# 30 | p38-38 | 빈 화면 만들기 | demo 07 (pixel_roi_copy)
# 31 | p39-39 | 일부 영역 색칠 | demo 07 (pixel_roi_copy)
# 32 | p40-40 | 이미지 복사 | demo 07 (pixel_roi_copy)
# 33 | p41-41 | 이미지와 색상 | demo 08 (color_channels_invert)
# 34 | p42-42 | 이미지와 색상 - RGB | demo 08 (color_channels_invert)
# 35 | p43-43 | 이미지 색상 변경 | demo 08 (color_channels_invert)
# 36 | p44-46 | 이미지 채널 분리와 병합 | demo 08 (color_channels_invert)
# 37 | p47-48 | 실습4. 이미지 흑백 반전 | demo 08 (color_channels_invert)
# 38 | p49-49 | 이미지 조정 | demo 09 (resize_interpolation)
# 39 | p50-52 | 이미지 리사이즈 | demo 09 (resize_interpolation)
# 40 | p53-55 | 이미지 리사이즈- 보간법 | demo 09 (resize_interpolation)
# 41 | p56-56 | 실습5. 영상 리사이즈 해서 출력 | demo 09 (resize_interpolation)
# 42 | p57-58 | 이미지 피라미드 | demo 10 (pyramids)
# 43 | p59-59 | 이미지 자르기 | demo 11 (crop_flip)
# 44 | p60-61 | 이미지 대칭 | demo 11 (crop_flip)
# 45 | p62-62 | 실습6. 이미지 조정 | demo 09 (resize_interpolation)
# 46 | p63-63 | 감사합니다 | -
# --------------------------------------------------------------------
# =============================================================================
# 0. 공통 헬퍼(이 파일 내부용)
def _load_or_make_image(path: str) -> Any:
    """
    [개념]
    - 실습에서 이미지 파일이 없을 수 있으므로,
      (1) path가 있으면 읽고
      (2) 없으면 자동 탐색 → 실패하면 더미 생성
    """
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

    # 더미 이미지: 컬러 그라데이션 + 노이즈를 섞어 특징이 보이게
    base = make_gradient(640, 420, direction="horizontal", start_bgr=(0, 0, 0), end_bgr=(255, 255, 255))
    noise = make_random_noise(640, 420)
    img = cv2.addWeighted(base, 0.7, noise, 0.3, 0)
    return img


def _open_capture(source: str) -> Any:
    """
    [개념] VideoCapture 오픈
    - source가 '0' 같은 숫자 문자열이면 웹캠 인덱스로 해석
    - 그 외는 파일 경로(또는 URL)로 해석
    """
    if not source:
        # 자동 비디오 탐색 -> 없으면 0(웹캠) 시도
        auto = auto_find_video(".")
        if auto:
            print(f"[INFO] auto video: {auto}")
            source = auto
        else:
            source = "0"

    cap = cv2.VideoCapture(parse_source_to_capture_arg(source))
    if not cap.isOpened():
        raise RuntimeError(f"VideoCapture 오픈 실패: source={source}")
    return cap


def _show_until_exit(winname: str) -> None:
    """
    [개념] 창 표시 후 q/ESC까지 대기하는 표준 루프.
    """
    while True:
        key = cv2.waitKey(20) & 0xFF
        if is_exit_key(key):
            break
    close_window(winname)


# =============================================================================
# demo 01. (OpenCV 기초/소개/설치/사용준비)
def demo_00_overview_and_image_representation(args: argparse.Namespace) -> None:
    """
    [개요] OpenCV 핵심 개념 + "이미지 = NumPy 배열" 표현

    포함 개념(요청 사항):
    - OpenCV 특징: 2500+ 알고리즘, C++/Python/Java/MATLAB, 멀티플랫폼, GPU 가속(CUDA/OpenCL)
    - 이미지 처리: 필터링/변환/색상/형태학/에지
    - 객체 탐지/인식: 얼굴/추적/특징점
    - 비디오 분석: 모션/배경 제거/광학 흐름
    - 딥러닝 추론: DNN(ONNX/TF/PyTorch)
    - 산업 응용: 자율주행/의료/보안/AR/VR

    - 이미지 표현:
        * 그레이스케일: (H, W) uint8, 픽셀 0~255
        * 컬러(BGR): (H, W, 3) uint8, 픽셀 [B,G,R]
        * OpenCV 기본 채널 순서: BGR (RGB 아님)
    - 더미 이미지 생성 예제:
        * black/white/단색/랜덤 노이즈/그라데이션/체크보드
    """
    cv2 = require_cv2()
    np = require_np()

    print("\n=== OpenCV 개요 ===")
    print(f"- OpenCV 버전: {cv2.__version__}")
    print("- OpenCV는 실시간 컴퓨터 비전을 위한 오픈소스 라이브러리입니다.")
    print("- 지원: C++/Python/Java/MATLAB, Windows/Linux/macOS/Android/iOS, GPU 가속(CUDA/OpenCL) 등")

    print("\n=== 이미지 = NumPy 배열 ===")
    gray_img = np.zeros((100, 200), dtype=np.uint8)
    color_img = np.zeros((100, 200, 3), dtype=np.uint8)
    print(f"- 그레이스케일 shape: {gray_img.shape}, dtype: {gray_img.dtype}")
    print(f"- 컬러(BGR) shape:     {color_img.shape}, dtype: {color_img.dtype}")

    # BGR vs RGB 간단 예시
    bgr_red = np.zeros((60, 60, 3), dtype=np.uint8)
    bgr_red[:, :, 2] = 255  # R 채널
    rgb_red = cv2.cvtColor(bgr_red, cv2.COLOR_BGR2RGB)
    print(f"- BGR 빨강 픽셀: {bgr_red[0,0].tolist()}  / RGB 변환 픽셀: {rgb_red[0,0].tolist()}")

    # 채널 분리/병합
    img = np.zeros((120, 180, 3), dtype=np.uint8)
    img[:, :, 0] = 100
    img[:, :, 1] = 150
    img[:, :, 2] = 200
    b, g, r = cv2.split(img)
    merged = cv2.merge([b, g, r])
    print(f"- split 결과: b{b.shape}, g{g.shape}, r{r.shape} / merge 결과: {merged.shape}")

    # -----------------------------
    # 더미 이미지 생성(갤러리)
    # -----------------------------
    black = np.zeros((240, 320, 3), dtype=np.uint8)
    white = np.ones((240, 320, 3), dtype=np.uint8) * 255

    blue = np.zeros((240, 320, 3), dtype=np.uint8)
    blue[:, :] = (255, 0, 0)
    green = np.zeros((240, 320, 3), dtype=np.uint8)
    green[:, :] = (0, 255, 0)
    red = np.zeros((240, 320, 3), dtype=np.uint8)
    red[:, :] = (0, 0, 255)

    random_img = make_random_noise(320, 240)

    gradient_h = make_gradient(320, 240, direction="horizontal")
    gradient_v = make_gradient(320, 240, direction="vertical")

    checker = make_checkerboard(320, 240, square=30, as_bgr=False)
    checker_bgr = cv2.cvtColor(checker, cv2.COLOR_GRAY2BGR)

    # 2x4 그리드로 보기 좋게 배치
    row1 = cv2.hconcat([black, white, blue, green])
    row2 = cv2.hconcat([red, random_img, gradient_h, checker_bgr])
    gallery = cv2.vconcat([row1, row2])

    safe_named_window("demo_00_gallery", resizable=True)
    cv2.imshow("demo_00_gallery", gallery)
    print("\n[조작] q 또는 ESC를 누르면 종료합니다.")
    while True:
        key = cv2.waitKey(20)
        if is_exit_key(key):
            break
    close_window("demo_00_gallery")


def demo_01_env_check(args) -> None:
    """
    [개념]
    - OpenCV 설치 확인
    - 버전 확인
    - 간단한 더미 이미지 생성 후 표시(환경에서 GUI가 되는지 확인)

    [추가 개념]
    - opencv-python: GUI 포함(대부분)
    - opencv-python-headless: GUI 제외(서버용). imshow 불가.
    """
    print("=== OpenCV Environment Check ===")
    print("Python:", sys.version.split()[0])
    print("OpenCV (cv2) version:", cv2.__version__)
    print("NumPy version:", np.__version__)

    img = make_gradient(640, 360, direction="vertical", start_bgr=(255, 0, 0), end_bgr=(0, 0, 255))
    safe_imshow("demo01_env_check (press q/ESC)", img, resizable=True, wait=1)
    _show_until_exit("demo01_env_check (press q/ESC)")
    close_all_windows()


# =============================================================================
# demo 02. (이미지 입력/출력/쓰기, 윈도우, 키보드 입력, 창 닫기)
def demo_02_image_io_window_keyboard(args) -> None:
    """
    [개념]
    - cv2.imread(path): 이미지 읽기
      * 주의: OpenCV는 기본 색상 순서가 BGR
    - cv2.imshow(winname, img): 창에 표시
    - cv2.waitKey(ms): 키보드 입력 대기 및 이벤트 루프 처리
      * waitKey를 호출해야 창이 '응답'합니다.
    - cv2.namedWindow(winname, flags):
      * WINDOW_NORMAL  : 창 크기 조절 가능
      * WINDOW_AUTOSIZE: 이미지 크기에 맞춰 자동, 보통 크기 조절 불가
    - cv2.destroyWindow / cv2.destroyAllWindows: 창 닫기

    [예제]
    - (1) resizable 창 vs 고정 창을 비교
    - (2) 키 입력에 따라 동작 변경
        - 'g': grayscale 보기
        - 'c': 컬러(BGR) 보기
        - 'i': 반전(invert) 보기
        - 's': 저장(save) (args.save 또는 임시 파일)
        - 'q'/'ESC': 종료
    """
    img = _load_or_make_image(args.image)
    gray = bgr_to_gray(img)
    inv = 255 - gray  # 흑백 반전

    win_resizable = "Resizable (WINDOW_NORMAL)"
    win_fixed = "Fixed (WINDOW_AUTOSIZE)"

    # resizable 창
    safe_named_window(win_resizable, resizable=True)
    cv2.imshow(win_resizable, img)

    # fixed 창
    safe_named_window(win_fixed, resizable=False)
    cv2.imshow(win_fixed, img)

    mode = "color"
    print("[KEY] g=gray, c=color, i=invert, s=save, q/ESC=quit")

    while True:
        # waitKey는 "GUI 이벤트 처리" 역할도 수행합니다.
        key = cv2.waitKey(30) & 0xFF

        if key == ord("g"):
            mode = "gray"
        elif key == ord("c"):
            mode = "color"
        elif key == ord("i"):
            mode = "invert"
        elif key == ord("s"):
            out = args.save or "demo02_saved.png"
            # mode별로 저장 대상 선택
            to_save = img if mode == "color" else (gray if mode == "gray" else inv)
            cv2.imwrite(out, to_save)
            print(f"[SAVE] {out}")
        elif is_exit_key(key):
            break

        # 모드별로 표시 갱신
        if mode == "color":
            cv2.imshow(win_resizable, img)
        elif mode == "gray":
            cv2.imshow(win_resizable, gray)
        else:
            cv2.imshow(win_resizable, inv)

    close_all_windows()


# =============================================================================
# demo 03. (이미지 Shape/파일 쓰기/실습1)
def demo_02b_window_flags_and_keyboard_color(args: argparse.Namespace) -> None:
    """
    [윈도우/키 이벤트] WINDOW 플래그 + resizeWindow/moveWindow + 키 입력으로 색상 토글

    포함 개념(요청 사항):
    - WINDOW_NORMAL / AUTOSIZE / FULLSCREEN / FREERATIO / KEEPRATIO 개념
      * cv2.WINDOW_NORMAL, cv2.WINDOW_AUTOSIZE
      * cv2.WINDOW_FULLSCREEN
      * cv2.WINDOW_FREERATIO, cv2.WINDOW_KEEPRATIO
    - resizeWindow(), moveWindow()
    - waitKey 반환값(ASCII) + & 0xFF 처리
    - 키 입력으로 이미지 색상 변경(r/g/b) 및 종료(q/ESC)
    """
    cv2 = require_cv2()
    np = require_np()

    img = np.zeros((300, 400, 3), dtype=np.uint8)

    # WINDOW_NORMAL: 크기 조절 가능
    safe_named_window("demo_02b_window", resizable=True)
    cv2.resizeWindow("demo_02b_window", 800, 600)
    cv2.moveWindow("demo_02b_window", 100, 100)

    print("\n[조작] r/g/b: 색 변경, q 또는 ESC: 종료")
    while True:
        cv2.imshow("demo_02b_window", img)
        key = cv2.waitKey(30) & 0xFF

        if key == ord("q") or key == 27:
            break
        elif key == ord("r"):
            img[:] = (0, 0, 255)
            print("-> 빨강")
        elif key == ord("g"):
            img[:] = (0, 255, 0)
            print("-> 초록")
        elif key == ord("b"):
            img[:] = (255, 0, 0)
            print("-> 파랑")

    close_window("demo_02b_window")


def demo_03_image_shape_and_write(args: argparse.Namespace) -> None:
    """
    [이미지 I/O] imread 플래그 + None 처리 + imwrite 옵션(JPEG 품질/PNG 압축)

    포함 개념(요청 사항):
    - cv2.imread(path, flag): COLOR/GRAYSCALE/UNCHANGED
    - 로드 실패(None) 처리
    - 지원 형식 개요(BMP/JPEG/PNG/TIFF/WebP 등)
    - cv2.imwrite(path, img, [옵션]): JPEG 품질, PNG 압축레벨
    """
    cv2 = require_cv2()
    np = require_np()

    # -----------------------------
    # 1) 이미지 읽기 (imread)
    # -----------------------------
    img_path = args.image if args.image else auto_find_image(".")
    if not img_path:
        print("[WARN] 샘플 이미지를 찾지 못했습니다. --image로 경로를 지정하거나, 현재 폴더에 이미지(JPG/PNG)를 두세요.")
    else:
        print(f"\n[imread] path = {img_path}")

        img_color = cv2.imread(img_path, cv2.IMREAD_COLOR)
        img_gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        img_unchanged = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

        if img_color is None:
            print("[ERROR] 이미지를 읽을 수 없습니다. 경로/형식/손상 여부를 확인하세요.")
        else:
            print(f"- COLOR shape: {img_color.shape} (BGR)")
            if img_gray is not None:
                print(f"- GRAYSCALE shape: {img_gray.shape}")
            if img_unchanged is not None:
                print(f"- UNCHANGED shape: {img_unchanged.shape} (알파 포함 가능)")

            safe_named_window("demo_03_color", resizable=True)
            cv2.imshow("demo_03_color", img_color)

            if img_gray is not None:
                safe_named_window("demo_03_gray", resizable=True)
                cv2.imshow("demo_03_gray", img_gray)

            if img_unchanged is not None and img_unchanged.ndim == 3 and img_unchanged.shape[2] == 4:
                # 알파 채널 포함(예: PNG)
                safe_named_window("demo_03_unchanged_RGBA", resizable=True)
                cv2.imshow("demo_03_unchanged_RGBA", img_unchanged)

            print("\n[조작] 아무 키나 누르면 저장(imwrite) 예제로 넘어갑니다.")
            cv2.waitKey(0)
            close_window("demo_03_color")
            close_window("demo_03_gray")
            close_window("demo_03_unchanged_RGBA")

    # -----------------------------
    # 2) 이미지 쓰기 (imwrite)
    # -----------------------------
    print("\n[imwrite] 저장 옵션 예제(랜덤 이미지 생성 후 저장)")
    rand_img = np.random.randint(0, 256, (600, 800, 3), dtype=np.uint8)

    # 출력 폴더
    # - 예제 파일이 현재 폴더에 무분별하게 쌓이지 않도록 기본 출력 폴더를 사용합니다.
    # - --save <폴더경로> 로 바꾸고 싶으면 폴더 경로를 지정하세요.
    out_dir = args.save.strip() if getattr(args, "save", "") else "_outputs"
    os.makedirs(out_dir, exist_ok=True)

    # 기본 저장
    ok = cv2.imwrite(os.path.join(out_dir, "output.jpg"), rand_img)
    print(f"- output.jpg 저장: {'성공' if ok else '실패'} (dir={out_dir})")

    # JPEG 품질(Quality): 0~100 (기본값은 보통 95)
    # - 높을수록 화질 ↑ 파일크기 ↑, 낮을수록 화질 ↓ 파일크기 ↓
    cv2.imwrite(os.path.join(out_dir, "low_quality.jpg"), rand_img, [cv2.IMWRITE_JPEG_QUALITY, 30])
    cv2.imwrite(os.path.join(out_dir, "high_quality.jpg"), rand_img, [cv2.IMWRITE_JPEG_QUALITY, 100])
    print("- low_quality.jpg (JPEG 품질 30), high_quality.jpg (JPEG 품질 100) 저장 완료")

    # PNG 압축(Compression): 0~9 (기본값은 보통 3)
    # - PNG는 '무손실 압축'이라 화질은 동일하고, 속도/파일크기만 변합니다.
    cv2.imwrite(os.path.join(out_dir, "fast_png.png"), rand_img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    cv2.imwrite(os.path.join(out_dir, "small_png.png"), rand_img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
    print("- fast_png.png (압축 0), small_png.png (압축 9) 저장 완료")

    # (추가) WebP 저장 품질 옵션: 1~100
    # - OpenCV 빌드/플러그인에 따라 WebP 저장이 불가할 수 있으므로 예외 처리
    try:
        cv2.imwrite(os.path.join(out_dir, "webp_q80.webp"), rand_img, [cv2.IMWRITE_WEBP_QUALITY, 80])
        print("- webp_q80.webp (WebP 품질 80) 저장 완료")
    except Exception as e:
        print("[WARN] WebP 저장 미지원/실패:", e)

    # (추가) PNG Strategy: 압축 전략 선택
    # - 이미지 특성에 따라 파일 크기/속도 차이가 날 수 있습니다.
    try:
        cv2.imwrite(
            os.path.join(out_dir, "png_strategy_default.png"),
            rand_img,
            [cv2.IMWRITE_PNG_COMPRESSION, 6, cv2.IMWRITE_PNG_STRATEGY, cv2.IMWRITE_PNG_STRATEGY_DEFAULT],
        )
        cv2.imwrite(
            os.path.join(out_dir, "png_strategy_filtered.png"),
            rand_img,
            [cv2.IMWRITE_PNG_COMPRESSION, 6, cv2.IMWRITE_PNG_STRATEGY, cv2.IMWRITE_PNG_STRATEGY_FILTERED],
        )
        cv2.imwrite(
            os.path.join(out_dir, "png_strategy_huffman.png"),
            rand_img,
            [cv2.IMWRITE_PNG_COMPRESSION, 6, cv2.IMWRITE_PNG_STRATEGY, cv2.IMWRITE_PNG_STRATEGY_HUFFMAN_ONLY],
        )
        print("- png_strategy_*.png (PNG_STRATEGY) 저장 완료")
    except Exception as e:
        print("[WARN] PNG_STRATEGY 저장 실패:", e)

    # (추가) TIFF 압축 방식(예시)
    # - TIFF는 옵션/압축 방식이 다양하고, 환경에 따라 codec 지원이 달라질 수 있습니다.
    try:
        cv2.imwrite(
            os.path.join(out_dir, "tiff_compression_1.tiff"),
            rand_img,
            [cv2.IMWRITE_TIFF_COMPRESSION, 1],
        )
        print("- tiff_compression_1.tiff (TIFF_COMPRESSION=1) 저장 완료")
    except Exception as e:
        print("[WARN] TIFF 저장 미지원/실패:", e)

    safe_named_window("demo_03_saved_preview", resizable=True)
    cv2.imshow("demo_03_saved_preview", rand_img)
    print("\n[조작] q 또는 ESC를 누르면 종료합니다.")
    while True:
        key = cv2.waitKey(20)
        if is_exit_key(key):
            break
    close_window("demo_03_saved_preview")


def demo_04_video_file_capture(args: argparse.Namespace) -> None:
    """
    [비디오] VideoCapture 기본 + 속성 읽기 + (파일일 때) 탐색(seek) 예제

    포함 개념(요청 사항):
    - VideoCapture(파일/카메라) 열기 + isOpened() 확인
    - cap.get()으로 주요 속성 읽기:
        * CAP_PROP_FRAME_WIDTH / HEIGHT
        * CAP_PROP_FPS
        * CAP_PROP_FRAME_COUNT
        * CAP_PROP_FOURCC
        * CAP_PROP_POS_FRAMES / POS_MSEC
    - (비디오 파일에서) cap.set()으로 위치 이동:
        * CAP_PROP_POS_FRAMES: 특정 프레임 번호로 이동
        * CAP_PROP_POS_MSEC  : 특정 시간(밀리초)으로 이동
    - 프레임 루프 재생 + waitKey로 재생 제어(속도/일시정지)
    """
    cv2 = require_cv2()

    source = args.source if args.source else (auto_find_video(".") or "0")

    cap = _open_capture(source)
    if cap is None:
        return

    print(f"\n[VideoCapture] source = {source}")

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fps = float(fps) if fps and fps > 1 else 30.0

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))

    print(f"- 해상도: {width}x{height}")
    print(f"- FPS: {fps:.2f}")
    if frame_count > 0:
        print(f"- 총 프레임 수: {frame_count}")
        print(f"- 재생 시간(추정): {frame_count / fps:.2f}초")
    else:
        print("- 총 프레임 수: (카메라/스트림은 보통 0 또는 -1)")

    print(f"- FOURCC(codec id): {fourcc}")

    win = "demo_04_video"
    safe_named_window(win, resizable=True)

    paused = False
    delay_ms = 30

    print("\n[조작]")
    print("- SPACE: 일시정지/재생")
    print("- +/-   : 재생 속도 조절")
    print("- 0     : 처음으로 이동(파일일 때)")
    print("- j     : 프레임 200으로 이동(파일일 때)")
    print("- t     : 5초 위치로 이동(파일일 때)")
    print("- s     : 현재 프레임 저장")
    print("- q/ESC : 종료")

    last_frame = None

    while True:
        if not paused:
            ret, frame = cap.read()
            if not ret:
                print("[INFO] 더 이상 읽을 프레임이 없습니다(재생 종료).")
                break
            last_frame = frame
        else:
            if last_frame is None:
                ret, frame = cap.read()
                if not ret:
                    break
                last_frame = frame
            frame = last_frame

        pos_frames = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
        pos_msec = float(cap.get(cv2.CAP_PROP_POS_MSEC) or 0.0)

        overlay = frame.copy()
        cv2.putText(
            overlay,
            f"frame={pos_frames}  time={pos_msec/1000:.2f}s  delay={delay_ms}ms  paused={paused}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2,
            cv2.LINE_AA,
        )

        cv2.imshow(win, overlay)
        key = cv2.waitKey(1 if paused else delay_ms) & 0xFF

        if key in (ord("q"), 27):
            break
        elif key == ord(" "):
            paused = not paused
        elif key == ord("+"):
            delay_ms = max(1, delay_ms - 5)
        elif key == ord("-"):
            delay_ms = min(200, delay_ms + 5)
        elif key == ord("s"):
            stem = args.save if args.save else "frame_capture"
            stem = os.path.splitext(stem)[0]
            out_path = f"{stem}_frame{pos_frames}.jpg"
            ok = cv2.imwrite(out_path, frame)
            print(f"[SAVE] {out_path} -> {'OK' if ok else 'FAIL'}")
        elif key == ord("0"):
            ok = cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            if not ok:
                print("[INFO] 프레임 이동(cap.set)이 지원되지 않을 수 있습니다(카메라/스트림).")
        elif key == ord("j"):
            ok = cap.set(cv2.CAP_PROP_POS_FRAMES, 200)
            if not ok:
                print("[INFO] 프레임 이동(cap.set)이 지원되지 않을 수 있습니다(카메라/스트림).")
        elif key == ord("t"):
            ok = cap.set(cv2.CAP_PROP_POS_MSEC, 5000)
            if not ok:
                print("[INFO] 시간 이동(cap.set)이 지원되지 않을 수 있습니다(카메라/스트림).")

    cap.release()
    close_window(win)


def demo_05_webcam_basics(args) -> None:
    """
    [개념]
    - 웹캠은 보통 source=0
    - cap.set으로 일부 속성(해상도/밝기 등)을 설정할 수 있지만
      카메라/드라이버가 지원하지 않으면 반영되지 않을 수 있습니다.

    [예제]
    - 'p' 키: 현재 프레임 저장(사진 찍기)
    - 'b'/'n': 밝기 조절 시도(CAP_PROP_BRIGHTNESS)
    - 'q'/ESC: 종료
    """
    # webcam은 기본 0으로
    src = args.source or "0"
    cap = _open_capture(src)

    # 해상도 설정 시도(지원하지 않으면 무시될 수 있음)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    brightness = cap.get(cv2.CAP_PROP_BRIGHTNESS)
    print(f"[INFO] initial brightness: {brightness}")
    print("[KEY] p=snapshot, b/n=brightness +/- , q/ESC=quit")

    snap_idx = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("demo05_webcam (press q/ESC)", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("p"):
            out = args.save or f"demo05_snapshot_{snap_idx:02d}.png"
            cv2.imwrite(out, frame)
            print(f"[SNAPSHOT] {out}")
            snap_idx += 1
        elif key == ord("b"):
            brightness = brightness + 0.05
            cap.set(cv2.CAP_PROP_BRIGHTNESS, brightness)
            print(f"[BRIGHTNESS] set -> {brightness}")
        elif key == ord("n"):
            brightness = brightness - 0.05
            cap.set(cv2.CAP_PROP_BRIGHTNESS, brightness)
            print(f"[BRIGHTNESS] set -> {brightness}")
        elif is_exit_key(key):
            break

    cap.release()
    close_all_windows()


# =============================================================================
# demo 06. (비디오 파일로 쓰기: VideoWriter)
def demo_06_video_writer(args) -> None:
    """
    [개념] VideoWriter
    - 저장 코덱(fourcc), fps, 프레임 크기(W,H)가 매우 중요합니다.
    - 입력 영상과 동일한 fps/해상도를 쓰는 것이 가장 안전합니다.

    [예제]
    - 입력 소스(파일/웹캠)에서 N초만큼 받아서 파일로 저장
    """
    cap = _open_capture(args.source)
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) or 640)
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) or 480)

    out_path = args.save or "demo06_output.mp4"

    # 코덱 지정 (mp4v는 비교적 호환성 좋음)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(out_path, fourcc, float(fps), (w, h))

    if not writer.isOpened():
        raise RuntimeError("VideoWriter 오픈 실패: 코덱/경로/권한 확인")

    seconds = 5
    max_frames = int(seconds * fps)
    print(f"[WRITE] {out_path}  ({seconds}s ≈ {max_frames} frames, {w}x{h}, fps={fps})")

    n = 0
    while n < max_frames:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame, (w, h))  # 안전을 위해 강제
        writer.write(frame)
        cv2.imshow("demo06_writing (press q/ESC)", frame)
        if is_exit_key(cv2.waitKey(1) & 0xFF):
            break
        n += 1

    writer.release()
    cap.release()
    close_all_windows()
    print("[DONE]")


# =============================================================================
# demo 07. (픽셀 접근/빈 화면/일부 영역 색칠/이미지 복사)
def demo_06b_webcam_record_toggle(args: argparse.Namespace) -> None:
    """
    [웹캠 녹화] r 키로 녹화 시작/중지 토글 + REC 표시 + 파일 저장(VideoWriter)

    포함 개념(요청 사항):
    - VideoCapture(0)로 웹캠 열기
    - VideoWriter 설정(fourcc/fps/size)
    - 녹화 상태 플래그(recording)로 out.write 제어
    - 녹화 중 화면에 빨간 원 + "REC" 텍스트 표시(circle/putText)
    """
    cv2 = require_cv2()

    cap = _open_capture("0")
    if cap is None:
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fps = 20  # 녹화 fps(고정)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    out_path = args.save if args.save else "recording.mp4"
    out = cv2.VideoWriter(out_path, fourcc, fps, (width, height))

    recording = False

    print("\n=== 웹캠 녹화 프로그램 ===")
    print("- r: 녹화 시작/중지")
    print("- q 또는 ESC: 종료")
    print(f"- 저장 파일: {out_path}")

    win = "demo_06b_record"
    safe_named_window(win, resizable=True)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if recording:
            cv2.circle(frame, (30, 30), 10, (0, 0, 255), -1)
            cv2.putText(frame, "REC", (50, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            out.write(frame)

        cv2.imshow(win, frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("r"):
            recording = not recording
            print(f"녹화: {'시작' if recording else '중지'}")
        elif key == ord("q") or key == 27:
            break

    cap.release()
    out.release()
    close_window(win)
    print("프로그램 종료")


def demo_07_pixel_access_roi(args) -> None:
    """
    [개념] 픽셀 접근
    - img[y, x] = (B, G, R)  (컬러)
    - ROI(관심영역): img[y1:y2, x1:x2]
      * 슬라이싱은 "뷰(view)"일 수 있으므로 원본이 같이 바뀔 수 있음
      * 복사본이 필요하면 .copy()

    [예제]
    - 빈 화면 생성 후 사각형 영역 색칠
    - 원본 이미지에서 ROI를 잘라 별도 창에 표시
    - ROI를 다른 위치에 복사(패치 복사)
    """
    img = _load_or_make_image(args.image)
    canvas = make_blank(640, 420, color_bgr=(30, 30, 30))

    # (요청 예제) 단일 픽셀 접근 (NumPy 인덱싱: [y, x])
    img_demo = np.zeros((200, 200, 3), dtype=np.uint8)
    pixel = img_demo[50, 100]  # y=50, x=100
    print(f"- img_demo[50,100] 읽기(BGR): {pixel}")
    img_demo[50, 100] = [200, 0, 0]
    print(f"- img_demo[50,100] 쓰기(BGR): {img_demo[50, 100]}")

    # 단일 픽셀 접근 예시 (NumPy 인덱싱: [y, x])
    pixel = canvas[50, 100]  # y=50, x=100
    print(f"- (50,100) 픽셀(BGR) 읽기: {pixel}")
    canvas[50, 100] = [200, 0, 0]  # 파란색 계열로 변경
    print(f"- (50,100) 픽셀(BGR) 쓰기: {canvas[50, 100]}")

    # 일부 영역 색칠(ROI)
    canvas[50:200, 80:300] = (0, 0, 255)   # 빨강(BGR)
    canvas[220:380, 320:600] = (0, 255, 0) # 초록

    # 원본에서 ROI 추출
    h, w = img.shape[:2]
    y1, y2 = int(h * 0.25), int(h * 0.65)
    x1, x2 = int(w * 0.25), int(w * 0.65)
    roi = img[y1:y2, x1:x2]
    roi_copy = roi.copy()  # "이미지 복사" 개념

    # ROI를 캔버스에 붙여넣기(크기 맞추기)
    roi_resized = cv2.resize(roi_copy, (220, 160))
    canvas[20:20 + 160, 20:20 + 220] = roi_resized

    safe_imshow("demo07_canvas (q/ESC)", canvas, resizable=True, wait=1)
    safe_imshow("demo07_roi (q/ESC)", roi_copy, resizable=True, wait=1)
    _show_until_exit("demo07_canvas (q/ESC)")
    close_all_windows()


# =============================================================================
# demo 08. (색상/RGB/BGR, 색상 변경, 채널 분리/병합, 실습4: 흑백 반전)
def demo_08_color_and_channels(args) -> None:
    """
    [개념] BGR vs RGB
    - OpenCV는 기본 BGR
    - Matplotlib 등은 보통 RGB를 기대
    - cv2.cvtColor로 변환: BGR↔RGB, BGR→GRAY 등

    [개념] 채널 분리/병합
    - b, g, r = cv2.split(img)
    - img2 = cv2.merge([b, g, r])

    [예제]
    - (1) 채널 분리 후 각 채널 시각화
    - (2) 특정 채널만 강조(예: R만 남기기)
    - (3) 흑백 반전(실습4)
    """
    img = _load_or_make_image(args.image)
    gray = bgr_to_gray(img)
    inv = 255 - gray

    b, g, r = cv2.split(img)

    # 채널을 3채널 이미지로 만들어서 보기 좋게 표시
    zeros = np.zeros_like(b)
    only_b = cv2.merge([b, zeros, zeros])
    only_g = cv2.merge([zeros, g, zeros])
    only_r = cv2.merge([zeros, zeros, r])

    # 색상 변경 예시: BGR→RGB
    rgb = bgr_to_rgb(img)

    safe_imshow("demo08_original(BGR) (q/ESC)", img, resizable=True, wait=1)
    safe_imshow("demo08_only_B (q/ESC)", only_b, resizable=True, wait=1)
    safe_imshow("demo08_only_G (q/ESC)", only_g, resizable=True, wait=1)
    safe_imshow("demo08_only_R (q/ESC)", only_r, resizable=True, wait=1)
    safe_imshow("demo08_gray (q/ESC)", gray, resizable=True, wait=1)
    safe_imshow("demo08_invert(gray) (q/ESC)", inv, resizable=True, wait=1)

    # 참고: RGB 배열을 OpenCV imshow로 보여도 "BGR로 해석"되므로 색이 뒤집혀 보입니다.
    # 따라서 여기서는 RGB 배열을 다시 BGR로 바꿔서 표시(시각적 비교 목적)
    bgr_from_rgb = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
    safe_imshow("demo08_RGB->BGR display (q/ESC)", bgr_from_rgb, resizable=True, wait=1)

    _show_until_exit("demo08_original(BGR) (q/ESC)")
    close_all_windows()


# =============================================================================
# demo 09. (이미지 조정/리사이즈/보간법)
def demo_09_resize_interpolation(args) -> None:
    """
    [개념] 리사이즈
    - cv2.resize(src, dsize, fx, fy, interpolation=...)
    - 보간법(interpolation) 선택이 화질에 큰 영향을 줍니다.
      * INTER_NEAREST: 가장 가까운 픽셀(빠름, 계단 현상)
      * INTER_LINEAR : 기본(확대/축소 무난)
      * INTER_AREA   : 축소에 유리
      * INTER_CUBIC / INTER_LANCZOS4: 확대에 유리(느리지만 품질 좋음)

    [예제]
    - 동일 이미지를 다양한 보간법으로 확대/축소 비교
    """
    img = _load_or_make_image(args.image)

    # 비교를 위해 축소/확대 비율
    scale_up = 1.8
    scale_down = 0.5

    def _resize(im, scale, inter):
        h, w = im.shape[:2]
        return cv2.resize(im, (int(w * scale), int(h * scale)), interpolation=inter)

    ups = {
        "NEAREST": _resize(img, scale_up, cv2.INTER_NEAREST),
        "LINEAR": _resize(img, scale_up, cv2.INTER_LINEAR),
        "CUBIC": _resize(img, scale_up, cv2.INTER_CUBIC),
        "LANCZOS4": _resize(img, scale_up, cv2.INTER_LANCZOS4),
    }
    downs = {
        "NEAREST": _resize(img, scale_down, cv2.INTER_NEAREST),
        "LINEAR": _resize(img, scale_down, cv2.INTER_LINEAR),
        "AREA": _resize(img, scale_down, cv2.INTER_AREA),
    }

    safe_imshow("demo09_original (q/ESC)", img, resizable=True, wait=1)
    for k, v in ups.items():
        safe_imshow(f"demo09_up_{k} (q/ESC)", v, resizable=True, wait=1)
    for k, v in downs.items():
        safe_imshow(f"demo09_down_{k} (q/ESC)", v, resizable=True, wait=1)

    _show_until_exit("demo09_original (q/ESC)")
    close_all_windows()


def demo_09b_exercise_5_resize_video(args) -> None:
    """
    [실습5] 영상 리사이즈 해서 출력
    - 비디오/웹캠 프레임을 읽어서 리사이즈 후 표시하는 실습
    """
    cap = _open_capture(args.source)
    target_w, target_h = 640, 360
    print("[KEY] q/ESC=quit")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        resized = cv2.resize(frame, (target_w, target_h), interpolation=cv2.INTER_AREA)
        cv2.imshow("demo09b_video_resized (q/ESC)", resized)
        if is_exit_key(cv2.waitKey(1) & 0xFF):
            break

    cap.release()
    close_all_windows()


# =============================================================================
# demo 10. (이미지 피라미드)
def demo_10_pyramids(args) -> None:
    """
    [개념] 이미지 피라미드
    - cv2.pyrDown: 한 단계 축소(가우시안 블러 + 다운샘플)
    - cv2.pyrUp  : 한 단계 확대(업샘플 + 블러)
    - 특징:
      * 단순 resize와 다르게, 피라미드는 멀티스케일 처리에 자주 쓰입니다.
      * 완벽한 역변환이 아니므로 pyrDown→pyrUp 해도 원본과 동일하지 않습니다.

    [예제]
    - 원본 → pyrDown → pyrDown → pyrUp → pyrUp 비교
    """
    img = _load_or_make_image(args.image)

    d1 = cv2.pyrDown(img)
    d2 = cv2.pyrDown(d1)
    u1 = cv2.pyrUp(d2)
    u2 = cv2.pyrUp(u1)

    safe_imshow("demo10_original (q/ESC)", img, resizable=True, wait=1)
    safe_imshow("demo10_pyrDown_1 (q/ESC)", d1, resizable=True, wait=1)
    safe_imshow("demo10_pyrDown_2 (q/ESC)", d2, resizable=True, wait=1)
    safe_imshow("demo10_pyrUp_1 (q/ESC)", u1, resizable=True, wait=1)
    safe_imshow("demo10_pyrUp_2 (q/ESC)", u2, resizable=True, wait=1)

    _show_until_exit("demo10_original (q/ESC)")
    close_all_windows()


# =============================================================================
# demo 11. (이미지 자르기/대칭/실습6: 이미지 조정)
def demo_11_crop_flip(args) -> None:
    """
    [개념] 이미지 자르기(crop)
    - ROI: img[y1:y2, x1:x2]
    - 필요 시 copy()

    [개념] 이미지 대칭(flip)
    - cv2.flip(src, flipCode)
      * flipCode > 0: 좌우 반전
      * flipCode == 0: 상하 반전
      * flipCode < 0: 상하좌우 반전

    [실습6] "이미지 조정"
    - crop + flip + resize를 조합해 보기
    """
    img = _load_or_make_image(args.image)
    h, w = img.shape[:2]

    # 중앙부 crop
    cy1, cy2 = int(h * 0.2), int(h * 0.8)
    cx1, cx2 = int(w * 0.2), int(w * 0.8)
    crop = img[cy1:cy2, cx1:cx2].copy()

    # flip variants
    flip_lr = cv2.flip(crop, 1)
    flip_ud = cv2.flip(crop, 0)
    flip_both = cv2.flip(crop, -1)

    # resize to compare
    crop_big = cv2.resize(crop, (w, h), interpolation=cv2.INTER_CUBIC)

    safe_imshow("demo11_original (q/ESC)", img, resizable=True, wait=1)
    safe_imshow("demo11_crop (q/ESC)", crop, resizable=True, wait=1)
    safe_imshow("demo11_crop_big (q/ESC)", crop_big, resizable=True, wait=1)
    safe_imshow("demo11_flip_lr (q/ESC)", flip_lr, resizable=True, wait=1)
    safe_imshow("demo11_flip_ud (q/ESC)", flip_ud, resizable=True, wait=1)
    safe_imshow("demo11_flip_both (q/ESC)", flip_both, resizable=True, wait=1)

    _show_until_exit("demo11_original (q/ESC)")
    close_all_windows()


# =============================================================================
# [추가 개념/응용] (PDF 외 확장)
def demo_12_bonus_frame_skip(args) -> None:
    """
    [추가 예제] 프레임 스킵(Frame Skipping)
    - 모든 프레임을 처리하면 CPU/GPU가 과부하될 수 있습니다.
    - 예: 30fps 영상에서 3프레마다 1번만 처리하면, 처리부하는 약 1/3로 감소.
    """
    cap = _open_capture(args.source)
    skip = 3
    idx = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        idx += 1
        if idx % skip != 0:
            continue

        cv2.imshow("demo12_frame_skip (q/ESC)", frame)
        if is_exit_key(cv2.waitKey(1) & 0xFF):
            break

    cap.release()
    close_all_windows()

# =============================================================================
# [추가] 사용자 제공 예제: 텍스트 그리기 + 마우스/키보드 이벤트 + 종합 실습 + 저장/웹캠
# -----------------------------------------------------------------------------
# 아래 데모(13~20)는 사용자가 제공한 'OpenCV 기초 01~05' 예제를
# 이 파일의 데모 러너 체계에 맞춰 그대로 실행 가능하도록 편입한 것입니다.
#
# 원문의 개념/예제는 생략하지 않았고, 실행 편의를 위해 "데모 단위"로만 묶었습니다.
# 저장 파일은 기본적으로 현재 작업 폴더의 output/ 아래에 생성됩니다.
# =============================================================================

from pathlib import Path


def _output_dir() -> Path:
    """
    결과물을 한 곳에 모으기 위한 출력 폴더 유틸리티.

    - 교육/실습 코드에서 파일이 여기저기 흩어지지 않도록 output/를 기본 경로로 사용합니다.
    - 폴더가 없으면 자동 생성합니다.
    """
    out = Path("output")
    out.mkdir(parents=True, exist_ok=True)
    return out


def draw_centered_text(img, text, font, scale, color, thickness=1):
    """
    이미지 중앙에 텍스트를 그려주는 함수.

    왜 필요할까?
    - cv2.putText()는 '텍스트 시작점'을 직접 지정해야 합니다.
    - 중앙 배치를 하려면 텍스트의 실제 픽셀 크기(가로/세로)를 먼저 계산해야 합니다.
    - 이 함수는 getTextSize()로 크기를 계산한 뒤, 중앙 좌표를 자동 산출하여 배치합니다.

    핵심 포인트:
    - OpenCV 좌표는 (x, y) 순서
    - 텍스트 위치 org는 "좌하단(baseline 기준)" 좌표
    - getTextSize()는 (text_width, text_height)와 baseline을 반환
    """
    cv = require_cv2()

    h, w = img.shape[:2]  # 이미지의 높이와 너비

    # 텍스트 크기 미리 계산하기
    # getTextSize()는 텍스트가 얼마나 큰 공간을 차지하는지 알려줍니다.
    # - text_width : 텍스트가 차지하는 가로 길이(픽셀)
    # - text_height: 텍스트가 차지하는 세로 높이(글자 위 ~ 기준선)
    # - baseline   : 'g', 'y', 'p' 같은 글자의 아래로 내려가는 부분을 위한 추가 공간
    (text_width, text_height), baseline = cv.getTextSize(text, font, scale, thickness)

    # 중앙에 배치할 시작 좌표 계산
    # - x: (전체 너비 - 텍스트 너비) / 2
    # - y: (전체 높이 + 텍스트 높이) / 2
    #   (주의) putText의 org는 baseline 기준이므로 text_height를 더해주는 형태가 자연스럽습니다.
    x = (w - text_width) // 2
    y = (h + text_height) // 2

    # 계산한 위치에 텍스트 그리기
    cv.putText(img, text, (x, y), font, scale, color, thickness, cv.LINE_AA)


def demo_13_centered_text(args: argparse.Namespace) -> None:
    """
    OpenCV 기초 - 01. 텍스트 그리기와 이벤트 처리 (파트 1)
    1) 이미지 중앙에 텍스트를 예쁘게 배치하는 방법
    """
    cv = require_cv2()
    np = require_np()

    canvas = np.zeros((300, 400, 3), dtype=np.uint8)

    # 중앙 정렬 텍스트 그리기
    draw_centered_text(
        canvas,
        "Centered Text",
        cv.FONT_HERSHEY_SIMPLEX,
        1.0,
        (255, 255, 255),
        thickness=2,
    )

    # 결과 표시
    safe_imshow("13 - Centered Text", canvas)
    print("[Demo 13] 중앙 정렬 텍스트를 표시했습니다. 아무 키(또는 닫기)로 종료하세요.")
    cv.waitKey(0)
    close_all_windows()


def demo_14_mouse_events(args: argparse.Namespace) -> None:
    """
    OpenCV 기초 - 01. 텍스트 그리기와 이벤트 처리 (파트 2)
    2) 마우스 클릭, 드래그 등의 마우스 이벤트 처리하기

    언제 사용할까?
    - 이미지에 그림을 그리는 프로그램 만들 때
    - 이미지에서 특정 영역을 선택할 때
    - 마우스로 물체의 위치를 표시할 때

    콜백 시그니처:
    mouse_callback(event, x, y, flags, param)

    - event: 어떤 마우스 동작이 일어났는지 (클릭, 드래그 등)
    - x, y : 마우스 좌표 (픽셀)
    - flags: Ctrl, Shift 같은 특수 키가 눌렸는지, 버튼이 눌린 상태인지
    - param: 추가로 전달할 데이터(사용자 정의)
    """
    cv = require_cv2()
    np = require_np()

    # 화면에 그릴 캔버스
    canvas = np.zeros((400, 600, 3), dtype=np.uint8)

    # 드래그 상태 관리용 딕셔너리(param으로 전달)
    state = {
        "dragging": False,
        "start": None,   # (x, y)
        "temp": canvas.copy(),  # 드래그 중 미리보기용
    }

    def mouse_callback(event, x, y, flags, param):
        """
        마우스 이벤트를 처리하는 콜백 함수.

        📌 자주 사용하는 마우스 이벤트:
        - cv2.EVENT_MOUSEMOVE     : 마우스를 움직일 때
        - cv2.EVENT_LBUTTONDOWN   : 왼쪽 버튼을 누를 때
        - cv2.EVENT_LBUTTONUP     : 왼쪽 버튼을 뗄 때
        - cv2.EVENT_LBUTTONDBLCLK : 왼쪽 버튼 더블클릭
        - cv2.EVENT_RBUTTONDOWN   : 오른쪽 버튼을 누를 때
        - cv2.EVENT_RBUTTONUP     : 오른쪽 버튼을 뗄 때
        - cv2.EVENT_MBUTTONDOWN   : 가운데 버튼(휠 클릭)
        - cv2.EVENT_MOUSEWHEEL    : 마우스 휠

        📌 flags로 특수 키/버튼 상태 확인:
        - cv2.EVENT_FLAG_LBUTTON  : 왼쪽 버튼이 눌린 상태인지
        - cv2.EVENT_FLAG_RBUTTON  : 오른쪽 버튼이 눌린 상태인지
        - cv2.EVENT_FLAG_CTRLKEY  : Ctrl 키가 눌렸는지
        - cv2.EVENT_FLAG_SHIFTKEY : Shift 키가 눌렸는지
        - cv2.EVENT_FLAG_ALTKEY   : Alt 키가 눌렸는지
        """
        st = param

        # 왼쪽 클릭 시작: 드래그 시작점 기록
        if event == cv.EVENT_LBUTTONDOWN:
            print(f"왼쪽 클릭: ({x}, {y})")
            st["dragging"] = True
            st["start"] = (x, y)
            st["temp"] = canvas.copy()

        # 마우스 이동: 드래그 중이면 사각형 미리보기
        elif event == cv.EVENT_MOUSEMOVE:
            if st["dragging"] and (flags & cv.EVENT_FLAG_LBUTTON):
                x0, y0 = st["start"]
                preview = canvas.copy()
                cv.rectangle(preview, (x0, y0), (x, y), (0, 255, 0), 2)
                st["temp"] = preview

        # 왼쪽 버튼 해제: 드래그 종료 + 사각형 확정
        elif event == cv.EVENT_LBUTTONUP:
            print(f"왼쪽 버튼 해제: ({x}, {y})")
            if st["dragging"]:
                x0, y0 = st["start"]
                cv.rectangle(canvas, (x0, y0), (x, y), (0, 255, 0), 2)
            st["dragging"] = False
            st["start"] = None
            st["temp"] = canvas.copy()

        # 오른쪽 클릭: 클릭 지점에 원 그리기 (추적/표시 예시)
        elif event == cv.EVENT_RBUTTONDOWN:
            print(f"오른쪽 클릭: ({x}, {y})")
            cv.circle(canvas, (x, y), 6, (0, 0, 255), -1)
            st["temp"] = canvas.copy()

    win = "14 - Mouse Event"
    cv.namedWindow(win, cv.WINDOW_NORMAL)
    cv.setMouseCallback(win, mouse_callback, state)

    print("[Demo 14] 마우스 이벤트 데모를 시작합니다.")
    print(" - 왼쪽 드래그: 사각형 그리기")
    print(" - 오른쪽 클릭: 점(원) 표시")
    print(" - q 또는 ESC: 종료")

    while True:
        # 드래그 중이면 미리보기(temp), 아니면 확정 캔버스(canvas)
        frame = state["temp"] if state["dragging"] else canvas
        safe_imshow(win, frame)

        key = cv.waitKey(15) & 0xFF
        if key in (ord("q"), 27):  # q 또는 ESC
            break

    close_all_windows()


def demo_15_keyboard_events(args: argparse.Namespace) -> None:
    """
    OpenCV 기초 - 01. 텍스트 그리기와 이벤트 처리 (파트 3)
    3) 키보드 입력 받아서 처리하기

    OpenCV에서는 cv2.waitKey()로 키보드 입력을 받을 수 있습니다.
    - cv2.waitKey(0): 키를 누를 때까지 무한 대기
    - cv2.waitKey(1): 1ms만 대기 (동영상 재생 등에 사용)
    - cv2.waitKey(100): 100ms 대기
    """
    cv = require_cv2()
    np = require_np()

    canvas = np.zeros((400, 600, 3), dtype=np.uint8)

    print("[Demo 15] 키 입력 테스트 시작! (q 또는 ESC로 종료)")

    while True:
        safe_imshow("15 - Keyboard", canvas)

        key = cv.waitKey(100)  # 100ms 동안 키 입력 대기

        # 키가 입력되지 않았으면 -1이 반환됨
        if key == -1:
            continue

        # 키 코드 추출 (운영체제/플랫폼에 따라 상위 비트가 섞일 수 있어 하위 8비트만 사용)
        key = key & 0xFF

        # 📌 자주 사용하는 특수 키 코드:
        # - 27: ESC
        # - 13: Enter
        # - 32: Space
        # - 8 : Backspace
        # - 9 : Tab
        #
        # ⚠️ 화살표 키는 운영체제마다 달라질 수 있습니다.
        # - Windows에서 화살표 키 등을 안정적으로 다루려면 cv2.waitKeyEx()를 고려합니다.

        if key == ord("q"):
            print("q 키로 종료")
            break
        if key == 27:
            print("ESC 키로 종료")
            break
        if key == 13:
            print("Enter 키를 눌렀습니다")
            continue
        if key == 32:
            print("Space 키를 눌렀습니다")
            continue
        if key == 8:
            print("Backspace 키를 눌렀습니다")
            continue

        # 일반 문자인 경우 출력 (ASCII 32~126만 가독성 있게 출력)
        ch = chr(key) if 32 <= key < 127 else "?"
        print(f"키 코드: {key}, 문자: {ch}")

    close_all_windows()


def demo_16_comprehensive_practice(args: argparse.Namespace) -> None:
    """
    OpenCV 기초 - 04. 종합 실습

    1) 여러 색상 영역으로 이루어진 이미지 만들기
    2) 채널 조작으로 색상 바꾸기
    3) ROI(관심 영역)를 이용한 이미지 복사
    4) 그라데이션 이미지 만들기
    """
    cv = require_cv2()
    np = require_np()

    # ------------------------------------------------------------
    # 실습 1: 빨강, 초록, 파랑 3색 정사각형 만들기
    # ------------------------------------------------------------
    img = np.zeros((300, 900, 3), dtype=np.uint8)
    img[:, 0:300] = [0, 0, 255]     # Red
    img[:, 300:600] = [0, 255, 0]   # Green
    img[:, 600:900] = [255, 0, 0]   # Blue

    safe_imshow("16-1 RGB Squares", img)
    print("[Demo 16-1] 3색 정사각형 생성 완료! 아무 키로 다음 단계.")
    cv.waitKey(0)
    close_all_windows()

    # ------------------------------------------------------------
    # 실습 2: 채널 조작으로 색상 바꾸기
    # ------------------------------------------------------------
    # 노란색 = Green + Red = BGR(0, 255, 255)
    img_yellow = np.zeros((200, 200, 3), dtype=np.uint8)
    img_yellow[:] = [0, 255, 255]

    # (중요) '원본' 비교를 위해 복사본을 만들어 둡니다.
    img_original = img_yellow.copy()

    # 채널을 "참조 형태"로 분리 (split보다 빠르고 메모리 효율적)
    b = img_yellow[:, :, 0]
    g = img_yellow[:, :, 1]
    r = img_yellow[:, :, 2]

    # Blue와 Green을 0으로 만들면 Red만 남아 빨간색이 됩니다.
    b[:] = 0
    g[:] = 0

    safe_imshow("16-2 Original (Yellow)", img_original)
    safe_imshow("16-2 Modified (Red)", img_yellow)
    print("[Demo 16-2] 채널 조작 완료! 노란색에서 B,G를 제거하면 빨간색이 됩니다. 아무 키로 다음.")
    cv.waitKey(0)
    close_all_windows()

    # ------------------------------------------------------------
    # 실습 3: ROI를 이용한 이미지 합성
    # ------------------------------------------------------------
    img1 = np.zeros((400, 400, 3), dtype=np.uint8)
    img1[:] = [255, 0, 0]  # Blue

    img2 = np.zeros((200, 200, 3), dtype=np.uint8)
    img2[:] = [0, 0, 255]  # Red

    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]

    y = (h1 - h2) // 2
    x = (w1 - w2) // 2

    img1[y : y + h2, x : x + w2] = img2

    safe_imshow("16-3 ROI Copy (Centered)", img1)
    print(f"[Demo 16-3] ROI 복사 완료! 중앙({x}, {y})에 200x200 빨간 사각형 배치. 아무 키로 다음.")
    cv.waitKey(0)
    close_all_windows()

    # ------------------------------------------------------------
    # 실습 4: 그라데이션 이미지 만들기
    # ------------------------------------------------------------
    # 수평 그라데이션: 왼쪽(검정) -> 오른쪽(흰색)
    h_grad = np.tile(np.linspace(0, 255, 300), (300, 1)).astype(np.uint8)

    # 수직 그라데이션: 위(검정) -> 아래(흰색)
    v_grad = np.tile(np.linspace(0, 255, 300), (300, 1)).T.astype(np.uint8)

    # 합성(평균): 오버플로우 방지를 위해 float32로 계산 후 uint8로 변환
    combined = ((h_grad.astype(np.float32) + v_grad.astype(np.float32)) / 2).astype(np.uint8)

    safe_imshow("16-4 Horizontal Gradient", h_grad)
    safe_imshow("16-4 Vertical Gradient", v_grad)
    safe_imshow("16-4 Combined Gradient", combined)
    print("[Demo 16-4] 그라데이션 생성 완료! 아무 키로 종료.")
    cv.waitKey(0)
    close_all_windows()


def demo_17_image_save_formats(args: argparse.Namespace) -> None:
    """
    OpenCV 기초 - 05. 이미지/비디오 저장과 웹캠 활용 (파트 1)
    1) 이미지를 다양한 형식(JPEG, PNG)과 품질로 저장하기
    """
    cv = require_cv2()
    np = require_np()

    out = _output_dir()

    # 480x640 크기의 랜덤 컬러 이미지 생성
    img = np.random.randint(0, 256, (480, 640, 3), dtype=np.uint8)

    print("[Demo 17] 이미지를 다양한 형식/품질로 저장합니다 (output/).")

    # JPEG 품질 50 (낮은 화질, 작은 파일)
    cv.imwrite(str(out / "test_jpg_q50.jpg"), img, [cv.IMWRITE_JPEG_QUALITY, 50])

    # JPEG 품질 95 (높은 화질, 큰 파일)
    cv.imwrite(str(out / "test_jpg_q95.jpg"), img, [cv.IMWRITE_JPEG_QUALITY, 95])

    # PNG (무손실)
    cv.imwrite(str(out / "test.png"), img)

    # 저장된 파일들의 크기 비교
    print("\n저장된 파일 크기 비교:")
    print("-" * 40)
    for fname in ["test_jpg_q50.jpg", "test_jpg_q95.jpg", "test.png"]:
        f = out / fname
        size = f.stat().st_size
        print(f"{fname}: {size/1024:.2f} KB")
    print("-" * 40)
    print("💡 JPEG 품질이 높을수록 파일이 커지고, PNG는 무손실이라 상대적으로 파일이 큽니다.\n")


def demo_18_safe_imread(args: argparse.Namespace) -> None:
    """
    OpenCV 기초 - 05. 이미지/비디오 저장과 웹캠 활용 (파트 2)
    2) 이미지 읽기 실패를 안전하게 처리하는 방법
    """
    cv = require_cv2()
    np = require_np()

    def safe_imread(filepath: str):
        """
        안전하게 이미지를 읽는 함수.

        - cv2.imread()는 실패 시 None을 반환합니다.
        - None 처리를 하지 않으면 이후 img.shape 등에서 예외가 발생합니다.
        - 본 예제에서는 실패 시에도 프로그램이 계속 진행되도록 기본 검은 이미지를 반환합니다.
        """
        img = cv.imread(filepath)
        if img is None:
            print(f"❌ 이미지를 찾을 수 없습니다: {filepath}")
            print("   대신 검은색 기본 이미지를 반환합니다.")
            img = np.zeros((300, 300, 3), dtype=np.uint8)
        else:
            print(f"✅ 이미지 읽기 성공! 크기: {img.shape}")
        return img

    print("[Demo 18] 존재하지 않는 파일 읽기 테스트:")
    img = safe_imread("nonexistent.jpg")

    safe_imshow("18 - safe_imread 결과", img)
    cv.waitKey(0)
    close_all_windows()


def demo_19_webcam_photo_capture(args: argparse.Namespace) -> None:
    """
    OpenCV 기초 - 05. 이미지/비디오 저장과 웹캠 활용 (파트 3)
    3) 웹캠으로 사진 촬영하고 저장하기

    사용법:
    - s: 현재 프레임을 사진으로 저장
    - q 또는 ESC: 종료
    """
    cv = require_cv2()

    out = _output_dir()

    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("❌ 웹캠을 열 수 없습니다. 웹캠 연결 상태를 확인하세요.")
        return

    photo_count = 1
    win = "19 - WebCam Photo"

    print("[Demo 19] 웹캠 촬영 모드 시작")
    print(" - s: 저장, q/ESC: 종료")
    print(f" - 저장 경로: {out.resolve()}")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ 프레임을 읽을 수 없습니다.")
            break

        # 미러 모드(좌우 반전)
        frame = cv.flip(frame, 1)

        # 안내 텍스트
        cv.putText(
            frame,
            "Press 's' to save, 'q'/'ESC' to quit",
            (10, 30),
            cv.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2,
            cv.LINE_AA,
        )

        safe_imshow(win, frame)

        key = cv.waitKey(1) & 0xFF
        if key == ord("s"):
            filename = out / f"Photo_{photo_count:03d}.jpg"
            cv.imwrite(str(filename), frame)
            print(f"📸 사진 저장됨: {filename.name}")
            photo_count += 1
        elif key in (ord("q"), 27):
            print("👋 웹캠 촬영을 종료합니다.")
            break

    cap.release()
    close_all_windows()


def demo_20_video_speed_control(args: argparse.Namespace) -> None:
    """
    OpenCV 기초 - 05. 이미지/비디오 저장과 웹캠 활용 (파트 4)
    4) 비디오 속도 조절하기 (배속, 슬로우모션)

    원리:
    - 2배속 : 프레임을 건너뛰며 저장 (예: 0,2,4,6...)
    - 0.5배속: 동일 프레임을 반복 저장 (각 프레임을 2번씩 기록)
    """
    cv = require_cv2()
    np = require_np()

    out = _output_dir()

    width, height = 640, 480
    fps = 30
    duration = 5
    total_frames = fps * duration

    fourcc = cv.VideoWriter_fourcc(*"mp4v")

    print("[Demo 20] 비디오 생성 중...")
    print(f" - 해상도: {width}x{height}, fps: {fps}, 길이: {duration}s, 프레임: {total_frames}")
    print(f" - 저장 경로: {out.resolve()}")

    # 1) 원본 비디오 생성 + 프레임 저장
    path_original = out / "original.mp4"
    out_original = cv.VideoWriter(str(path_original), fourcc, fps, (width, height))

    frames = []
    for i in range(total_frames):
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        frame[:, :, 0] = int(255 * i / total_frames)

        cv.putText(
            frame,
            f"Frame: {i}",
            (50, 50),
            cv.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2,
            cv.LINE_AA,
        )

        out_original.write(frame)
        frames.append(frame)

    out_original.release()
    print(f"✅ {path_original.name} 생성 완료! (5초, 30fps)")

    # 2) 2배속
    path_2x = out / "speed_2x.mp4"
    out_2x = cv.VideoWriter(str(path_2x), fourcc, fps, (width, height))
    for i in range(0, len(frames), 2):
        out_2x.write(frames[i])
    out_2x.release()
    print(f"✅ {path_2x.name} 생성 완료! (2.5초, 2배속)")

    # 3) 0.5배속(슬로우모션)
    path_half = out / "speed_0.5x.mp4"
    out_half = cv.VideoWriter(str(path_half), fourcc, fps, (width, height))
    for frame in frames:
        out_half.write(frame)
        out_half.write(frame)
    out_half.release()
    print(f"✅ {path_half.name} 생성 완료! (10초, 0.5배속)")

    print("🎉 비디오 생성 완료!")


def main() -> None:
    parser = build_cli_parser("OpenCV Basics (PDF1) - demos")
    args = parser.parse_args()

    demos = [
            Demo("00", "OpenCV 소개 + 이미지(NumPy) 표현 + 더미 이미지 생성(갤러리)", demo_00_overview_and_image_representation),
            Demo("01", "환경/설치/버전 확인", demo_01_env_check),
            Demo("02", "이미지 I/O + 윈도우/키 입력(리사이즈 가능 vs 불가 포함)", demo_02_image_io_window_keyboard),
            Demo("02b", "윈도우 플래그/조작 + 키 이벤트(색상 토글)", demo_02b_window_flags_and_keyboard_color),
            Demo("03", "이미지 I/O(imread 플래그/None 처리) + 저장 옵션(imwrite 품질/압축)", demo_03_image_shape_and_write),
            Demo("04", "비디오 입력(VideoCapture) + 속성(get/set) + 탐색(seek) + 재생 제어", demo_04_video_file_capture),
            Demo("05", "웹캠 연결 + 사진찍기 + 밝기 컨트롤(실습3)", demo_05_webcam_basics),
            Demo("06", "비디오 저장(VideoWriter)", demo_06_video_writer),
            Demo("06b", "웹캠 녹화 토글(REC 표시) + 파일 저장", demo_06b_webcam_record_toggle),
            Demo("07", "픽셀/ROI/빈화면/영역색칠/복사", demo_07_pixel_access_roi),
            Demo("08", "색상/채널 split/merge + grayscale/invert(실습4)", demo_08_color_and_channels),
            Demo("09", "리사이즈/보간법 비교", demo_09_resize_interpolation),
            Demo("09b", "영상 리사이즈(실습5)", demo_09b_exercise_5_resize_video),
            Demo("10", "이미지 피라미드(pyrDown/pyrUp)", demo_10_pyramids),
            Demo("11", "crop/flip + 실습6 조정", demo_11_crop_flip),
            Demo("12", "BONUS: 프레임 스킵(성능 최적화)", demo_12_bonus_frame_skip),
        
        Demo("13", "Centered text (cv2.putText + getTextSize)", demo_13_centered_text),
        Demo("14", "Mouse events (click/drag via setMouseCallback)", demo_14_mouse_events),
        Demo("15", "Keyboard events (cv2.waitKey handling)", demo_15_keyboard_events),
        Demo("16", "Comprehensive practice (colors/ROI/gradients)", demo_16_comprehensive_practice),
        Demo("17", "Save formats & quality (JPEG/PNG)", demo_17_image_save_formats),
        Demo("18", "Safe imread (handle None)", demo_18_safe_imread),
        Demo("19", "Webcam photo capture (save on 's')", demo_19_webcam_photo_capture),
        Demo("20", "Video speed control (2x / 0.5x)", demo_20_video_speed_control),
]

    run_demos(demos, args)


if __name__ == "__main__":
    main()
