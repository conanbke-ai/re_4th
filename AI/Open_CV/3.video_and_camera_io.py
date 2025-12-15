"""
3.video_and_camera_io.py

[파일 개요]
- 동영상 파일을 읽어서 프레임 단위로 재생하는 예제.
- 웹캠(카메라)에서 실시간 영상을 받아 화면에 출력하는 예제.
- 웹캠에서 읽은 영상을 일정 시간 동안 녹화하여 파일로 저장하는 예제.

[연결되는 이론 개념]
1) 비디오 캡처 객체 (cv2.VideoCapture)
   - 파일 경로 또는 카메라 인덱스를 인자로 전달.
   - cap.read()를 통해 연속된 프레임을 하나씩 읽어옴.
   - isOpened()로 열렸는지 여부를 확인.

2) 프레임 속성 (cap.get)
   - CAP_PROP_FPS          : 초당 프레임 수
   - CAP_PROP_FRAME_COUNT  : 전체 프레임 수
   - CAP_PROP_FRAME_WIDTH  : 프레임 너비
   - CAP_PROP_FRAME_HEIGHT : 프레임 높이

3) 비디오 저장 (cv2.VideoWriter)
   - VideoWriter_fourcc 를 이용해 코덱 지정 (예: 'DIVX', 'XVID' 등)
   - (파일 경로, fourcc, fps, frame_size)를 지정해 객체 생성.
   - out.write(frame)으로 프레임을 차례대로 기록.

4) 키 입력 제어 (waitKey)
   - 'q' 키 등 특정 키를 눌러 재생/녹화 중단.

[사전 준비]
- AI/videos/sample.mp4 에 테스트용 동영상 파일이 있다고 가정.
- 카메라 장치가 연결되어 있고, device_index=0 이 기본 웹캠이라고 가정.
"""

### cap.isOpened(): bool
# 정상적으로 파일이 열렸는지, 카메라 사용시 카메라가 연결됐는지 확인

### cap.read(): (ret, frame) 값을 반환
# ret: bool, 프레임을 정상적으로 읽었는지 반환
# frame: numpy, 읽어온 영상의 프레임 하나, ret 이 false라면 None
# frame 은 image 데이터이기 때문에 cv2.imshow()를 통해 화면에 보여줄 수 있음

### cap.release(): 영상 재생이 끝나고 메모리, 카메라 점유등 자원을 반납

import cv2
import os


def play_video_file(video_path: str):
    """
    동영상 파일을 프레임 단위로 읽어서 재생하는 함수.

    Parameters
    ----------
    video_path : str
        재생할 비디오 파일 경로.

    동작
    ----
    - VideoCapture로 비디오 파일을 연다.
    - FPS와 총 프레임 수를 출력해 정보 확인.
    - 루프를 돌면서 매 프레임을 읽어 화면에 보여준다.
    - 'q' 키를 누르면 재생을 중단한다.
    """
    cap = cv2.VideoCapture(video_path)
    
    ### cap.get(int 속성의ID>cv2.[정해진상수])
    print("- CAP_PROP_FRAME_WIDTH:",  cap.get(cv2.CAP_PROP_FRAME_WIDTH))   # 예: 1280.0
    print("- CAP_PROP_FRAME_HEIGHT:", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 예: 720.0
    print("- CAP_PROP_FPS:",          cap.get(cv2.CAP_PROP_FPS))           # 예: 25.0
    print("- CAP_PROP_FRAME_COUNT:",  cap.get(cv2.CAP_PROP_FRAME_COUNT))   # 예: 411.0
    print("- CAP_PROP_POS_FRAMES:",   cap.get(cv2.CAP_PROP_POS_FRAMES))    # 예: 0.0

    # 비디오 파일이 정상적으로 열렸는지 확인
    if not cap.isOpened():
        print(f"[ERROR] 비디오를 열 수 없습니다: {video_path}")
        return

    # FPS와 총 프레임 수 확인 (정보용)
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    print(f"[INFO] FPS: {fps}, 총 프레임 수: {total_frames}")

    # FPS가 0이면 (정보를 못 가져왔을 때) 기본 딜레이 30ms 사용
    delay = int(1000 / fps) if fps > 0 else 30

    while True:
        # ret: 프레임 읽기 성공 여부, frame: 실제 이미지 데이터
        ret, frame = cap.read()

        if not ret:
            print("[INFO] 영상 재생이 끝났거나 프레임을 읽지 못했습니다.")
            break

        # 읽어온 프레임을 화면에 출력
        cv2.imshow("video_playback", frame)

        # delay ms 동안 키 입력 대기, 'q' 키를 누르면 재생 종료
        key = cv2.waitKey(delay) & 0xFF
        if key == ord("q"):
            print("[INFO] 사용자 입력(q)로 영상 재생을 종료합니다.")
            break

    # 비디오 캡처 자원 해제, 창 닫기
    cap.release()
    cv2.destroyAllWindows()


def camera_preview_and_capture(device_index: int = 0):
    """
    웹캠(카메라)로부터 실시간 영상을 받아 프리뷰 화면을 보여주고,
    'c' 키를 누를 때마다 현재 프레임을 이미지 파일로 저장하는 함수.

    Parameters
    ----------
    device_index : int, optional
        사용할 카메라 장치 번호 (기본값 0).

    저장 경로
    --------
    - 캡처 이미지는 ./AI/images/capture/ 하위에 순차적으로 저장된다.
    """
    cap = cv2.VideoCapture(device_index)

    if not cap.isOpened():
        print(f"[ERROR] 카메라를 열 수 없습니다. device_index={device_index}")
        return

    # 카메라 해상도 설정 (예: 640x480)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # 캡처 이미지를 저장할 폴더 생성
    os.makedirs("./AI/images/capture", exist_ok=True)
    capture_count = 0

    print("[INFO] 카메라 미리보기를 시작합니다. 'c' 키로 캡처, 'q' 키로 종료.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] 카메라 프레임을 읽지 못했습니다.")
            break

        # 현재 프레임을 화면에 표시
        cv2.imshow("camera_preview", frame)
        key = cv2.waitKey(10) & 0xFF

        if key == ord("c"):
            # 현재 프레임을 파일로 저장
            save_path = f"./AI/images/capture/capture_{capture_count:03d}.jpg"
            cv2.imwrite(save_path, frame)
            print(f"[INFO] 캡처 저장: {save_path}")
            capture_count += 1
        elif key == ord("q"):
            print("[INFO] 사용자 입력(q)로 카메라 미리보기를 종료합니다.")
            break

    cap.release()
    cv2.destroyAllWindows()


def record_video_from_camera(device_index: int = 0, duration_sec: int = 5):
    """
    웹캠에서 일정 시간 동안 영상을 받아 비디오 파일로 저장하는 예제.

    Parameters
    ----------
    device_index : int, optional
        사용할 카메라 장치 번호 (기본값 0).
    duration_sec : int, optional
        녹화할 시간(초 단위).

    저장 경로
    --------
    - 녹화된 비디오는 videos/output/camera_record.avi 로 저장된다.
    """
    cap = cv2.VideoCapture(device_index)

    if not cap.isOpened():
        print(f"[ERROR] 카메라를 열 수 없습니다. device_index={device_index}")
        return

    # 카메라에서 FPS 정보를 가져옴 (일부 장치는 0 또는 부정확할 수 있음)
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        fps = 30  # 정보가 없으면 기본값 30 FPS 사용

    # 프레임 크기 (너비, 높이)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    size = (width, height)

    print(f"[INFO] 카메라 정보 - size: {size}, fps: {fps}")

    # 출력 폴더 생성
    os.makedirs("./AI/videos/output", exist_ok=True)
    output_path = "./AI/videos/output/camera_record.avi"

    # 비디오 코덱 설정 (여기서는 DIVX 예시)
    fourcc = cv2.VideoWriter_fourcc(*"DIVX")
    out = cv2.VideoWriter(output_path, fourcc, fps, size)

    # 녹화할 총 프레임 수 (fps * 녹화시간)
    frame_limit = int(fps * duration_sec)
    frame_count = 0

    print(f"[INFO] {duration_sec}초 동안 녹화를 시작합니다. (약 {frame_limit} 프레임)")

    while frame_count < frame_limit:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] 카메라 프레임을 읽지 못했습니다.")
            break

        # 파일에 현재 프레임 기록
        out.write(frame)
        # 녹화 중인 화면을 프리뷰로 출력
        cv2.imshow("recording", frame)
        frame_count += 1

        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("[INFO] 사용자 입력(q)로 녹화를 조기 종료합니다.")
            break

    print(f"[INFO] 녹화 종료. 저장 파일: {output_path}")

    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # 1) 영상 파일 재생 예제
    # play_video_file("./AI/videos/dog.mp4")

    # 2) 웹캠 미리보기 + 캡처 예제
    camera_preview_and_capture(device_index=0)

    # 3) 웹캠 녹화 예제
    # record_video_from_camera(device_index=0, duration_sec=5)/

'''
1) 영상 파일 재생 예제

- CAP_PROP_FRAME_WIDTH: 1280.0
- CAP_PROP_FRAME_HEIGHT: 720.0
- CAP_PROP_FPS: 25.0
- CAP_PROP_FRAME_COUNT: 411.0
- CAP_PROP_POS_FRAMES: 0.0
[INFO] FPS: 25.0, 총 프레임 수: 411.0
[INFO] 사용자 입력(q)로 영상 재생을 종료합니다. or [INFO] 영상 재생이 끝났거나 프레임을 읽지 못했습니다.
'''
'''
2) 웹캠 미리보기 + 캡처 예제

[INFO] 카메라 미리보기를 시작합니다. 'c' 키로 캡처, 'q' 키로 종료.
[INFO] 캡처 저장: ./AI/images/capture/capture_000.jpg
[INFO] 캡처 저장: ./AI/images/capture/capture_001.jpg
[INFO] 사용자 입력(q)로 카메라 미리보기를 종료합니다.
'''
'''
3) 웹캠 녹화 예제

[INFO] 카메라 정보 - size: (640, 480), fps: 30.0
[INFO] 5초 동안 녹화를 시작합니다. (약 150 프레임)
[INFO] 녹화 종료. 저장 파일: ./AI/videos/output/camera_record.avi
'''