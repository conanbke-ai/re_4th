# NumPy
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
* 설치 및 기본 사용법
    - pip install numpy
    - conda환경에서
        conda install numpy

* import
    import numpy as np  # Numpy를 np라는 별칭(alias)로 임포트
'''

# 사용 예제 - 배열 생성
import numpy as np

# 리스트를 Numpy 배열로 변환
arr = np.array([1, 2, 3, 4, 5])
print(arr)  # [1 2 3 4 5]
print(type(arr))    # <class 'numpy.ndarray'>

'- np.array() : 파이썬 리스트나 튜플을 Numpy 배열로 변환'

'''
ndarray
    Numpy의 핵심 데이터 구조, 동일한 자료형을 가진 다차원 배열
        - Python의 리스트보다 성능과 메모리 효율성에서 우수
        
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

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)  # (2, 3) → 2행 3열
print(a.ndim)   # 2차원

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
np.zeros((2, 3))    # 2행 3열, 값은 모두 0.0

# np.ones(shape) : 모든 요소가 1
np.ones((3, 2))    # 3행 2열, 값은 모두 1

# np.empty(shape) : 초기화되지 않은 배열(쓰레기 값)
np.empty((2, 2))    # 값이 초기화되지 않음 → 빠르지만 위험

# np.full(shape, value) : 주어진 값으로 채운 배열
np.full((2, 2), 7)    # [[7 7]
                      #  [7 7]]
                      
# np.eye(N, M=None, k=0)
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
                    
'''
범위 기반 배열
'''
# arange
# np,arange(start, stop, step) : range() 와 유사함
#   시작(start)이상 ~ 끝(stop) 미만의 정수 배열을 step 간격으로 생성
np.arange(0, 10, 2) # [0 2 4 6 8]

# linspace
# np.linspace(start, stop, num)
#   시작(start) ~ 끝(stop)까지 균일 간격으로 num 개 생성
np.linspace(0, 1, 5)    # []