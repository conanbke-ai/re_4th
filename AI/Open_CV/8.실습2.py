"""
AI/OpenCV/8.실습2.py

OpenCV / NumPy 실습 모음 (실습 1~4 + 추가 실습 1~4) - 단일 .py 파일 버전

저장 규칙(요청 반영)
- 결과물(이미지/비디오)은 기본적으로 "ouput" 디렉토리에 저장합니다.
  ※ 디렉토리명은 요청하신 그대로 "ouput" 입니다(일반적으로는 output을 많이 사용).
- outdir는 "현재 작업 디렉토리"가 아니라 "이 스크립트가 있는 폴더" 기준으로 생성합니다.
  -> 예: AI/OpenCV/8.실습.py 위치에서 AI/OpenCV/ouput/ 아래로 저장

요구사항
- Python 3.x
- pip install opencv-python numpy

실행 방법
1) 목록 보기
   python ./AI/Open_CV/8.실습2.py --list

2) 특정 실습 실행
   python ./AI/Open_CV/8.실습2.py --task ex1

3) 출력 폴더 변경(선택)
   python ./AI/Open_CV/8.실습2.py --task ex1 --outdir ouput   # 기본값이므로 보통 생략 가능

주의
- cv2.imshow()는 GUI 환경(로컬 PC)에서 정상 동작합니다.
  (주피터/서버/헤드리스 환경에서는 창이 안 뜰 수 있음)
- 이 스크립트는 imshow 실패 시 자동으로 파일 저장으로 대체하도록 설계했습니다.

작업(Task) ID
- ex1      : (실습1) 컬러 이미지 생성(기본) - 빨강/초록/파랑 3정사각형
- ex2      : (실습2) 채널 조작(응용) - 노란색에서 B채널 0 만들기
- ex3      : (실습3) ROI 복사(응용) - 빨간 이미지(200x200)를 파란 배경(400x400) 중앙에 복사
- ex4      : (실습4) 그라데이션 이미지(도전) - 수평+수직 그라데이션 합성

- extra1   : (추가1) 이미지 저장 비교(기본) - JPG(50), JPG(95), PNG 크기 비교
- extra2   : (추가2) 이미지 읽기 실패 처리(응용) - safe_imread 구현
- extra3   : (추가3) 웹캠 캡처 및 저장(응용) - 's' 저장, 'q' 종료
- extra4   : (추가4) 비디오 속도 조절(도전) - 원본/2배속/0.5배속 생성
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Optional, Tuple

import cv2
import numpy as np

# Pillow(PIL)는 한글 텍스트 렌더링을 위해 사용합니다.
# (OpenCV 기본 putText는 한글/유니코드 렌더링 불가)
try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError as e:
    raise ImportError(
        "Pillow가 설치되어 있지 않습니다. 한글 텍스트 출력을 위해 pillow가 필요합니다.\n"
        "설치: pip install pillow"
    ) from e


# =============================================================================
# 공통 유틸리티
# =============================================================================

def script_dir() -> Path:
    """
    현재 스크립트 파일이 위치한 디렉토리 경로를 반환합니다.

    왜 필요한가?
    - 보통 파이썬 스크립트는 실행한 위치(CWD)에 영향을 받습니다.
    - 하지만 실습 결과 파일을 "항상 스크립트 폴더 기준"으로 저장하고 싶을 때,
      __file__ 기반으로 경로를 잡아두는 것이 가장 안전합니다.

    Returns
    -------
    Path
        이 스크립트가 위치한 폴더(절대 경로)
    """
    return Path(__file__).resolve().parent


def ensure_outdir(outdir: Path) -> Path:
    """
    출력 디렉토리를 생성(없으면 생성)하고, Path를 반환합니다.

    Parameters
    ----------
    outdir : Path
        생성/확인할 디렉토리 경로

    Returns
    -------
    Path
        실제 존재하게 된 출력 디렉토리 경로
    """
    outdir.mkdir(parents=True, exist_ok=True)
    return outdir


def safe_imshow(winname: str, img: np.ndarray, out_fallback_path: Optional[Path] = None, wait: int = 0) -> None:
    """
    OpenCV 창으로 이미지를 띄웁니다.
    GUI 환경이 아니거나, imshow가 실패할 경우(out_fallback_path가 있으면) 파일로 저장합니다.

    왜 이런 처리가 필요한가?
    - Windows/로컬 PC에서는 보통 문제 없지만,
      서버/가상환경/원격 환경에서는 GUI가 없어 imshow가 실패할 수 있습니다.
    - 실습 결과가 완전히 사라지지 않도록 "저장 파일"을 안전장치로 둡니다.

    Parameters
    ----------
    winname : str
        창 제목
    img : np.ndarray
        표시할 이미지(BGR 또는 Grayscale)
    out_fallback_path : Optional[Path]
        imshow 실패 시 저장할 파일 경로 (예: outdir/'result.png')
    wait : int
        cv2.waitKey 대기 시간(ms). 0이면 키 입력까지 대기.
    """
    try:
        cv2.imshow(winname, img)
        cv2.waitKey(wait)
        cv2.destroyWindow(winname)
    except cv2.error as e:
        print(f"[WARN] cv2.imshow 실패: {e}")
        if out_fallback_path is not None:
            cv2.imwrite(str(out_fallback_path), img)
            print(f"[INFO] 대체 저장 완료: {out_fallback_path}")


def bgr_note() -> None:
    """
    OpenCV는 색상 채널 순서가 RGB가 아니라 BGR임을 안내합니다.
    (실습 초기에 가장 자주 헷갈리는 포인트)
    """
    print("[NOTE] OpenCV 색상 채널 순서: BGR (Blue, Green, Red)")


# =============================================================================
# 한글 텍스트 렌더링 유틸 (핵심)
# =============================================================================

def find_korean_font_path() -> Optional[str]:
    """
    '폰트 파일을 따로 준비하지 않았다'는 상황을 고려하여,
    OS에 기본으로 설치되어 있을 가능성이 높은 한글 폰트 경로를 자동 탐색합니다.

    - Windows: malgun.ttf(맑은 고딕), gulim.ttc(굴림) 등이 기본 탑재인 경우가 많음
    - macOS: AppleSDGothicNeo.ttc 등
    - Linux: Nanum, NotoSansCJK 등 (환경에 따라 다름)

    Returns
    -------
    Optional[str]
        사용 가능한 폰트 파일 경로(str). 못 찾으면 None.
    """
    candidates = [
        # Windows (대부분 존재)
        r"C:\Windows\Fonts\malgun.ttf",
        r"C:\Windows\Fonts\malgunbd.ttf",
        r"C:\Windows\Fonts\gulim.ttc",
        r"C:\Windows\Fonts\batang.ttc",

        # macOS (대부분 존재)
        "/System/Library/Fonts/AppleSDGothicNeo.ttc",
        "/Library/Fonts/AppleGothic.ttf",

        # Linux (배포판별 상이)
        "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",
        "/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
    ]

    for p in candidates:
        if Path(p).exists():
            # "파일이 존재"하더라도 Pillow가 truetype 로딩에 실패할 수도 있어 확인합니다.
            try:
                _ = ImageFont.truetype(p, 20)
                return p
            except Exception:
                continue

    return None


def draw_center_text_unicode(
    bgr_img: np.ndarray,
    text: str,
    font_path: Optional[str],
    font_size: int = 24,
    color: Tuple[int, int, int] = (255, 255, 255),
    line_gap: int = 10,
    fallback_english: Optional[str] = None,
) -> np.ndarray:
    """
    OpenCV(BGR) 이미지에 '유니코드 텍스트(한글 포함)'를 정중앙에 표시합니다.

    구현 전략
    - OpenCV putText는 한글 미지원 -> Pillow로 텍스트 렌더링
    - Pillow는 RGB 기반 -> BGR<->RGB 변환이 필요

    폰트를 못 찾는 경우
    - font_path가 None이면 한글 렌더링 불가
    - 이때는 "영문 안내(fallback_english)"를 OpenCV putText로 표시(깨짐 방지)

    Parameters
    ----------
    bgr_img : np.ndarray
        대상 이미지(BGR)
    text : str
        출력할 문자열(여러 줄 가능: '\n' 사용)
    font_path : Optional[str]
        TTF/TTC/OTF 폰트 경로. None이면 한글 렌더링 불가.
    font_size : int
        폰트 크기
    color : Tuple[int,int,int]
        텍스트 색상
    line_gap : int
        줄 간격(px)
    fallback_english : Optional[str]
        font_path가 없을 때 표시할 영문 메시지

    Returns
    -------
    np.ndarray
        텍스트가 오버레이된 BGR 이미지
    """
    # ------------------------------------------------------------
    # 1) 폰트가 없으면: OpenCV 기본 폰트(영문)로 대체
    # ------------------------------------------------------------
    if not font_path:
        out = bgr_img.copy()
        msg = fallback_english or "Message"
        h, w = out.shape[:2]

        # OpenCV putText는 baseline 기준 좌표 -> 중앙 배치를 위해 크기 계산
        (tw, th), _ = cv2.getTextSize(msg, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
        x = max(10, (w - tw) // 2)
        y = max(th + 10, (h + th) // 2)
        cv2.putText(out, msg, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        return out

    # ------------------------------------------------------------
    # 2) 폰트가 있으면: Pillow로 한글/유니코드 렌더링
    # ------------------------------------------------------------
    rgb = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(rgb)
    draw = ImageDraw.Draw(pil_img)

    font = ImageFont.truetype(font_path, font_size)

    lines = text.split("\n")

    bboxes = [draw.textbbox((0, 0), line, font=font) for line in lines]
    widths = [(b[2] - b[0]) for b in bboxes]
    heights = [(b[3] - b[1]) for b in bboxes]

    total_h = sum(heights) + line_gap * (len(lines) - 1)
    H, W = bgr_img.shape[:2]
    y = (H - total_h) // 2

    for i, line in enumerate(lines):
        x = (W - widths[i]) // 2
        draw.text((x, y), line, font=font, fill=color)
        y += heights[i] + line_gap

    out = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    return out


# =============================================================================
# 실습 1~4
# =============================================================================

def exercise_1_color_squares(outdir: Path) -> None:
    """
    (실습 1) 컬러 이미지 생성(기본)

    목표
    - NumPy로 이미지 버퍼(배열)를 직접 만들 수 있다.
    - 슬라이싱으로 영역(ROI)을 나누어 색을 채울 수 있다.

    결과
    - 300x900 이미지
    - 왼쪽부터 빨강/초록/파랑 정사각형(300x300씩)
    """
    bgr_note()

    img = np.zeros((300, 900, 3), dtype=np.uint8)

    img[:, 0:300] = (0, 0, 255)
    img[:, 300:600] = (0, 255, 0)
    img[:, 600:900] = (255, 0, 0)

    out_path = outdir / "ex1_color_squares.png"
    cv2.imwrite(str(out_path), img)
    print(f"[OK] 저장: {out_path}")

    safe_imshow("Exercise1 - Color Squares", img, out_fallback_path=out_path, wait=0)


def exercise_2_channel_manipulation(outdir: Path) -> None:
    """
    (실습 2) 채널 조작(응용)

    목표
    - cv2.split / cv2.merge로 채널을 분리/재결합할 수 있다.
    - 특정 채널만 수정해서 색 변화를 이해한다.

    실습 내용
    - 노란색 이미지(BGR: 0,255,255)를 만든다.
    - B 채널을 0으로 만든다.
    - 결과가 어떻게 변하는지 확인한다.

    핵심 개념
    - 노란색(BGR)은 원래부터 B=0이므로, B를 0으로 만들어도 '거의 변화 없음'이 정상입니다.
    """
    bgr_note()

    img = np.zeros((300, 300, 3), dtype=np.uint8)
    img[:] = (0, 255, 255)

    b, g, r = cv2.split(img)
    b[:] = 0
    img_b0 = cv2.merge([b, g, r])

    out_orig = outdir / "ex2_original_yellow.png"
    out_b0 = outdir / "ex2_b_channel_zero.png"
    cv2.imwrite(str(out_orig), img)
    cv2.imwrite(str(out_b0), img_b0)

    print(f"[OK] 저장: {out_orig}")
    print(f"[OK] 저장: {out_b0}")
    print("[ANS] 원본이 (0,255,255)로 B=0이므로, B를 0으로 만들어도 결과는 거의 동일한 '노란색'입니다.")

    safe_imshow("Exercise2 - Original Yellow", img, out_fallback_path=out_orig, wait=1)
    safe_imshow("Exercise2 - B=0", img_b0, out_fallback_path=out_b0, wait=0)


def exercise_3_roi_copy(outdir: Path) -> None:
    """
    (실습 3) ROI 복사(응용)

    목표
    - ROI(Region Of Interest)를 이용해 특정 영역에 이미지를 복사할 수 있다.
    - 중심 좌표 계산을 통해 '중앙 배치'를 구현할 수 있다.

    실습 내용
    - 400x400 파란 배경(img1)
    - 200x200 빨간 이미지(img2)
    - img2를 img1 중앙에 복사
    """
    bgr_note()

    img1 = np.zeros((400, 400, 3), dtype=np.uint8)
    img1[:] = (255, 0, 0)

    img2 = np.zeros((200, 200, 3), dtype=np.uint8)
    img2[:] = (0, 0, 255)

    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]

    y0 = (h1 - h2) // 2
    x0 = (w1 - w2) // 2

    img1[y0:y0 + h2, x0:x0 + w2] = img2

    out_path = outdir / "ex3_roi_copy.png"
    cv2.imwrite(str(out_path), img1)
    print(f"[OK] 저장: {out_path}")

    safe_imshow("Exercise3 - ROI Copy", img1, out_fallback_path=out_path, wait=0)


def exercise_4_gradient(outdir: Path) -> None:
    """
    (실습 4) 그라데이션 이미지(도전)

    목표
    - 1D 그라데이션을 만들고, 브로드캐스팅으로 2D로 확장할 수 있다.
    - 오버플로우(overflow) 문제를 피하기 위해 dtype을 적절히 바꿀 수 있다.

    실습 내용
    - 300x300
    - 좌->우 0->255 수평 그라데이션
    - 위->아래 0->255 수직 그라데이션
    - 두 값을 합성하여 "2D 그라데이션" 만들기
    """
    h, w = 300, 300

    gx = np.linspace(0, 255, w, dtype=np.uint8)[None, :]
    gy = np.linspace(0, 255, h, dtype=np.uint8)[:, None]

    grad = ((gx.astype(np.uint16) + gy.astype(np.uint16)) // 2).astype(np.uint8)
    img = cv2.merge([grad, grad, grad])

    out_path = outdir / "ex4_gradient.png"
    cv2.imwrite(str(out_path), img)
    print(f"[OK] 저장: {out_path}")

    safe_imshow("Exercise4 - 2D Gradient", img, out_fallback_path=out_path, wait=0)


# =============================================================================
# 추가 실습 1~4
# =============================================================================

def extra_1_save_format_compare(outdir: Path) -> None:
    """
    (추가 실습 1) 이미지 저장 비교(기본)

    목표
    - 같은 이미지라도 파일 포맷/압축 품질에 따라 용량이 크게 달라짐을 확인한다.
    - JPG 품질 옵션(IMWRITE_JPEG_QUALITY)을 이해한다.

    실습 내용
    - 640x480 랜덤 컬러 이미지 생성
    - JPG(품질 50), JPG(품질 95), PNG 저장
    - 파일 크기(bytes) 비교 출력
    """
    rng = np.random.default_rng()
    img = rng.integers(0, 256, size=(480, 640, 3), dtype=np.uint8)

    f_q50 = outdir / "extra1_rand_q50.jpg"
    f_q95 = outdir / "extra1_rand_q95.jpg"
    f_png = outdir / "extra1_rand.png"

    cv2.imwrite(str(f_q50), img, [cv2.IMWRITE_JPEG_QUALITY, 50])
    cv2.imwrite(str(f_q95), img, [cv2.IMWRITE_JPEG_QUALITY, 95])
    cv2.imwrite(str(f_png), img)

    print("[INFO] 파일 크기 비교(bytes):")
    for f in [f_q50, f_q95, f_png]:
        print(f" - {f.name}: {os.path.getsize(f)} bytes")

    safe_imshow("Extra1 - Random Image", img, out_fallback_path=f_png, wait=0)


def safe_imread(filepath: str | Path, default_shape: Tuple[int, int] = (300, 300)) -> np.ndarray:
    """
    (추가 실습 2) 이미지 읽기 실패 처리(응용)

    목표
    - cv2.imread는 실패 시 None을 반환한다는 점을 이해한다.
    - 파일이 없거나/손상되었을 때도 "프로그램이 죽지 않게" 안전하게 처리한다.
    - 실패 시 print 메시지뿐 아니라, 반환 이미지 중앙에 "한글 안내"를 표시하여
      imshow로 띄우면 '창에서도' 바로 문제를 확인할 수 있게 한다.

    한글 출력 핵심
    - OpenCV putText는 한글 미지원 -> Pillow 사용
    - 폰트 파일을 별도로 두지 않아도 시스템 폰트를 자동 탐색
    - 폰트를 못 찾으면 영문 메시지로 fallback (깨짐 방지)

    Returns
    -------
    np.ndarray
        성공 시 로드된 이미지(BGR),
        실패 시 안내 텍스트가 포함된 검정 이미지(BGR)
    """
    filepath = Path(filepath)
    font_path = find_korean_font_path()

    if not filepath.exists():
        print(f"이미지를 찾을 수 없습니다: {filepath}")
        h, w = default_shape
        fallback = np.zeros((h, w, 3), dtype=np.uint8)
        msg_kr = f"이미지를 찾을 수 없습니다\n{filepath.name}"
        msg_en = f"Image not found: {filepath.name}"
        return draw_center_text_unicode(
            fallback, text=msg_kr, font_path=font_path, font_size=22, line_gap=10, fallback_english=msg_en
        )

    img = cv2.imread(str(filepath))
    if img is None:
        print(f"이미지 로드 실패: {filepath}")
        h, w = default_shape
        fallback = np.zeros((h, w, 3), dtype=np.uint8)
        msg_kr = f"이미지 로드 실패\n{filepath.name}"
        msg_en = f"Load failed: {filepath.name}"
        return draw_center_text_unicode(
            fallback, text=msg_kr, font_path=font_path, font_size=22, line_gap=10, fallback_english=msg_en
        )

    h, w = img.shape[:2]
    print(f"이미지 로드 성공: {filepath.name} / size={w}x{h}")
    return img


def extra_2_safe_imread_demo(outdir: Path) -> None:
    """
    (추가 실습 2) safe_imread 데모

    - 존재하지 않는 파일을 일부러 읽어 실패 상황을 만들고,
      반환된 이미지(검정 배경 + 중앙 안내 텍스트)를 저장/표시합니다.
    """
    img = safe_imread(outdir / "nonexistent.jpg")
    out_path = outdir / "extra2_safe_imread_result.png"
    cv2.imwrite(str(out_path), img)
    print(f"[OK] 결과 저장: {out_path}")
    safe_imshow("Extra2 - safe_imread result", img, out_fallback_path=out_path, wait=0)


def _next_photo_index(outdir: Path, prefix: str = "photo_", ext: str = ".jpg") -> int:
    """
    photo_001.jpg, photo_002.jpg ... 형태로 저장할 때 다음 인덱스를 계산합니다.
    - 이미 존재하는 파일을 스캔하여 가장 큰 번호 다음 번호를 반환
    """
    max_idx = 0
    for p in outdir.glob(f"{prefix}*{ext}"):
        stem = p.stem
        parts = stem.split("_")
        if len(parts) >= 2 and parts[-1].isdigit():
            max_idx = max(max_idx, int(parts[-1]))
    return max_idx + 1


def extra_3_webcam_capture(outdir: Path, camera_index: int = 0) -> None:
    """
    (추가 실습 3) 웹캠 캡처 및 저장(응용)

    - 's' 키: 사진 저장
    - 'q' 키: 종료
    """
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        raise RuntimeError(f"웹캠을 열 수 없습니다. VideoCapture({camera_index}) 실패")

    count = _next_photo_index(outdir)
    print("[INFO] Webcam started. 's' to save, 'q' to quit.")
    print(f"[INFO] 저장 폴더: {outdir}")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[WARN] 프레임을 읽을 수 없습니다.")
            break

        cv2.imshow("Extra3 - Webcam", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
        if key == ord("s"):
            filename = outdir / f"photo_{count:03d}.jpg"
            cv2.imwrite(str(filename), frame)
            print("사진 저장됨:", filename.name)
            count += 1

    cap.release()
    cv2.destroyAllWindows()
    print("[INFO] Webcam closed.")


def _make_synthetic_frame(i: int, total: int, w: int, h: int) -> np.ndarray:
    """
    (추가 실습 4) 비디오 생성에 사용할 합성 프레임 생성 함수.
    프레임 번호에 따라 배경색이 변하고 텍스트가 표시되도록 만듭니다.
    """
    frame = np.zeros((h, w, 3), dtype=np.uint8)

    color = (i % 256, (i * 2) % 256, (i * 3) % 256)
    frame[:] = color

    cv2.putText(
        frame,
        f"frame {i+1}/{total}",
        (20, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (255, 255, 255),
        2,
        cv2.LINE_AA,
    )
    return frame


def extra_4_video_speed_control(outdir: Path, w: int = 640, h: int = 480, fps: int = 30, sec: int = 5) -> None:
    """
    (추가 실습 4) 비디오 속도 조절(도전)

    - 원본 비디오 생성 (5초, 30fps, 컬러 프레임)
    - 2배속 비디오 생성 (프레임 간격을 2로 -> 매 2프레임마다 1프레임만 기록)
    - 0.5배속 비디오 생성 (프레임 중복 -> 각 프레임을 2번 기록)
    """
    total = fps * sec
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    f_org = outdir / "extra4_video_original.mp4"
    f_2x = outdir / "extra4_video_2x.mp4"
    f_0_5x = outdir / "extra4_video_0_5x.mp4"

    out_org = cv2.VideoWriter(str(f_org), fourcc, fps, (w, h))
    out_fast = cv2.VideoWriter(str(f_2x), fourcc, fps, (w, h))
    out_slow = cv2.VideoWriter(str(f_0_5x), fourcc, fps, (w, h))

    if not out_org.isOpened() or not out_fast.isOpened() or not out_slow.isOpened():
        raise RuntimeError(
            "VideoWriter 열기 실패. 코덱/확장자 문제일 수 있습니다.\n"
            "- 해결: fourcc를 'XVID'로 바꾸고 확장자를 .avi로 바꿔 시도하세요."
        )

    print(f"[INFO] 비디오 저장 폴더: {outdir}")

    for i in range(total):
        out_org.write(_make_synthetic_frame(i, total, w, h))

    for i in range(0, total, 2):
        out_fast.write(_make_synthetic_frame(i, total, w, h))

    for i in range(total):
        frame = _make_synthetic_frame(i, total, w, h)
        out_slow.write(frame)
        out_slow.write(frame)

    out_org.release()
    out_fast.release()
    out_slow.release()

    print(f"[OK] 생성 완료: {f_org.name}")
    print(f"[OK] 생성 완료: {f_2x.name}")
    print(f"[OK] 생성 완료: {f_0_5x.name}")


# =============================================================================
# CLI (명령행) 인터페이스
# =============================================================================

TASKS = {
    "ex1": ("실습1: 컬러 정사각형 이미지 생성", exercise_1_color_squares),
    "ex2": ("실습2: 채널 조작(노란색에서 B=0)", exercise_2_channel_manipulation),
    "ex3": ("실습3: ROI 복사(중앙에 복사)", exercise_3_roi_copy),
    "ex4": ("실습4: 수평+수직 그라데이션 합성", exercise_4_gradient),
    "extra1": ("추가1: 저장 포맷 비교(JPG 품질/PNG)", extra_1_save_format_compare),
    "extra2": ("추가2: safe_imread(실패 처리) 데모(한글 중앙 안내)", extra_2_safe_imread_demo),
    "extra3": ("추가3: 웹캠 캡처 및 저장", None),
    "extra4": ("추가4: 비디오 속도 조절(원본/2x/0.5x)", extra_4_video_speed_control),
}


def list_tasks() -> None:
    print("사용 가능한 --task 목록:")
    for k, (desc, _) in TASKS.items():
        print(f" - {k:<7} : {desc}")


def main() -> None:
    parser = argparse.ArgumentParser(description="OpenCV 실습 1~4 + 추가 실습 1~4 (단일 파일)")
    parser.add_argument("--list", action="store_true", help="가능한 task 목록 출력")
    parser.add_argument("--task", type=str, default=None, help="실행할 task id (예: ex1, ex2, extra3 ...)")
    parser.add_argument("--outdir", type=str, default="ouput", help="결과 저장 폴더(기본: ouput)")
    parser.add_argument("--camera", type=int, default=0, help="웹캠 인덱스 (extra3에서 사용)")
    parser.add_argument("--path", type=str, default=None, help="extra2에서 테스트할 이미지 경로(선택)")

    args = parser.parse_args()

    if args.list:
        list_tasks()
        return

    if args.task is None:
        list_tasks()
        print("\n예) python 8.실습2.py --task ex1")
        return

    task = args.task.strip()

    if task not in TASKS:
        print(f"[ERROR] 알 수 없는 task: {task}")
        list_tasks()
        return

    outdir = ensure_outdir(script_dir() / args.outdir)

    if task == "extra3":
        extra_3_webcam_capture(outdir, camera_index=args.camera)
        return

    if task == "extra2" and args.path:
        img = safe_imread(args.path)
        out_path = outdir / "extra2_custom_path_result.png"
        cv2.imwrite(str(out_path), img)
        print(f"[OK] 커스텀 경로 테스트 결과 저장: {out_path}")
        safe_imshow("Extra2 - custom path result", img, out_fallback_path=out_path, wait=0)
        return

    _, fn = TASKS[task]
    if fn is None:
        print(f"[ERROR] task 함수가 비어 있습니다: {task}")
        return

    fn(outdir)


if __name__ == "__main__":
    main()
