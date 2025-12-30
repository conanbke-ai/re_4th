# -*- coding: utf-8 -*-
"""
16.openCV_객체탐지_OCR.py
================================================================================
[대주제] openCV 객체 탐지 & 문자인식 (Face/Haar, YOLO(DNN), Tesseract OCR)

이 파일은 업로드된 PDF:
- 14_OpenCV(4)_객체탐지및문자인식.pdf
의 대주제를 빠짐없이 정리한 뒤,
추가 개념/응용 예제까지 확장한 학습 스크립트입니다.

실행 방식
--------------------------------------------------------------------------------
0) 기본 실행(가장 간단):
    python ./AI/수업자료/16.openCV_객체탐지_OCR.py

   * 기본 데모(보통 00)가 바로 실행됩니다.
   * 데모 선택 메뉴가 필요하면 --menu 옵션을 사용하세요.

python ./AI/수업자료/16.openCV_객체탐지_OCR.py --list

# 얼굴 인식(이미지)
python ./AI/수업자료/16.openCV_객체탐지_OCR.py --demo 01 --image ./Images/face.jpg

# 얼굴 인식(웹캠)
python ./AI/수업자료/16.openCV_객체탐지_OCR.py --demo 02 --source 0

# YOLO (cfg/weights/names 필요)
python ./AI/수업자료/16.openCV_객체탐지_OCR.py --demo 03 --image ./Images/street.jpg \
    --yolo_cfg ./yolo/yolov3.cfg --yolo_weights ./yolo/yolov3.weights --yolo_names ./yolo/coco.names

# OCR (Tesseract 설치 필요)
python ./AI/수업자료/16.openCV_객체탐지_OCR.py --demo 04 --image ./Images/text.png --lang kor+eng

- 공통 종료 키: 'q' 또는 ESC

작성일: 2025-12-26
"""

from __future__ import annotations

import os
from typing import Any, List, Tuple

from openCV_공용 import (
    require_cv2, require_np,
    auto_find_image,
    make_blank, make_gradient,
    bgr_to_gray,
    safe_imshow, safe_named_window, close_all_windows,
    build_cli_parser, run_demos, Demo,
    parse_source_to_capture_arg, is_exit_key
)

cv2 = require_cv2()
np = require_np()


# =============================================================================
# [PDF 체크리스트] 14_OpenCV(4)_객체탐지및문자인식.pdf 대주제 → 코드 매핑
# PDF 체크리스트(슬라이드 대주제 → 코드 위치)
# --------------------------------------------------------------------
# 번호 | 슬라이드(p) | 대주제 | 코드 섹션/데모
# --------------------------------------------------------------------
# 01 | p01-01 | 표지/개요 | demo 00 (overview)
# 02 | p02-17 | 얼굴 인식(Haar Cascade) | demo 01-02 (face detection image/webcam)
# 03 | p18-24 | 객체 탐지(YOLO / OpenCV DNN) | demo 03 (yolo detection)
# 04 | p25-35 | 문자인식(OCR: Tesseract/pytesseract) | demo 04-05 (ocr basics + preprocess)
# 05 | p36-36 | 감사합니다 | -
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

    # 더미: OCR/전처리 데모를 위해 텍스트가 있는 이미지를 합성(영문)
    img = make_blank(800, 420, color_bgr=(255, 255, 255))
    cv2.putText(img, "OpenCV OCR 1234", (40, 170), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 0, 0), 5, cv2.LINE_AA)
    cv2.putText(img, "KOR needs PIL font", (40, 250), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 3, cv2.LINE_AA)
    return img


def _open_capture(source: str) -> Any:
    cap = cv2.VideoCapture(parse_source_to_capture_arg(source))
    if not cap.isOpened():
        raise RuntimeError(f"VideoCapture 오픈 실패: source={source}")
    return cap


# =============================================================================
# demo 00. 개요
def demo_00_overview(args) -> None:
    """
    [개념] 객체 탐지(Object Detection) vs 문자인식(OCR)
    - 객체 탐지: 이미지/프레임에서 "어떤 객체가 어디에 있는지" (클래스 + 박스)
      예: 사람/자동차/고양이 등의 bounding box
    - 얼굴 인식/검출: 객체 탐지의 한 유형(얼굴 박스)
      * Haar Cascade: 고전적 방법(빠르지만 조명/각도에 민감)
      * DNN 기반: 정확하지만 모델 파일 필요
    - OCR: 이미지 속 글자를 문자열로 변환
      * Tesseract: 범용 OCR 엔진, pytesseract로 파이썬 연동

    실무에서의 공통 패턴
    - 입력 → (전처리) → 모델/알고리즘 → 후처리(박스/텍스트 정리) → 저장/표시
    """
    img = _load_or_make_image(args.image)
    safe_imshow("demo00_overview (q/ESC)", img, True, 1)
    while True:
        if is_exit_key(cv2.waitKey(20) & 0xFF):
            break
    close_all_windows()


# =============================================================================
# demo 01. 얼굴 인식(이미지) - Haar Cascade
def demo_01_face_detection_image(args) -> None:
    """
    [개념] Haar Cascade 얼굴 검출
    - cv2.CascadeClassifier(xml_path)
    - detectMultiScale(gray, scaleFactor, minNeighbors, minSize, flags)

    주요 파라미터
    - scaleFactor: 이미지 피라미드 축소 비율(1.05~1.3 사이가 흔함)
    - minNeighbors: 후보 박스를 얼마나 엄격히 통과시킬지(값이 클수록 엄격)
    - minSize: 검출 최소 크기

    주의
    - 정면 얼굴에 강함(측면/가림/역광에 약함)
    """
    img = _load_or_make_image(args.image)
    gray = bgr_to_gray(img)

    face_xml = os.path.join(cv2.data.haarcascades, "haarcascade_frontalface_default.xml")
    face_cascade = cv2.CascadeClassifier(face_xml)
    if face_cascade.empty():
        raise RuntimeError(f"cascade 로드 실패: {face_xml}")

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.12, minNeighbors=5, minSize=(40, 40))
    vis = img.copy()

    for (x, y, w, h) in faces:
        cv2.rectangle(vis, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.putText(vis, f"faces={len(faces)}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), 2, cv2.LINE_AA)
    safe_imshow("demo01_face_detection_image (q/ESC)", vis, True, 1)

    while True:
        if is_exit_key(cv2.waitKey(20) & 0xFF):
            break
    close_all_windows()


# =============================================================================
# demo 02. 얼굴 인식(웹캠) + 트랙바(파라미터 튜닝) + 눈 검출(응용)
def demo_02_face_detection_webcam(args) -> None:
    """
    [개념] 실시간 얼굴 검출
    - 웹캠 프레임마다 detectMultiScale 수행
    - 성능을 위해:
      * 프레임 다운스케일(예: 0.5배)
      * grayscale 처리
      * ROI 기반 추적(이전 프레임 얼굴 주변만 검색)
      등을 적용할 수 있습니다.

    [응용] 눈 검출(eye cascade)
    - 얼굴 영역(ROI) 안에서만 eye detector를 돌리면 오탐이 줄어듭니다.
    """
    cap = _open_capture(args.source or "0")

    face_xml = os.path.join(cv2.data.haarcascades, "haarcascade_frontalface_default.xml")
    eye_xml = os.path.join(cv2.data.haarcascades, "haarcascade_eye.xml")
    face_cascade = cv2.CascadeClassifier(face_xml)
    eye_cascade = cv2.CascadeClassifier(eye_xml)

    if face_cascade.empty():
        cap.release()
        raise RuntimeError(f"face cascade 로드 실패: {face_xml}")

    win = "demo02_face_webcam | q=quit"
    safe_named_window(win, resizable=True)

    # 트랙바: scaleFactor(105~130 => 1.05~1.30), minNeighbors(1~15)
    def _noop(_v: int) -> None:
        pass

    cv2.createTrackbar("scale(x100)", win, 112, 130, _noop)
    cv2.createTrackbar("minNeighbors", win, 5, 15, _noop)

    print("[KEY] q/ESC=quit  | trackbar: scaleFactor/minNeighbors")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        scale100 = cv2.getTrackbarPos("scale(x100)", win)
        minN = cv2.getTrackbarPos("minNeighbors", win)

        scaleFactor = max(1.01, float(scale100) / 100.0)
        minNeighbors = max(1, int(minN))

        # downscale for speed (optional)
        small = cv2.resize(frame, None, fx=0.75, fy=0.75, interpolation=cv2.INTER_AREA)
        gray = bgr_to_gray(small)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=minNeighbors, minSize=(40, 40))
        vis = small.copy()

        for (x, y, w, h) in faces:
            cv2.rectangle(vis, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # 눈 검출(얼굴 ROI 안)
            if not eye_cascade.empty():
                roi_gray = gray[y:y + h, x:x + w]
                roi_vis = vis[y:y + h, x:x + w]
                eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.10, minNeighbors=5, minSize=(15, 15))
                for (ex, ey, ew, eh) in eyes[:6]:
                    cv2.rectangle(roi_vis, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)

        cv2.putText(vis, f"faces={len(faces)} sf={scaleFactor:.2f} n={minNeighbors}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow(win, vis)
        if is_exit_key(cv2.waitKey(1) & 0xFF):
            break

    cap.release()
    close_all_windows()


# =============================================================================
# demo 03. YOLO 객체 탐지 (OpenCV DNN)
def demo_03_yolo_detection(args) -> None:
    """
    [개념] OpenCV DNN + YOLO
    - YOLO는 one-stage detector로, 이미지에서 한 번의 forward로 박스/클래스를 예측합니다.
    - OpenCV에서는 dnn 모듈로 Darknet(cfg/weights) 또는 ONNX 모델을 로드할 수 있습니다.

    [필요 파일]
    - args.yolo_cfg:    예) yolov3.cfg
    - args.yolo_weights:예) yolov3.weights
    - args.yolo_names:  예) coco.names (클래스 이름)

    참고
    - 모델 파일은 용량이 크므로 본 코드에 포함하지 않았습니다.
    - 준비가 되면, 이미지/비디오(source) 모두 처리할 수 있습니다.
    """
    cfg = args.yolo_cfg
    weights = args.yolo_weights
    names = args.yolo_names

    if not (cfg and weights and os.path.isfile(cfg) and os.path.isfile(weights)):
        print("[ERROR] YOLO cfg/weights 파일이 필요합니다.")
        print("        예: --yolo_cfg ./yolo/yolov3.cfg --yolo_weights ./yolo/yolov3.weights --yolo_names ./yolo/coco.names")
        return

    classes: List[str] = []
    if names and os.path.isfile(names):
        with open(names, "r", encoding="utf-8") as f:
            classes = [ln.strip() for ln in f if ln.strip()]

    net = cv2.dnn.readNetFromDarknet(cfg, weights)

    # CPU/GPU 설정(가능한 경우)
    try:
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
    except Exception:
        pass

    layer_names = net.getLayerNames()
    out_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers().flatten()]

    conf_th = float(args.conf)
    nms_th = float(args.nms)

    def detect(frame: Any) -> Any:
        H, W = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(frame, scalefactor=1/255.0, size=(416, 416),
                                     mean=(0, 0, 0), swapRB=True, crop=False)
        net.setInput(blob)
        outs = net.forward(out_layers)

        boxes: List[List[int]] = []
        confidences: List[float] = []
        class_ids: List[int] = []

        for out in outs:
            for det in out:
                scores = det[5:]
                class_id = int(np.argmax(scores))
                confidence = float(scores[class_id])
                if confidence < conf_th:
                    continue
                cx, cy, w, h = det[0:4]
                x = int((cx - w / 2) * W)
                y = int((cy - h / 2) * H)
                bw = int(w * W)
                bh = int(h * H)
                boxes.append([x, y, bw, bh])
                confidences.append(confidence)
                class_ids.append(class_id)

        idxs = cv2.dnn.NMSBoxes(boxes, confidences, conf_th, nms_th)

        vis = frame.copy()
        if len(idxs) > 0:
            for i in idxs.flatten():
                x, y, bw, bh = boxes[i]
                x = max(0, x); y = max(0, y)
                cv2.rectangle(vis, (x, y), (x + bw, y + bh), (0, 0, 255), 2)
                name = classes[class_ids[i]] if classes and class_ids[i] < len(classes) else str(class_ids[i])
                cv2.putText(vis, f"{name} {confidences[i]:.2f}", (x, max(10, y - 5)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2, cv2.LINE_AA)
        return vis

    # 이미지 모드
    if args.image and os.path.isfile(args.image):
        img = cv2.imread(args.image, cv2.IMREAD_COLOR)
        if img is None:
            raise ValueError("이미지 로드 실패")
        vis = detect(img)
        safe_imshow("demo03_yolo_image (q/ESC)", vis, True, 1)
        while True:
            if is_exit_key(cv2.waitKey(20) & 0xFF):
                break
        close_all_windows()
        return

    # 비디오/웹캠 모드
    cap = _open_capture(args.source or "0")
    out_path = args.save or ""
    writer = None

    if out_path:
        fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
        w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) or 640)
        h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) or 480)
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        writer = cv2.VideoWriter(out_path, fourcc, float(fps), (w, h))
        if not writer.isOpened():
            writer = None
            print("[WARN] VideoWriter 오픈 실패. 저장 없이 진행합니다.")

    print("[KEY] q/ESC=quit")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        vis = detect(frame)
        if writer is not None:
            writer.write(vis)
        cv2.imshow("demo03_yolo_video (q/ESC)", vis)
        if is_exit_key(cv2.waitKey(1) & 0xFF):
            break

    if writer is not None:
        writer.release()
    cap.release()
    close_all_windows()


# =============================================================================
# demo 04. OCR 기본(pytesseract) + 전처리(그레이/이진화)
def demo_04_ocr_basic(args) -> None:
    """
    [개념] Tesseract OCR + pytesseract
    - pip install pytesseract
    - (별도 설치) Tesseract 엔진 설치 필요
      * Windows: tesseract.exe 경로를 pytesseract.pytesseract.tesseract_cmd에 지정
      * Mac/Linux: 설치 후 PATH에 잡히면 자동 인식되는 경우 많음

    [전처리]
    - OCR은 원본 그대로보다 "그레이스케일 + 이진화 + 노이즈 제거"가 성능을 크게 올립니다.
    """
    img = _load_or_make_image(args.image)

    try:
        import pytesseract  # type: ignore
    except Exception as e:
        print("[ERROR] pytesseract가 설치되어 있지 않습니다. pip install pytesseract")
        print("        detail:", e)
        return

    # (선택) tesseract 실행 파일 경로 지정
    if args.tesseract_cmd:
        pytesseract.pytesseract.tesseract_cmd = args.tesseract_cmd

    gray = bgr_to_gray(img)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    _ret, binimg = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    safe_imshow("demo04_input (q/ESC)", img, True, 1)
    safe_imshow("demo04_binary (q/ESC)", binimg, True, 1)

    # OCR 수행
    try:
        text_raw = pytesseract.image_to_string(img, lang=args.lang)
        text_bin = pytesseract.image_to_string(binimg, lang=args.lang)
    except Exception as e:
        print("[ERROR] OCR 실패:", e)
        return

    print("\n===== OCR (raw) =====\n", text_raw)
    print("\n===== OCR (binary) =====\n", text_bin)

    while True:
        if is_exit_key(cv2.waitKey(20) & 0xFF):
            break
    close_all_windows()


# =============================================================================
# demo 05. OCR 응용: 숫자/한정 문자 인식 + ROI + 모폴로지
def demo_05_ocr_digits_roi(args) -> None:
    """
    [응용] 숫자만 인식하기 / ROI 기반 인식
    - config 예:
      --psm 7  (한 줄 텍스트 가정)
      -c tessedit_char_whitelist=0123456789

    [ROI]
    - 전체 이미지에서 문자가 있는 영역만 잘라 OCR하면 오인식이 줄어듭니다.
    - 본 데모는 간단히 중앙 ROI를 사용합니다(마우스 ROI 선택은 과제 형태로 확장 가능)
    """
    img = _load_or_make_image(args.image)

    try:
        import pytesseract  # type: ignore
    except Exception as e:
        print("[ERROR] pytesseract가 설치되어 있지 않습니다. pip install pytesseract")
        print("        detail:", e)
        return

    if args.tesseract_cmd:
        pytesseract.pytesseract.tesseract_cmd = args.tesseract_cmd

    H, W = img.shape[:2]

    # 중앙 ROI(예시): 필요 시 직접 수정
    x1, y1 = int(0.10 * W), int(0.30 * H)
    x2, y2 = int(0.90 * W), int(0.65 * H)
    roi = img[y1:y2, x1:x2].copy()

    gray = bgr_to_gray(roi)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    _ret, binimg = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 모폴로지로 글자 구멍 메우기/잡음 제거(상황에 따라 열림/닫힘 선택)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    closed = cv2.morphologyEx(binimg, cv2.MORPH_CLOSE, kernel, iterations=1)

    cfg = "--psm 7 -c tessedit_char_whitelist=0123456789"
    try:
        text = pytesseract.image_to_string(closed, lang=args.lang, config=cfg)
    except Exception as e:
        print("[ERROR] OCR 실패:", e)
        return

    vis = img.copy()
    cv2.rectangle(vis, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.putText(vis, "ROI", (x1, max(20, y1 - 5)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    safe_imshow("demo05_roi_box (q/ESC)", vis, True, 1)
    safe_imshow("demo05_roi_binary_closed (q/ESC)", closed, True, 1)
    print("\n===== OCR (digits whitelist) =====\n", text)

    while True:
        if is_exit_key(cv2.waitKey(20) & 0xFF):
            break
    close_all_windows()


def main() -> None:
    parser = build_cli_parser("Object Detection & OCR (PDF4) - demos")

    # YOLO 관련 옵션
    parser.add_argument("--yolo_cfg", default="", help="YOLO cfg path (e.g., yolov3.cfg)")
    parser.add_argument("--yolo_weights", default="", help="YOLO weights path (e.g., yolov3.weights)")
    parser.add_argument("--yolo_names", default="", help="class names path (e.g., coco.names)")
    parser.add_argument("--conf", default=0.5, type=float, help="confidence threshold")
    parser.add_argument("--nms", default=0.4, type=float, help="NMS threshold")

    # OCR 관련 옵션
    parser.add_argument("--tesseract_cmd", default="", help="path to tesseract executable (Windows often needs this)")
    parser.add_argument("--lang", default="eng", help="OCR language (e.g., eng, kor, kor+eng)")

    args = parser.parse_args()

    demos = [
        Demo("00", "개요(객체탐지/문자인식)", demo_00_overview),
        Demo("01", "얼굴 인식(이미지) - Haar Cascade", demo_01_face_detection_image),
        Demo("02", "얼굴 인식(웹캠) + 트랙바 튜닝 + 눈 검출", demo_02_face_detection_webcam),
        Demo("03", "YOLO 객체 탐지(OpenCV DNN) - 이미지/비디오", demo_03_yolo_detection),
        Demo("04", "OCR 기본(pytesseract) + 전처리(이진화)", demo_04_ocr_basic),
        Demo("05", "OCR 응용(숫자/ROI/모폴로지)", demo_05_ocr_digits_roi),
    ]

    run_demos(demos, args)


if __name__ == "__main__":
    main()
