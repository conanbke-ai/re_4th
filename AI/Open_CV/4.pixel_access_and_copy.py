"""
4.pixel_access_and_copy.py

[파일 개요]
- 이미지에서 특정 픽셀의 값을 읽고/수정하는 방법을 다룬다.
- Numpy 배열을 이용해 새로운 이미지를 직접 생성하는 방법을 보여준다.
- 얕은 복사(shallow copy)와 깊은 복사(deep copy)의 차이를 시각적으로 확인한다.

[연결되는 이론 개념]
1) 픽셀 단위 접근
   - img[y, x] 로 (y행, x열)의 픽셀에 접근 (주의: (x, y)가 아니라 (y, x)).
   - 컬러 이미지(BGR)에서는 img[y, x]가 [B, G, R] 형태의 배열.

2) Numpy 배열로 이미지 생성
   - np.zeros((높이, 너비, 채널), dtype=np.uint8) 로 검정색(0) 이미지 생성.
   - 특정 영역에 값을 할당하여 직사각형, 선 등을 표현 가능.

3) 얕은 복사 vs 깊은 복사
   - 얕은 복사: 같은 메모리 공유 → 원본/복사본 중 하나를 수정하면 둘 다 바뀜.
   - 깊은 복사: 메모리 완전 복제 → 서로 독립적으로 수정 가능.
"""

import cv2
import numpy as np


def create_black_image():
    """
    검정색 배경의 이미지를 생성하고, 특정 영역에 색을 칠하는 예제.

    Returns
    -------
    img : np.ndarray
        - 크기: 480 x 640
        - 채널: 3 (B, G, R)
        - 초기값: 0 (검정색)
        - 왼쪽 상단 일부 영역에 파란색 직사각형이 칠해져 있음.
    """
    # 높이 480, 너비 640, 채널 3 (BGR), 값 범위 0~255
    img = np.zeros((480, 640, 3), dtype=np.uint8)

    # [y1:y2, x1:x2] 영역에 파란색(B=255, G=0, R=0)으로 채우기
    img[50:150, 50:200] = (255, 0, 0)

    return img


def pixel_read_write_example(img):
    """
    이미지의 중앙 픽셀 색상 값을 읽어서 출력하고,
    주변 픽셀을 빨간색으로 칠하는 예제.

    Parameters
    ----------
    img : np.ndarray
        BGR 컬러 이미지.
    """
    h, w = img.shape[:2]
    # 중심 좌표 (y, x)
    center_y, center_x = h // 2, w // 2

    # (center_y, center_x)에 해당하는 BGR 값 읽기
    b, g, r = img[center_y, center_x]
    print(f"[INFO] 중심 픽셀 BGR 값: ({b}, {g}, {r})")

    # 중심 주변 5x5 영역을 빨간색(0,0,255)으로 칠하기
    img[center_y - 2:center_y + 3, center_x - 2:center_x + 3] = (0, 0, 255)


def shallow_vs_deep_copy(img):
    """
    얕은 복사와 깊은 복사의 차이를 시각적으로 확인하는 예제.

    Parameters
    ----------
    img : np.ndarray
        원본 BGR 이미지.

    과정
    ----
    1) shallow_copy = img  : 같은 메모리를 가리키는 얕은 복사
    2) deep_copy = img.copy() : 별도의 메모리에 복사된 깊은 복사
    3) 원본/얕은 복사 이미지에 초록색 사각형을 그리면,
       shallow_copy에도 동일한 변화가 반영됨.
    4) 깊은 복사 이미지에 파란색 사각형을 그리면,
       원본/얕은 복사에는 영향을 주지 않음.
    """
    # 얕은 복사: 실제로는 같은 Numpy 배열을 가리킴
    shallow_copy = img
    # 깊은 복사: 완전 복제된 별도의 배열
    deep_copy = img.copy()

    h, w = img.shape[:2]

    # 원본+shallow_copy에 초록색 사각형 (0,255,0)
    img[h // 4:h // 2, w // 4:w // 2] = (0, 255, 0)

    # deep_copy에는 파란색 사각형 (255,0,0)
    deep_copy[h // 4:h // 2, w // 2:w * 3 // 4] = (255, 0, 0)

    # 원본(=shallow_copy)와 deep_copy를 각각 보여주기
    cv2.imshow("original_and_shallow (green)", img)
    cv2.imshow("deep_copy (blue)", deep_copy)

    print("[INFO] 초록 사각형: 원본+shallow, 파란 사각형: deep copy")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # 1) 검정 바탕 이미지를 만들어 픽셀 조작 예제 수행
    base_img = create_black_image()
    pixel_read_write_example(base_img)
    cv2.imshow("pixel_edit", base_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 2) 실제 이미지 파일을 읽어서 shallow/deep copy 비교
    img_path = "./AI/images/berries.jpg"
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)

    if img is None:
        print(f"[ERROR] 이미지를 찾을 수 없습니다: {img_path}")
    else:
        shallow_vs_deep_copy(img)

'''
[INFO] 중심 픽셀 BGR 값: (0, 0, 0)
[INFO] 초록 사각형: 원본+shallow, 파란 사각형: deep copy
'''