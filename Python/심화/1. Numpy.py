# NumPy
# python -m venv 폴더이름
# python -m venv venv

'''
- NumPy 공식 홈페이지: https://numpy.org/
- 공식 튜토리얼: https://numpy.org/doc/stable/user/quickstart.html
'''
'''
* 행렬
    숫자나 수식을 가로줄(행)과 세로줄(열)로 배열한 2차원 구조의 수학적 객체
    
    ex)
            제 1열  제 2열  제 3열
    제 1행     1       2      3
    제 2행     4       5      6
    
    → 2 X 3 또는 2행 3열의 행렬
'''
'''
다차원 배열(행렬)을 쉽게 처리하고 효율적으로 사용할 수 있도록 지원하는 파이썬의 라이브러리
    - Numpy : Numerical Python 의 약자
    - 수치해석, 통계 관련 기능을 구현한다고 할 때 가장 기본이 되는 모듈

* 파이썬 리스트의 한계와 Numpy
    - Numpy 배열은 내부적으로 C언어 기반의 연속된 메모리 블록을 사용 → 빠른 계산 가능
    - Python 리스트는 각각의 요소가 포인터로 연결된 객체이기 때문에 비효율적
    - 브로드캐스팅, 벡터 연산 등을 통해 for 루프 없이도 대량의 계산 처리

* 활용 분야
    과학 계산, 데이터 분석, 인공지능, 통계, 신호 처리, 이미지 처리, 시뮬레이션, 금융공학 등
        ex) Pandas, SciPy, scikit-learn, TensorFlow 등 다양한 파이썬 데이터/AI 생태계의 기반
        
    - 대용량 데이터의 통계 분석 및 행렬 연산
    - 선형대수 계산(벡터/행렬 곱)
    - 난수 생성, 수학 함수 적용
    - 이미지 데이터(픽셀 배열) 처리 등
'''
'''
* 주요 특징:
1. 다차원 배열 객체 (ndarray)
2. 빠른 연산 속도
3. 메모리 효율성
4. 벡터화 연산 지원
5. 선형대수, 푸리에 변환, 난수 생성 등 다양한 수학 함수 제공
6. NumPy는 다양한 데이터 타입을 지원
    - 정수형: int8, int16, int32, int64
    - 부동소수점: float16, float32, float64
    - 복소수: complex64, complex128
    - 불린: bool
    - 문자열: string_, unicode_
'''
print('=== 정수 배열 ===')
int_array = np.array([1, 2, 3, 4, 5])
print('정수 배열:', int_array)
print('데이터 타입:', int_array.dtype)  # int64 (시스템에 따라 다를 수 있음)
print()

print('=== 실수 배열 ===')
"""
실수가 하나라도 포함되면 전체가 실수형으로 변환됩니다.
"""
float_array = np.array([1.1, 2.2, 3.3, 4.4, 5])
print('실수 배열:', float_array)
print('데이터 타입:', float_array.dtype)  # float64
print()

print('=== 명시적 타입 지정 ===')
"""
dtype 매개변수로 원하는 데이터 타입을 명시적으로 지정할 수 있습니다.
장점:
- 메모리 절약 (float32는 float64의 절반 메모리 사용)
- 호환성 (특정 라이브러리나 하드웨어 요구사항 충족)
"""
specified_array = np.array(['1', '2', 3, 4, 5], dtype=np.float32)
print('명시적 배열:', specified_array)
print('데이터 타입:', specified_array.dtype)  # float32
print()

print('=== 문자열 배열 ===')
"""
<U10 의미:
- <: little-endian (바이트 순서)
- U: 유니코드 문자열
- 10: 최대 문자 길이
"""
string_array = np.array(['apple', 'banana', 'cherry'])
print('문자열 배열:', string_array)
print('데이터 타입:', string_array.dtype)  # <U6 (가장 긴 문자열 기준)
print()

'''
* Numpy 사용 이유

문제점: 파이썬은 인터프리터 언어로 실행속도가 느립니다.

해결책 1 - 속도 개선:
- NumPy는 C언어로 구현되어 있어 대용량 데이터 연산을 매우 빠르게 처리
- 일반 파이썬 리스트보다 10~100배 이상 빠름

해결책 2 - 메모리 효율성:
- 파이썬 리스트: 각 요소가 객체로 저장되어 메모리 오버헤드가 큼
  예) [1, 2, 3] → 각 숫자가 별도의 파이썬 객체로 저장
- NumPy 배열: 연속된 메모리 공간에 같은 타입의 데이터를 저장
  예) array([1, 2, 3]) → 연속된 메모리에 정수만 저장

해결책 3 - 벡터화 연산:
- 반복문 없이 전체 배열에 대한 연산을 한번에 수행
- 코드가 간결하고 가독성이 좋음
'''
'''
* 설치 및 기본 사용법
    - pip install numpy
    - conda환경에서
        conda install numpy

* import
    import numpy as np  # Numpy를 np라는 별칭(alias)로 임포트
'''

# 사용 예제 - 배열 생성
import numpy as np
print('Numpy 버전:', np.__version__)
print('Numpy 설치 경로:', np.__file__)

# 리스트를 Numpy 배열로 변환
arr = np.array([1, 2, 3, 4, 5])
print(arr)  # [1 2 3 4 5]
print(type(arr))    # <class 'numpy.ndarray'>

'- np.array() : 파이썬 리스트나 튜플을 Numpy 배열로 변환'

'''
* ndarray
    Numpy의 핵심 데이터 구조, 동일한 자료형(같은 타입)을 가진 다차원 배열
        - Python의 리스트보다 성능과 메모리 효율성에서 우수
        - 고정된 크기의 동질적인(homogeneous) 배열
* 핵심 속성:
- dtype: 배열 요소의 데이터 타입
- shape: 배열의 형태 (각 차원의 크기)
- ndim: 배열의 차원 수
- size: 배열의 전체 요소 개수
- itemsize: 각 요소의 바이트 크기
'''
'''
* Python vs Numpy

- 차이점 1: 타입 고정성
    파이썬 리스트:
    - 서로 다른 타입의 요소를 담을 수 있음 (이질적)
    - 각 요소가 독립적인 파이썬 객체
    - 유연하지만 메모리와 속도 측면에서 비효율적

    NumPy 배열:
    - 모든 요소가 같은 타입이어야 함 (동질적)
    - 다른 타입이 섞이면 자동으로 상위 타입으로 변환
    - 변환 우선순위: bool < int < float < complex < string
'''
python_list = [1, 2.5, '3', True]  # 다양한 타입 가능
numpy_array = np.array([1, 2, 3, True])  # True는 1로 변환됨
print('파이썬 리스트:', python_list)
print('Numpy 배열:', numpy_array)  # [1 2 3 1] - 모두 정수로 통일
'''
- 차이점 2: 연산 방식
    파이썬 리스트 + 연산:
    - 리스트 연결(concatenation)
    - [1,2,3] + [4,5,6] = [1,2,3,4,5,6]

    NumPy 배열 + 연산:
    - 요소별(element-wise) 연산
    - [1,2,3] + [4,5,6] = [5,7,9]
    - 벡터화 연산으로 매우 빠름
'''
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print('리스트 더하기:', list1 + list2)  # [1, 2, 3, 4, 5, 6] - 연결

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print('Numpy 배열 더하기:', arr1 + arr2)  # [5 7 9] - 요소별 덧셈
'''     
* Python list vs Numpy ndarray
- Python list
    - 다양한 자료형을 담을 수 있는 가변 길이의 시퀀스 자료형
    - 1차원부터 n차원까지 중첩 리스트로 표현 가능하지만, 명시적인 다차원 구조는 없음
- Numpy ndarray
    - 동일한 자료의 데이터를 정해진 크기의 다차원 배열로 저장
    - 수치 계산에 최적화된 자료구조이며, 내부적으로 C언어 기반의 연속 메모리 구조 사용
    
    1. 자료형 차이
        - [list]    : 원소로 여러가지 자료형 허용
        - [Ndarray] : 원소로 한 가지 자료형만 허용
    2. 내부 배열의 원소 개수
        - [list]    : 내부 배월의 원소 개수가 달라도 됨
        - [Ndarray] : 내부 배열의 원소 개수가 같아야 함
    3. 연산의 차이
        - [list]    : 빼기, 곱하기, 나누니 연산 불가
        - [Ndarray] : 산술 연산 - 같은 위치의 원소끼리 연산
'''

# 1. 자료형 차이
a = [1, 2, 'a', 'b']
b = np.array([1, 2, 'a', 'b'])
print(a)    # [1, 2, 'a', 'b']
print(b)    # ['1', '2', 'a', 'b']

# 2. 내부 배열의 원소 개수
e = np.array([[1, 2], [3, 4], [5, 6]])
print(e)    # [[1 2]
            #  [3 4]
            #  [5 6]
            
# 3. 연산의 차이
# list
list1 = [1, 3, 5]
list2 = [2, 4, 6]
print(list1 + list2)    # [1, 3, 5, 2, 4, 6]

# Ndarray
ndarray1 = np.array([1, 3, 5])
ndarray2 = np.array([2, 4, 6])
print(ndarray1 + ndarray2)  # array([3, 7, 11])

ndarray3 = np.array([1, 3, 5, 7])
print(ndarray1 + ndarray3)  # 오류 발생(배열의 개수가 다를 경우 오류 발생)

print('=== ndarray 기본 속성 ===')
print('1. 객체 타입:', type(arr))  # <class 'numpy.ndarray'>
print('2. 데이터 타입:', arr.dtype)  # int64 (64비트 정수)
print('3. 배열 모양:', arr.shape)  # (5,) - 1차원 배열, 5개 요소
print('4. 차원 수:', arr.ndim)  # 1 - 1차원
print('5. 전체 요소 수:', arr.size)  # 5개

'''
차원(Dimension)과 축(Axis)
    - 차원(Dimension) : 배열이 몇 단계로 중첩되어 있는지 나타냄
        - 1D : [1, 2, 3]
        - 2D : [[1, 2], [3, 4]]
        - 3D : [[[1], [2]], [[3], [4]]]
    - 축(Axis) : 다차원 배열의 특정 방향을 의미함
        - axis=0 : 행 방향(세로 축)
        - axis=1 : 열 방향(가로 축)
'''
'- .shape : 배열의 구조를 튜플로 반환'
'- .ndim : 배열의 차원 수'
'''
- 1차원 배열: 벡터 (vector)
- 2차원 배열: 행렬 (matrix)
    행렬 표현:
    [1, 2, 3]
    [2, 3, 4]
    [4, 5, 6]

    shape (3, 3) 의미:
    - 첫 번째 3: 행(row)의 개수
    - 두 번째 3: 열(column)의 개수
- 3차원 배열: 텐서 (tensor)
    - 여러 개의 2차원 행렬을 쌓은 형태
    - 이미지 처리: (높이, 너비, 색상채널)
    - 동영상 처리: (프레임, 높이, 너비)
    - 딥러닝: (배치크기, 높이, 너비)

    shape (2, 3, 4) 의미:
    - 2: 2개의 행렬
    - 3: 각 행렬은 3행
    - 4: 각 행렬은 4열
- 4차원 이상: 고차원 텐서
'''
# matrix(행렬)
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)  # (2, 3) → 2행 3열
print(a.ndim)   # 2차원

matrix = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [4, 5, 6]
])
print('2차원 배열:\n', matrix)
print('모양:', matrix.shape)  # (3, 3) - 3행 3열
print('차원:', matrix.ndim)  # 2 - 2차원
print('크기:', matrix.size)  # 9 - 총 9개 요소

# 반복문으로 배열 생성
rows = []
for i in range(3):
    row = [i * 3 + j for j in range(4)]  # [0, 1, 2, 3], [3, 4, 5, 6], ...
    rows.append(row)

matrix2 = np.array(rows)
print('동적 생성 행렬:\n', matrix2)

# tensor 텐서
tensor = np.array([
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ],
    [
        [13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24],
    ],
])

print('3차원 배열 모양:', tensor.shape)  # (2, 3, 4)
print('차원:', tensor.ndim)  # 3
print('크기:', tensor.size)  # 24개 요소

'''
Numpy 데이터 타입
    모든 ndarray는 동일한 자료형을 가져야 하며, .dtype 속성으로 확인 가능
        - 주요 자료형 : int32, int64, float32, float64, bool, complex64, str 등
    - astype() 메서드로 자료형 변환 가능
'''
arr = np.array([1, 2, 3])
print(arr.dtype)    # int64 또는 시스템에 따라 int32

float_arr = np.array([1.0, 2.0])
print(float_arr.dtype)  # float64

arr = np.array([1, 2, 3])
float_arr = arr.astype(np.float32)
print(float_arr.dtype)  # float32

'''
배열 초기화 함수
'''

# np.zeros(shape) : 모든 요소가 0
# 용도:
# - 배열 초기화
# - 누적 계산용 배열 준비
# - 이미지 처리 (검은색 이미지 생성)

np.zeros((2, 3))    # 2행 3열, 값은 모두 0.0

zeros_1d = np.zeros(5)
print('1차원 zeros:', zeros_1d)

zeros_2d = np.zeros((3, 4))
print('2차원 zeros:\n', zeros_2d)

zeros_2d_int = np.zeros((3, 4), dtype=int)
print('2차원 zeros (정수):\n', zeros_2d_int)

arr1 = np.zeros((3, 4)) + 5
print('arr1\n', arr1)

matrix = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [4, 5, 6]
])
# 기존 배열과 같은 모양의 0 배열
zeros_copy = np.zeros_like(matrix)
print('zeros_like:\n', zeros_copy)

# np.ones(shape) : 모든 요소가 1
# 용도:
# - 가중치 초기화
# - 마스크 배열 생성
#       원본 데이터 배열과 같은 형태를 가지며, 해당 위치의 원본 데이터가 유효한지 여부를 불리언(True/False) 값으로 표시
#       배열의 유효하지 않거나 특정 조건을 만족하지 않는 데이터를 숨기거나 무시하기 위해 사용하는 기법
# - 곱셈 항등원

np.ones((3, 2))    # 3행 2열, 값은 모두 1

ones_1d = np.ones(5)
print('1차원 ones:', ones_1d)

ones_2d = np.ones((3, 4))
print('2차원 ones:\n', ones_2d)

ones_2d_bool = np.ones((3, 4), dtype=bool)
print('2차원 ones (불린):\n', ones_2d_bool)

# 원본 배열 생성
arr = np.array([-1, 5, 0, -3, 8, 2])

# 0보다 작은 데이터를 마스킹하는 마스크 생성
mask = arr < 0

# 마스크가 적용된 배열 생성 (마스크된 데이터는 무시됨)
masked_arr = np.ma.array(arr, mask=mask)

print(masked_arr)
# 출력 결과: [-- 5 -- -- 8 2]


# np.empty(shape) : 초기화되지 않은 배열(쓰레기 값)
# - 메모리만 할당하고 초기화하지 않음
# - 쓰레기 값(garbage value)이 들어있음
# - 빠르지만 위험할 수 있음
# - 반드시 나중에 값을 채워야 함

# 사용 시기:
# - 즉시 값을 채울 예정일 때
# - 속도가 매우 중요할 때

np.empty((2, 2))    # 값이 초기화되지 않음 → 빠르지만 위험

# np.full(shape, value) : 주어진 값으로 채운 배열
# 용도:
# - 초기값이 있는 배열 생성
# - 기본값 설정

np.full((2, 2), 7)    # [[7 7]
                      #  [7 7]]

full_array = np.full((3, 4), 7)
print('7로 채운 배열:\n', full_array)

matrix = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [4, 5, 6]
])
full_like = np.full_like(matrix, 999)
print('999로 채운 배열:\n', full_like)
                      
# np.eye(N, M=None, k=0)
# 단위 행렬/항등 행렬 (Identity Matrix):
# - 대각선은 1, 나머지는 0
# - 행렬 곱셈의 항등원 (A × I = A)

# 용도:
# - 선형대수 연산
# - 머신러닝 초기화
# - 공분산 행렬 생성
'- N : (핑수) 행(row)의 수 '
'- M : (선택) 열(column)의 수, 생략하면 M = N으로 처리되어 정방 행렬 생성'
'- k : (선택) 1이 위치할 대각선의 인덱스, 기본값 0(주대각선)'
'       k > 0 이면 위쪽 대각선, k < 0 이면 아래쪽 대각선'

np.eye(3)   # [[1., 0., 0.],
            #   [0., 1., 0.],
            #   [0., 0., 1.]]
            
np.eye(3, 5, k=1)   # [[0., 1., 0., 0., 0.],
                    #  [0., 0., 1., 0., 0.],
                    #  [0., 0., 0., 1., 0.]]

identity = np.eye(3)
print('3x3 항등 행렬:\n', identity)

matrix = np.eye(4, 5)  # 4행 5열
print('4x5 대각 행렬:\n', matrix)

matrix = np.eye(4, k=1)  # 대각선을 위로 1칸 이동
print('위쪽 대각선:\n', matrix)

matrix = np.eye(4, k=-1)  # 대각선을 아래로 1칸 이동
print('아래쪽 대각선:\n', matrix)

arr7 = np.random.randint(0, 100, (10, 10))
print('arr7\n', arr7)
arr7 = arr7 + np.eye(10)  # 대각선에 1씩 더해짐
print('arr7\n', arr7)

# identity: 정방 항등 행렬
# eye와의 차이:
# - identity는 정사각형만 생성 가능
# - eye는 직사각형도 가능하고 대각선 위치 조정 가능

identity = np.identity(4)
print('4x4 항등 행렬:\n', identity)
                    
'''
범위 기반 배열
'''
# arange : 연속된 숫자 배열
# np,arange(start, stop, step) : range() 와 유사함
#   시작(start)이상 ~ 끝(stop) 미만의 정수 배열을 step 간격으로 생성
#   - 파이썬 range()와 유사하지만 NumPy 배열 반환
#   - stop 값은 포함되지 않음 (미만)
#   - step에 실수도 사용 가능

np.arange(0, 10, 2) # [0 2 4 6 8]

arr1 = np.arange(10)  # 0부터 9까지
print('0부터 9까지:', arr1)

arr2 = np.arange(1, 11)  # 1부터 10까지
print('1부터 10까지:', arr2)

arr3 = np.arange(1, 21, 2)  # 1, 3, 5, ..., 19
print('1부터 20까지 홀수만:', arr3)

arr4 = np.arange(1, 11, 0.5)  # 0.5 간격
print('1부터 11까지 0.5 간격:', arr4)


# linspace : 균등 간격 배열
# np.linspace(start, stop, num, endpoint=True)
#   시작(start) ~ 끝(stop)까지 균일 간격으로 num 개 생성
#   - 시작과 끝 사이를 균등하게 나눈 숫자들
#   - num: 생성할 요소의 개수
#   - endpoint=True: 끝값 포함 (기본값)
#   - endpoint=False: 끝값 미포함
# 계산 공식:
# - endpoint=True: step = (stop - start) / (num - 1)
# - endpoint=False: step = (stop - start) / num
# 사용 예시:
# - 그래프 그리기 (x축 좌표 생성)
# - 수치해석 (등간격 샘플링)
# - 신호처리 (시간 축 생성)

np.linspace(0, 1, 5)    # [0.   0.25 0.5  0.75 1.  ]

arr1 = np.linspace(0, 10, 5)  # 0, 2.5, 5, 7.5, 10
print('0부터 10까지 5개 요소:', arr1)

arr2 = np.linspace(0, 10, 5, endpoint=False)  # 0, 2, 4, 6, 8
print('끝값 제외:', arr2)

'''
랜덤 배열 생성
'''
# rand : 균일 분포 난수
'''
균일 분포 (Uniform Distribution):
- 특정 구간 안에서 모든 값이 똑같은 확률로 나옴
- 치우침 없이 고르게 퍼져 있는 확률 분포

사용 예:
- 게임 개발 (랜덤 아이템 드롭)
- 시뮬레이션 (몬테카를로 방법)
- 초기화 (가중치 랜덤 초기화)
'''
# np.random.rand(m, n)
#   m x n 크기의 배열 생성 및 0 ~ 1 사이의 난수로 초기화
np.random.rand(2, 2)

# [[0.90304384 0.08198118]
#  [0.50991854 0.44998101]] 

random_uniform = np.random.rand(3, 3)  # 0~1 사이 균일 분포
print('0~1 균일 분포:\n', random_uniform)

rounded = np.round(random_uniform, 2)  # 소수점 2자리
print('0~1 균일 분포 (반올림):\n', rounded)

# 특정 범위로 스케일링
low, high = 10, 20
random_range = low + (high - low) * np.random.rand(3, 3)
print(f'{low}~{high} 균일 분포:\n', random_range)

# 더 직관적인 방법
uniform = np.random.uniform(low=0, high=100, size=(2, 3))
print('0~100 균일 분포:\n', uniform)

# randn : 정규분포 난수
'''
정규 분포 (Normal Distribution / Gaussian Distribution):
- 평균을 중심으로 좌우 대칭인 종 모양 분포
- 자연계의 많은 현상이 정규 분포를 따름
- 표준 정규 분포: 평균 0, 표준편차 1

68-95-99.7 규칙:
- 평균 ± 1σ: 68% 데이터
- 평균 ± 2σ: 95% 데이터
- 평균 ± 3σ: 99.7% 데이터

사용 예:
- 실제 데이터 시뮬레이션 (키, 몸무게, 시험 점수)
- 머신러닝 가중치 초기화
- 노이즈 추가
'''
# np.random.randn(m, n)
#   m x n 크기의 배열 생성 및 표준 정규분포를 따르는 난수로 초기화
np.random.randn(2, 2)

# [[ 0.07567784 -2.27938642]
#  [ 0.02239584  1.258831  ]]

random_normal1 = np.random.randn(3, 3)
print('표준 정규 분포:\n', random_normal1)

# 평균 100, 표준편차 15인 정규 분포 (예: 시험 점수)
mean, std = 100, 15
scores = mean + std * np.random.randn(1000)
print('시험 점수 시뮬레이션 (일부):', scores[:10])
print('실제 평균:', round(scores.mean(), 2))
print('실제 표준편차:', round(scores.std(), 2))

# randint : 정수 난수
'''
randint(low, high, size)
- low 이상 high 미만의 정수
- 이산 균일 분포

사용 예:
- 게임 (주사위, 카드)
- 랜덤 샘플링
- 랜덤 인덱스 생성
'''
# np.random.randint(low, high, size)
#   low이상 high미만의 숫자로 size형태의 정수 배열을 생성
np.random.randint(0, 10, (2, 3))    # 0 ~ 9 사이 정수 2 x 3 배열

# [[0 8 3]
#  [7 2 2]]

random_int = np.random.randint(0, 10, size=(3, 4))
print('0~9 정수 난수:\n', random_int)

# 주사위 시뮬레이션
dice = np.random.randint(1, 7, size=10)
print('주사위 10번 굴리기:', dice)

arr8 = np.random.randint(0, 10, (2, 3, 4))
print('arr8\n', arr8)

# seed
'''
시드 (Seed):
- 난수 생성의 시작점
- 같은 시드 = 같은 난수 시퀀스
- 디버깅과 재현성을 위해 중요

사용 시기:
- 실험 재현
- 디버깅
- 테스트 코드 작성
'''
# np.random.seed()
#   시드는 난수 생성기의 시작값 → 같은 시드를 주면 항상 같은 결과를 얻을 수 있음
np.random.seed(42)  # 시드 설정
print(np.random.rand(3))    # 항상 동일한 결과

np.random.seed(42)  # 시드 고정
random1 = np.random.rand(5)
print('첫 번째 난수:', random1)

np.random.seed(42)  # 같은 시드 사용
random2 = np.random.rand(5)
print('두 번째 난수:', random2)
print('같은 난수인가?', np.array_equal(random1, random2))  # True

# np.random.normal() : 랜덤 숫자 만들기(평균 중심)
'''
np.random.normal(평균, 범위, 개수)

쉽게 설명:
- 평균 주변에서 랜덤 숫자를 만들어줌
- 평균에서 멀어질수록 나올 확률이 낮아짐
- 예: 평균 키 170cm 주변에서 랜덤 키 만들기
'''
# 사용 예제
# 평균 0 주변의 랜덤 숫자 10개
numbers = np.random.normal(size=10)
print('랜덤 숫자 10개:', numbers)

# 사용 예제 - 평균 지정
# 평균 100 주변의 랜덤 숫자 10개 (예: 시험 점수)
scores = np.random.normal(loc=100, scale=15, size=10)
print('시험 점수 10개:', scores)
print('평균:', round(scores.mean(), 1))

# 사용 예제 - 2차원 배열로 만들기
# 3행 4열의 랜덤 숫자
matrix = np.random.normal(loc=50, scale=10, size=(3, 4))
print('3x4 랜덤 배열:\n', matrix)

# 사용 예제 - 키 데이터 만들기
# 평균 키 170cm 주변에서 랜덤 키 100개 만들기
heights = np.random.normal(loc=170, scale=7, size=100)
print('키 10명:', [round(h, 1) for h in heights[:10]])
print('평균 키:', round(heights.mean(), 1), 'cm')
print('가장 큰 키:', round(heights.max(), 1), 'cm')
print('가장 작은 키:', round(heights.min(), 1), 'cm')

# reshpe() : 배열릐 형태 변경
'''
array.reshape(new_shape)
또는
np.reshape(array, new_shape)

중요:
- 전체 요소 개수는 변하지 않음
- 원본 배열은 변경되지 않음 (새 view 반환)
- -1을 사용하면 자동으로 크기 계산
'''
# 사용 예제
# 1차원 → 2차원
arr = np.arange(12)  # [0, 1, 2, ..., 11]
print('원본 배열:', arr)
print('원본 shape:', arr.shape)  # (12,)

reshaped = arr.reshape(3, 4)  # 3행 4열
print('\n3x4로 변환:\n', reshaped)
print('변환 후 shape:', reshaped.shape)  # (3, 4)

arr5 = np.arange(1, 21).reshape(4, 5)
print('arr5\n', arr5)

arr6 = np.linspace(0, 1, 12).reshape(3, 4)
print('arr6\n', arr6)

# 사용 예제 - 다양한 형태 변환
arr = np.arange(24)

# 2차원 변환
matrix_2x12 = arr.reshape(2, 12)
print('2x12 행렬:\n', matrix_2x12)

matrix_4x6 = arr.reshape(4, 6)
print('\n4x6 행렬:\n', matrix_4x6)

matrix_6x4 = arr.reshape(6, 4)
print('\n6x4 행렬:\n', matrix_6x4)

# 24개 요소 → (2, 3, 4)
tensor = arr.reshape(2, 3, 4)
print('3차원 텐서 shape:', tensor.shape)
print('3차원 텐서:\n', tensor)

# 사용 예제 - -1 사용 : 자동 크기 계산
'''
-1의 의미:
- "나머지를 자동으로 계산해줘"
- 한 차원에만 사용 가능
- 전체 요소 개수를 기준으로 자동 계산

예: 12개 요소를 (3, -1)로 reshape
→ 12 / 3 = 4이므로 (3, 4)가 됨
'''
arr = np.arange(12)

auto_reshape1 = arr.reshape(3, -1)  # (3, 4)로 자동 계산
print('(3, -1) → shape:', auto_reshape1.shape)
print(auto_reshape1)

auto_reshape2 = arr.reshape(-1, 4)  # (3, 4)로 자동 계산
print('\n(-1, 4) → shape:', auto_reshape2.shape)
print(auto_reshape2)

auto_reshape3 = arr.reshape(2, 2, -1)  # (2, 2, 3)으로 자동 계산
print('\n(2, 2, -1) → shape:', auto_reshape3.shape)
print(auto_reshape3)

# 사용 예제 - 1차원으로 펼치기
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print('원본 2차원 배열:\n', matrix)

# 방법 1: reshape(-1)
flattened1 = matrix.reshape(-1)
print('\nreshape(-1):', flattened1)

# 방법 2: flatten() - 복사본 생성
flattened2 = matrix.flatten()
print('flatten():', flattened2)

# 방법 3: ravel() - view 반환 (더 빠름)
flattened3 = matrix.ravel()
print('ravel():', flattened3)

# 열 벡터, 행 벡터 변환
'''
reshape를 사용한 벡터 형태 변환:
- 행 벡터: (1, n)
- 열 벡터: (n, 1)
'''

arr = np.array([1, 2, 3, 4, 5])
print('원본 배열:', arr, '| shape:', arr.shape)

# 행 벡터 (1행 n열)
row_vector = arr.reshape(1, -1)
print('\n행 벡터:\n', row_vector, '| shape:', row_vector.shape)

# 열 벡터 (n행 1열)
col_vector = arr.reshape(-1, 1)
print('\n열 벡터:\n', col_vector, '| shape:', col_vector.shape)

# reshape 오류 예시
'- 요소 개수가 맞지 않으면 오류 발생'
arr = np.arange(12)  # 12개 요소
print('배열 크기:', arr.size)

try:
    wrong_reshape = arr.reshape(3, 5)  # 3 * 5 = 15 (불가능)
except ValueError as e:
    print('오류 발생:', e)

# 사용 예제 - 이미지 데이터 변환
'''
이미지 처리에서 reshape는 필수:
- (높이, 너비, 채널) ↔ (배치, 높이, 너비, 채널)
- 2D ↔ 1D (머신러닝 입력)
'''
# 가상의 RGB 이미지 데이터 (28x28x3)
image = np.random.randint(0, 256, size=(28, 28, 3))
print('원본 이미지 shape:', image.shape)  # (28, 28, 3)

# 1D 벡터로 펼치기 (머신러닝 입력용)
image_flat = image.reshape(-1)
print('펼친 이미지 shape:', image_flat.shape)  # (2352,)

# 다시 원래 형태로 복원
image_restored = image_flat.reshape(28, 28, 3)
print('복원된 이미지 shape:', image_restored.shape)  # (28, 28, 3)
print('복원 성공?', np.array_equal(image, image_restored))  # True

# 사용 예제 - 배치 처리를 위한 reshape : 딥러닝에서 자주 사용하는 패턴
# 100개의 28x28 흑백 이미지
images = np.random.rand(100, 28, 28)
print('이미지 데이터 shape:', images.shape)

# 각 이미지를 1D로 펼치기 (100, 784)
images_flat = images.reshape(100, -1)
print('펼친 데이터 shape:', images_flat.shape)

# 다시 원래 형태로
images_restored = images_flat.reshape(100, 28, 28)
print('복원된 데이터 shape:', images_restored.shape)
print()

print('=== 10. newaxis를 사용한 차원 추가 ===')
"""
reshape의 대안: np.newaxis
- 새로운 차원을 추가할 때 더 직관적
- None과 동일
"""
arr = np.array([1, 2, 3, 4, 5])
print('원본:', arr.shape)

# 행 벡터 (1, 5)
row = arr[np.newaxis, :]
print('행 벡터:', row.shape)

# 열 벡터 (5, 1)
col = arr[:, np.newaxis]
print('열 벡터:', col.shape)

# RNG(Random Number Generator)
'''
- NumPy 1.17 이상에서 권장하는 방식
- 더 나은 성능과 통계적 품질
- 여러 generator를 독립적으로 사용 가능

장점:
- 스레드 안전성
- 더 빠른 속도
- 더 좋은 난수 품질
'''
# Numpy에서 독립적으로 난수를 생성하고 관리할 수 있는 Generator 클래스 기반의 난수 생성기
#   Numpy 개발팀은 향후 Generator 기반의 RNG 사용을 표준 방식으로 권장

# 기존 방식(np.random.seed)
#   전역 상태(global state)를 사용함 : 코드 전반에서 예측 어려움
#   → RNG로는 간섭하지 않는 독립적인 난수 시권스 생성 가능

rng = np.random.default_rng(seed=42)
random3 = rng.random((2, 3))  # 0~1 균일 분포
print('새로운 방식 난수:\n', random3)

# 독립적인 generator 생성
rng1 = np.random.default_rng(seed=42)
rng2 = np.random.default_rng(seed=42)
print('독립적 generator 1:', rng1.random(3))
print('독립적 generator 2:', rng2.random(3))

# 주요 메서드
'''
메서드                              설명                    반환범위
integers(low, high, size)       정수 난수                   [low, high]
random(size)[0.0, 1.0] 사이의 실수      균등분포
normal(loc, scale, size)        정규분포 난수               평균=loc. 표준편차=scale
uniform(low, high, size)        균등분포 난수               [low, high]
'''

from numpy.random import default_rng
rng = default_rng(seed=42)  # rng 객체 생성

print(rng.integers(1, 10, size=5))  # 정수 난수
print(rng.random(3))                # 실수 난수
print(rng.normal(0, 1, size=(2, 2)))    # 정규 분포
print(rng.uniform(5, 10, size=3))       # 균등 분포
# default_rng()는 numpy.random.Gen                    erator 객체를 생성하는 함수, seed는 생략 가능

######################################################################################################
# 실습 1 배열 초기화 및 생성
'''
1. 0으로 채워진 크기 (3, 4) 배열을 생성한 후, 모든 값을 5로 채우는 새로운 배열을 만드세요.
'''
array = np.full((3, 4), 5)
print(array)

# [[5 5 5 5]
#  [5 5 5 5]
#  [5 5 5 5]]
'''
2. 0부터 20까지 2씩 증가하는 1차원 배열을 생성하세요.
'''
array = np.arange(0, 21, 2)
print(array)    # [ 0  2  4  6  8 10 12 14 16 18 20]
'''
3. 0 ~ 1 사이의 실수 난수를 가지는 (2, 3) 크기의 배열을 생성하세요.
'''
array = np.random.uniform(low=0, high=1, size=(2, 3))
print(array)

# [[0.32792803 0.21500652 0.46293375]
#  [0.66784338 0.22991139 0.73757779]]

'''
4. 평균이 100, 표준편차가 20인 정규분포 난수 6개를 생성하새요.
'''
mean, std = 100, 20
randnum = mean + std * np.random.randn(6)
print(randnum)

# [ 87.10968554 140.12817661  86.04949491 101.42982091  92.22413302
#   47.70592223]

'''
5. 1부터 20까지의 정수를 포함하는 1차원 배열을 만들고, 이 배열을 (4, 5) 크기의 2차원 배열로 변환하세요.
'''
array1 = np.arange(1, 21)
array2 = array1.reshape(4, 5)
print(array2)

# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]]

'''
6. 0부터 1까지 균등 가격으로 나눈 12개의 값을 가지는 배열을 생성하고, 이를 (3, 4) 크기로 변환하세요.
'''
array1 = np.linspace(0, 1, 12)
array2 = array1.reshape(3, 4)
print(array2)

# [[0.         0.09090909 0.18181818 0.27272727]
#  [0.36363636 0.45454545 0.54545455 0.63636364]
#  [0.72727273 0.81818182 0.90909091 1.        ]]

'''
7. 0 ~ 99 사이의 난수로 이루어진 (10. 10) 배열을 생성한 뒤, np.eye()로 만든 단위 행렬을 더하여 대각선 요소가 1씩 증가된 배열을 만드세요.
'''
array = np.random.uniform(low=0, high=100, size=(10, 10))
array2 = np.eye(10, 10)
print(array + array2)

# [[2.31837882e+01 3.73342376e+00 6.98873816e+01 5.26333082e+01
#   5.79432273e+01 2.97234468e+01 1.38760095e+00 5.11125168e+01
#   9.95555417e+01 7.51422838e+01]
#  [9.24670745e+01 1.76215474e+01 3.10617746e+01 5.18192702e+01
#   3.87267384e+01 4.76861101e+01 9.54071725e+01 3.96975543e+01
#   5.08985242e+01 9.58462954e-02]
#  [4.24005478e+01 8.59016905e+01 9.83696834e+01 4.81021279e+01
#   3.26810481e+00 6.72469515e+01 6.24290744e+01 5.61172621e+01
#   3.30938105e+01 8.88103329e+01]
#  [4.13403738e+01 1.16871663e+01 9.91575945e+01 1.94970598e+01
#   4.83189086e+01 1.41923188e+01 3.77405626e+01 3.74399680e+01
#   6.84211786e+01 5.69426860e+01]
#  [9.41339386e+01 2.97628534e+01 7.29648257e+01 6.55159559e+00
#   8.24164300e+01 5.22478539e+01 7.38251924e+01 9.59933348e+01
#   5.72211268e+01 4.57128224e+01]
#  [1.04205023e+00 6.20083465e+01 2.20256075e+01 1.91256817e+01
#   4.09525985e+00 5.30308616e+01 7.92176824e+01 7.18726581e+01
#   1.72548480e+01 5.19564360e+01]
#  [6.51876797e+01 4.94747152e+01 2.12530980e+01 4.49946739e+01
#   8.32055518e+00 9.81169175e+01 7.86111300e+01 1.39225103e+01
#   6.93077298e+00 4.68293241e+01]
#  [8.83513857e+01 5.54446541e+00 1.16114868e+01 5.59130011e+01
#   9.08716347e+01 7.41387518e+01 3.80213534e+01 8.29835128e+01
#   1.92256212e+01 4.74418860e+01]
#  [1.04321454e+01 6.34943635e+01 7.53482523e+01 9.81795050e+01
#   5.26149700e+01 1.97970058e+01 5.51434382e+01 7.13651293e+01
#   6.93351106e+01 9.92841350e+01]
#  [2.69345793e+01 4.62636708e+01 2.29929388e+01 3.17128118e+01
#   4.66947155e+01 2.53001024e+01 5.93690713e+01 6.45878262e+00
#   5.87806665e+01 4.26134885e+01]]

'''
8. 0 ~ 9 사이의 난수로 이루어진 (2, 3, 4) 3차원 배열을 생성하세요.
'''
array = np.random.uniform(low=0, high=9, size=(2, 3, 4))
print(array)

# [[6.90372994 3.04733448 3.42707787 6.3416123 ]
#   [2.24849473 1.4306441  3.7276504  3.51423437]
#   [4.78752799 2.85551564 4.36963579 5.17625771]]]

'''
NumPy 핵심 개념 요약:

1. ndarray는 동질적(같은 타입), 고정 크기의 다차원 배열
2. 파이썬 리스트보다 빠르고 메모리 효율적
3. 벡터화 연산으로 반복문 없이 전체 배열 연산 가능
4. dtype으로 데이터 타입 명시 가능
5. shape, ndim, size로 배열 구조 파악
6. 다양한 생성 함수: zeros, ones, arange, linspace 등
7. 난수 생성: 균일 분포, 정규 분포, 정수 난수
8. 시드 설정으로 재현 가능한 난수 생성
'''
'''
np.random.normal() 핵심:
1. 정규 분포(가우시안 분포) 난수 생성
2. loc(평균), scale(표준편차), size(배열 크기) 지정
3. 실제 데이터 시뮬레이션에 유용
4. randn()보다 유연하지만 조금 느림

reshape() 핵심:
1. 배열의 형태를 변경 (전체 요소 개수는 동일)
2. 원본은 변경하지 않음 (새 view 반환)
3. -1 사용으로 자동 크기 계산 가능
4. 이미지/텐서 데이터 변환에 필수
5. flatten(), ravel()로 1D 변환 가능

주의사항:
- reshape는 요소 개수가 맞아야 함
- normal()은 충분히 큰 샘플에서 평균/표준편차가 정확함
'''