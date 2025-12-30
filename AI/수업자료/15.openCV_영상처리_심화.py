# -*- coding: utf-8 -*-
"""
15.openCV_영상처리_심화.py
================================================================================
[대주제] openCV 영상처리 심화 (회전/원근/문서스캐너/엣지/윤곽선/히스토그램/모폴로지)

이 파일은 업로드된 PDF:
- 13_OpenCV(3)_영상처리심화.pdf
의 대주제를 빠짐없이 정리한 뒤,
추가 개념/응용 예제까지 확장한 학습 스크립트입니다.

실행 방식
--------------------------------------------------------------------------------
0) 기본 실행(가장 간단):
    python ./AI/수업자료/15.openCV_영상처리_심화.py

   * 기본 데모(보통 00)가 바로 실행됩니다.
   * 데모 선택 메뉴가 필요하면 --menu 옵션을 사용하세요.

python ./AI/수업자료/15.openCV_영상처리_심화.py --list
python ./AI/수업자료/15.openCV_영상처리_심화.py --demo 02 --image ./Images/doc.jpg
python ./AI/수업자료/15.openCV_영상처리_심화.py --demo 03 --source 0

- 공통 종료 키: 'q' 또는 ESC

작성일: 2025-12-26
"""

from __future__ import annotations

import os
from typing import Any, List, Tuple

from openCV_공용 import (
    require_cv2, require_np,
    auto_find_image, auto_find_video,
    make_blank, make_gradient,
    bgr_to_gray,
    safe_imshow, safe_named_window, close_all_windows, close_window,
    build_cli_parser, run_demos, Demo,
    parse_source_to_capture_arg, is_exit_key
)

cv2 = require_cv2()
np = require_np()


# =============================================================================
# [PDF 체크리스트] 13_OpenCV(3)_영상처리심화.pdf 대주제 → 코드 매핑
# PDF 체크리스트(슬라이드 대주제 → 코드 위치)
# --------------------------------------------------------------------
# 번호 | 슬라이드(p) | 대주제 | 코드 섹션/데모
# --------------------------------------------------------------------
# 01 | p02-02 | 영상 처리 심화 | demo 00 (overview)
# 02 | p03-03 | 이미지 회전 | demo 01 (rotation/affine)
# 03 | p04-05 | 이미지 회전 - rotate | demo 01 (rotation/affine)
# 04 | p06-09 | 이미지 회전 – 아핀 변환 | demo 01 (rotation/affine)
# 05 | p10-10 | 원근 변환 | demo 02 (perspective/docscan)
# 06 | p11-14 | 원근변환 | demo 02 (perspective/docscan)
# 07 | p15-15 | 실습1. 이미지 원근 변환하기 | demo 02 (perspective/docscan)
# 08 | p16-20 | 마우스 이벤트 | demo 02 (perspective/docscan)
# 09 | p21-22 | 실습2. 반자동 문서 스캐너 만들기 | demo 02 (perspective/docscan)
# 10 | p23-29 | 경계선 검출 | demo 03 (edges/camera)
# 11 | p30-30 | 실습3. 캠 화면에 검출 | demo 03 (edges/camera)
# 12 | p31-38 | 윤곽선 검출 | demo 04 (contours/bbox/crop)
# 13 | p39-41 | 윤곽선 경계 사각형 | demo 04 (contours/bbox/crop)
# 14 | p42-42 | 실습4. 순서대로 박스 표시 | demo 04 (contours/bbox/crop)
# 15 | p43-43 | 실습5. 카드 하나씩 새 창에 표시 | (covered)
# 16 | p44-47 | 히스토그램 | demo 05 (histogram/equalize)
# 17 | p48-48 | 실습6. | (covered)
# 18 | p49-49 | 팽창과 침식 | demo 06 (morphology)
# 19 | p50-51 | 팽창 | demo 06 (morphology)
# 20 | p52-53 | 침식 | demo 06 (morphology)
# 21 | p54-54 | 열림 | demo 06 (morphology)
# 22 | p55-55 | 닫힘 | demo 06 (morphology)
# 23 | p56-56 | 감사합니다 | -
# --------------------------------------------------------------------
# =============================================================================
# 0. 입력 로드
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

    # 더미: 문서 스캐너/원근변환이 잘 보이도록 "사각형 문서"를 합성
    img = make_gradient(800, 520, direction="vertical", start_bgr=(40, 40, 40), end_bgr=(70, 70, 70))
    # 사다리꼴 문서(원근)
    pts = np.array([[180, 120], [620, 90], [690, 420], [140, 460]], dtype=np.int32)
    cv2.fillPoly(img, [pts], (230, 230, 230))
    cv2.polylines(img, [pts], True, (0, 0, 0), 3, cv2.LINE_AA)
    cv2.putText(img, "DOC", (330, 290), cv2.FONT_HERSHEY_SIMPLEX, 3.0, (40, 40, 40), 6, cv2.LINE_AA)
    return img


def _open_capture(source: str) -> Any:
    if not source:
        auto = auto_find_video(".")
        source = auto if auto else "0"
    cap = cv2.VideoCapture(parse_source_to_capture_arg(source))
    if not cap.isOpened():
        raise RuntimeError(f"VideoCapture 오픈 실패: source={source}")
    return cap


# =============================================================================
# demo 00. 개요
def demo_00_overview(args) -> None:
    """
    [개념] 영상처리 심화는 "기본 처리(블러/이진화)"를 기반으로 다음을 수행합니다.
    - 기하 변환: 회전(rotate/warpAffine), 원근(perspective)
    - 엣지/경계선: Canny, Sobel 등으로 경계 강조
    - 윤곽선(contour): 객체 외곽선을 추출해 위치/크기/개수/바운딩박스 계산
    - 히스토그램: 밝기/대비 특성 파악, equalize/CLAHE로 대비 개선
    - 모폴로지: 팽창/침식/열림/닫힘으로 형태 기반 노이즈 제거/복원
    """
    img = _load_or_make_image(args.image)
    safe_imshow("demo00_overview (q/ESC)", img, resizable=True, wait=1)
    while True:
        if is_exit_key(cv2.waitKey(20) & 0xFF):
            break
    close_all_windows()


# =============================================================================
# demo 01. 이미지 회전(rotate / warpAffine / affine)
def demo_01_rotation_affine(args) -> None:
    """
    [개념] rotate vs warpAffine
    - cv2.rotate: 90/180/270도 회전(정해진 각도) - 간단/빠름
    - warpAffine: 임의 각도 회전(회전행렬 + 보간)
      * center/scale 지정 가능
      * 회전 후 이미지가 잘리는 문제 해결을 위해 캔버스 확장 로직이 필요할 수 있음

    [개념] 아핀 변환(Affine)
    - 직선은 직선으로 유지
    - 평행성 유지(원근과 다름)
    - 2x3 행렬로 표현 (cv2.warpAffine)

    [예제]
    - rotate 90/180/270
    - 임의 각도(예: 25도) 회전
    - 3점 매핑으로 아핀 변환
    """
    img = _load_or_make_image(args.image)
    h, w = img.shape[:2]

    r90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    r180 = cv2.rotate(img, cv2.ROTATE_180)
    r270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # 임의 각도 회전(warpAffine)
    angle = 25.0
    center = (w / 2.0, h / 2.0)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)

    # 아핀: 3점 매핑
    src_pts = np.float32([[0, 0], [w - 1, 0], [0, h - 1]])
    dst_pts = np.float32([[0, 0], [int(0.85 * (w - 1)), int(0.15 * h)], [int(0.15 * w), h - 1]])
    A = cv2.getAffineTransform(src_pts, dst_pts)
    affine = cv2.warpAffine(img, A, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)

    safe_imshow("demo01_original (q/ESC)", img, True, 1)
    safe_imshow("demo01_rotate_90 (q/ESC)", r90, True, 1)
    safe_imshow("demo01_rotate_180 (q/ESC)", r180, True, 1)
    safe_imshow("demo01_rotate_270 (q/ESC)", r270, True, 1)
    safe_imshow("demo01_warpAffine_rotate_25deg (q/ESC)", rotated, True, 1)
    safe_imshow("demo01_affine_transform (q/ESC)", affine, True, 1)

    while True:
        if is_exit_key(cv2.waitKey(20) & 0xFF):
            break
    close_all_windows()


# =============================================================================
# demo 02. 원근 변환 + 마우스 이벤트 + (응용) 문서 스캐너
def demo_02_perspective_docscan_mouse(args) -> None:
    """
    [개념] 원근 변환(Perspective transform)
    - cv2.getPerspectiveTransform(src4, dst4) -> 3x3 행렬
    - cv2.warpPerspective(img, H, dsize)

    [마우스 이벤트]
    - cv2.setMouseCallback(window, callback)
      callback(event, x, y, flags, param)

    [문서 스캐너(응용)]
    - 문서 4 꼭짓점을 클릭 → 투시 변환으로 "반듯한 문서"로 펼침
    - 실무에서는:
      * 자동으로 윤곽선 찾기 + 4점 추정
      * 정렬(시계방향), 크롭
      등을 추가합니다.
    """
    img = _load_or_make_image(args.image).copy()
    disp = img.copy()

    win = "demo02_docscan_click4 (TL,TR,BR,BL) | w=warp, r=reset, q=quit"
    safe_named_window(win, resizable=True)

    points: List[Tuple[int, int]] = []

    def draw_points() -> None:
        nonlocal disp
        disp = img.copy()
        for i, (x, y) in enumerate(points):
            cv2.circle(disp, (x, y), 6, (0, 0, 255), -1)
            cv2.putText(disp, str(i + 1), (x + 8, y - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        if len(points) == 4:
            cv2.polylines(disp, [np.array(points, dtype=np.int32)], True, (255, 0, 0), 2, cv2.LINE_AA)

    def on_mouse(event, x, y, flags, param) -> None:
        nonlocal points
        if event == cv2.EVENT_LBUTTONDOWN:
            if len(points) < 4:
                points.append((x, y))
                draw_points()

    cv2.setMouseCallback(win, on_mouse)
    draw_points()

    warped = None
    while True:
        cv2.imshow(win, disp)
        key = cv2.waitKey(20) & 0xFF

        if key == ord("r"):
            points = []
            draw_points()
            warped = None
        elif key == ord("w") and len(points) == 4:
            # 클릭 순서: TL, TR, BR, BL 권장
            src = np.float32(points)

            # 출력 크기 추정(간단 버전): 가로/세로를 두 변의 평균 길이로 잡기
            def dist(a, b):
                return float(((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5)

            w1 = dist(points[0], points[1])
            w2 = dist(points[3], points[2])
            h1 = dist(points[0], points[3])
            h2 = dist(points[1], points[2])
            out_w = int(max(w1, w2))
            out_h = int(max(h1, h2))
            out_w = max(out_w, 200)
            out_h = max(out_h, 200)

            dst = np.float32([[0, 0], [out_w - 1, 0], [out_w - 1, out_h - 1], [0, out_h - 1]])
            H = cv2.getPerspectiveTransform(src, dst)
            warped = cv2.warpPerspective(img, H, (out_w, out_h))
            safe_imshow("demo02_warped_document (q/ESC)", warped, resizable=True, wait=1)

        elif is_exit_key(key):
            break

    close_all_windows()


# =============================================================================
# demo 03. 경계선(엣지) 검출: Sobel/Laplacian/Canny + (실습) 캠 화면
def demo_03_edges_canny_camera(args) -> None:
    """
    [개념] 엣지(Edge)란?
    - 픽셀 밝기 변화(기울기)가 큰 지점 = 경계선 후보
    - 경계선은 객체 검출/윤곽선 추출의 전처리로 자주 사용

    [대표 기법]
    - Sobel: 1차 미분 기반(가로/세로 기울기)
    - Laplacian: 2차 미분 기반
    - Canny: (블러→기울기→비최대 억제→이중 임계값) 파이프라인으로 비교적 강력/안정적

    [예제]
    - 이미지(또는 웹캠) 입력 → Canny 결과를 실시간 표시
    """
    use_camera = bool(args.source)  # source 지정하면 비디오, 아니면 이미지
    if use_camera:
        cap = _open_capture(args.source)
        print("[KEY] q/ESC=quit")
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            gray = bgr_to_gray(frame)
            blur = cv2.GaussianBlur(gray, (5, 5), 1.2)
            edges = cv2.Canny(blur, 70, 140)

            # 시각화(좌:원본, 우:엣지)
            vis = np.hstack([frame, cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)])
            cv2.imshow("demo03_edges_camera (q/ESC)", vis)
            if is_exit_key(cv2.waitKey(1) & 0xFF):
                break
        cap.release()
        close_all_windows()
    else:
        img = _load_or_make_image(args.image)
        gray = bgr_to_gray(img)
        blur = cv2.GaussianBlur(gray, (5, 5), 1.2)

        sobelx = cv2.Sobel(blur, cv2.CV_32F, 1, 0, ksize=3)
        sobely = cv2.Sobel(blur, cv2.CV_32F, 0, 1, ksize=3)
        mag = cv2.magnitude(sobelx, sobely)
        mag_u8 = cv2.convertScaleAbs(mag)

        lap = cv2.Laplacian(blur, cv2.CV_32F, ksize=3)
        lap_u8 = cv2.convertScaleAbs(lap)

        edges = cv2.Canny(blur, 70, 140)

        safe_imshow("demo03_original (q/ESC)", img, True, 1)
        safe_imshow("demo03_sobel_magnitude (q/ESC)", mag_u8, True, 1)
        safe_imshow("demo03_laplacian (q/ESC)", lap_u8, True, 1)
        safe_imshow("demo03_canny (q/ESC)", edges, True, 1)

        while True:
            if is_exit_key(cv2.waitKey(20) & 0xFF):
                break
        close_all_windows()


# =============================================================================
# demo 04. 윤곽선(contour) + 바운딩 박스 + (실습) 카드/객체 추출
def demo_04_contours_bounding_sort_crop(args) -> None:
    """
    [개념] 윤곽선(contour)
    - 이진화된 이미지(전경/배경)에서 "전경의 경계"를 추적한 점들의 집합
    - cv2.findContours(binary, mode, method)

    [바운딩 박스]
    - x,y,w,h = cv2.boundingRect(contour)
    - rect = cv2.minAreaRect(contour) (회전 박스)
    - 면적: cv2.contourArea(contour)

    [실습(카드 추출) 아이디어]
    - 전경을 이진화 → 큰 윤곽선 N개 선택 → boundingRect로 crop
    - 더 정확한 "카드 펼치기"는 원근변환(4점)까지 결합(문서 스캐너와 유사)
    """
    img = _load_or_make_image(args.image).copy()
    gray = bgr_to_gray(img)
    blur = cv2.GaussianBlur(gray, (5, 5), 1.2)

    # 간단한 이진화(오츠)
    _ret, binimg = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 윤곽선 찾기
    contours, hierarchy = cv2.findContours(binimg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 큰 윤곽선 몇 개만 선택
    contours_sorted = sorted(contours, key=cv2.contourArea, reverse=True)
    top = contours_sorted[:8]

    vis = img.copy()
    crops: List[Any] = []
    for i, cnt in enumerate(top):
        area = cv2.contourArea(cnt)
        if area < 300:  # 너무 작은 잡음 제외
            continue
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(vis, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(vis, f"{i} area={int(area)}", (x, max(10, y - 5)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

        crop = img[y:y + h, x:x + w].copy()
        crops.append(crop)

    safe_imshow("demo04_contours_bboxes (q/ESC)", vis, True, 1)
    safe_imshow("demo04_binary (q/ESC)", binimg, True, 1)

    # crop 결과는 여러 장일 수 있으므로, 순차로 표시
    for j, c in enumerate(crops[:6]):
        safe_imshow(f"demo04_crop_{j} (q/ESC)", c, True, 1)

    while True:
        if is_exit_key(cv2.waitKey(20) & 0xFF):
            break
    close_all_windows()


# =============================================================================
# demo 04b. (실습5) 카드 영상 저장: 비디오에서 컨투어/박스 오버레이 후 VideoWriter로 저장
def demo_04b_card_video_save(args) -> None:
    """
    [실습5 대응] 카드 영상 저장
    - 입력: 비디오 파일 또는 웹캠(args.source)
    - 처리: 프레임마다 간단 이진화/윤곽선 → 바운딩 박스 오버레이
    - 출력: args.save(기본 demo04b_card_overlay.mp4) 로 저장(VideoWriter)

    실무 팁
    - 저장 코덱/해상도/FPS가 맞지 않으면 파일이 재생되지 않거나 깨질 수 있습니다.
    - 입력 해상도를 그대로 쓰는 것이 안전합니다.
    """
    cap = _open_capture(args.source or "0")

    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) or 640)
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) or 480)

    out_path = args.save or "demo04b_card_overlay.mp4"
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(out_path, fourcc, float(fps), (w, h))

    if not writer.isOpened():
        cap.release()
        raise RuntimeError("VideoWriter 오픈 실패: 코덱/경로/권한 확인")

    print(f"[WRITE] {out_path} (fps={fps}, size={w}x{h})  | q/ESC=quit")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = bgr_to_gray(frame)
        blur = cv2.GaussianBlur(gray, (5, 5), 1.2)
        _ret, binimg = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        contours, _hier = cv2.findContours(binimg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        vis = frame.copy()
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area < 800:
                continue
            x, y, bw, bh = cv2.boundingRect(cnt)
            cv2.rectangle(vis, (x, y), (x + bw, y + bh), (0, 0, 255), 2)

        writer.write(vis)
        cv2.imshow("demo04b_card_video_save (q/ESC)", vis)

        if is_exit_key(cv2.waitKey(1) & 0xFF):
            break

    writer.release()
    cap.release()
    close_all_windows()
    print("[DONE]")


# =============================================================================
# demo 05. 히스토그램 + 대비 개선(equalizeHist / CLAHE)
def demo_05_histogram_equalize(args) -> None:
    """
    [개념] 히스토그램(Histogram)
    - 각 밝기값(0~255)이 몇 번 등장하는지 카운트한 분포
    - 어두운/밝은/대비가 낮은 이미지 판별에 유용

    [대비 개선]
    - global equalization: cv2.equalizeHist(gray)
    - CLAHE(국소 대비 개선): cv2.createCLAHE(...).apply(gray)

    [예제]
    - 원본 gray, equalized, clahe 비교
    - matplotlib이 있으면 히스토그램을 그래프로 출력(없으면 수치 요약)
    """
    img = _load_or_make_image(args.image)
    gray = bgr_to_gray(img)

    eq = cv2.equalizeHist(gray)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)).apply(gray)

    safe_imshow("demo05_gray (q/ESC)", gray, True, 1)
    safe_imshow("demo05_equalizeHist (q/ESC)", eq, True, 1)
    safe_imshow("demo05_CLAHE (q/ESC)", clahe, True, 1)

    # 히스토그램 계산
    hist_gray = cv2.calcHist([gray], [0], None, [256], [0, 256])
    hist_eq = cv2.calcHist([eq], [0], None, [256], [0, 256])
    hist_clahe = cv2.calcHist([clahe], [0], None, [256], [0, 256])

    try:
        import matplotlib.pyplot as plt  # type: ignore
        # 색 지정은 하지 말라는 규칙은 "차트 색상 지정 금지" 도구 룰이지만,
        # 이 코드는 사용자 로컬 실행용이며, 기본 색상(자동)을 사용합니다.
        plt.figure()
        plt.title("Histogram: gray vs equalize vs clahe")
        plt.plot(hist_gray, label="gray")
        plt.plot(hist_eq, label="equalize")
        plt.plot(hist_clahe, label="clahe")
        plt.legend()
        plt.show()
    except Exception as e:
        print("[WARN] matplotlib not available:", e)
        # 수치 요약(평균/표준편차)
        for name, arr in [("gray", gray), ("equalize", eq), ("clahe", clahe)]:
            print(name, "mean=", float(np.mean(arr)), "std=", float(np.std(arr)))

    while True:
        if is_exit_key(cv2.waitKey(20) & 0xFF):
            break
    close_all_windows()


# =============================================================================
# demo 06. 모폴로지(팽창/침식/열림/닫힘)
def demo_06_morphology(args) -> None:
    """
    [개념] 팽창(Dilation) / 침식(Erosion)
    - 팽창: 흰색(전경)을 확장 → 구멍 메우기/끊어진 부분 연결
    - 침식: 흰색(전경)을 축소 → 작은 잡음 제거

    [열림/닫힘]
    - 열림(open): 침식 → 팽창 (작은 흰색 잡음 제거)
    - 닫힘(close): 팽창 → 침식 (작은 검은 구멍 메우기)

    [예제]
    - 오츠 이진화 후 다양한 morphology 비교
    """
    img = _load_or_make_image(args.image)
    gray = bgr_to_gray(img)
    _ret, binimg = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    dil = cv2.dilate(binimg, kernel, iterations=1)
    ero = cv2.erode(binimg, kernel, iterations=1)
    open_ = cv2.morphologyEx(binimg, cv2.MORPH_OPEN, kernel, iterations=1)
    close_ = cv2.morphologyEx(binimg, cv2.MORPH_CLOSE, kernel, iterations=1)

    def bgr(x):
        return cv2.cvtColor(x, cv2.COLOR_GRAY2BGR)

    vis = np.vstack([
        np.hstack([bgr(binimg), bgr(dil)]),
        np.hstack([bgr(ero), bgr(open_)]),
        np.hstack([bgr(close_), cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)]),
    ])

    safe_imshow("demo06_morphology (q/ESC)", vis, True, 1)
    while True:
        if is_exit_key(cv2.waitKey(20) & 0xFF):
            break
    close_all_windows()


# =============================================================================
# [추가 개념/응용] (PDF 외 확장)
def demo_07_bonus_hough_lines(args) -> None:
    """
    [BONUS] 허프 변환(Hough Transform)으로 직선 검출
    - 엣지(Canny) 결과에서 직선을 검출할 수 있습니다.
    - 실무 예: 차선 인식, 문서의 직선 경계 추정 등
    """
    img = _load_or_make_image(args.image)
    gray = bgr_to_gray(img)
    edges = cv2.Canny(cv2.GaussianBlur(gray, (5, 5), 1.2), 70, 140)

    lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi / 180.0, threshold=80,
                            minLineLength=60, maxLineGap=10)

    vis = img.copy()
    if lines is not None:
        for (x1, y1, x2, y2) in lines[:, 0]:
            cv2.line(vis, (x1, y1), (x2, y2), (0, 0, 255), 2, cv2.LINE_AA)

    safe_imshow("demo07_hough_lines (q/ESC)", vis, True, 1)
    safe_imshow("demo07_edges (q/ESC)", edges, True, 1)
    while True:
        if is_exit_key(cv2.waitKey(20) & 0xFF):
            break
    close_all_windows()


def main() -> None:
    parser = build_cli_parser("Image Processing Advanced (PDF3) - demos")
    args = parser.parse_args()

    demos = [
        Demo("00", "개요(영상처리 심화)", demo_00_overview),
        Demo("01", "이미지 회전(rotate/warpAffine) + 아핀 변환", demo_01_rotation_affine),
        Demo("02", "원근 변환 + 마우스 이벤트 + 문서 스캐너", demo_02_perspective_docscan_mouse),
        Demo("03", "경계선 검출(Sobel/Laplacian/Canny) + 캠 화면", demo_03_edges_canny_camera),
        Demo("04", "윤곽선(contour) + 바운딩 박스 + 객체 추출(카드 실습)", demo_04_contours_bounding_sort_crop),
        Demo("04b", "실습5: 카드 영상 저장(오버레이 비디오 저장)", demo_04b_card_video_save),
        Demo("05", "히스토그램 + equalize/CLAHE", demo_05_histogram_equalize),
        Demo("06", "모폴로지(팽창/침식/열림/닫힘)", demo_06_morphology),
        Demo("07", "BONUS: 허프 변환 직선 검출(HoughLinesP)", demo_07_bonus_hough_lines),
    ]

    run_demos(demos, args)


if __name__ == "__main__":
    main()
