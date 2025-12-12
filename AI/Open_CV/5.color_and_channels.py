"""
5.color_and_channels.py

[파일 개요]
- BGR, RGB, GRAY 등 색 공간 변환을 실습한다.
- 채널 분리(split) / 합치기(merge) 예제를 통해 B, G, R 채널이
  어떻게 구성되는지 시각적으로 확인한다.

[연결되는 이론 개념]
1) 색 공간(Color Space)
   - BGR : OpenCV 기본 컬러 순서 (Blue, Green, Red)
   - RGB : 일반적으로 많이 사용하는 순서 (Red, Green, Blue)
   - GRAY : 색상 정보가 없는 단일 채널 밝기 이미지

2) 색 공간 변환 (cv2.cvtColor)
   - COLOR_BGR2GRAY : 컬러 → 그레이스케일
   - COLOR_BGR2RGB  : BGR → RGB로 채널 순서를 변경

3) 채널 분리 / 합치기
   - cv2.split(img) : 다채널 이미지를 (B, G, R) 채널로 분리
   - cv2.merge([B, G, R]) : 단일 채널 여러 개를 다시 합쳐서 컬러 이미지로 구성
"""

import cv2
import numpy as np


def color_space_demo(img_path: str):
    """
    BGR 이미지를 GRAY와 RGB로 변환하여 비교하는 함수.

    Parameters
    ----------
    img_path : str
        입력 이미지 경로.
    """
    # BGR 컬러로 이미지 읽기
    img_bgr = cv2.imread(img_path, cv2.IMREAD_COLOR)
    if img_bgr is None:
        print(f"[ERROR] 이미지를 찾을 수 없습니다: {img_path}")
        return

    # BGR → GRAY(밝기 정보만 남긴 단일 채널)
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    # BGR → RGB (채널 순서 변경)
    # OpenCV는 내부적으로 BGR 기준이므로, 다른 라이브러리(matplotlib 등)와
    # 연동할 때 색이 뒤바뀌지 않게 하려면 RGB로 바꿔서 사용하는 경우가 많다.
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    cv2.imshow("BGR (original)", img_bgr)
    cv2.imshow("GRAY", img_gray)
    cv2.imshow("RGB (converted)", img_rgb)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def split_merge_demo(img_path: str):
    """
    BGR 이미지를 채널별로 분리한 뒤, 각 채널을 시각화하고,
    다시 합치는 예제.

    Parameters
    ----------
    img_path : str
        입력 이미지 경로.
    """
    img_bgr = cv2.imread(img_path, cv2.IMREAD_COLOR)
    if img_bgr is None:
        print(f"[ERROR] 이미지를 찾을 수 없습니다: {img_path}")
        return

    # 채널 분리: B, G, R 각각은 단일 채널(2D) 이미지가 됨.
    b, g, r = cv2.split(img_bgr)

    # 각 채널만 강조해서 보여주기 위해,
    # 다른 채널은 0(검정)으로 채운 뒤 merge.
    zeros = np.zeros_like(b)

    # Blue만 보이도록 (B, 0, 0)
    img_b = cv2.merge([b, zeros, zeros])
    # Green만 보이도록 (0, G, 0)
    img_g = cv2.merge([zeros, g, zeros])
    # Red만 보이도록 (0, 0, R)
    img_r = cv2.merge([zeros, zeros, r])

    cv2.imshow("original BGR", img_bgr)
    cv2.imshow("Blue channel", img_b)
    cv2.imshow("Green channel", img_g)
    cv2.imshow("Red channel", img_r)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 채널 순서를 바꾸어 merge(R, G, B)하면,
    # 사실상 RGB처럼 보이는 이미지가 된다.
    img_rgb_like = cv2.merge([r, g, b])
    cv2.imshow("Reordered channels (R,G,B)", img_rgb_like)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    img_path = "./AI/images/berries.jpg"

    # 색 공간 변환 데모
    color_space_demo(img_path)

    # 채널 분리/합치기 데모
    split_merge_demo(img_path)
