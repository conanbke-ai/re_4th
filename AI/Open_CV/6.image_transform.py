"""
6.image_transform.py

[파일 개요]
- 이미지 크기를 변경(resize)하는 다양한 방법을 실습한다.
- 이미지의 일부분만 잘라내는(crop) 방법을 다룬다.
- 이미지를 상하/좌우로 뒤집는(flip) 방법을 실습한다.
- 이미지 피라미드(pyrDown, pyrUp)를 통해 계층적 해상도 변화를 확인한다.

[연결되는 이론 개념]
1) 크기 변경 (cv2.resize)
   - dsize (너비, 높이)를 명시적으로 지정.
   - 또는 fx, fy 비율로 배율 확대/축소.
   - interpolation 보간법: INTER_NEAREST, INTER_LINEAR, INTER_AREA,
     INTER_CUBIC, INTER_LANCZOS4 등.

2) 잘라내기(Crop)
   - Numpy 슬라이싱: img[y1:y2, x1:x2]
   - 실제로는 새로운 view가 아닌 부분 참조가 될 수 있으므로 주의
     (필요하면 .copy()로 복사).

3) 뒤집기 (cv2.flip)
   - flipCode > 0 : 좌우 반전
   - flipCode = 0 : 상하 반전
   - flipCode < 0 : 상하 + 좌우 반전

4) 이미지 피라미드
   - pyrDown : 가로/세로를 반으로 줄여 해상도 축소.
   - pyrUp   : 가로/세로를 2배로 늘려 해상도 확대.
"""

import cv2


def resize_demo(img):
    """
    다양한 방식의 크기 변경을 수행하고 결과를 보여주는 함수.

    Parameters
    ----------
    img : np.ndarray
        입력 BGR 이미지.
    """
    h, w = img.shape[:2]

    # 1) 절대 크기 지정 (예: 300 x 300)
    #    interpolation=cv2.INTER_LINEAR : 일반적인 보간법 (기본값)
    resized_fixed = cv2.resize(img, (300, 300), interpolation=cv2.INTER_LINEAR)

    # 2) 비율로 크기 지정: 가로/세로 0.5배 축소
    #    INTER_AREA : 축소에 유리한 보간법
    resized_half = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    # 3) 비율로 크기 지정: 1.5배 확대
    #    INTER_CUBIC : 확대 시 비교적 좋은 화질을 제공하지만 계산량이 많음
    resized_1_5 = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

    cv2.imshow("original", img)
    cv2.imshow("resized_fixed_300x300", resized_fixed)
    cv2.imshow("resized_half (0.5x)", resized_half)
    cv2.imshow("resized_1_5 (1.5x)", resized_1_5)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def crop_demo(img):
    """
    이미지의 중앙 부분만 잘라내는(crop) 예제.

    Parameters
    ----------
    img : np.ndarray
        입력 BGR 이미지.

    동작
    ----
    - 전체 이미지에서 중앙 50% 영역을 슬라이싱으로 잘라낸 뒤,
      원본과 함께 비교하여 표시한다.
    """
    h, w = img.shape[:2]

    # 중앙 50% 영역 계산
    y1, y2 = h // 4, h * 3 // 4
    x1, x2 = w // 4, w * 3 // 4

    # Numpy 슬라이싱을 이용해 중앙 영역을 잘라냄
    cropped = img[y1:y2, x1:x2]

    cv2.imshow("original", img)
    cv2.imshow("cropped_center", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def flip_demo(img):
    """
    이미지를 상하/좌우로 뒤집는 예제.

    Parameters
    ----------
    img : np.ndarray
        입력 BGR 이미지.

    flipCode
    --------
    - 1  : 좌우 반전 (왼쪽 ↔ 오른쪽)
    - 0  : 상하 반전 (위 ↔ 아래)
    - -1 : 상하+좌우 반전
    """
    # 좌우 반전
    flip_lr = cv2.flip(img, 1)
    # 상하 반전
    flip_ud = cv2.flip(img, 0)
    # 상하+좌우 반전
    flip_both = cv2.flip(img, -1)

    cv2.imshow("original", img)
    cv2.imshow("flip_lr (left-right)", flip_lr)
    cv2.imshow("flip_ud (up-down)", flip_ud)
    cv2.imshow("flip_both", flip_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def pyramid_demo(img):
    """
    이미지 피라미드를 이용한 해상도 축소/확대 예제.

    Parameters
    ----------
    img : np.ndarray
        입력 BGR 이미지.

    동작
    ----
    - pyrDown : 한 단계 내려가면서 해상도가 1/2로 감소.
    - pyrUp   : 한 단계 올라가면서 해상도가 2배로 증가.
    """
    # 해상도 1/2 축소
    down = cv2.pyrDown(img)
    # 해상도 2배 확대
    up = cv2.pyrUp(img)

    cv2.imshow("original", img)
    cv2.imshow("pyrDown (1/2 size)", down)
    cv2.imshow("pyrUp (2x size)", up)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    img_path = "./AI/images/berries.jpg"
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)

    if img is None:
        print(f"[ERROR] 이미지를 찾을 수 없습니다: {img_path}")
    else:
        # 1) 크기 변경
        resize_demo(img)

        # 2) 중앙 영역 잘라내기
        crop_demo(img)

        # 3) 이미지 뒤집기
        flip_demo(img)

        # 4) 피라미드
        pyramid_demo(img)
