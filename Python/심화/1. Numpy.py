# NumPy
# python -m venv 폴더이름
# python -m venv venv
import numpy as np

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
- shape: 배열의 형태 (각 차원의 크기를 나타내는 튜플)
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

# 1차원 배열
arr_1d = np.array([1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6])
print('shape:', arr_1d.shape)  # (12,) - 12개의 요소를 가진 1차원 배열
print('ndim:', arr_1d.ndim)    # 1 - 1차원
print('size:', arr_1d.size)    # 12 - 총 12개의 요소

# 2차원 배열
matrix = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [4, 5, 6]
])
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

# reshpe() : 배열의 형태 변경
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
# 원본 2차원 배열:
#  [[1 2 3]
#  [4 5 6]]

# 방법 1: reshape(-1)
flattened1 = matrix.reshape(-1)
print('\nreshape(-1):', flattened1) # reshape(-1): [1 2 3 4 5 6]

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

######################################################################################################
# 인덱싱과 슬라이싱

'''
Numpy 배열은 Python 시퀀스와 동일하게 0부터 시작하는 인덱스 사용
    - 인덱싱과 슬라이싱의 기본적인 문법은 동일함
    - 다차원 인덱싱과 조건 기반 요소 선택 등의 편의 기능을 제공
    - Python 시퀀스보다 더 빠른 연산을 수행할 수 있음
'''

# 1차원 배열 인덱싱
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])   # 첫 번째 요소 : 10
print(arr[-1])  # 마지막 요소 : 50

# 2차원 배열 인덱싱
arr2 = np.array([1, 2, 3],
                [4, 5, 6],
                [7, 8, 9])
print(arr2[0, 0])   # 1행 1열 : 1
print(arr2[2, 1])   # 3행 2열 : 8
'- arr2[행, 열] 형식으로 접근 가능'
'- 음수 인덱스도 사용 가능(arr2[-1, -1] : 9)'

# 2차원 배열 인덱싱 - 파이썬과의 차이
# Python 리스트 : 각 차원을 따로 접근(중첩 리스트로 표현)
matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix[1][2]) # 6

# Numpy 배열 : 다차원 구조 지원(콤마(,)로 차원별 인덱스 지정)
arr2 = np.array([[1, 2 ,3], [4, 5, 6]])
print(arr2[1, 2])   # 6 (한번에 접근 가능)

# 다차원 배열 인덱싱
arr3 = np.array(24).reshape(2, 3, 4)    # 3차원 (2, 3, 4)
print(arr3[0, 1, 2])    # 첫 번째 블록 → 두 번째 행 → 세 번째 열
'- 차원이 늘어나면 arr[dim1, dim2, dim3, ...] 형식 사용'

######################################################################################################
# 슬라이싱과 뷰

'''
Numpy는 Python 리스트의 슬라이싱과 동일한 문법을 사용하지만, 결과가 일반 리스트가 아니라 뷰(View)라는 점이 다름

* 뷰(view)
    - 뷰는 원본 데이터의 메모리를 공유 ↔ Python의 슬라이싱은 새로운 리스트 객체를 생성
    - 슬라이스 결과를 수정하면 원본 배열도 변경됨
'''

# 1차원 배열 슬라이싱
arr = np.array([10, 20, 30, 40, 50])
print(arr[1:4]) # 20, 30, 40
print(arr[:3])  # 처음부터 3개
print(arr[2:])  # 2번째부터 끝까지
print(arr[::2]) # 2칸씩 건너뛰기

# 2차원 배열 슬라이싱
arr2 = np.array([1, 2 ,3],
                [4, 5, 6],
                [7, 8, 9])
print(arr2[:2, 1:]) # 상위 2행, 2열부터 끝까지

# 파이썬과의 차이
# Python 리스트 : 새 리스트 생성
lst = [10, 20, 30, 40]
sub_lst = lst[1:3]
sub_lst[0] = 99
print(lst)  # [10, 20,30 ,40] (원본 변경 없음)

# Numpy 배열 : View 반환
arr = np.array([10, 20, 30, 40])
sub_arr = arr[1:3]
sub_arr[0] = 99
print(arr)  # [10, 99 , 30, 40] (원본 변경됨)
'- Numpy에서 슬라이스를 수정하면 원본 배열도 변경'

# 배열의 복사(copy) 와 참조(view)
# 1. 얕은 복사(Shallow Copy) = view
arr = np.array([1, 2, 3])
sub_arr = arr[1:3]
sub_arr[0] = 99
print(arr)  # [99, 2, 3] (원본 변경됨)
'- Numpy 에서 슬라이스 수정 시, 원본 배열도 변경'
'- 슬라이싱, view() 메서드 등은 얕은 복사'
'- 슬라이싱 원본과 메모리를 공유하여 한 쪽을 수정하면 다른 쪽도 바뀜'

# 2. 깊은 복사(Deep Copy) - copy
copy_arr = arr.copy()
copy_arr[1] = 100
print(arr)      # [99 2 3] (원본 그대로)
print(copy_arr) # [99 100 3]
'- copy() 메서드를 사용하면 원본과 독립적인 배열을 생성'

# Fancy Indexing
arr = np.array([10, 20, 30, 40, 50])
print(arr[[0, 2, 4]])   # [10 30 50]
'- 정수 배열을 사용하여 여러 인덱스를 한 번에 선택'

# Boolean Indexing
arr = np.array([10, 20, 30, 40, 50])
print(arr[arr > 30])    # 30보다 큰 값만 선택
'- 조건식을 사용하여 요소 선택'
'- 조건을 변수로 처리하여 인덱싱 가능(Boolean Masking)'

######################################################################################################
# 실습2 인덱싱과 슬라이싱
'''
1. 다음 배열에서 2, 4, 6번째 요소를 Fancy Indexing으로 선택하세요.
    arr = np.arrange(10, 30, 2)
'''
arr = np.arange(10, 30, 2)
print(arr)  # [10 12 14 16 18 20 22 24 26 28]
print(arr[[1, 3, 5]])   # [12 16 20]

'''
2. 3 X 3 배열에서 왼쪽 위 → 오른쪽 아래 대각선의 요소만 인덱싱으로 추출하세요.
    arr = np.arange(1, 10).reshape(3, 3)
'''
arr = np.arange(1, 10).reshape(3, 3)
print(arr)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

print(arr[[0, 1, 2], [0, 1, 2]])    # [1 5 9]

diagonal = np.diag(arr)
print(diagonal) # [1 5 9]
'- np.diag() : 대각선 값 추출'

'''
3. 3 X 4 배열에서 마지막 열만 선택해 모두 -1로 변경하세요.
    arr = np.arange(1, 13).reshape(3, 4)
'''
arr = np.arange(1, 13).reshape(3, 4)
print(arr)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

arr[:, -1] = -1

print(arr)
# [[ 1  2  3 -1]
#  [ 5  6  7 -1]
#  [ 9 10 11 -1]]

'''
4. 4 X 4 배열에서 행을 역순, 열을 역순으로 각각 슬라이싱해 출력하세요.
    arr = np.arange(1, 17).reshape(4, 4)
'''
arr = np.arange(1, 17).reshape(4, 4)
print(arr)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]]

print(arr[::-1, ::-1])
# [[16 15 14 13]
#  [12 11 10  9]
#  [ 8  7  6  5]
#  [ 4  3  2  1]]

'''
5. 4 X 5 배열에서 가운데 2 X 3 부분을 슬라이싱한 뒤 copy()를 이용해 독립 배열을 만드세요.
    arr = np.arange(1, 21).reshape(4, 5)
'''
arr = np.arange(1, 21).reshape(4, 5)
print(arr)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]]

print(arr[1:3, 1:4].copy())
# [[ 7  8  9]
#  [12 13 14]]

'''
6. 3 X 4 배열에서 짝수이면서 10 이상인 값만 선택하세요. (& 활용)
    arr = np.array([[4, 9, 12, 7], [10, 15,18, 3], [2, 14, 5, 20]])
'''
arr = np.array([[4, 9, 12, 7], [10, 15,18, 3], [2, 14, 5, 20]])
print(arr)
# [[ 4  9 12  7]
#  [10 15 18  3]
#  [ 2 14  5 20]]

print(arr[(arr % 2 == 0) & (arr > 10)]) # [12 18 14 20]
'- 반드시 각 연산을 ()괄호 처리 해주어야 함'

'''
7. 5 X 5 배열에서 2, 4번째 행을 선택하고, 선택된 행에서 열 순서를 [4, 0, 2]로 재배치하세요.
    arr = np.arange(1, 26).reshape(5, 5)
'''
arr = np.arange(1, 26).reshape(5, 5)
print(arr)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]]

print(arr[[1, 3], :])
# [[ 6  7  8  9 10]
#  [16 17 18 19 20]]

print(arr[[1, 3], :][:, [4, 0, 2]])
# [[10  6  8]
#  [20 16 18]]

######################################################################################################
# 실습 3 Numpy 종합 연습

'''
1. 0부터 24까지 정수를 가진 배열을 만들고, (5, 5) 배열로 변환한 뒤 가운데 행(3번째행)과
    가운데 열(3번째 열)을 각각 1차원 배열로 출력하세요.
'''
arr = np.arange(0, 25).reshape(5, 5)
print(arr)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]
#  [20 21 22 23 24]]

# 가운데 행(3번째 행)
print(arr[2:3])     # [[10 11 12 13 14]]
# 가운데 열(3번째 열)
print(arr[:, 2:3].reshape(1, 5))    #  [[ 2  7 12 17 22]]

'''
2. 0 ~ 99 난수로 이루어진 (10, 10) 배열을 생성하고, 짝수 인덱스의 행만 선택하여 출력하세요.
'''
arr = np.random.randint(0, 100, (10, 10))
print(arr)
# [[ 2 97 57 84 80 77 54 48 50 19]
#  [86 89 49 42  1 39 85 62 61 80]
#  [93 41 87 72 70 86  6 69 54 36]
#  [28 39 23 88  6 78 38  9 72  9]
#  [34  8 76 99 27  6  2 50 25 30]
#  [16 92 13 88 56 98 73 53 72 43]
#  [38 47 23 29 36 13 46  9 10 81]
#  [35 62 65 33 48 83 15 39 21  9]
#  [55 62 23 15 98 69 73 30 22 45]
#  [45 93 78 91 89  2 23 46 77 40]]
print(arr[::2])
# [[ 2 97 57 84 80 77 54 48 50 19]
#  [93 41 87 72 70 86  6 69 54 36]
#  [34  8 76 99 27  6  2 50 25 30]
#  [38 47 23 29 36 13 46  9 10 81]
#  [55 62 23 15 98 69 73 30 22 45]]

'''
3. 0부터 49까지 정수를 가진 배열을 (5, 10) 배열로 변환한 후, 2행 3열부터 4행 7열까지 부분 배열을 추출하세요.
'''
arr = np.arange(0, 50).reshape(5, 10)
print(arr)
# [[ 0  1  2  3  4  5  6  7  8  9]
#  [10 11 12 13 14 15 16 17 18 19]
#  [20 21 22 23 24 25 26 27 28 29]
#  [30 31 32 33 34 35 36 37 38 39]
#  [40 41 42 43 44 45 46 47 48 49]]
print(arr[1:4, 2:7])
# [[12 13 14 15 16]
#  [22 23 24 25 26]
#  [32 33 34 35 36]]
'''
4. 0 ~ 9 난수로 이루어진 (4, 4)배열을 생성하고, 각각 인덱싱으로 추출해 출력하세요. (for문)
    - 주 대각선 요소 (왼쪽 위 → 오른쪽 아래)
    - 부 대각선 요소 (오른쪽 위 → 왼쪽 아래)
'''
arr = np.random.randint(0, 10, (4, 4))
print(arr)
# [[0 3 8 4]
#  [0 4 7 2]
#  [8 0 2 8]
#  [6 5 0 2]]

print("주 대각선 요소:")
for i in range(4):
    print(arr[i, i], end=" ")   # 0 4 2 2

main_diag = np.diag(arr)
print("주 대각선:", main_diag)  # [0 4 2 2]

print("\n부 대각선 요소:")
for i in range(4):
    print(arr[i, 3-i], end=" ") # 4 7 0 6

sub_diag = np.diag(np.fliplr(arr))
print("부 대각선:", sub_diag)   # [4 7 0 6]

'- np.fliplr() : 좌우 반전'

# 주 대각선 요소 리스트 (np.int32 그대로)
main_diag = [arr[i, i] for i in range(4)]
# 부 대각선 요소 리스트 (np.int32 그대로)
sub_diag = [arr[i, 3 - i] for i in range(4)]

print("\n주 대각선 요소 리스트:", [repr(x) for x in main_diag]) # 주 대각선 요소 리스트: ['np.int32(0)', 'np.int32(4)', 'np.int32(2)', 'np.int32(2)']   
print("부 대각선 요소 리스트:", [repr(x) for x in sub_diag])    # 부 대각선 요소 리스트: ['np.int32(4)', 'np.int32(7)', 'np.int32(0)', 'np.int32(6)'] 

'''
5. 0 ~ 9 난수로 이루어진 (3, 4, 5) 3차원 배열을 생성하고, 두 번째 층에서 첫 번째 행과 마지막 열의 값을 출력하세요.
'''
arr = np.random.randint(0, 10, (3, 4, 5))
print(arr)
# [[[8 3 8 5 5]
#   [7 3 1 2 8]
#   [9 5 8 8 3]
#   [4 6 5 3 3]]

#  [[7 7 2 5 2]
#   [2 7 3 7 8]
#   [2 8 3 9 4]
#   [8 0 5 1 3]]

#  [[9 1 4 4 3]
#   [8 4 1 2 9]
#   [5 1 8 4 1]
#   [9 8 7 4 8]]]

print(arr[1, 0, -1])    # 2

'''
6. 35부터 74까지의 순차적인 수로 이루어진 1차원 배열을 만들고 10 X 4 배열로 변환한 후 출력해주세요.
'''
arr = np.arange(35, 75).reshape(10, 4)
print(arr)
# [[35 36 37 38]
#  [39 40 41 42]
#  [43 44 45 46]
#  [47 48 49 50]
#  [51 52 53 54]
#  [55 56 57 58]
#  [59 60 61 62]
#  [63 64 65 66]
#  [67 68 69 70]
#  [71 72 73 74]]

'''
7. 6에서 만든 배열을 맨 끝의 행부터 역순으로 출력해주세요.
'''
print(arr[::-1, ::-1])
# [[74 73 72 71]
#  [70 69 68 67]
#  [66 65 64 63]
#  [62 61 60 59]
#  [58 57 56 55]
#  [54 53 52 51]
#  [50 49 48 47]
#  [46 45 44 43]
#  [42 41 40 39]
#  [38 37 36 35]]

'''
8. 6번에서 만든 배열 중 두 번째 행부터 마지막 직전행까지, 세 번째 열부터 마지막 열까지 슬라이싱해서 출력해주세요.
'''
print(arr[1:-1, 2:])
# [[41 42]
#  [45 46]
#  [49 50]
#  [53 54]
#  [57 58]
#  [61 62]
#  [65 66]
#  [69 70]]

'''
9. 1 부터 50까지의 난수로 된 5 X 6 배열을 만들고, 배열에서 짝수만 선택하여 출력하는 코드를 작성하세요.
'''
arr = np.random.randint(1, 51, (5, 5))
print(arr)
# [[ 5 38 27  8 30]
#  [16 29 16 13 49]
#  [ 5 26  4 15  8]
#  [22 49 23 50 37]
#  [16 33 25 45 32]]
print(arr[arr % 2 == 0])
# [38  8 30 16 16 26  4  8 22 50 16 32] 

''''
10. 0부터 99까지의 정수로 이루어진 (10, 10)배열을 생성한 후, [1, 3, 5]번째 행과 [2, 4, 6]번재 열의 교차하는 원소들만 선택하여 출력하세요.
'''
arr = np.random.randint(0, 100, (10, 10))
print(arr)
# [[ 7 80 39 73 80 69 17 94 77 71]
#  [79  9 83 78 72 11 57 82 79 44]
#  [12  0  0 75 45 57 46 12 75 37]
#  [75 79 64 96 23 32  4 47 32 54]
#  [20 40 14 23 25 36 45 45 85  8]
#  [59 58 66 61 65  4  7 65  3 55]
#  [46 67 27 49 80 61 23 63 38  4]
#  [74 61 34 88 95 32 38 39 42 43]
#  [92 75 78 32 75  5 78 92 49 64]
#  [27 36 60 94 69 16 32 94 77 79]]

# 선택할 행, 열 인덱스 (0부터 시작)
row_idx = [1, 3, 5]
col_idx = [2, 4, 6]

# np.ix_() 활용 → 교차하는 원소 추출
print(arr[np.ix_(row_idx, col_idx)])
# [[83 72 57]
#  [64 23  4]
#  [66 65  7]]

'''
11. 0 ~ 9 난수로 이루어진 1차원 배열(길이 15)을 생성하고, 짝수 인덱스 위치에 있는 값들 중에서 5 이상인 값만 선택해 출력하세요.
'''
arr = np.random.uniform(low= 0, high=9, size=15)
print(arr)  # [7.72564798 7.78678288 0.98823535 8.13123301 7.11978527 0.15802879
            #  1.46656779 5.11989295 4.3214646  5.85135498 4.71779748 7.87184461
            #  6.34744812 8.51828414 6.52958224]
print(arr[::2][arr[::2] > 5])   # [7.72564798 7.11978527 6.34744812 6.52958224]

######################################################################################################
# 배열 연산

'''
Numpy 배열 연산은 요소 단위로 수행됨
    - 배열과 배열 간 또는 배열과 스칼라 값 간의 연산을 지원
    - 브로드캐스팅을 통해 서로 다른 크기의 배열 간 연산도 자동으로 확장 가능
'''
# 배열 간 연산(Element-wise Operations)
# NumPy는 같은 크기의 배열끼리 요소별(element-wise)로 연산을 수행
# 각 위치의 요소들끼리 연산이 이루어짐
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2)  # [5 7 9]
print(arr1 * arr2)  # [4 10 18]
'- 같은 크기의 배열끼리는 요소별로 연산이 이루어짐'
'- +, -, *, /와 같은 산술 연산자를 바로 사용할 수 있음'

# 덧셈: 같은 위치의 요소끼리 더함
print('덧셈 (a + b):', a + b)  # [1+5, 2+4, 3+3, 4+2, 5+1] = [6, 6, 6, 6, 6]

# 뺄셈: 같은 위치의 요소끼리 뺌
print('뺄셈 (a - b):', a - b)  # [1-5, 2-4, 3-3, 4-2, 5-1] = [-4, -2, 0, 2, 4]

# 곱셈: 같은 위치의 요소끼리 곱함 (행렬 곱셈이 아님!)
print('곱셈 (a * b):', a * b)  # [1*5, 2*4, 3*3, 4*2, 5*1] = [5, 8, 9, 8, 5]

# 거듭제곱: a의 각 요소를 b의 해당 요소만큼 제곱
# [1^5, 2^4, 3^3, 4^2, 5^1] = [1, 16, 27, 16, 5]
print('거듭제곱 (a ** b):', a ** b)

# 나눗셈: 같은 위치의 요소끼리 나눔 (결과는 실수)
# [1/5, 2/4, 3/3, 4/2, 5/1] = [0.2, 0.5, 1.0, 2.0, 5.0]
print('나눗셈 (a / b):', a / b)

# 정수 나눗셈: 몫만 반환
# [1//5, 2//4, 3//3, 4//2, 5//1] = [0, 0, 1, 2, 5]
print('몫 (a // b):', a // b)

# 나머지 연산
print('나머지 (a % b):', a % b)  # [1%5, 2%4, 3%3, 4%2, 5%1] = [1, 2, 0, 0, 0]

# 배열과 스칼라 연산(Broadcasting의 기본 형태)
# 스칼라(단일 값)는 자동으로 배열의 모든 요소와 연산됨
# 이것이 브로드캐스팅의 가장 기본적인 예시
arr = np.array([1, 2, 3])
print(arr + 10) # [11 12 13]
print(arr * 2)  # [2 4 6]
'- 배열과 단일 값(스칼라)의 연산 시, 요소 별로 단일 값 연산이 적용됨'

a = np.array([1, 2, 3, 4, 5])
scalar = 10

print('원본 배열 a:', a)
print()

# 스칼라 10이 [10, 10, 10, 10, 10]으로 브로드캐스트됨
print('+ 스칼라 10:', a + scalar)  # [11, 12, 13, 14, 15]
print('- 스칼라 10:', a - scalar)  # [-9, -8, -7, -6, -5]
print('* 스칼라 10:', a * scalar)  # [10, 20, 30, 40, 50]
print('/ 스칼라 10:', a / scalar)  # [0.1, 0.2, 0.3, 0.4, 0.5]

# 순서를 바꿔도 작동 (교환법칙 성립)
print('스칼라 10 / 배열:', scalar / a)  # [10/1, 10/2, 10/3, 10/4, 10/5]
print()

# 같은 크기의 행렬끼리는 요소별로 연산됨

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
B = np.array([
    [7, 8, 9],
    [10, 11, 12]
])

print('행렬 A:\n', A)
print('행렬 B:\n', B)
print()

# 행렬 덧셈: 같은 위치의 요소끼리 더함
print('행렬 A + B:\n', A + B)
# 결과: [[1+7, 2+8, 3+9],    [[8, 10, 12],
#       [4+10, 5+11, 6+12]] = [14, 16, 18]]
print()

# 행렬 요소별 곱셈: 같은 위치의 요소끼리 곱함 (Hadamard product)
# 주의: 수학의 행렬 곱셈과는 다름!
print('행렬 A * B (요소별 곱셈):\n', A * B)
# 결과: [[1*7, 2*8, 3*9],    [[7, 16, 27],
#       [4*10, 5*11, 6*12]] = [40, 55, 72]]
print()

# 행렬 요소별 나눗셈
print('행렬 A / B:\n', A / B)

# @ 연산자 또는 np.matmul()을 사용하여 수학적 행렬 곱셈 수행
# A(m×n) @ B(n×p) = C(m×p)
# 첫 번째 행렬의 열 개수와 두 번째 행렬의 행 개수가 같아야 함

A = np.array([
    [1, 2],
    [3, 4]
])
B = np.array([
    [7, 8],
    [9, 10]
])

print('행렬 A (2×2):\n', A)
print('행렬 B (2×2):\n', B)
print()

# 행렬 곱셈: A @ B
# 결과[i,j] = A의 i번째 행과 B의 j번째 열의 내적
print('행렬 곱셈 (A @ B):\n', A @ B)
# 계산 과정:
# [1,2] · [7,9] = 1*7 + 2*9 = 25    [1,2] · [8,10] = 1*8 + 2*10 = 28
# [3,4] · [7,9] = 3*7 + 4*9 = 57    [3,4] · [8,10] = 3*8 + 4*10 = 52
# 결과: [[25, 28],
#       [57, 62]]

'''
* 브로드캐스팅
    자동으로 배열의 크기를 확장하여 서로 다른 크기의 배열 간 연산을 가능하게 하는 기능
        → 작은 배열이 큰 배열의 모양에 맞게 "늘어난 것처럼" 연산됨

    * 규칙
        -  차원 비교 : 두 배열의 각 차원을 뒤에서부터 비교
        - 규칙 
            - 크기가 같거나
            - 한 쪽이 1인 경우 → 확장 가능
        어느 차원도 위 조건을 만족하지 않으면 에러 발생
'''
# 브로드캐스팅 과정(1)
# 2D 배열과 1D 배열
'- 1단계 : 배열의 shape 확인'
'   - arr2d.shpe = (2, 3) → 2행 3열(2차원)'
'   - arr1d.shape = (3, ) → 길이가 3인 1차원 배열'
arr2d = np.array([1, 2, 3],
                 [4, 5, 6])
arr1d = np.array([10, 20, 30])

print(arr2d + arr1d)

# 예제 1: 1차원 배열과 스칼라
arr = np.array([1, 2, 3, 4, 5])
scalar = 10

# 스칼라 10이 [10, 10, 10, 10, 10]으로 브로드캐스트됨
result = arr + scalar  # [11, 12, 13, 14, 15]

# 예제 2: 2차원 배열과 1차원 배열
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
vector = np.array([10, 20, 30])

print('행렬 (3×3):\n', matrix)
print('벡터 (3,):', vector)
print()

# vector가 각 행에 브로드캐스트됨
print('행렬 + 벡터:\n', matrix + vector)
# 과정:
# [[1, 2, 3],     [[10, 20, 30],     [[11, 22, 33],
#  [4, 5, 6],  +   [10, 20, 30],  =   [14, 25, 36],
#  [7, 8, 9]]      [10, 20, 30]]      [17, 28, 39]]

# 브로드캐스팅 과정(2)
'- 2단계 : 차원 수 맞추기'
'       브로드캐스팅 규칙에 따라 차원이 다르면 앞쪽(왼쪽)에 1을 추가하여 비교'
'       - arr2d.shape = (2, 3)'
'       - arr1d.shape = (3, ) → (1, 3)으로 간주'
'- 3단계 : 뒤에서부터 차원 비교'
'       - 마지막 차원 : 3 vs 3 → 크기가 같으므로 그대로 연산 가능'
'       - 첫 번째 차원 : 2 vs 1 → 한 쪽이 1이므로 1 → 2로 확장 가능'
'- 4단계 : 요소별 연산 수행'
'       - 이제 두 배열의 shape 가 동일해져서 요소 별 덧셈이 가능'

# 사용 예제 - 성공 케이스
A = np.array([1],
             [2],
             [3])   # shape(3, 1)

B = np.array([10, 20, 30])  # shape(3, )

print(A + B)    # (3, 3)
'- 1단계 : 차원 수 맞추기'
'       - A : (1, 3)'
'       - B : (3, ) → (1, 3)로 확장'
'- 2단계 : 비교 및 확장'
'       - 마지막 차원 : 1 vs 3 → 1 확장 → 3'
'       - 첫번째 차원 : 3 vs 1 → 1 확장 → 3'
'- 3단계 : 최종 결과'
'       - (3, 3)'

# 예제: (3,) + (3, 1)
a = np.array([1, 2, 3])           # shape: (3,)
b = np.array([[4], [5], [6]])     # shape: (3, 1)

# 브로드캐스팅 과정:
# 1. a의 shape을 (1, 3)으로 확장
# 2. (1, 3) + (3, 1) 연산
# 3. 각 차원에서 브로드캐스트:
#    - 첫 번째 차원: 1 → 3으로 확장
#    - 두 번째 차원: 3 ← 1로 확장
# 4. 최종 결과 shape: (3, 3)

print('a (3,):', a)
print('b (3, 1):\n', b)
print()
print('a + b 결과 (3, 3):\n', a + b)
# 결과:
# [[1+4, 2+4, 3+4],     [[5, 6, 7],
#  [1+5, 2+5, 3+5],  =   [6, 7, 8],
#  [1+6, 2+6, 3+6]]      [7, 8, 9]]

# 규칙 2 예제: 호환 가능한 shape
# (4, 3) + (3,) → (4, 3) + (1, 3) → (4, 3)
a = np.ones((4, 3))  # 4행 3열
b = np.ones((3,))    # 3개 요소

print('(4, 3) + (3,) 연산:')
print('결과 shape:', (a + b).shape)  # (4, 3)
print(a + b)

# 사용 예제 - 실패 케이스
A = np.ones((2, 3))
B = np.ones((3, 2))

print(A + B)    # ValueError 발생

'- 마지막 차원 : 3 vs 2 → 다르고 1도 아님 → 브로드캐스팅 불가'

# 호환 불가능한 예: (3, 2) + (1, 4)
# 두 번째 차원에서 2와 4가 서로 다르고 둘 다 1이 아니므로 에러 발생
# a = np.ones((3, 2))
# b = np.ones((1, 4))
# print(a + b)  # ValueError: operands could not be broadcast together


######################################################################################################
# 실습 1 배열 연산

'''
1. 다음 배열을 생성하고, 모든 요소에 3을 더하세요.
    arr = np.array([1, 2, 3, 4])
'''
arr = np.array([1, 2, 3, 4])
print(arr + 3)  # [4 5 6 7]

'''
2. 아래 2차원 배열에서 각 요소를 -1로 곱한 새로운 배열을 만드세요.
    arr = np.array([[5, 10],
                    [15, 29]])
'''
arr = np.array([[5, 10],
                    [15, 29]])
print(arr * -1) # [[ -5 -10] 
                #  [-15 -29]]

'''
3. 아래 두 배열의 요소별 곱셈과 나눗셈 결과를 각각 출력하세요.
    arr1 = np.array([2, 4, 6])
    arr2 = np.array([1, 2, 3])
'''
arr1 = np.array([2, 4, 6])
arr2 = np.array([1, 2, 3])
print(arr1 * arr2)  # [ 2  8 18] 
print(arr1/arr2)    # [2. 2. 2.] 

'''
4. 아래 배열에서 모든 요소를 최대값 100으로 만들기 위해 필요한 값을 더한 결과 배열을 브로드캐스팅으로 만드세요.
    arr = np.array([[95, 97],
                    [80, 85]])
'''
arr = np.array([[95, 97],
                    [80, 85]])

broadcast_arr = 100 - arr

print(broadcast_arr)
# [[ 5  3]
#  [20 15]]

'''
5. 아래 2차원 배열에서 각 행에 다른 값을 곲하여 새로운 배열을 만드세요.(브로드캐스팅 이용)
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    첫 번째 행은 10을 곱하고
    두 번째 행은 100을 곱해야 합니다.
'''
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr[0:1,:] = arr[0:1,:] * 10
arr[1:2,:] = arr[1:2,:] * 100
print(arr)
# [[ 10  20  30]
#  [400 500 600]]

arr = np.array([[1, 2, 3], [4, 5, 6]])
broadcast_arr = np.array([10, 100]) 
print(arr * broadcast_arr[:, np.newaxis])
# [[ 10  20  30]
#  [400 500 600]]

'- 배열의 차원을 늘릴고 싶은 경우 사용'
'   - 세로 방향 차원 추가 : [:, np.newaxis]'
'   - 가로 방향 차원 추가 : [np.newaxis, :]'

'''
6. 아래 배열에서 각 행마다 다른 스칼라 값을 더하기 위해
    1차원 배열을 만들어 브로드캐스팅 연산을 수행하세요.
    첫 번째 행에 100, 두 번째 행에 200, 세 번째 행에 300을 더하세요.
    arr = np.array([[10, 20],
                    [30, 40],
                    [50, 60]])
'''
arr = np.array([[10, 20],
                    [30, 40],
                    [50, 60]])

broadcast_arr = np.array([100, 200, 300])
print(arr + broadcast_arr[:, np.newaxis])
# [[110 120]
#  [230 240]
#  [350 360]]

######################################################################################################
# 통계 함수 및 집계 연산(Aggregation Functions)
# NumPy는 배열의 통계량을 계산하는 다양한 함수를 제공
'''
* 활용 메서드
    - np.sum() : 합계
    - np.mean() : 평균
    - np.std() : 표준 편차
    - np.min()/np,max() : 최소/최대값
    - np.var() : 분산
    - np.ptp() : max - min
    - np.argmin() : 배열에서 최소값이 있는 인덱스 반환
    - np.argmax() : 배열에서 최대값이 있는 인덱스 반환
    - np.cumsum() : 누적 합
    - np.cumprod() : 누적 곱
'''
arr = np.array([1, 2, 3], 
               [4, 5, 6])
print(np.sum(arr))  # 21
print(np.mean(arr)) # 3.5
print(np.std(arr))  # 1.707
print(np.min(arr))  # 1
print(np.max(arr))  # 6

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print('원본 배열:', arr)
print()

# 기본 통계 함수들
print('합계 (sum):', np.sum(arr))          # 45
print('평균 (mean):', np.mean(arr))        # 5.0
print('중앙값 (median):', np.median(arr))  # 5.0
print('표준편차 (std):', np.std(arr))      # 약 2.58
print('최댓값 (max):', np.max(arr))        # 9
print('최솟값 (min):', np.min(arr))        # 1
print('분산 (var):', np.var(arr))          # 약 6.67
print('범위 (ptp):', np.ptp(arr))          # 9 - 1 = 8 (peak to peak)
print()

# 누적 연산: 각 위치까지의 누적값을 배열로 반환
print('누적 합 (cumsum):', np.cumsum(arr))
# [1, 1+2, 1+2+3, ..., 1+2+...+9] = [1, 3, 6, 10, 15, 21, 28, 36, 45]

print('누적 곱 (cumprod):', np.cumprod(arr))
# [1, 1*2, 1*2*3, ..., 1*2*...*9] = [1, 2, 6, 24, 120, ...]

arr = np.array([10, 3, 25, 7])

min_index = np.argmin(arr)
max_index = np.argmax(arr)

print("최소값 인덱스 : ", min_index)    # 1 (값 : 3)
print("최대값 인덱스 : ", max_index)    # 2 (값 : 25)

'''
* 축(axis) 단위 연산
    축(axis) : 다차원 배열에서 연산이 적용되는 방향
        - axis = 0 : 행을 따라(행을 증가시키며) 연산, 즉 세로 방향으로 계산(열 방향 (세로, ↓) - 각 열에 대해 행들을 따라 연산)
        - axis = 1 : 열을 따라(열을 증가시키며) 연산, 즉 가로 방향으로 계산(행 방향 (가로, →) - 각 행에 대해 열들을 따라 연산)
        - axis = None : 전체 배열에 대해 연산 (기본값)
'''
# 사용 예제 - 축 단위 연산 예시
arr = np.array([1, 2, 3],
               [4, 5, 6])
print(np.sum(arr, axis=0))  # 열별 합 [5 7 9]
print(np.num(arr, asix=1))  # 행별 합 [6 15]

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print('행렬:\n', matrix)
print()

# 행별 합 (axis=1): 각 행의 요소들을 모두 더함
print('행별 합 (axis=1):', np.sum(matrix, axis=1))
# [1+2+3, 4+5+6, 7+8+9] = [6, 15, 24]

# 열별 합 (axis=0): 각 열의 요소들을 모두 더함
print('열별 합 (axis=0):', np.sum(matrix, axis=0))
# [1+4+7, 2+5+8, 3+6+9] = [12, 15, 18]
print()

# 평균도 동일한 방식으로 작동
print('행별 평균 (axis=1):', np.mean(matrix, axis=1))
# [평균(1,2,3), 평균(4,5,6), 평균(7,8,9)] = [2.0, 5.0, 8.0]

print('열별 평균 (axis=0):', np.mean(matrix, axis=0))
# [평균(1,4,7), 평균(2,5,8), 평균(3,6,9)] = [4.0, 5.0, 6.0]
print()

# 누적 연산
arr = np.array([1, 2, 3, 4])
print(np.cumsum(arr))   # [1 3 6 10]
print(np.cumprod(arr))  # [1 2 6 24]

# cumsum과 cumprod도 axis를 지정할 수 있음

# 행별 누적 합 (axis=1): 각 행 내에서 왼쪽에서 오른쪽으로 누적
print('행별 누적 합 (axis=1):\n', np.cumsum(matrix, axis=1))
# [[1, 1+2, 1+2+3],         [[1, 3, 6],
#  [4, 4+5, 4+5+6],      =   [4, 9, 15],
#  [7, 7+8, 7+8+9]]          [7, 15, 24]]

# 열별 누적 합 (axis=0): 각 열 내에서 위에서 아래로 누적
print('열별 누적 합 (axis=0):\n', np.cumsum(matrix, axis=0))
# [[1,   2,   3],           [[1,  2,  3],
#  [1+4, 2+5, 3+6],      =   [5,  7,  9],
#  [1+4+7, 2+5+8, 3+6+9]]    [12, 15, 18]]

######################################################################################################
# 실습 2 통계 함수 및 집계 연산

'''
1. 아래 배열의 전체 합계와 평균을 각각 구하시오.
    arr = np.array([5, 10, 15, 20])
'''
arr = np.array([5, 10, 15, 20])
print(np.sum(arr), np.mean(arr))    # 50 12.5

'''
2. 다음 2차원 배열에서 전체 최소값과 최대값을 구하세요.
    arr = np.array([[3, 7, 1],
                    [9, 2, 8]])
'''
arr = np.array([[3, 7, 1],
                    [9, 2, 8]])

print(np.min(arr), np.max(arr)) # 1 9

'''
3. 아래 배열에서 각 열의 합계와 각 행의 합계를 각각 구하세요.
    arr = np.array([[1, 2, 3],
                    [4, 5, 6], 
                    [7, 8, 9]])
'''
arr = np.array([[1, 2, 3],
                    [4, 5, 6], 
                    [7, 8, 9]])
print(np.sum(arr, axis=0), np.sum(arr, axis=1)) # [12 15 18] [ 6 15 24]

'''
4. 아래 배열에서 행별 평균과 열별 평균을 각각 구하세요.
    arr = np.array([[10, 20],
                    [30, 40],
                    [50, 60]])
'''
arr = np.array([[10, 20],
                    [30, 40],
                    [50, 60]])

print(np.mean(arr, axis=1), np.mean(arr, axis=0))   # [15. 35. 55.] [30. 40.]

'''
5. 1차원 배열에서 전체 표준편차를 구하고, 각 요소가 평균으로부터 얼마나 떨어져 있는지 편차 배열을 만드세요.(값 - 평균)
    arr = np.array([2, 4, 4, 4, 5, 5, 7, 9])
'''
arr = np.array([2, 4, 4, 4, 5, 5, 7, 9])
print(np.std(arr), np.std(arr) - arr)   # 2.0 [ 0. -2. -2. -2. -3. -3. -5. -7.]

'''
6. 아래 2차원 배열에서 행 단위 누적 합과 열 단위 누적 곱을 각각 구하세요.
    arr = np.array([[1, 2, 3],
                    [4, 5, 6]])
'''
arr = np.array([[1, 2, 3],
                    [4, 5, 6]])

print(np.cumsum(arr, axis=1), np.cumprod(arr, axis=0)) 
# [[ 1  3  6]
#  [ 4  9 15]] 
# [[ 1  2  3]
#  [ 4 10 18]]

######################################################################################################
# 논리 연산과 조건 연산

'''
논리 연산자(&, |, ~)와 조건 연산 함수(np.where)를 사용해 배열 요소를 조건에 따라 선택하거나 값을 변경할 수 있음
    파이썬의 and, or 대신 Numpy의 논리 연산자를 사용해야 함
    - 각 조건은 반드시 괄호로 묶어야 함
'''
'''
조건 기반 선택 함수
    np.where()
        - 조건 기반 선택을 수행하는 함수
        - Python의 삼항 연산자와 유사한 역할을 함
    
    * 기본 문법
        np.where(condition, [x, y])
        - 조건에 따라 다른 값을 가지는 새 배열 생성
        - condition : 배열에서 조건(불리언 배열 또는 조건식)
        - x : 조건이 True일 때 선택할 값
        - y : 조건이 False일 때 선택할 값
'''
# 사용 예제
arr = np.array([10, 20, 30, 40, 50])
result = np.where(arr>30, "High", "Low")
print(result)   # ['Low', 'Low', 'Low', 'High', 'High']
'- arr > 30 : [False, False, False, True, True]'
'- 조건이 True인 위치는 "High", False인 위치는 "Low"를 반환'

# 사용 예제
arr = np.array([10, 20 ,30 , 40, 50])
indices = np.where(arr > 30)
print(indices)  # (array([3, 4]), )
print(arr[indices]) # [40 50]
'- x, y 값을 지정하지 않으면 조건을 만족하는 인덱스를 반환함'

'''
논리 연산
    두 개 이상의 조건을 조합하거나 부정하여 참/거짓을 반환하는 연산
    - 배열의 요소 단위로 비교 수행
    - Numpy에서는 파이썬 키워드(and, or, not) 대신 비트 연산자 형태를 사용

* 연산자 종류
연산        연산자      의미
논리 AND    &           두 조건이 모두 참일 때 True
논리 OR     |           한 조건이 참일 때 True
논리 NOT    ~           조건의 반대 값[True ↔ False]

* np.logical_* 함수
함수                    설명
np.logical_and(x,y)     AND 연산
np.logical_or(x,y)      OR 연산
np.logical_not(x)       NOT 연산
np.logical_xor(x, y)    XOR(배타적 OR)

- 논리 연산자를 대체하거나 복잡한 조건에서 가독성을 높이기 위해 사용

* np.select(conditions, arr, default=)
    - 여러 조건을 명확하게 표현
    - 중첩 np.where보다 가독성이 좋음
    - 조건 리스트와 값 리스트를 분리하여 관리
'''
# 사용 예제 - &(and) 연산
arr = np.array([10, 20, 30, 40, 50])
# AND : 20 < x < 50
mask_and = (arr > 20) & (arr < 50)
print(mask_and)     # [False False True True False]
print(arr[mask_and])    # [30 40]

'''
문제: 10보다 크고 20보다 작은 값 찾기
해결 과정:
    1. arr1 > 10 → [False, True, True, False, False, False]
    2. arr1 < 20 → [True, True, True, True, False, False]
    3. 두 조건 AND → [False, True, True, False, False, False]
    4. True인 위치의 값만 선택 → [12, 18]
'''

arr1 = np.array([5, 12, 18, 7, 30, 25])
print('원본 배열:', arr1)

# 조건별 결과 확인
print('10보다 큰가?', arr1 > 10)
print('20보다 작은가?', arr1 < 20)

# AND 조건: 두 조건을 모두 만족
result = arr1[(arr1 > 10) & (arr1 < 20)]
print('1. 결과 (10 < x < 20):', result)  # [12, 18]

# 사용 예제 - |(or) 연산
arr = np.array([10, 20 , 30, 40, 50])
# OR : x < 20 or X > 40
mask_or = (arr < 20) | (arr > 40)
print(mask_or)      # [True False Fasle False True]
print(arr[mask_or]) # [10 50]

'''
문제: 15 이하이거나 30 이상인 값 찾기
해결 과정:
    1. arr2 <= 15 → [True, True, False, False, False, False]
    2. arr2 >= 30 → [False, False, False, False, True, True]
    3. 두 조건 OR → [True, True, False, False, True, True]
    4. True인 위치의 값만 선택 → [10, 15, 30, 35]
'''

arr2 = np.array([10, 15, 20, 25, 30, 35])
print('원본 배열:', arr2)

# 조건별 결과 확인
print('15 이하인가?', arr2 <= 15)
print('30 이상인가?', arr2 >= 30)

# OR 조건: 두 조건 중 하나라도 만족
result = arr2[(arr2 <= 15) | (arr2 >= 30)]
print('2. 결과 (x ≤ 15 또는 x ≥ 30):', result)  # [10, 15, 30, 35]

# 사용 예제 - ~(not) 연산
arr = np.array([10, 20, 30, 40, 50])
# NOT : 조건 부정
mask_not = ~(arr > 30)
print(arr[mask_not])    # [10 20 30]

# 사용 예제
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
mask = (arr2d % 2 == 0) | (arr2d > 7)
print(mask)
# [[False True False],
#  [True False True],
#  [False True True]]
print(arr2d[mask])  # [2 4 6 8 9]

'''
개념 설명:
    - 불린 인덱싱으로 값을 직접 수정 가능
    - 조건을 만족하는 모든 요소를 한 번에 변경
    
문제: 10 이상인 값을 모두 0으로 변경
해결 과정:
    1. arr3 >= 10 → [False, False, True, False, False, True]
    2. True인 위치의 값을 0으로 변경
    3. [3, 8, 0, 6, 2, 0]
'''

arr3 = np.array([3, 8, 15, 6, 2, 20])
print('원본 배열:', arr3)
print('10 이상인가?', arr3 >= 10)

# 조건을 만족하는 요소를 0으로 변경
arr3[arr3 >= 10] = 0
print('3. 결과 (10 이상 → 0):', arr3)  # [3, 8, 0, 6, 2, 0]

# 조건 리스트 정의
conditions = [
    arr9 >= 70,        # 첫 번째 조건
    arr9 >= 30,        # 두 번째 조건
    # 세 번째는 default로 처리
]

# 각 조건에 대응하는 값 리스트
choices = [
    "A",  # 70 이상
    "B",  # 30 이상 70 미만
]

# np.select 사용 (default는 조건을 모두 만족하지 않을 때)
result_select = np.select(conditions, choices, default="C")
print('np.select 결과:')
print(result_select)

# ============================================================================
# 보너스: 실전 예제 - 학생 성적 처리
# ============================================================================
print('=== 보너스: 실전 예제 ===')

# 학생 성적 데이터
scores = np.array([45, 78, 92, 35, 88, 67, 55, 98, 42, 73])
print('학생 성적:', scores)
print()

# 1. 낙제자(60점 미만) 찾기
fail = scores[scores < 60]
print('낙제자 점수:', fail)
print('낙제자 수:', len(fail), '명')
print()

# 2. 등급 부여
grades = np.where(scores >= 90, 'A',
                  np.where(scores >= 80, 'B',
                           np.where(scores >= 70, 'C',
                                    np.where(scores >= 60, 'D', 'F'))))
print('등급:', grades)
print()

# 3. 보정 (60점 미만은 60점으로 상향)
adjusted = np.where(scores < 60, 60, scores)
print('보정 후 점수:', adjusted)
print()

# 4. 통계
print(f'평균: {scores.mean():.2f}점')
print(f'최고점: {scores.max()}점')
print(f'최저점: {scores.min()}점')
print(f'합격률: {(scores >= 60).sum() / len(scores) * 100:.1f}%')

######################################################################################################
# 실습 3 논리 연산과 조건 연산

'''
1. 1차원 배열 [5, 12, 18, 7, 30, 25]에서 10보다 크고 20보다 작은 값만 필터링하세요.
'''
arr = np.array([5, 12, 18, 7, 30, 25])
print(arr[(arr>10) & (arr<20)]) # [12 18]

'''
2. 1차원 배열 [10, 15, 20, 25, 30, 35]에서 15이하이거나 30이상인 값만 필터링하세요.
'''
arr = np.array([10, 15, 20, 25, 30, 35])
print(arr[(arr<=15) | (arr>=30)])   # [10 15 30 35]
'''
3. 1차원 배열 [3, 8, 15, 6, 2, 20]에서 10이상인 값을 모두 0으로 변경하세요.
'''
arr = np.array([3, 8, 15, 6, 2, 20])
arr[arr>=10] = 0
print(arr)  # [3 8 0 6 2 0]
'''
4. 1차원 배열 [7, 14, 21, 28, 35]에서 20이상인 값음 "High", 나머지는 "Low"로 표시하여 배열을 생성하세요.
'''
arr = np.array([7, 14, 21, 28, 35])

print(np.where(arr>=20, "High", "Low")) # ['Low' 'Low' 'High' 'High' 'High']


'''
5. 0 ~ 9 범위의 배열에서 짝수는 그대로 두고, 홀수는 홀수 값 X 10으로 변환한 배열을 만드세요.
'''
arr = np.random.randint(0, 10, size=10)
print(arr)  # [5 6 9 8 8 1 8 0 8 1]
arr[(arr % 2 == 1)] *= 10
print(arr)  # [50  6 90  8  8 10  8  0  8 10] 
'''
6. 아래 2차원 배열에서 20 이상 40 이하인 값만 선택하세요.
    [[10, 25, 30],
    [40, 5, 15],
    [20, 35, 50]]
'''
arr = np.array([[10, 25, 30],
                [40, 5, 15],
                [20, 35, 50]])
print(arr[(arr>=20) & (arr<=40)])   # [25 30 40 20 35]
'''
7. 1차원 배열[1, 2, 3, 4, 5, 6] 에서 3의 배수가 아닌 값만 선택하세요.
'''
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr[~(arr % 3 == 0)]) # [1 2 4 5]
'''
8. 랜덤 정수(0 ~ 100) 10개 배열에서 아래와 같이 새로운 배열을 만드세요.
    - 50 이상인 값은 그대로
    - 50 미만인 값은 50으로 변경

    - 클리핑(Clipping): 특정 범위로 값을 제한
    - 50 미만인 값을 모두 50으로 올림 (최솟값 보장)
    - 데이터 전처리에서 자주 사용
'''
arr = np.random.randint(0, 101, size=10)
print(arr)  # [  4  32  42  46  67  46  94  65 100 100]
print(np.where(arr >= 50, arr, 50)) # 원본을 변경하지 않음

# arr[arr<50] = 50
# print(arr)  # [ 50  50  50  50  67  50  94  65 100 100]

print(np.where(arr >= 50, arr, 50))
'''
9. 2차원 배열에서 아래와 같이 분류된 문자열 배열을 생성하세요.
    - 70 이상 : "A"
    - 30 이상 70 미만 : "B"
    - 30 미만 : "C"
    [[5, 50, 95],
    [20, 75, 10],
    [60, 30, 85]]
'''
arr = np.array([[5, 50, 95],
                [20, 75, 10],
                [60, 30, 85]])
print(np.where(arr>= 70, "A", np.where(arr>=30, "B", "C")))
# [['C' 'B' 'A']
#  ['C' 'A' 'C']
#  ['B' 'B' 'A']]

######################################################################################################
# 행렬 곱셈

'''
두 행렬을 곱하여 새로운 행렬을 생성하는 연산
    첫 번째 행렬의 열 수 = 두 번째 행렬의 행 수여야 곱셈이 가능

- np.dot(a, b) : 배열의 내적 연산
    * 내적 : 두 벡터가 서로 얼마나 같은 방향을 보고 있는지 숫자로 나타내는 것
        - 내적의 계산 : 같은 위치의 숫자끼리 곱하여 모두 더함
            a = (a1, a2), b = (b1, b2)
                a*b = a1*b1 + a2*b2
- np.matmul(a,b) : 행렬 곱셈(matrix multiplication)에 특화된 함수
    - 1D와 2D 배열에서 np.dot과 비슷하지만 일부 동작이 다름
    - 행렬 곱셈만 전용으로 수행 → 행렬 연산을 할 때는 matmul을 사용하는 것 권장
- @ 연산자 : Python 3.5 이상에서는 @가 np.matmul과 같은 의미로 동작함
'''
# 사용 예제 - np.dot(a,b) - 0차원(스칼라) 연산
a = np.array(3) # 0차원
b = np.array(4) # 0차원
print(np.dot(a,b))  # 12
'- 스칼라(숫자 하나)끼리 곱하기 → 일반 곱셈과 동일'

# 사용 예제 - np.dot(a,b) - 1차원 연산 : 내적
a = np.array([1, 2, 3]) # 1차원
b = np.array([4, 5, 6]) # 1차원
# 1*4 + 2*5 + 3*6 = 32
print(np.dot(a,b))  # 32
'- 같은 위치의 숫자를 곱하고 모두 더함(내적)'
'- 결과 = 숫자(스칼라)'

# 사용 예제 - np.dot(a,b) - 2차원 연산 : 행렬 곱셈
a = np.array([1, 2],
             [3, 4]) # 2차원
b = np.array([5, 6],
             [7, 8]) # 2차원
# [[1*5+2*7, 1*6+2*8],
# [3*5+4*7], 3*6+4*8]] 
print(np.dot(a,b))
# [[19 22]
#  [43 50]]

# 사용 예제 - np.matmul(a, b) - 0차원(스칼라) 연산 X
a = np.array(3) # 0차원
b = np.array(4) # 0차원
print(np.dot(a,b))  # ValueError
'- 스칼라 연산은 지원하지 않음 → * 연산자 사용'

# 사용 예제 - np.matmul(a,b) - 1차원 연산 : 내적
a = np.array([1, 2, 3]) # 1차원
b = np.array([4, 5, 6]) # 1차원
# 1*4 + 2*5 + 3*6 = 32
print(np.matmul(a,b))  # 32

# 사용 예제 - np.matmul(a,b) - 2차원 연산 : 행렬 곱셈
A = np.array([[1, 2],
              [3, 4]])  # (2, 2)
B = np.array([[5, 6], 
              [7, 8]])  # (2, 2)
print(np.matmul(A, B))
# [[19 22]
#  [43 50]]

C = np.array([[1, 2, 3],
              [4, 5, 6]])   # (2, 3)
D = np.array([[7, 8],
              [9, 10],
              [11, 12]])    # (3, 2)
print(np.matmul(C, D))
# [[58 64]
#  [139 154]]

E = np.array([[2, 4, 6]])   # (1, 3)
F = np.array([[1, 3],
              [5, 7],
              [9, 11]]) # (3, 2)
print(np.matmul(E, F))
# [[76 100]]

# 사용 예제 - @ 연산자
A = np.array([[1, 2],
              [3, 4]])  # (2, 2)
B = np.array([[5, 6], 
              [7, 8]])  # (2, 2)
print((A @ B))  # np.matmul(A, B)와 동일
# [[19 22]
#  [43 50]]

######################################################################################################
# 실습 4 행렬 곱셈

'''
1. 1부터 9까지의 정수로 채워진 (3, 3) 배열 A와, 모두 2로 채워진 (3, 2) 배열 B를 만들고 곱하세요.
'''
A = np.random.randint(1, 10, size=(3, 3))
B = np.full((3, 2), 2)
print(A)
# [4 4 4]
#  [6 3 2]
#  [9 7 8]]
print(B)
# [[2 2]
#  [2 2]
#  [2 2]]
print(np.dot(A, B))
# [[24 24]
#  [22 22]
#  [48 48]]

'''
2. 4 X 4 단위행렬 I와 4 X 4 난수 행렬 M(0 ~ 9 사이 정수) 간의 곱을 구하고, 결과와 M이 동일한지 확인하세요.
'''
I = np.eye(4, 4)
M = np.random.uniform(0, 10, size=(4, 4))

print(np.dot(I, M))
# [[5.41440073 1.20149489 3.62994872 4.98190661]
#  [4.55363355 7.8679835  5.03208152 7.33224346]
#  [5.44373295 7.36721741 6.47332667 0.16999049]
#  [8.69179738 2.39437884 7.70328776 7.96864796]]
print(f'행렬 곱 결과가 M과 같은가? \n{np.dot(I, M) == M}')
# 행렬 곱 결과가 M과 같은가? 
# [[ True  True  True  True]
#  [ True  True  True  True]
#  [ True  True  True  True]
#  [ True  True  True  True]]

'''
3. 모든 값이 1인 (2, 5) 배열 X와, 5부터 14까지의 연속된 정수로 채워진 (5, 2) 배열 Y를 만들어 곱하세요.
'''
X = np.full((2, 5), 1)
Y = np.random.randint(5, 15, size=(5, 2))
print(np.dot(X, Y))
# [[46 47]
#  [46 47]]

'''
4. 0 이상 5 미만의 임의의 정수로 채워진 (3, 2) 배열 C와 (2, 3) 배열 D를 각각 만들어 곱한 결과의 shape와 값을 출력하세요.
'''
C = np.random.randint(0, 5, size=(3, 2))
D = np.random.randint(0, 5, size=(2, 3))
print(np.dot(C, D).shape, np.dot(C, D))
# (3, 3)
# [[ 4  4  2]
#  [12  9  5]
#  [ 4  1  1]]

######################################################################################################
# 배열의 형태 변형과 차원 확장/축소

'''
배열 형태 변형
    - array.reshape(newshape)
        - 배열의 shape(형태, 차원)을 새로운 형태로 바꿔주는 함수
        - reshpape은 데이터를 복사하지 않고 shape만 바꿈
        - 변환 후 전체 원소 개수는 원본과 동일해야 함
            ex) (12, ) → (3, 4) 는 가능
                (12, ) → (2, 5) 는 불가능(12 ≠ 10)
    - array.ravel()
        - 다차원 배열을 1차원 배열로 펼친 view(원본과 연결된 뷰) 반환
        - 빠르지만 원본이 변경될 수 있어 주의 필요
        -   기준은 order 인자로 결정됨:
            'C': row-major (기본값, 행 기준 → 가로로 먼저 읽음)
            'F': column-major (열 기준 → 세로로 먼저 읽음)
            'K': 메모리에 저장된 순서 그대로
    - array.flatten()
        - 배열을 1차원으로 펴서 복사본을 반환(원본과 독립적)
        - 메모리를 더 사용하지만 안전함

        * 선택 기준
            - 원본 보호 필요 → flatten() 사용
            - 성능 중요 → ravel() 사용 (단, 의도치 않은 변경 주의)
        
    - np.newaxis : 차원 확장
        - 배열에 새로운 차원(축) 추가
        - 1차원 배열을 2차원으로 변환할 때 주로 사용
        - 브로드캐스팅이나 행렬 연산을 위해 차원을 맞출 때 필요
            - 행 벡터 생성: (5,) → (1, 5)
            - 열 벡터 생성: (5,) → (5, 1)
            - 차원 호환을 위한 shape 조정
    - np.expand_dims(a, axis) : 차원 확장
        - 지정한 위치에 차원 추가
        - 원본에 영향 없음
        - axis 매개변수로 어디에 차원을 추가할지 지정
        - np.newaxis보다 명시적이고 가독성이 좋음
            - axis=0: 맨 앞에 차원 추가 (행 추가)
            - axis=1: 두 번째 위치에 차원 추가 (열 추가)
            - axis=-1: 맨 뒤에 차원 추가

    - np.squeeze(a, axis=None)
        - 배열에서 크기가 1인 차원(즉, 길이가 1인 축)을 제거해주는 함수
            rlatten/ravel과 달리 데이터의 전체 구조를 1차원으로 펴는 것이 아니라 차원 수만 줄임
        - a : 입력 배열
        - axis : 특정 축만 1인 경우에 한해 제거하고 싶을 때 사용
                지정하지 않으면 shape이 1인 모든 차원이 제거됨
            - 신경망 출력에서 배치 차원 제거
            - 불필요하게 추가된 차원 정리
            - 차원 단순화로 연산 효율 개선
    - np.unique(a, return_index=False, return_inverse=False, return_counts=False, axis=None)
        - 배열의 중복된 요소 제거
        - 자동으로 정렬된 결과 반환
        - 다양한 옵션으로 추가 정보 제공
        - a : 입력 배열
        - return_index : True이면, 원본에서 고유값이 처음 나타난 위치 인덱스 반환
        - return_inverse : True이면, 원본 배열을 재구성할 수 있는 인덱스 배열 반환
                        arr[inv] 하면 원본 배열을 복원할 수 있음
        - return_counts : True이면, 각 고유값의 등장 횟수 반환
        - axis : 다차원 배열에서 축별 중복제거(1.13버전 이상)
    
'''
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print('원본 2차원 배열:')
print(arr)

# 사용 예제 - array.ravel()
arr = np.array([1, 2], [3, 4])
flat = arr.ravel()
print(flat) # [1 2 3 4]
'- 반환된 배열 수정 시, 원본에도 영향이 있을 수 있음'

# ravel: 뷰 반환 (원본 메모리 공유)
raveled = arr.ravel()
print('ravel 결과:', raveled)

# ravel로 만든 배열 수정 → 원본도 변경됨!
raveled[0] = 999
print()
print('원본 배열 (변경됨!):')
print(arr)  # 원본도 999로 변경됨
print('ravel 배열:', raveled)
print()

# ravel을 사용하되 복사본이 필요한 경우
raveled_copy = arr.ravel().copy()
raveled_copy[1] = 888

print('원본 배열:')
print(arr)  # 999는 유지, 888은 영향 없음
print('ravel().copy() 배열:', raveled_copy)

# 사용 예제 - array.flatten()
arr = np.array([1, 2], [3, 4])
flat = arr.flatten()
print(flat) # [1 2 3 4]

# flatten: 복사본 반환
flattened = arr.flatten()
print('flatten 결과:', flattened)  # [1 2 3 4 5 6 7 8 9]

# flatten으로 만든 배열 수정 → 원본 영향 없음
flattened[0] = 999
print()
print('원본 배열 (변경 없음):')
print(arr)  # 원본은 그대로 1
print('flatten 배열:', flattened)  # 999로 변경됨

# 사용 예제 - np.newaxis
arr = np.array([1, 2, 3, 4, 5])
print('원본 배열:', arr)
print('원본 shape:', arr.shape)  # (5,) - 1차원 배열
print()

# 행 벡터로 변환: 앞에 차원 추가
# [1, 2, 3, 4, 5] → [[1, 2, 3, 4, 5]]
row_vec = arr[np.newaxis, :]
print('행 벡터:\n', row_vec)
print('행 벡터 shape:', row_vec.shape)  # (1, 5) - 1행 5열
print()

# 열 벡터로 변환: 뒤에 차원 추가
# [1, 2, 3, 4, 5] → [[1], [2], [3], [4], [5]]
col_vec = arr[:, np.newaxis]
print('열 벡터:\n', col_vec)
print('열 벡터 shape:', col_vec.shape)  # (5, 1) - 5행 1열

# 사용 예제 - np.expand_dims(a, axis)
a = np.array([1, 2, 3]) # (3,)
b = np.expand_dims(a, axis=0)   # (1, 3)
c = np.expand_dims(a, axis=1)   # (3, 1)
'- 반환됨 배열을 수정해도 원본에 영향 없음'

arr = np.array([[1, 2, 3],
                [4, 5, 6]])   # (2, 3)
# axis = 0
arr0 = np.expand_dims(arr, axis=0)
print(arr0.shape)   # (1, 2, 3) # 덩어리개수, 행, 열
print(arr0)
# [[[1 2 3]
#   [4 5 6]]]

# axis = 1
arr1= np.expand_dims(arr, axis=1)
print(arr1.shape)   # (2, 1, 3)
print(arr1)
# [[[1 2 3]]

#  [[4 5 6]]]

# axis = 2
arr2= np.expand_dims(arr, axis=2)
print(arr2.shape)   # (2, 3, 1)
print(arr2)
# [[[1]
#   [2]
#   [3]]

#  [[4]
#   [5]
#   [6]]]

arr = np.array([1, 2, 3, 4, 5])
print('원본:', arr, '- shape:', arr.shape)  # (5,)
print()

# axis=0: 첫 번째 축에 차원 추가
# (5,) → (1, 5)
arr_expanded0 = np.expand_dims(arr, axis=0)
print('axis=0:\n', arr_expanded0)
print('shape:', arr_expanded0.shape)  # (1, 5)
print()

# axis=1: 두 번째 축에 차원 추가
# (5,) → (5, 1)
arr_expanded1 = np.expand_dims(arr, axis=1)
print('axis=1:\n', arr_expanded1)
print('shape:', arr_expanded1.shape)  # (5, 1)

# 사용 예제 - np.squeeze(a, axis) - shape 이 1인 모든 차원 제거
arr = np.array([[[1], [2], [3]]])
print("원본 shape : ", arr.shape) # (1, 3, 1)
squeezed = np.squeeze(arr)
print("squeeze 결과 shape :", squeezed.shape)   # (3,)
print(squeezed) # [1 2 3]
'- 축을 지정하지 않으면 shape이 1인 모든 차원 제거됨'

# 사용 예제 - np.squeeze(a, axis) - 특정 축만 제거
arr2 = np.zeros((1, 4, 1, 2))
print(arr2.shape)   # (1, 4, 1, 2)
s1 = np.squeeze(arr2, axis=0)   # 0번째 축만 제거 → (4, 1, 2)
print(s1.shape)
s2 = np.squeeze(arr2, axis=2) # 2번째 축만 제거 → (1, 4, 2)
print(s2.shape)
'- 크기가 1이 아닌 축을 지정해 squeeze 하려 하면 ValueError 발생'

arr = np.array([[[1, 2, 3]]])  # 3차원 배열
print('원본:\n', arr)
print('원본 shape:', arr.shape)  # (1, 1, 3)
print()

# 모든 크기 1인 차원 제거
# (1, 1, 3) → (3,)
squeezed = np.squeeze(arr)
print('squeeze 후:\n', squeezed)
print('shape:', squeezed.shape)  # (3,)
print()

# 특정 축만 제거: axis=0
# (1, 1, 3) → (1, 3)
squeezed0 = np.squeeze(arr, axis=0)
print('axis=0 squeeze:\n', squeezed0)
print('shape:', squeezed0.shape)  # (1, 3)
print()

# 주의: 크기가 1이 아닌 차원을 squeeze하면 에러
# squeezed2 = np.squeeze(arr, axis=2)  # ValueError: 크기가 1이 아님

# 사용 예제 - np.unique()
arr = np.array([1, 2, 3, 2, 4, 1, 2])
uniq = np.unique(arr)
print(uniq) # [1 2 3 4]

# 등장 위치, 재구성, 개수
uniq, idx, inv, cnt = np.unique(arr, return_index=True, return_inverse=True, return_counts=True)
print("고유값 : ", uniq)           # 고유값 :  [1 2 3 4]
print("첫 등장 인덱스 : ", idx)     # 첫 등장 인덱스 :  [0 1 2 4]
print("원본 → 고유값 인덱스 : ", inv)   # 원본 → 고유값 인덱스 :  [0 1 2 1 3 0 1]
print("등장 횟수 : ", cnt)          # 등장 횟수 :  [2 3 1 1]
'- uniq : 중복없이 오름차순 정렬된 고유값 배열'
'- idx : 원본 배열에서 각 고유값이 처음 등장한 위치'
'- inv : uniq[inv]로 원본 배열을 재구성 가능'
'- cnt : 각 고유값이 몇 번 등장했는지'

######################################################################################################
# 실습 1 배열 형태 변형, 차원 확장·축소

'''
1. 아래의 배열을 사용해서
    arr = np.array([[10, 20], [30, 40], [50, 60]])
        - ravel과 flatten을 각각 사용해 1차원 배열로 변환하고,
        - arr의 첫 번째 원소(arr[0,0])를 999로 바꾼 뒤 ravel 결과와 flatten 결과에 어떤 변화가 있는지 확인하세요.
'''
arr = np.array([[10, 20], [30, 40], [50, 60]])
print(f'ravel : {arr.ravel()}')         # ravel : [10 20 30 40 50 60]
print(f'flatten : {arr.flatten()}')     # flatten : [10 20 30 40 50 60]  
arr[0,0] = 999
print(f'변경된 arr : {arr}')            # 변경된 arr : [[999  20] [ 30  40] [ 50  60]]
print(f'ravel : {arr.ravel()}')        # ravel : [999  20  30  40  50  60] 
print(f'flatten : {arr.flatten()}')     # flatten : [999  20  30  40  50  60]


'''
2. 크기가 32 X 32인 이미지 데이터를 가정하고, 이 배열에 대해 expand_dims를 사용하여 shape(1, 32, 32)로 바꾸는 코드를 작성하세요.
    img = np.random.rand(32, 32)
'''
img = np.random.rand(32, 32)
print(img)
# [[0.88297946 0.49084264 0.15457926 ... 0.02511333 0.55677599 0.34625851]  
#  [0.10526191 0.51764186 0.29481863 ... 0.64542926 0.97414638 0.62665913]  
#  [0.10385713 0.52869733 0.37124995 ... 0.62693398 0.71975451 0.11030162]  
#  ...
#  [0.16193719 0.79202433 0.00276352 ... 0.05506179 0.38568412 0.54991087]  
#  [0.385534   0.10262878 0.90695774 ... 0.57337997 0.81101844 0.90356205]  
#  [0.88758006 0.67408006 0.33067988 ... 0.33560394 0.44636252 0.70882825]]

print(np.shape(img))    # (32, 32)

expand_img = np.expand_dims(img, axis=0)
print(expand_img)
# [[[0.88297946 0.49084264 0.15457926 ... 0.02511333 0.55677599 0.34625851] 
#   [0.10526191 0.51764186 0.29481863 ... 0.64542926 0.97414638 0.62665913] 
#   [0.10385713 0.52869733 0.37124995 ... 0.62693398 0.71975451 0.11030162] 
#   ...
#   [0.16193719 0.79202433 0.00276352 ... 0.05506179 0.38568412 0.54991087] 
#   [0.385534   0.10262878 0.90695774 ... 0.57337997 0.81101844 0.90356205] 
#   [0.88758006 0.67408006 0.33067988 ... 0.33560394 0.44636252 0.70882825]]]

print(np.shape(expand_img)) # (1, 32, 32)


'''
3. 아래 배열에서 불필요한 1차원을 모두 제거하여 shape이 (28, 28)이 되도록 만드세요.
    img = np.random.randint(0, 255, (1, 28, 28, 1))
'''
img = np.random.randint(0, 255, (1, 28, 28, 1))
print(np.shape(np.squeeze(img)))    # (28, 28)

'''
4. 아래 2차원 배열을 1차원 배열로 만든 후 중복값을 제거한 뒤 shape(1, n)으로 재구성하세요.
    arr = np.array([[3, 1, 2, 2],
                    [1, 2, 3, 1],
                    [2, 2, 1, 4]])
'''
arr = np.array([[3, 1, 2, 2],
                    [1, 2, 3, 1],
                    [2, 2, 1, 4]])

print(np.unique(arr.flatten()).reshape(1, -1))  # [[1 2 3 4]]


'''
5. 다음 배열을 shape(10,)로 만든 뒤 고유값 배열을 구하세요.
    arr = np.array([[1], [3], [1], [3], [2], [3], [1], [2], [3]])   # shape(1, 10, 1)
'''
arr = np.array([[1], [3], [1], [3], [2], [3], [1], [2], [3]])

print(np.unique(np.squeeze(arr)))   # [1 2 3]

'''
6. 다음 배열을 1차원 배열로 만든 후 고유값만 추출해서 shape(고유값 개수, 1)인 2차원 배열로 변환하세요.
    arr = np.array([[[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]],
                    [[3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]])    # shape(2, 3, 4)
'''
arr = np.array([[[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]],
                    [[3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]]) 

print(np.unique(arr.flatten()).reshape(len(np.unique(arr.flatten())), 1))
# [[0]
#  [1]
#  [2]
#  [3]
#  [4]
#  [5]
#  [6]
#  [7]
#  [8]]

######################################################################################################
# 배열의 결합과 분리

'''
배열 결합 : concatenate
    - np.concatenate((a1, a2, ...), axis=0, out=None)
        - 기존 축을 따라 배열 시퀀스를 결합
        - 같은 차원의 배열들을 특정 축(axis)를 따라 이어붙임
        - 결합할 배열들은 결합 축을 제외한 나머지 차원이 일치해야 함
        - a1, a2, ... : 결합할 배열 시퀀스
        - axis : 결합할 축(기본값 = 0, 즉 행 방향으로 결합)
            - axis = 0 : 행(세로)로 이어붙임
            - axis = 1 : 열(가로)로 이어붙임
        - 결합하는 axis를 제외한 나머지 차원이 같아야 함
            ex) (2, 2)와 (2, 2)는 axis=0/1 모두 결합 가능
                (2, 2)와 (1, 2)는 axis=0만 가능
    - np.stack((a1, a2, ...), axis=0)
        - 새로운 축을 따라 배열 시퀀스를 결합
        - 배열의 차원이 1 증가
        - axis : 새로 생성할 축의 위치
            기본값 : 0, 즉 맨 앞에 새로운 차원 추가
    - np.hstack((a1, a2, ...)) : 수평 스택 (axis=1과 동일)
        - 배열을 수평(열 방향)으로 순서대로 쌓음
    - np.vstack((a1, a2, ...)) : 수직 스택 (axis=0과 동일)
        - 배열을 세로로(행 방향)으로 순서대로 쌓음
    - np.split(a, indices_or_sections, axis=0)
        - 배열을 여러 개의 하위 배열로 분할
        - 데이터를 배치로 나누거나 훈련/검증 세트로 분리할 때 사용
            *분할 방법:
                1. 균등 분할: 정수로 개수 지정
                2. 인덱스 분할: 특정 위치에서 자르기
        - a : 분할할 배열
        - indices_or_sections : 정수(N등분) 또는 분할 인덱스 리스트
        - axis : 분할 축(기본값=0, 즉 행 기준)
'''
# 사용 예제 - np,concatenate()
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

# 행방향 결합
result = np.concatenate((a, b), axis=0)
print(result)
# [[1 2]
#  [3 4]
#  [5 6]]

# 열방향 결합
c = np.array([[7], [8], [9]])
result2 = np.concatenate((result, c), axis=1)
print(result2)
# [[1 2 7]
#  [3 4 8]
#  [5 6 9]]

# 1차원 배열 결합
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])

concat_1d = np.concatenate([a, b, c])
print('1차원 배열 결합:', concat_1d)  # [1 2 3 4 5 6 7 8 9]
print()

# 2차원 배열 결합
A = np.array([
    [1, 2, 3],
    [3, 4, 5]
])
B = np.array([
    [5, 3, 5]
])

print('A shape:', A.shape)  # (2, 3)
print('B shape:', B.shape)  # (1, 3)
print()

# axis=0: 세로 방향 결합 (행 추가)
# A의 밑에 B를 붙임
concat_v = np.concatenate([A, B], axis=0)
print('axis=0 (수직 결합):')
print(concat_v)
print('결과 shape:', concat_v.shape)  # (3, 3)
print()

# axis=1: 가로 방향 결합 (열 추가)
# 주의: A는 (2, 3), B는 (1, 3)이므로 axis=1로 결합 불가
# 행의 개수가 일치하지 않아 에러 발생
# concat_h = np.concatenate([A, B], axis=1)  # ValueError

# 사용 예제 - np.stack()
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# axis=0
stacked = np.stack((a, b), axis=0)
print(stacked)  # shape(2, 3)
# [[1 2 3]
#  [4 5 6]]

# axis=1
stacked2 = np.stack((a, b), axis=1)
print(stacked2) # shape(3, 2)
# [[1 4]
#  [2 5]
#  [3 6]]

# 사용 예제 - np.hstack(), vstack()
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# hstack() : 열 방향(가로)로 결합
h = np.hstack((a, b))
print(h)    # [1 2 3 4 5 6]

# vstack() : 행 방향(세로)로 결합
a2 = np.array([[1], [2], [3]])
b2 = np.array([[4], [5], [6]])
v = np.vstack((a2, b2))
print(v)
# [[1]
#  [2]
#  [3]
#  [4]
#  [5]
#  [6]]

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# vstack: 위아래로 쌓기
# [[1, 2, 3],
#  [4, 5, 6]]
vstacked = np.vstack([a, b])
print('vstack (수직):')
print(vstacked)
print('shape:', vstacked.shape)  # (2, 3)
print()

# hstack: 좌우로 이어붙이기
# [1, 2, 3, 4, 5, 6]
hstacked = np.hstack([a, b])
print('hstack (수평):')
print(hstacked)
print('shape:', hstacked.shape)  # (6,)

# 사용 예제 - np.split() - 1차원 배열
a = np.arange(9)    # [0 1 2 3 4 5 6 7 8]
split_arr = np.split(a, 3)  # 3등분
print(split_arr)    # [array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8])]

# 사용 예제 - np.split() - 2차원 배열
arr = np.arange(16).reshape(4, 4)
print("원본 배열:\n", arr)
# 원본 배열:
#  [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]

# 행 기준(axis=0) 분할
parts1 = np.split(arr, 2, axis=0)
print("첫 번째 부분:\n", parts1[0])
# 첫 번째 부분:
#  [[0 1 2 3]
#  [4 5 6 7]]
print("두 번째 부분:\n", parts1[1])
# 두 번째 부분:
#  [[ 8  9 10 11]
#  [12 13 14 15]]

# 인덱스 [1, 3]에서 분할 → 0~0행, 1~2행, 3~끝까지
split_arr = np.split(arr, [1, 3], axis=0)
for i, part in enumerate(split_arr) :
    print(f'part {i}:\n', part)
# part 0:
#  [[0 1 2 3]]
# part 1:
#  [[ 4  5  6  7]
#  [ 8  9 10 11]]
# part 2:
#  [[12 13 14 15]]

# 열 기준(axis=1) 분할
parts2 = np.split(arr, 2, axis=1)
print("좌측 부분:\n", parts2[0])
# 좌측 부분:
#  [[ 0  1]
#  [ 4  5]
#  [ 8  9]
#  [12 13]]
print("우측 부분:\n", parts2[1])
# 우측 부분:
#  [[ 2  3]
#  [ 6  7]
#  [10 11]
#  [14 15]]

arr = np.arange(12)  # [0 1 2 3 4 5 6 7 8 9 10 11]
print('원본 배열:', arr)
print()

# 균등 분할: 3개의 동일한 크기로 분할
# 12개 요소를 3개로 나누면 각 4개씩
splits_equal = np.split(arr, 3)
print('3개로 균등 분할:', splits_equal)
for idx, sub in enumerate(splits_equal, 1):
    print(f'{idx}번째 조각:', sub)
print()

# 인덱스 분할: [0:3], [3:7], [7:]
# 인덱스 3과 7에서 자르기
splits_idx = np.split(arr, [3, 7])
for idx, sub in enumerate(splits_idx, 1):
    print(f'{idx}번째 조각:', sub)
print()

# 2차원 배열 분할
arr = np.arange(24).reshape(4, 6)
print('2차원 배열 (4×6):')
print(arr)
print()

# axis=0: 행 방향 분할 (가로로 자르기)
# 4행을 2개로 나누면 각 2행씩
row_splits = np.split(arr, 2, axis=0)
print('행 방향 분할 (axis=0):')
for i, sub in enumerate(row_splits, 1):
    print(f'{i}번째 조각:\n', sub)
print()

# axis=1: 열 방향 분할 (세로로 자르기)
# 6열을 2개로 나누면 각 3열씩
col_splits = np.split(arr, 2, axis=1)
print('열 방향 분할 (axis=1):')
for i, sub in enumerate(col_splits, 1):
    print(f'{i}번째 조각:\n', sub)

######################################################################################################
# 실습 2 배열의 결합과 분리

'''
1. 다음 두 배열을 행 방향으로 이어붙이세요.
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6]])
'''
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
print(np.vstack((a, b)))
# [[1 2]
#  [3 4]
#  [5 6]]

'''
2. 아래 배열을 3개로 같은 크기로 분할하세요.
    a = np.arange(12)
'''
a = np.arange(12)
print(np.split(a, 3))   # [array([0, 1, 2, 3]), array([4, 5, 6, 7]), array([ 8,  9, 10, 11])] 

'''
3. 다음 배열들을 새로운 축에 쌓아 shape이 (3, 2)인 배열을 만드세요.
    a = np.array([1, 2])
    b = np.array([3, 4])
    c = np.array([5, 6])
'''
a = np.array([1, 2])
b = np.array([3, 4])
c = np.array([5, 6])

print(np.stack([a, b, c], axis=0))
# [[1 2]
#  [3 4]
#  [5 6]]

'''
4. shape가 (2, 3)인 아래 두 배열을 shape(2, 2, 3)인 3차원 배열을 만드세요.
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([[7, 8, 9], [10, 11, 12]])
'''
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

print(np.stack((a, b), axis=0))
# [[[ 1  2  3]
#   [ 4  5  6]]

#  [[ 7  8  9]
#   [10 11 12]]]

'''
5. 아래의 2차원 배열을 2:3:3 비율(총 3개)로 분할하세요.
    arr = np.arange(8)
'''
arr = np.arange(8)

print(np.split(arr, [2, 5]))    # [array([0, 1]), array([2, 3, 4]), array([5, 6, 7])]

'''
6. 아래 두 배열을 axis=0, axis=1로 각각 stack하여 두 경우의 결과 shape을 모두 구하세요.
    a = np.ones((2, 3))
    b = np.zeros((2, 3))
'''
a = np.ones((2, 3))
b = np.zeros((2, 3))

print(np.stack((a, b), axis=0))
# [[[1. 1. 1.]
#   [1. 1. 1.]]

#  [[0. 0. 0.]
#   [0. 0. 0.]]]

print(np.stack((a, b), axis=1))
# [[[1. 1. 1.]
#   [0. 0. 0.]]

#  [[1. 1. 1.]
#   [0. 0. 0.]]]

######################################################################################################
# 배열의 정렬

'''
    - np.sort(a, axis=-1, kind='quicksort', order=None)
        - 정렬된 복사본 반환(오름차순만 지원)
        - 원본 유지됨
        - a : 입력 배열
        - axis : 정렬 축(기본 : 마지막 축)
            * axis 매개변수:
                - axis=0: 각 열을 독립적으로 정렬
                - axis=1: 각 행을 독립적으로 정렬
                - axis=None: 평탄화 후 전체 정렬
        - kind : 정렬 알고리즘 (보통 quicksort/mergesort/heapsort)
    - a.sort(axis=-1, kind='quicksort', order=None)
        - 원본 배열 직접 정렬
    - np.argsort(a, axis=-1, kind='quicksort', order=None)
        - 정렬 인덱스 반환
        - 원본 배열의 어떤 요소가 정렬 후 어디로 가는지 알려줌
        - 간접 정렬에 유용 (다른 배열을 같은 순서로 정렬할 때)
'''
# 사용 예제 - np.sort()
arr = np.array([3, 1, 2])
sorted_arr = np.sort(arr)
print(sorted_arr)   # [1 2 3]

# 원본 배열 직접 정렬
arr.sort()
print(arr)  # [1 2 3]

# 2차원 배열 행 기준 정렬
arr2d = np.array([[3, 2, 1], [6, 5, 4]])
print(np.sort(arr2d,axis=1))
# [[1 2 3]
#  [4 5 6]]

arr = np.array([3, 1, 2])
idx = np.argsort(arr)
print(idx)      # [1 2 0]
print(arr[idx]) # [1 2 3]

arr = np.array([3, 1, 2])
# 내림차순 정렬
print(np.sort(arr)[::-1])   # [3 2 1]
'- 정렬 후 반전해주어야 함'

arr = np.array([3, 1, 2, 5, 4, 2])
print('원본:', arr)

# 복사본 정렬 (원본 유지)
sorted_copy = np.sort(arr)
print('정렬된 복사본:', sorted_copy)
print('원본 (변경 없음):', arr)
print()

# 원본 직접 정렬
arr.sort()
print('원본 정렬 후:', arr)
print()

# 2차원 배열 정렬
arr2 = np.array([
    [2, 1, 5],
    [3, 2, 1]
])
print('원본 2차원 배열:')
print(arr2)
print()

# axis=0: 각 열을 독립적으로 정렬
# 첫 번째 열 [2, 3] → [2, 3]
# 두 번째 열 [1, 2] → [1, 2]
# 세 번째 열 [5, 1] → [1, 5]
sorted_axis0 = np.sort(arr2, axis=0)
print('axis=0 정렬 (열 방향):')
print(sorted_axis0)
print()

# axis=1: 각 행을 독립적으로 정렬
# 첫 번째 행 [2, 1, 5] → [1, 2, 5]
# 두 번째 행 [3, 2, 1] → [1, 2, 3]
sorted_axis1 = np.sort(arr2, axis=1)
print('axis=1 정렬 (행 방향):')
print(sorted_axis1)
print()

# axis=None: 평탄화 후 전체 정렬
sorted_None = np.sort(arr2, axis=None)
print('axis=None 정렬 (전체):')
print(sorted_None)  # [1 1 2 2 3 5]

# 사용 예제 - np.argsort
# - 점수로 정렬하되 이름도 함께 정렬
# - 여러 배열을 하나의 기준으로 동시 정렬

names = np.array(['김철수', '이영희', '박민수', '정수진', '최동욱'])
scores = np.array([85, 92, 78, 95, 88])

print('원본 데이터:')
for name, score in zip(names, scores):
    print(f'{name}: {score}점')
print()

# 점수 기준으로 정렬 인덱스 구하기
# argsort는 기본적으로 오름차순이므로 [::-1]로 내림차순 변환
sorted_idx = np.argsort(scores)[::-1]
print('정렬 인덱스 (점수 높은 순):', sorted_idx)
print()

# 인덱스를 사용하여 이름과 점수를 함께 정렬
print('점수 순위:')
for rank, idx in enumerate(sorted_idx, 1):
    print(f'{rank}위: {names[idx]} - {scores[idx]}점')

# 출력 예시:
# 1위: 정수진 - 95점
# 2위: 이영희 - 92점
# 3위: 최동욱 - 88점
# 4위: 김철수 - 85점
# 5위: 박민수 - 78점


######################################################################################################
# 실습 3 배열의 정렬

'''
1. 아래의 1차원 배열을 오름차순과 내림차순으로 각각 정렬하는 코드를 작성하세요.
    arr = np.array([7, 2, 9, 4, 5])
'''
arr = np.array([7, 2, 9, 4, 5])
print(np.sort(arr))     # [2 4 5 7 9]
print(np.sort(arr)[::-1])   # [9 7 5 4 2]

'''
2. 아래의 2차원 배열에서 각 행(row) 별로 오름차순 정렬된 배열을 구하세요.
    arr = np.array([[9, 2, 5],
                    [3, 8, 1]])
'''
arr = np.array([[9, 2, 5],
                    [3, 8, 1]])
print(np.sort(arr, axis=0))
# [[3 2 1]
#  [9 8 5]]

'''
3. 아래의 1차원 배열에서 정렬 결과(오름차순)가 되는 인덱스 배열을 구하고, 
    그 인덱스를 이용해 원본 배열을 직접 재정렬하는 코드를 작성하세요.
    arr = np.array([10, 3, 7, 1, 9]) 
'''
arr = np.array([10, 3, 7, 1, 9])
idx = np.argsort(arr)
print(arr[idx]) # [ 1  3  7  9 10]

'''
4. 아래 2차원 배열을 열(column) 기준(axis=0)으로 오름차순 정렬된 배열을 구하세요.
    arr = np.array([[4, 7, 2],
                    [9, 1, 5],
                    [6, 8, 3]])
'''
arr = np.array([[4, 7, 2],
                    [9, 1, 5],
                    [6, 8, 3]])

print(np.sort(arr, axis=0))

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
<<<<<<< Updated upstream
'''
1. 불린 인덱싱:
   - 조건식으로 배열 필터링
   - & (AND), | (OR), ~ (NOT) 사용
   - 각 조건은 괄호로 묶기
   
2. np.where:
   - 조건부 값 할당
   - np.where(조건, 참일_때, 거짓일_때)
   - 중첩 사용으로 다중 조건 처리
   
3. 연산자:
   - 비교: ==, !=, <, >, <=, >=
   - 논리: & (AND), | (OR), ~ (NOT)
   - 산술: %, //, *, + 등
   
4. 실전 활용:
   - 데이터 필터링
   - 이상치 제거/처리
   - 조건부 변환
   - 등급/카테고리 분류
   - 클리핑 (범위 제한)
   
5. 성능 팁:
   - 불린 인덱싱은 벡터화 연산 (빠름)
   - 반복문보다 효율적
   - 대용량 데이터 처리에 적합
'''
'''
1. 배열 속성:
   - shape: 각 차원의 크기
   - ndim: 차원 수
   - size: 전체 요소 개수

2. 산술 연산:
   - 같은 크기의 배열: 요소별(element-wise) 연산
   - 행렬 곱셈: @ 연산자 사용

3. 브로드캐스팅:
   - 다른 크기의 배열 간 연산을 자동으로 처리
   - 규칙: 차원 맞춤 → 크기 1인 차원 확장

4. 집계 함수:
   - sum, mean, median, std, max, min 등
   - cumsum, cumprod: 누적 연산

5. axis 파라미터:
   - axis=0: 열 방향 (세로)
   - axis=1: 행 방향 (가로)
   - axis=None: 전체 배열
'''
'''
1. 차원 조작:
   - 추가: np.newaxis, np.expand_dims
   - 제거: np.squeeze
   - 평탄화: flatten (복사본), ravel (뷰)
   
2. 배열 결합:
   - concatenate: axis 지정하여 결합
   - vstack: 수직 결합 (행 추가)
   - hstack: 수평 결합 (열 추가)
   
3. 배열 분할:
   - split: 균등 분할 또는 인덱스 분할
   - axis로 분할 방향 지정
   
4. 정렬:
   - sort: 값 정렬
   - argsort: 인덱스 정렬 (간접 정렬)
   
5. 기타:
   - unique: 고유값 추출
   - 다양한 옵션으로 추가 정보 획득
'''
=======

######################################################################################################
# 인덱스와 슬라이싱

'''
Numpy 배열은 Python 시퀀스와 동일하게 0부터 시작하는 인덱스 사용
    - 인덱싱과 슬라이싱의 기본적인 문법은 동일함
    - 다차원 인덱싱과 조건 기반 요소 선택 등의 편의 기능을 제공
    - Python 시퀀스보다 더 빠른 연산을 수행할 수 있음
'''
import numpy as np

# 1차원 배열 인덱싱
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])   # 첫 번째 요소 : 10
print(arr[-1])  # 마지막 요소 : 50

# 2차원 배열 인덱싱
arr2 = np.array([1, 2, 3],
                [4, 5, 6],
                [7, 8, 9])
print(arr2[0, 0])   # 1행 1열 (1)
print(arr2[2, 1])  # 3행 2열 (8)

# 2차원 배열 인덱싱 - 파이썬과 차이
# Python 리스트 : 중첩 리스트로 표현(각 차원 따로 접근)
matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix[1][2]) # 6

# Numpy 배열 : 다차원 구조 지원(콤마(,) 로 차원별 인덱스 지정)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2[1, 2])   # 6 (한번에 접근 가능)

# 다차원 배열 인덱싱
arr3 = np.arange(24).reshape(2, 3, 4)   # 3ckdnjs (2, 3, 4)
print(arr3[0, 1, 2])    # 첫 번째 블록 → 두 번째 행 → 세 번째 열
>>>>>>> Stashed changes
