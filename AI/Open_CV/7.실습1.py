"""
체스보드(체커보드) 생성/검출 실습 통합 코드

핵심 목표
- 체크보드(체스보드) 패턴을 직접 생성(합성 이미지)
- 실제 촬영/캘리브레이션용 이미지에서 코너 검출
- "코너 검출 1장만 성공해도" 그 결과로부터
  -> 내부 코너 수(pattern_size) + 한 칸 크기(square_px)를 추정하고
  -> 새로운 체크보드(합성) 이미지를 즉시 생성하여 창으로 띄운다.

주의
- calibrateCamera(진짜 카메라 캘리브레이션)는 원칙적으로 여러 장이 필요
- 하지만 지금 실습 목적은 "패턴 검출 성공 결과로 새 체크보드 생성" 이므로
  calibrateCamera 성공 여부와 무관하게 1장 성공만 해도 합성 체크보드를 만든다.
"""

# ------------------------------------------------------------
# [중요] 상대경로 문제 방지
# ------------------------------------------------------------
from pathlib import Path
import sys
import glob
import cv2
import numpy as np

# =============================================================================
# 0) 실행 옵션
# =============================================================================
ENABLE_GUI = True
# - True  : imshow 창 출력 + 키 입력으로 단계 진행
# - False : 저장 결과로만 확인(헤드리스 환경)

# 합성 이미지 데모(검정/흰색/단색/랜덤/그라데이션/체커보드 등)
RUN_SYNTHETIC_DEMOS = True

# 체크보드 2가지 케이스(일반사진 vs 캘리브레이션용 여러장)
RUN_CHESSBOARD_TWO_CASES = True

# =============================================================================
# 1) 버전 출력 + dtype 별칭(기존 코드에서 dtype=uint8 같은 표현을 살리기 위함)
# =============================================================================
print(f"Python version: {sys.version.split()[0]}")
print(f"OpenCV version: {cv2.__version__}")
print(f"NumPy version : {np.__version__}")

# 기존 코드에서 dtype=uint8 라고 쓰는 부분이 있어 NameError를 막기 위해 별칭 제공
uint8 = np.uint8

# =============================================================================
# 2) 경로 세팅
# =============================================================================
try:
    BASE_DIR = Path(__file__).resolve().parent
except NameError:
    BASE_DIR = Path.cwd()

AI_DIR = BASE_DIR.parent
IMG_DIR = AI_DIR / "images"

# 사용자 환경(윈도우 절대경로 힌트) fallback
WINDOWS_IMG_DIR_HINT = Path(r"C:\Users\baesa\OneDrive\Documents\GitHub\re_4th\AI\images")
if not IMG_DIR.exists() and WINDOWS_IMG_DIR_HINT.exists():
    IMG_DIR = WINDOWS_IMG_DIR_HINT

OUT_DIR = IMG_DIR / "output"
OUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_CALIB_DIR = IMG_DIR / "output_calib_two_cases"
OUT_CALIB_DIR.mkdir(parents=True, exist_ok=True)

print(f"[PATH] BASE_DIR      : {BASE_DIR}")
print(f"[PATH] IMG_DIR       : {IMG_DIR}")
print(f"[PATH] OUT_DIR       : {OUT_DIR}")
print(f"[PATH] OUT_CALIB_DIR : {OUT_CALIB_DIR}")


# =============================================================================
# 3) 유틸 함수(출력/창/패널)
# =============================================================================
def describe_image(tag: str, img: np.ndarray) -> None:
    """이미지 기본 정보 출력: shape/dtype/min/max"""
    if img is None:
        print(f"[{tag}] img=None")
        return
    print(f"\n[{tag}]")
    print(f" shape: {img.shape}")
    print(f" dtype: {img.dtype}")
    print(f" min/max: {img.min()} {img.max()}")


def safe_imread(path: Path, flags=cv2.IMREAD_COLOR) -> np.ndarray:
    """cv2.imread 실패(None) 시 즉시 예외"""
    img = cv2.imread(str(path), flags)
    if img is None:
        raise FileNotFoundError(f"[imread 실패] 파일을 찾을 수 없거나 읽을 수 없습니다: {path}")
    return img


def show_windows(title: str, img: np.ndarray, start_w: int = 1100, start_h: int = 700) -> None:
    """
    AUTOSIZE
    - AUTOSIZE: 보통 창 크기 조절 불가(이미지 크기에 고정)
    """
    if not ENABLE_GUI:
        print(f"[GUI OFF] show_windows skipped: {title}")
        return

    win_auto = f"{title} - AUTOSIZE"

    cv2.namedWindow(win_auto, cv2.WINDOW_AUTOSIZE)

    cv2.imshow(win_auto, img)

    print(" - 아무 키나 누르면 다음 단계로 진행합니다.\n")

    cv2.waitKey(0)
    cv2.destroyWindow(win_auto)

def put_text(img: np.ndarray, text: str, x: int, y: int) -> np.ndarray:
    """패널 라벨용 텍스트 그리기"""
    out = img.copy()
    cv2.putText(out, text, (x, y),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (0, 255, 0), 2, cv2.LINE_AA)
    return out


def make_image_panel(images, labels=None, cols=3, cell_w=520, cell_h=360, pad=10):
    """
    여러 이미지를 한 장(panel)으로 합치는 함수
    - 비교 실습에 매우 유용
    - 이미지 크기를 cell_w/cell_h로 통일해 붙임
    """
    if labels is None:
        labels = [""] * len(images)

    n = len(images)
    if n == 0:
        return None

    rows = (n + cols - 1) // cols
    panel_h = rows * cell_h + (rows + 1) * pad
    panel_w = cols * cell_w + (cols + 1) * pad
    panel = np.zeros((panel_h, panel_w, 3), dtype=np.uint8)

    for i, (img, label) in enumerate(zip(images, labels)):
        r = i // cols
        c = i % cols

        y0 = pad + r * (cell_h + pad)
        x0 = pad + c * (cell_w + pad)

        if img.ndim == 2:
            img_bgr = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        else:
            img_bgr = img

        resized = cv2.resize(img_bgr, (cell_w, cell_h), interpolation=cv2.INTER_AREA)
        if label:
            resized = put_text(resized, label, 10, 30)

        panel[y0:y0 + cell_h, x0:x0 + cell_w] = resized

    return panel


# =============================================================================
# 4) 합성 이미지 생성(체커보드)
# =============================================================================
def make_checkerboard_from_squares(
    num_sq_x: int,
    num_sq_y: int,
    square_px: int,
    margin_px: int = 0,
    invert: bool = False
):
    """
    "사각형 개수(칸 수)" 기준으로 체커보드(체스보드) 생성

    요구사항(중요)
    - margin_px=0이면, 진짜로 '딱 num_sq_x x num_sq_y 칸'만 생성되어야 함
      => 이미지 크기 = (num_sq_y*square_px, num_sq_x*square_px)
    - 기존 구현처럼 margin 영역을 흰색으로 덮는 로직은 margin_px>0일 때만 적용해야 함
      (margin_px=0일 때 -0 == 0 이므로 전체가 덮여버리는 치명적 버그 발생)

    파라미터
    - num_sq_x : 가로 칸 수
    - num_sq_y : 세로 칸 수
    - square_px: 한 칸의 픽셀 크기
    - margin_px: 바깥 여백(픽셀). 0이면 여백 없음(정확히 칸만 생성)
    - invert   : 흑백 반전

    반환
    - board_gray: (H,W) uint8 그레이 이미지 (0 또는 255)
    """

    # ---------------------------------------------------------------------
    # [1] 안전장치: square_px는 최소 1 이상이어야 division//가 의미가 있습니다.
    # ---------------------------------------------------------------------
    square_px = int(square_px)
    if square_px < 1:
        square_px = 1

    # ---------------------------------------------------------------------
    # [2] "칸만" 만들 내부 보드의 기본 크기(여백 제외)
    #     - 여기서 이미 "딱 칸 수만"의 크기가 결정됩니다.
    # ---------------------------------------------------------------------
    inner_w = num_sq_x * square_px
    inner_h = num_sq_y * square_px

    # yy: (H,1), xx: (1,W) 형태로 만들어 브로드캐스팅으로 (H,W) 패턴 생성
    yy = np.arange(inner_h).reshape(-1, 1)
    xx = np.arange(inner_w).reshape(1, -1)

    # (행 index + 열 index)의 parity로 체크 패턴 구성
    board = ((yy // square_px + xx // square_px) % 2).astype(np.uint8) * 255

    if invert:
        board = 255 - board

    # ---------------------------------------------------------------------
    # [3] margin이 필요하면, "흰 배경 캔버스"를 만든 뒤 inner board를 중앙 삽입
    #     - 이 방식이 margin_px=0 버그를 원천적으로 피합니다.
    # ---------------------------------------------------------------------
    margin_px = int(margin_px)
    if margin_px > 0:
        canvas_h = inner_h + 2 * margin_px
        canvas_w = inner_w + 2 * margin_px

        # 캔버스는 흰색(255)
        canvas = np.full((canvas_h, canvas_w), 255, dtype=np.uint8)

        # 중앙에 체커보드 삽입
        canvas[margin_px:margin_px + inner_h, margin_px:margin_px + inner_w] = board
        board = canvas

    return board  # (H,W) gray

def run_synthetic_demos():
    print("\n" + "=" * 80)
    print("[SYNTH] 합성 이미지 데모")
    print("=" * 80)

    # 기본 체커보드(예시)
    chess = make_checkerboard_from_squares(num_sq_x=9, num_sq_y=7, square_px=30, margin_px=25)

    panel = make_image_panel(
        images=[chess],
        labels=[
            "Checkerboard (example)"
        ],
        cols=3, cell_w=460, cell_h=320
    )

    out_panel = OUT_DIR / "synthetic_panel.png"
    cv2.imwrite(str(out_panel), panel)
    print(f"[saved] {out_panel}")

    show_windows("Synthetic Panel", panel, start_w=1300, start_h=850)


# =============================================================================
# 5) 체스보드 코너 검출(1장 성공 시: 그 결과로 "새 체크보드 생성"이 목표)
# =============================================================================
def find_chessboard(gray: np.ndarray, pattern_size: tuple, use_sb: bool = True):
    """
    체스보드 내부 코너 검출
    - pattern_size = (cols, rows) = 내부 코너 수
    """
    if use_sb and hasattr(cv2, "findChessboardCornersSB"):
        ok, corners = cv2.findChessboardCornersSB(
            gray, pattern_size,
            flags=cv2.CALIB_CB_NORMALIZE_IMAGE
        )
        return ok, corners

    flags = cv2.CALIB_CB_ADAPTIVE_THRESH | cv2.CALIB_CB_NORMALIZE_IMAGE | cv2.CALIB_CB_FAST_CHECK
    ok, corners = cv2.findChessboardCorners(gray, pattern_size, flags)
    if not ok:
        return False, None

    # cornerSubPix로 보정(정밀도 향상)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    corners_refined = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
    return True, corners_refined


def draw_corners(img_bgr: np.ndarray, pattern_size: tuple, corners: np.ndarray, ok: bool):
    """코너 시각화"""
    vis = img_bgr.copy()
    cv2.drawChessboardCorners(vis, pattern_size, corners, ok)
    return vis


def estimate_square_px_from_corners(corners: np.ndarray, pattern_size: tuple) -> int:
    """
    (핵심) 코너 검출 1장 성공 결과로부터 "한 칸(square) 픽셀 크기"를 추정

    원리(매우 중요)
    - 내부 코너는 격자 형태로 정렬되어 있음
    - 인접한 코너 간 거리는 대략 "한 칸"에 대응
    - (가로 인접 거리 평균 + 세로 인접 거리 평균)을 이용해 square_px를 추정

    corners 형태:
    - (N,1,2)
    - N = cols*rows
    - 순서는 일반적으로 row-major(위에서 아래로, 좌에서 우로)
    """
    cols, rows = pattern_size
    pts = corners.reshape(-1, 2)  # (N,2)

    # row-major로 배열을 다시 (rows, cols, 2) 형태로 재구성
    grid = pts.reshape(rows, cols, 2)

    # 가로 방향 인접거리(각 row에서 col->col+1)
    h_dists = []
    for r in range(rows):
        for c in range(cols - 1):
            p0 = grid[r, c]
            p1 = grid[r, c + 1]
            h_dists.append(np.linalg.norm(p1 - p0))

    # 세로 방향 인접거리(각 col에서 row->row+1)
    v_dists = []
    for c in range(cols):
        for r in range(rows - 1):
            p0 = grid[r, c]
            p1 = grid[r + 1, c]
            v_dists.append(np.linalg.norm(p1 - p0))

    # 평균값
    h_mean = float(np.mean(h_dists)) if h_dists else 0.0
    v_mean = float(np.mean(v_dists)) if v_dists else 0.0

    # 둘 다 있으면 평균, 하나만 있으면 그것 사용
    if h_mean > 0 and v_mean > 0:
        sq = (h_mean + v_mean) / 2.0
    else:
        sq = max(h_mean, v_mean)

    # 너무 작거나 0이면 안전장치로 기본값
    sq = max(10.0, sq)

    # 실습에서 보기 좋게 약간 반올림
    square_px = int(round(sq))

    print(f"[pattern->square_px] h_mean={h_mean:.2f}, v_mean={v_mean:.2f} => square_px≈{square_px}px")
    return square_px


def generate_checkerboard_from_detection(pattern_size: tuple, square_px: int):
    """
    패턴 검출 결과(pattern_size=내부 코너 수)로부터 "딱 그 칸 수만" 체커보드 생성

    핵심
    - 내부 코너 수 = (cols, rows)
    - 실제 칸 수 = (cols, rows)
    - 생성 이미지 크기 = ( (rows)*square_px, (cols)*square_px )
    - 여백(margin) = 0  (요청사항: 딱 칸만)
    - 이미지 위 텍스트 오버레이도 제거(요청사항 취지: 패턴 그대로)

    반환
    - board_bgr: (H,W,3) BGR 이미지
    """

    cols, rows = pattern_size

    # 내부 코너 -> 칸 수로 변환
    num_sq_x = cols
    num_sq_y = rows

    # 실습용 clamp(너무 작거나 너무 커서 보기 어려운 상황 방지)
    square_px = int(np.clip(int(square_px), 10, 200))

    # 요청사항: "딱 칸 수만" => margin_px=0
    board_gray = make_checkerboard_from_squares(
        num_sq_x=num_sq_x,
        num_sq_y=num_sq_y,
        square_px=square_px,
        margin_px=0,      # ★ 핵심: 여백 제거
        invert=False
    )

    # OpenCV 표시 편의(BGR로 변환)
    board_bgr = cv2.cvtColor(board_gray, cv2.COLOR_GRAY2BGR)

    return board_bgr

# =============================================================================
# 6) 2 CASE 통합(중요: CASE2에서 1장 성공만 해도 즉시 "새 체크보드 생성" 창 출력)
# =============================================================================
def run_chessboard_two_cases():
    # ---------------------------------------
    # CASE 1: checkboard.png (체스말 있는 일반 사진)
    # ---------------------------------------
    print("\n" + "=" * 80)
    print("[CASE 1] checkboard.png (체스말 있는 일반 사진)")
    print("=" * 80)

    case1_path = IMG_DIR / "checkboard.png"
    if not case1_path.exists():
        alt = list(IMG_DIR.glob("check*board*.png"))
        if alt:
            case1_path = alt[0]

    if case1_path.exists():
        case1_bgr = safe_imread(case1_path, cv2.IMREAD_COLOR)
        case1_gray = cv2.cvtColor(case1_bgr, cv2.COLOR_BGR2GRAY)

        describe_image("case1 input bgr", case1_bgr)
        describe_image("case1 input gray", case1_gray)

        # 일반 사진은 실패가 흔하므로, 여기서는 대표 패턴 하나만 시도(로그 일관성)
        pat = (7, 7)
        ok, corners = find_chessboard(case1_gray, pat, use_sb=True)

        if not ok:
            print(f"[CASE1] 원본에서 코너 검출 실패 ({pat[0]}x{pat[1]})")
            print(" - 말 가림/무늬/반사/원근 때문에 실패가 매우 흔합니다.")
            out_fail = OUT_CALIB_DIR / "case1_original_corners.png"
            cv2.imwrite(str(out_fail), case1_bgr)
            print(f"[saved] {out_fail}")
            show_windows("CASE1 - ORIGINAL try", case1_bgr, start_w=1100, start_h=750)
        else:
            vis = draw_corners(case1_bgr, pat, corners, True)
            out_ok = OUT_CALIB_DIR / "case1_original_corners.png"
            cv2.imwrite(str(out_ok), vis)
            print(f"[CASE1] 코너 검출 성공 pattern={pat}")
            print(f"[saved] {out_ok}")
            show_windows("CASE1 - ORIGINAL corners", vis, start_w=1100, start_h=750)
    else:
        print("[CASE1] checkboard.png 파일을 찾지 못했습니다.")
        print(f" - IMG_DIR: {IMG_DIR}")

    # ---------------------------------------
    # CASE 2: checkboard_cali*.png (캘리브레이션/패턴 검출용 여러 장)
    # ---------------------------------------
    print("\n" + "=" * 80)
    print("[CASE 2] checkboard_cali*.png (캘리브레이션/패턴 검출용 여러 장)")
    print("=" * 80)

    cali_paths = sorted([Path(p) for p in glob.glob(str(IMG_DIR / "checkboard_cali*.png"))])
    if len(cali_paths) == 0:
        print("[CASE2] checkboard_cali*.png 파일을 찾지 못했습니다.")
        print(f" - IMG_DIR: {IMG_DIR}")
        return

    print(f"[CASE2] 발견된 이미지 수: {len(cali_paths)}")
    for p in cali_paths:
        print(f" - {p.name}")

    # 후보 pattern_size (내부 코너 수 후보)
    # - 사용자 로그에서 (7,6)이 선택됐던 점을 반영
    CANDIDATE_PATTERN_SIZES = [
        (7, 6), (6, 7),
        (7, 7),
        (8, 6), (6, 8),
        (8, 7), (7, 8),
        (9, 6), (6, 9),
    ]

    # 후보별 성공 개수 집계 + 결과 저장
    pattern_scores = {}
    per_pattern_results = {}

    for pat in CANDIDATE_PATTERN_SIZES:
        results = []
        success = 0

        for p in cali_paths:
            bgr = safe_imread(p, cv2.IMREAD_COLOR)
            gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)

            ok, corners = find_chessboard(gray, pat, use_sb=True)
            results.append((p, ok, corners))
            if ok:
                success += 1

        pattern_scores[pat] = success
        per_pattern_results[pat] = results

    # 가장 성공이 많은 패턴 선택
    best_pattern = max(pattern_scores.items(), key=lambda x: x[1])[0]
    best_success_count = pattern_scores[best_pattern]

    print(f"\n[CASE2] 자동 선택된 pattern_size: {best_pattern} (초기 성공: {best_success_count} 장)")

    # 모든 이미지 결과 패널(OK/FAIL 표시)
    all_vis = []
    all_labels = []
    for p, ok, corners in per_pattern_results[best_pattern]:
        bgr = safe_imread(p, cv2.IMREAD_COLOR)
        if ok:
            vis = draw_corners(bgr, best_pattern, corners, True)
            all_labels.append(f"{p.name} : OK")
        else:
            vis = bgr
            all_labels.append(f"{p.name} : FAIL")
        all_vis.append(vis)

    panel_all = make_image_panel(all_vis, all_labels, cols=3)
    out_all_panel = OUT_CALIB_DIR / "case2_all_images_corners_panel.png"
    cv2.imwrite(str(out_all_panel), panel_all)
    print(f"[saved] {out_all_panel}")
    show_windows("CASE2 - All Images Panel", panel_all, start_w=1300, start_h=850)

    # ------------------------------------------------------------
    # (중요) 1장이라도 성공하면:
    # - 그 성공 이미지(seed)에서 square_px 추정
    # - "그 값으로" 새로운 체크보드(합성) 생성
    # - 즉시 새 창으로 출력
    # ------------------------------------------------------------
    success_items = [(p, corners) for (p, ok, corners) in per_pattern_results[best_pattern] if ok]

    if len(success_items) >= 1:
        seed_path, seed_corners = success_items[0]
        seed_bgr = safe_imread(seed_path, cv2.IMREAD_COLOR)
        seed_gray = cv2.cvtColor(seed_bgr, cv2.COLOR_BGR2GRAY)

        print("\n" + "-" * 80)
        print("[CASE2] 1장 성공 기반: '검출 패턴으로 새 체크보드 생성' 실행")
        print(f" - seed image: {seed_path.name}")
        print(f" - pattern_size(inner corners): {best_pattern}")
        print("-" * 80)

        # (핵심) 성공한 코너에서 한 칸 픽셀 크기 추정
        square_px = estimate_square_px_from_corners(seed_corners, best_pattern)

        # (핵심) 추정값으로 체크보드 합성 생성
        generated_board = generate_checkerboard_from_detection(best_pattern, square_px)

        # 저장 + 창 표시
        out_gen = OUT_CALIB_DIR / f"generated_checkerboard_from_{best_pattern[0]}x{best_pattern[1]}_{square_px}px.png"
        cv2.imwrite(str(out_gen), generated_board)
        print(f"[saved] {out_gen}")

        # 요청사항: "새로운 체크보드 이미지 창 생성"
        show_windows(
            f"GENERATED CHECKERBOARD (from {best_pattern[0]}x{best_pattern[1]} / {square_px}px)",
            generated_board,
            start_w=1100, start_h=750
        )
    else:
        print("\n[CASE2] 선택된 pattern_size에서 성공 이미지가 0장입니다.")
        print(" - 후보 pattern_size를 늘리거나, 이미지 대비/선명도를 개선하세요.")
        return

    # ------------------------------------------------------------
    # 참고:
    # calibrateCamera는 여러 장 필요하므로 여기서는 목적상 강제하지 않음.
    # (원하면 성공 장수가 충분할 때만 별도 섹션으로 추가 가능)
    # ------------------------------------------------------------
    print("\n[CASE2] 현재 실습 목적(패턴 기반 새 체크보드 생성)은 완료되었습니다.")
    print(" - calibrateCamera(진짜 캘리브레이션)는 성공 이미지가 충분할 때 진행하세요.\n")


# =============================================================================
# 7) main
# =============================================================================
def main():
    if RUN_SYNTHETIC_DEMOS:
        run_synthetic_demos()

    if RUN_CHESSBOARD_TWO_CASES:
        run_chessboard_two_cases()

    print("[END] done.")


if __name__ == "__main__":
    main()
