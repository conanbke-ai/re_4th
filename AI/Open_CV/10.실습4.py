# -*- coding: utf-8 -*-
"""
AI/Open_CV/10.실습4.py

python ./AI/Open_CV/10.실습4.py --task ex1 --trackbar

[실습 1] Sobel 필터 비교(기본)
- Sobel 필터의 방향별 결과를 비교합니다.
  1) 수평(x) 에지: dx=1, dy=0
  2) 수직(y) 에지: dx=0, dy=1
  3) 크기(magnitude): sqrt(gx^2 + gy^2)  (cv2.magnitude 사용)
- 3개 결과를 나란히 표시/저장하고, 어떤 에지가 강조되는지 관찰합니다.

[실습 2] Canny 파라미터 조정(응용)
- Canny 에지 검출기의 임계값(threshold)을 조절해 결과를 관찰합니다.
  - 낮은 임계값: (50, 100)
  - 중간 임계값: (100, 200)
  - 높은 임계값: (150, 300)
- (선택) 트랙바(슬라이더)로 실시간 조절합니다.

[입력 이미지]
- 기본 경로(사용자 요청):
  C:\\Users\\baesa\\OneDrive\\Documents\\GitHub\\re_4th\\AI\\images\\Cameraman.png
- 필요 시 --path로 다른 경로를 지정할 수 있습니다.

[저장 규칙]
- 결과물(이미지)은 기본적으로 "ouput" 디렉토리에 저장합니다.
- outdir는 '현재 작업 디렉토리'가 아니라 '이 스크립트가 있는 폴더' 기준으로 생성합니다.
  -> 예: AI/Open_CV/10.실습4.py 위치에서 AI/Open_CV/ouput/ 아래로 저장

[주의]
- cv2.imshow / trackbar는 GUI 환경에서만 동작합니다.
- GUI가 막힌 환경(헤드리스/주피터/원격 등)에서는 자동으로 파일 저장만 수행하도록 설계했습니다.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional, Tuple

import cv2
import numpy as np


# =============================================================================
# 0) 경로/출력 유틸
# =============================================================================

DEFAULT_IMAGE_PATH = r"C:\Users\baesa\OneDrive\Documents\GitHub\re_4th\AI\images\Cameraman.png"


def script_dir() -> Path:
    """
    현재 스크립트(10.실습4.py)가 위치한 폴더 경로를 반환합니다.

    왜 필요한가?
    - 파이썬 실행 위치(CWD)가 어디든 결과 저장 폴더를 "스크립트 기준"으로 고정하기 위함.
    """
    return Path(__file__).resolve().parent


def ensure_outdir(outdir: Path) -> Path:
    """
    출력 폴더(outdir)를 생성(없으면 생성)하고 Path를 반환합니다.
    """
    outdir.mkdir(parents=True, exist_ok=True)
    return outdir


# =============================================================================
# 1) 안전한 이미지 표시(헤드리스 환경에서도 죽지 않게)
# =============================================================================

def safe_imshow(winname: str, img: np.ndarray, out_fallback_path: Optional[Path] = None, wait: int = 0) -> int:
    """
    안전한 imshow:
    - GUI가 가능한 환경이면 창으로 표시
    - GUI가 불가능하면(out_fallback_path가 있으면) 파일로 저장하고 종료

    OpenCV highgui 관련 주의:
    - 어떤 환경에서는 imshow 자체는 실패하지 않아도 destroyWindow에서 "NULL window" 에러가 날 수 있습니다.
      -> 이를 방지하기 위해 namedWindow로 창을 먼저 생성하고,
         destroyWindow 실패 시 destroyAllWindows로 fallback 합니다.

    Returns
    -------
    int
        GUI 성공 시 waitKey 반환값 / 실패 시 -1
    """
    try:
        cv2.namedWindow(winname, cv2.WINDOW_NORMAL)
        cv2.imshow(winname, img)
        key = cv2.waitKey(wait)

        # 창 닫기(환경에 따라 destroyWindow가 실패할 수 있어 방어적으로 처리)
        try:
            cv2.destroyWindow(winname)
        except cv2.error:
            cv2.destroyAllWindows()

        return key

    except cv2.error as e:
        print(f"[WARN] cv2.imshow 실패(GUI 미지원 가능): {e}")
        if out_fallback_path is not None:
            cv2.imwrite(str(out_fallback_path), img)
            print(f"[INFO] 대체 저장 완료: {out_fallback_path}")

        # 혹시 남아 있는 창 정리(안전)
        try:
            cv2.destroyAllWindows()
        except Exception:
            pass

        return -1


# =============================================================================
# 2) 안전한 이미지 로드(파일 없거나 로드 실패 시에도 진행 가능하도록)
# =============================================================================

def safe_imread_gray(filepath: str | Path, default_shape: Tuple[int, int] = (512, 512)) -> np.ndarray:
    """
    그레이스케일 이미지를 안전하게 로드합니다.

    요구사항 관점에서 왜 필요한가?
    - 실습 코드가 "입력 파일이 없으면 즉시 죽는" 형태이면, 사용자 환경 문제(경로 오타 등)에서 실습이 중단됩니다.
    - 이 함수는 실패 시 기본 검정 이미지로 대체하여, 코드 흐름(저장/처리)을 유지합니다.

    한글 깨짐 주의:
    - OpenCV 기본 putText는 한글이 깨지므로,
      실패 메시지는 콘솔 print로 안내하고, 이미지에는 영문으로만 표기합니다.

    Returns
    -------
    np.ndarray
        (H,W) uint8 grayscale
    """
    p = Path(filepath)

    if not p.exists():
        print(f"[ERROR] 이미지를 찾을 수 없습니다: {p}")
        h, w = default_shape
        img = np.zeros((h, w), dtype=np.uint8)
        # 이미지 중앙에 영문 메시지(한글은 깨질 수 있음)
        cv2.putText(img, "FILE NOT FOUND", (20, h // 2), cv2.FONT_HERSHEY_SIMPLEX, 1.0, 255, 2, cv2.LINE_AA)
        return img

    img = cv2.imread(str(p), cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"[ERROR] 이미지 로드 실패(손상/권한/포맷 문제 가능): {p}")
        h, w = default_shape
        img = np.zeros((h, w), dtype=np.uint8)
        cv2.putText(img, "LOAD FAILED", (20, h // 2), cv2.FONT_HERSHEY_SIMPLEX, 1.0, 255, 2, cv2.LINE_AA)
        return img

    print(f"[OK] 이미지 로드 성공: {p.name} / shape={img.shape[::-1]}(W,H)")
    return img


# =============================================================================
# 3) [실습 1] Sobel 필터 비교
# =============================================================================

def sobel_compare(gray: np.ndarray, outdir: Path) -> None:
    """
    Sobel의 x, y 방향 결과와 magnitude를 계산하여 비교 이미지로 저장/표시합니다.

    구현 디테일(중요)
    - cv2.Sobel 출력은 보통 float 계열(CV_64F)을 권장합니다.
      이유: 음수 기울기(gradient) 값이 나오기 때문.
    - 화면 표시/저장을 위해서는 uint8로 스케일링이 필요합니다.
      -> convertScaleAbs 사용(절댓값 + 스케일 + uint8 변환)

    magnitude는:
    - gx, gy의 실수 배열을 준비한 뒤 cv2.magnitude(gx, gy)로 계산
    - 결과를 0~255로 정규화하여 보기 좋게 변환

    저장 파일
    - ouput/10_sobel_x.png
    - ouput/10_sobel_y.png
    - ouput/10_sobel_mag.png
    - ouput/10_sobel_compare.png
    """
    # 노이즈가 많으면 Sobel/Canny가 거칠어질 수 있어 가벼운 블러를 선적용(권장)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)

    # 1) x 방향 기울기(수직 에지가 강조됨: 좌우 변화에 민감)
    gx = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
    gx_u8 = cv2.convertScaleAbs(gx)

    # 2) y 방향 기울기(수평 에지가 강조됨: 상하 변화에 민감)
    gy = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)
    gy_u8 = cv2.convertScaleAbs(gy)

    # 3) magnitude(두 방향을 합친 전체 에지 강도)
    #    - magnitude는 실수 타입 입력이 적합
    mag = cv2.magnitude(gx.astype(np.float32), gy.astype(np.float32))

    # mag를 0~255로 정규화해서 시각화 가능한 uint8로 변환
    mag_norm = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
    mag_u8 = mag_norm.astype(np.uint8)

    # 보기 편하게 라벨(영문) 추가: 한글은 깨질 수 있어 영문 사용
    def label(img_u8: np.ndarray, text: str) -> np.ndarray:
        bgr = cv2.cvtColor(img_u8, cv2.COLOR_GRAY2BGR)
        cv2.putText(bgr, text, (12, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2, cv2.LINE_AA)
        return bgr

    x_bgr = label(gx_u8, "Sobel X")
    y_bgr = label(gy_u8, "Sobel Y")
    m_bgr = label(mag_u8, "Magnitude")

    # 3개를 나란히(가로) 결합
    compare = cv2.hconcat([x_bgr, y_bgr, m_bgr])

    # 저장
    out_x = outdir / "10_sobel_x.png"
    out_y = outdir / "10_sobel_y.png"
    out_m = outdir / "10_sobel_mag.png"
    out_cmp = outdir / "10_sobel_compare.png"

    cv2.imwrite(str(out_x), gx_u8)
    cv2.imwrite(str(out_y), gy_u8)
    cv2.imwrite(str(out_m), mag_u8)
    cv2.imwrite(str(out_cmp), compare)

    print(f"[OK] 저장: {out_x}")
    print(f"[OK] 저장: {out_y}")
    print(f"[OK] 저장: {out_m}")
    print(f"[OK] 저장: {out_cmp}")

    safe_imshow("Sobel Compare (X | Y | Magnitude)", compare, out_fallback_path=out_cmp, wait=0)


# =============================================================================
# 4) [실습 2] Canny 파라미터 조정
# =============================================================================

def canny_presets(gray: np.ndarray, outdir: Path) -> None:
    """
    Canny를 3개 임계값 세트로 실행하고 결과를 비교 저장합니다.

    Canny 임계값(Threshold) 개념
    - Canny는 두 임계값을 사용합니다: lowThreshold, highThreshold
      * highThreshold 이상: 강한 에지(확실)
      * lowThreshold 이상 ~ highThreshold 미만: 약한 에지(강한 에지와 연결되면 유지)
      * lowThreshold 미만: 제거
    - 임계값이 높아질수록 에지가 "덜" 검출됩니다(더 엄격).

    저장 파일
    - ouput/10_canny_low_50_100.png
    - ouput/10_canny_mid_100_200.png
    - ouput/10_canny_high_150_300.png
    - ouput/10_canny_compare.png
    """
    blur = cv2.GaussianBlur(gray, (3, 3), 0)

    presets = [
        ("LOW  (50,100)", 50, 100, "10_canny_low_50_100.png"),
        ("MID  (100,200)", 100, 200, "10_canny_mid_100_200.png"),
        ("HIGH (150,300)", 150, 300, "10_canny_high_150_300.png"),
    ]

    cells = []
    for title, low, high, fname in presets:
        edges = cv2.Canny(blur, threshold1=low, threshold2=high)
        out_path = outdir / fname
        cv2.imwrite(str(out_path), edges)
        print(f"[OK] 저장: {out_path}")

        bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        cv2.putText(bgr, title, (12, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.85, (255, 255, 255), 2, cv2.LINE_AA)
        cells.append(bgr)

    compare = cv2.hconcat(cells)
    out_cmp = outdir / "10_canny_compare.png"
    cv2.imwrite(str(out_cmp), compare)
    print(f"[OK] 저장: {out_cmp}")

    safe_imshow("Canny Compare (LOW | MID | HIGH)", compare, out_fallback_path=out_cmp, wait=0)


def _next_index(outdir: Path, prefix: str, ext: str = ".png") -> int:
    """
    저장 파일 이름을 prefix_001.png, prefix_002.png ... 형태로 만들기 위한 인덱스 계산기.
    """
    max_idx = 0
    for p in outdir.glob(f"{prefix}_*{ext}"):
        # 예: prefix_003.png -> stem: prefix_003 -> split -> ["prefix", "003"]
        parts = p.stem.split("_")
        if parts and parts[-1].isdigit():
            max_idx = max(max_idx, int(parts[-1]))
    return max_idx + 1


def canny_trackbar(gray: np.ndarray, outdir: Path) -> None:
    """
    트랙바로 Canny 임계값(low/high)을 실시간 조절합니다.

    키 조작
    - q : 종료
    - s : 현재 결과 저장 (10_canny_live_001.png ...)

    GUI 미지원 환경 처리
    - createTrackbar / imshow가 실패하면 예외가 발생할 수 있음
    - 이 경우 preset 비교 저장만으로도 실습 목표를 달성할 수 있으므로
      '경고 출력 후 종료'하도록 설계

    저장 파일(사용자가 s를 누를 때마다)
    - ouput/10_canny_live_001.png
    - ouput/10_canny_live_002.png
    - ...
    """
    blur = cv2.GaussianBlur(gray, (3, 3), 0)

    win = "Canny Trackbar (q=quit, s=save)"
    try:
        cv2.namedWindow(win, cv2.WINDOW_NORMAL)

        # 트랙바 범위는 넉넉하게
        # low: 0~500, high: 0~500
        # (카메라맨 이미지에서는 0~300 수준이면 충분하지만, 범용성을 위해 500)
        cv2.createTrackbar("low", win, 100, 500, lambda v: None)
        cv2.createTrackbar("high", win, 200, 500, lambda v: None)

        idx = _next_index(outdir, "10_canny_live", ext=".png")
        print("[INFO] 트랙바 모드 시작: q=종료, s=저장")
        print(f"[INFO] 저장 폴더: {outdir}")

        while True:
            low = cv2.getTrackbarPos("low", win)
            high = cv2.getTrackbarPos("high", win)

            # 안정 장치: high는 항상 low보다 크도록
            if high <= low:
                high = low + 1

            edges = cv2.Canny(blur, threshold1=low, threshold2=high)

            # 보기 좋게 라벨(영문)
            view = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
            cv2.putText(view, f"low={low}  high={high}", (12, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.85, (255, 255, 255), 2, cv2.LINE_AA)

            cv2.imshow(win, view)

            key = cv2.waitKey(10) & 0xFF
            if key == ord("q"):
                break
            if key == ord("s"):
                out_path = outdir / f"10_canny_live_{idx:03d}.png"
                cv2.imwrite(str(out_path), edges)
                print(f"[OK] 저장됨: {out_path.name} (low={low}, high={high})")
                idx += 1

        try:
            cv2.destroyWindow(win)
        except cv2.error:
            cv2.destroyAllWindows()

    except cv2.error as e:
        print(f"[WARN] 트랙바/GUI 실행 불가(GUI 미지원 가능): {e}")
        print("[INFO] GUI가 안 되는 환경이면 preset 비교 이미지(10_canny_compare.png)로 확인하세요.")
        try:
            cv2.destroyAllWindows()
        except Exception:
            pass


# =============================================================================
# 5) CLI
# =============================================================================

TASKS = {
    "ex1": ("실습1: Sobel 필터 비교(X/Y/Magnitude)", "sobel"),
    "ex2": ("실습2: Canny 파라미터(프리셋 + 트랙바 선택)", "canny"),
    "all": ("실습1+실습2 모두 실행", "all"),
}


def list_tasks() -> None:
    print("사용 가능한 --task 목록:")
    for k, (desc, _) in TASKS.items():
        print(f" - {k:<4} : {desc}")


def main() -> None:
    parser = argparse.ArgumentParser(description="OpenCV 에지 검출 실습 (Sobel / Canny)")
    parser.add_argument("--list", action="store_true", help="task 목록 출력")
    parser.add_argument("--task", type=str, default="all", help="ex1 / ex2 / all")
    parser.add_argument("--outdir", type=str, default="ouput", help="결과 저장 폴더(기본: ouput)")
    parser.add_argument("--path", type=str, default=DEFAULT_IMAGE_PATH, help="입력 이미지 경로")
    parser.add_argument("--trackbar", action="store_true", help="ex2에서 트랙바 모드 실행(선택)")

    args = parser.parse_args()

    if args.list:
        list_tasks()
        return

    task = args.task.strip().lower()
    if task not in TASKS:
        print(f"[ERROR] 알 수 없는 task: {task}")
        list_tasks()
        return

    outdir = ensure_outdir(script_dir() / args.outdir)

    # 입력 로드(그레이스케일)
    gray = safe_imread_gray(args.path)

    if task == "ex1":
        sobel_compare(gray, outdir)
        return

    if task == "ex2":
        canny_presets(gray, outdir)
        if args.trackbar:
            canny_trackbar(gray, outdir)
        else:
            print("[INFO] 트랙바를 실행하려면: --trackbar 옵션을 추가하세요.")
        return

    # all
    sobel_compare(gray, outdir)
    canny_presets(gray, outdir)
    if args.trackbar:
        canny_trackbar(gray, outdir)
    else:
        print("[INFO] 트랙바를 실행하려면: --trackbar 옵션을 추가하세요.")


if __name__ == "__main__":
    main()
