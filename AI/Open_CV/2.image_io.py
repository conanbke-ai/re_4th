"""
2.image_io.py

[파일 개요]
- OpenCV에서 이미지 파일을 읽고(imread), 화면에 출력(imshow)하고,
  키 입력(waitKey)을 통해 창을 제어한 뒤, 다른 이름/형식으로 저장(imwrite)하는 예제.
- 이미지의 크기와 채널 수를 확인하기 위해 shape(높이, 너비, 채널)도 출력한다.

[연결되는 이론 개념]
1) 이미지 읽기 (cv2.imread)
   - 플래그에 따라 컬러/그레이스케일/알파채널 포함 등 다양한 방식으로 로드 가능
   - IMREAD_COLOR      : BGR 3채널 (기본값)
   - IMREAD_GRAYSCALE  : 단일 채널 (0~255 밝기)
   - IMREAD_UNCHANGED  : 원본을 그대로 (알파 채널 포함)

2) 이미지 출력 (cv2.imshow)
   - 지정한 윈도우 이름에 이미지를 띄운다.
   - 실제로 화면에 렌더링되려면 반드시 cv2.waitKey()가 호출되어야 함.

3) 키 입력 대기 (cv2.waitKey)
   - 인자로 ms(밀리초)를 받으며, 그 시간 동안 키 입력 대기.
   - 0이면 무한 대기.
   - 반환값은 눌린 키의 ASCII 코드 (또는 -1).

4) 이미지 저장 (cv2.imwrite)
   - 메모리에 있는 이미지 배열(Numpy 배열)을 디스크에 파일로 저장.
   - 확장자에 따라 JPEG, PNG 등으로 저장 가능.

[사전 준비]
- pip install opencv-python
- AI/Images/sample.jpg 경로에 테스트용 이미지를 하나 두고 실행하면 된다.
"""

import cv2
import os


def load_images_with_flags(img_path: str):
    """
    동일한 이미지 파일을 세 가지 플래그로 읽어서 반환하는 함수.

    Parameters
    ----------
    img_path : str
        읽어올 이미지 파일의 경로.

    Returns
    -------
    img_color : np.ndarray or None
        컬러(BGR)로 로드된 이미지.
    img_gray : np.ndarray or None
        그레이스케일(단일 채널)로 로드된 이미지.
    img_unchanged : np.ndarray or None
        알파 채널 등 원본 정보를 그대로 유지하여 로드된 이미지.
    """
    # 컬러(BGR)로 읽기 - 기본 값
    img_color = cv2.imread(img_path, cv2.IMREAD_COLOR)

    # 그레이스케일(밝기 정보만)로 읽기
    img_gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # 원본 그대로 (알파 채널 포함 등)
    img_unchanged = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

    return img_color, img_gray, img_unchanged


def show_and_print_shapes(img_color, img_gray, img_unchanged):
    """
    세 가지 방식으로 읽어온 이미지의 shape 정보를 출력하고,
    각각을 별도의 윈도우에 띄우는 함수.

    Parameters
    ----------
    img_color, img_gray, img_unchanged : np.ndarray
        load_images_with_flags 함수에서 반환된 이미지들.
    """
    # 각 이미지의 shape 출력
    # 컬러: (높이, 너비, 채널수) / 그레이: (높이, 너비)
    print(f"[INFO] IMREAD_COLOR     shape: {img_color.shape}")
    print(f"[INFO] IMREAD_GRAYSCALE shape: {img_gray.shape}")
    print(f"[INFO] IMREAD_UNCHANGED shape: {img_unchanged.shape}")

    # 각각 다른 이름의 윈도우에 이미지 출력
    cv2.imshow("color", img_color)
    cv2.imshow("gray", img_gray)
    cv2.imshow("unchanged", img_unchanged)

    print("[INFO] 아무 키나 누르면 창이 닫히고, 저장 예제가 실행됩니다.")
    # 0: 키 입력을 무한 대기
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def save_images_example(img_color, img_gray):
    """
    메모리에 로드된 이미지를 다른 형식/이름으로 저장하는 예제.

    Parameters
    ----------
    img_color : np.ndarray
        컬러로 읽어온 원본 이미지.
    img_gray : np.ndarray
        그레이스케일로 변환된 이미지.
    """
    # 출력 폴더 생성 (이미 있으면 그대로 사용)
    os.makedirs("Images/output", exist_ok=True)

    # 저장 경로 설정 (확장자에 따라 포맷이 결정됨)
    color_save_path = "./AI/images/output/sample_color.png"
    gray_save_path = "./AI/images/output/sample_gray.jpg"

    # PNG 형식으로 컬러 이미지 저장
    cv2.imwrite(color_save_path, img_color)
    # JPEG 형식으로 그레이 이미지 저장
    cv2.imwrite(gray_save_path, img_gray)

    print(f"[INFO] 컬러 이미지를 저장했습니다: {color_save_path}")
    print(f"[INFO] 그레이 이미지를 저장했습니다: {gray_save_path}")


if __name__ == "__main__":
    # 테스트에 사용할 이미지 경로
    img_path = "./AI/images/berries.jpg"

    # 다양한 플래그로 이미지 로드
    img_color, img_gray, img_unchanged = load_images_with_flags(img_path)

    # 파일 경로가 잘못되었거나 읽기 권한이 없으면 None이 반환됨
    if img_color is None:
        print(f"[ERROR] 이미지를 찾을 수 없습니다: {img_path}")
    else:
        # shape 출력 + 화면에 보여주기
        show_and_print_shapes(img_color, img_gray, img_unchanged)
        # 다른 이름/형식으로 저장
        save_images_example(img_color, img_gray)

'''
[INFO] IMREAD_COLOR     shape: (427, 640, 3)
[INFO] IMREAD_GRAYSCALE shape: (427, 640)
[INFO] IMREAD_UNCHANGED shape: (427, 640, 3)
[INFO] 아무 키나 누르면 창이 닫히고, 저장 예제가 실행됩니다.
[INFO] 컬러 이미지를 저장했습니다: images/output/sample_color.png
[INFO] 그레이 이미지를 저장했습니다: images/output/sample_gray.jpg
'''