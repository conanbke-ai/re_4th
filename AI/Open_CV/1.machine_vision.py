# 머신 비전
'''
인간이 시각정보를 보고 판단하듯, 컴퓨터는 영상 데이터를 보고 판단
    - 이미지 획득(이미지 센서) → 이미지 분석/이해 → 특정 작업 수행
    
* 비디오 파일이 만들어지는 과정
    이미지 센서가 빛의 양을 감지하여 숫자로 변환
        - 빛의 양 감지 → 전기 신호로 변환 → 디지털화(숫자로 변환)
        
    - 아날로그 : 연속적으로 변화하는 물리량을 표현하는 데 사용하는 용어(연속적)
    - 디지털 : 데이터나 물리적인 양을 0과 1이라는 2진 부호의 숫자로 표현하는 것(불연속적)
    
    * Analogue to Digital 변환
        [아날로그 → 디지털]
        샘플링, 양자화를 거쳐 실제 장면이 픽셀(Pixel) 단위의 숫자로만 이루어진 영상 데이터(2차원 배열)로 변환됨
        
        - 샘플링(Sampling)
            : 특정 주기(Frequency, 가로축)로 아날로그 데이터의 값을 기록
                - 초에 60번 샘플링(Sampling rate): 60Hz(FPS)
                - 샘플링을 더 촘촘하게 할 수록 실제 장면과 가까워짐
        - 양자화(Quantization)
            : 특정 단위(Bite, 세로축)로 아날로그 데이터의 값을 수정
                - 8bit 컬러 = 2의 8승 → 256, 24bit 컬러 = 2의 24승 → 더 자연스러움
                - 양자화를 더 촘촘하게 할 수록 실제 장면과 가까워짐
                
    * 영상 처리 과정
    
    [입력 데이터] 해결하기 원하는 문제에 대한 이미지 또는 영상 입력
         ↓
    [전처리 과정] 각종 필터 및 마스킹을 통한 영상 노이즈 제거
         ↓    
    [특징 검출] 윤곽선, 코너, 특정 색 등 목표한 특징 검출
         ↓    
    [데이터 해석] 검출된 데이터를 기반으로 해석 및 문제 해결
         ↓    
    [출력 데이터] 목표한 최종 데이터 출력
    
'''
'''
* 머신비전 라이브러리
    - OpenCV : 무료, BSD 라이센스, 코드 공개 의무 없음, 상업적 이용 가능
    - Halcon : 유료, 비쌈, 강력한 성능, 다양한 기능, 전문가 우대
    - MIL : 유료, 적당히 비쌈, 국내에서 많이 사용
    - Vision Pro : 유료, 코드 리딩 또는 패턴 매칭에 많이 사용
'''

'''
* Open CV(Open Source Computer Vision Library)
    - Intel에서 최초 개발(1999)
    - 컴퓨터 비전 분야를 발전시키기 위한 목적
    - C/C++, C#, Python, Java 지원
    - 500가지가 넘는 영상 처리 알고리즘이 최적화 되어있음
    - GPU 가속 모듈 지원
    - 머신러닝과 관련된 모듈 포함
    
    - 공식 홈페이지 : https://opencv.org/
    - 파이썬 튜토리얼 : https://docs.opencv.org/4.10.0/d6/d00/tutorial_py_root.html
    
    - 설치 방법 : pip install opencv-python
    - 불러오기 : import cv2 as cv
'''
import cv2

##### 1. 이미지를 불러서 창으로 띄우는 작업

### 1-1 imread(이미지경로): 이미지 반환(numpy)
blackberries = cv2.imread("./AI/images/blackberries.jpg")
blueberries = cv2.imread("./AI/images/blueberries.jpg", cv2.IMREAD_GRAYSCALE)
# print("img:", img) # numpy 배열 출력


### 1-2 imshow(윈도우이름, 읽어온이미지): 이미지를 새창으로 열어주는 함수
cv2.imshow("blackberries image", blackberries)
cv2.imshow("blueberries image grayscale", blueberries)

### 1-3 waitKey(밀리초): ASCII CODE 반환
# 윈도우가 시간초만큼 대기후에 종료된다.
# waitKey가 없다면 윈도우가 대기하지 않고 바로 꺼진다.
key=cv2.waitKey(0) # 0은 무한대기
print("key", key)

changeToChar = chr(key)
changToASCII = ord(changeToChar)
print(f"문자: {changeToChar}, ASCII CODE: {changToASCII}")


cv2.destroyAllWindows()

##### 2. 이미지 저장, shape 속성 확인
strawberries = cv2.imread("./AI/images/strawberries.jpg", cv2.IMREAD_COLOR)
strawberries_gray = cv2.imread("./AI/images/strawberries.jpg", cv2.IMREAD_GRAYSCALE)

### 2-1 shape 속성: 세로, 가로, (채널값)을 튜플형태로 반환
# grayscale 사진일 경우, 채널 값이 없음
print("color strawberries image shape", strawberries.shape) # (427, 640, 3)
print("gray strawberries image shape", strawberries_gray.shape) # (427, 640)

cv2.imshow("cute strawberries color", strawberries)
cv2.imshow("cute strawberries_gray gray", strawberries_gray)


h2, w2, c2 = strawberries.shape
print("color height", h2)
print("color width", w2)
print("color channel", c2)

h3, w3 = strawberries.shape[:2]
print("color height3", h3)
print("color width3", w3)

h1, w1 = strawberries_gray.shape
print("gray height", h1)
print("gray width", w1)

cv2.waitKey(0)
cv2.destroyAllWindows()

## imwrite("저장할 경로명", 저장할이미지)
cv2.imwrite("./AI/images/output/strawberries_gray.png", strawberries_gray)

'''
key 98
문자: b, ASCII CODE: 98
color strawberries image shape (427, 640, 3)
gray strawberries image shape (427, 640)
color height 427
color width 640
color channel 3
color height3 427
color width3 640
gray height 427
gray width 640
'''