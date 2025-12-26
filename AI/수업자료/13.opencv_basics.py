# -*- coding: utf-8 -*-
"""
13.opencv_basics.py
================================================================================
[대주제] OpenCV 기초 (이미지/비디오 I/O, 윈도우/키 입력, 픽셀/ROI, 색상/채널,
        리사이즈/보간/피라미드/자르기/대칭)

이 파일은 업로드된 PDF:
- 11_OpenCV(1)_OpenCV기초.pdf
의 "개념 + 실습 예제"를 빠짐없이(대주제 단위) 정리한 뒤,
추가 개념/응용 예제까지 확장한 학습 스크립트입니다.

실행 방식
--------------------------------------------------------------------------------
1) 데모 목록 보기:
    python 13.opencv_basics.py --list

2) 데모 실행:
    python ./AI/수업자료/13.opencv_basics.py --demo 02 --image ./Images/sample.jpg
    python ./AI/수업자료/13.opencv_basics.py --demo 04 --source ./Videos/sample.mp4
    python ./AI/수업자료/13.opencv_basics.py --demo 05 --source 0

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

from opencv_common import (
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
# =============================================================================
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
# =============================================================================
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
# =============================================================================
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
# =============================================================================
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
# =============================================================================
def demo_03_image_shape_and_write(args) -> None:
    """
    [개념] 이미지 Shape
    - img.shape: (H, W, C)  (컬러) / (H, W) (그레이)
    - img.dtype: 보통 uint8 (0~255)
    - img.size / img.nbytes: 메모리 사용량 추정

    [예제]
    - 선택한 이미지를 읽고 속성 출력
    - 저장(imwrite) 테스트

    [실습1 대응]
    - "원하는 이미지 띄우기"
      * args.image 지정 또는 자동 탐색
    """
    img = _load_or_make_image(args.image)
    print("=== Image Properties ===")
    print("shape:", img.shape)
    print("dtype:", img.dtype)
    print("size (elements):", img.size)
    print("nbytes:", img.nbytes)

    safe_imshow("demo03 (press q/ESC)", img, resizable=True, wait=1)

    out = args.save or "demo03_saved.jpg"
    ok = cv2.imwrite(out, img)
    print(f"[WRITE] {out} -> {ok}")

    _show_until_exit("demo03 (press q/ESC)")
    close_all_windows()


# =============================================================================
# demo 04. (영상 입력/출력/쓰기, VideoCapture 초기화/설정/get, 프레임, 실습2)
# =============================================================================
def demo_04_video_file_capture(args) -> None:
    """
    [개념] VideoCapture 주요 포인트
    - cap = cv2.VideoCapture(filename or camera_index)
    - cap.isOpened(): 열렸는지 확인
    - cap.read(): (ret, frame)  ret=False면 종료/실패
    - cap.get(propId) / cap.set(propId, value)
      * CAP_PROP_FRAME_WIDTH/HEIGHT/FPS/FRAME_COUNT/POS_FRAMES 등

    [실습2 대응] "영상 프레임 조절"
    - 프레임을 빨리/느리게: waitKey 딜레이(ms)를 조정
      * 딜레이가 작을수록 빠르게 재생(그러나 CPU 사용률 증가 가능)
    """
    cap = _open_capture(args.source)

    # 영상 속성 얻기(get)
    fps = cap.get(cv2.CAP_PROP_FPS)
    w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    print("=== Video Properties ===")
    print(f"CAP_PROP_FPS: {fps}")
    print(f"CAP_PROP_FRAME_WIDTH: {w}")
    print(f"CAP_PROP_FRAME_HEIGHT: {h}")
    print(f"CAP_PROP_FRAME_COUNT: {count}")

    delay = 30  # ms
    print("[KEY] +/- : speed, SPACE: pause, q/ESC: quit")
    paused = False

    while True:
        if not paused:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow("demo04_video (press q/ESC)", frame)

        key = cv2.waitKey(delay) & 0xFF

        if key in (ord("+"), ord("=")):
            delay = max(1, delay - 5)   # 빠르게(딜레이 감소)
            print(f"[SPEED] delay={delay}ms")
        elif key in (ord("-"), ord("_")):
            delay = min(200, delay + 5) # 느리게(딜레이 증가)
            print(f"[SPEED] delay={delay}ms")
        elif key == ord(" "):
            paused = not paused
            print(f"[PAUSE] {paused}")
        elif is_exit_key(key):
            break

    cap.release()
    close_all_windows()


# =============================================================================
# demo 05. (웹캠 연결/사진찍기/카메라 컨트롤: 실습3)
# =============================================================================
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
# =============================================================================
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
# =============================================================================
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
# =============================================================================
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
# =============================================================================
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
# =============================================================================
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
# =============================================================================
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
# =============================================================================
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


def main() -> None:
    parser = build_cli_parser("OpenCV Basics (PDF1) - demos")
    args = parser.parse_args()

    demos = [
        Demo("01", "환경/설치/버전 확인", demo_01_env_check),
        Demo("02", "이미지 I/O + 윈도우/키 입력(리사이즈 가능 vs 불가 포함)", demo_02_image_io_window_keyboard),
        Demo("03", "이미지 속성(shape/dtype) + 저장 + 실습1", demo_03_image_shape_and_write),
        Demo("04", "비디오 입력(VideoCapture) + 속성(get/set) + 재생속도(실습2)", demo_04_video_file_capture),
        Demo("05", "웹캠 연결 + 사진찍기 + 밝기 컨트롤(실습3)", demo_05_webcam_basics),
        Demo("06", "비디오 저장(VideoWriter)", demo_06_video_writer),
        Demo("07", "픽셀/ROI/빈화면/영역색칠/복사", demo_07_pixel_access_roi),
        Demo("08", "색상/채널 split/merge + grayscale/invert(실습4)", demo_08_color_and_channels),
        Demo("09", "리사이즈/보간법 비교", demo_09_resize_interpolation),
        Demo("09b", "영상 리사이즈(실습5)", demo_09b_exercise_5_resize_video),
        Demo("10", "이미지 피라미드(pyrDown/pyrUp)", demo_10_pyramids),
        Demo("11", "crop/flip + 실습6 조정", demo_11_crop_flip),
        Demo("12", "BONUS: 프레임 스킵(성능 최적화)", demo_12_bonus_frame_skip),
    ]

    run_demos(demos, args)


if __name__ == "__main__":
    main()
