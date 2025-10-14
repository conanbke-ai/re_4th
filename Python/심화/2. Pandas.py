# ============================================================================
# 데이터 분석 프로세스 개요
# ============================================================================
"""
데이터 분석의 6단계:
    1. 데이터 수집 (Data Collection)
       - 분석할 자료를 모으는 단계
       - 예: CSV 파일, 데이터베이스, API, 웹 스크래핑
    
    2. 데이터 정제 (Data Cleaning)
       - 분석 가능한 형태로 만드는 단계
       - 결측치 처리, 중복 제거, 데이터 타입 변환
    
    3. 데이터 탐색 (Data Exploration)
       - 데이터의 특성을 파악하는 단계
       - 기술 통계, 분포 확인, 패턴 탐색
    
    4. 데이터 분석 (Data Analysis)
       - 가설을 검증하고 패턴을 찾는 단계
       - 통계 분석, 머신러닝 모델 적용
    
    5. 시각화 (Visualization)
       - 결과를 이해하기 쉽게 표현하는 단계
       - 그래프, 차트, 대시보드
    
    6. 인사이트 도출 (Insight Generation)
       - 분석 결과를 의사결정에 활용하는 단계
       - 비즈니스 액션 아이템 도출

실무 예시 - 편의점 사장님의 고민:
    문제: 어떤 제품을 더 많이 주문해야 할까?
    데이터: 지난 3개월 판매 기록
    분석: 요일별, 시간대별 판매 패턴 파악
    인사이트: 금요일 저녁에 맥주가 가장 많이 팔린다
    행동: 금요일 전에 맥주 재고 확충
"""
######################################################################################################
# Pandas
'''
- Pandas 공식 홈페이지: https://pandas.pydata.org/
- 사용자 가이드: https://pandas.pydata.org/docs/user_guide/index.html
- Pandas 튜토리얼: https://pandas.pydata.org/pandas-docs/stable/getting_started/tutorials.html

파이썬 기반의 강력하고 사용하기 쉬운 데이터 분석 및 조작 라이브러리
    - 구조화된 데이터나 표 형식의 데이터를 빠르고 쉽게 다룰 수 있음
    - 활용분야 : 데이터 분석 및 전처리, 통계 분석 및 리포팅, 금융, 통계, 연구, 빅데이터 등 다양한 산업 분야

* 주요 특징
    - 데이터 처리 용이성 : 데이터 분석에 필요한 다양한 연산을 쉽고 효율적으로 지원
    - 강력한 입출력(I/O) : 다양한 파일 및 데이터베이스 포맷과 호환
    - 데이터 클린징과 전처리, 통계 분석, 시계열 분석 등 고급 데이터 분석 기능 내장
        cef) Exel은 시각적으로 친숙하나 대규모 데이터, 자동화, 복잡한 데이터 조작에는 한계가 있음

* 설치
# pip로 설치
pip install pandas

# conda 가상환경에서 설치
# 가상환경 진입 후
conda install pandas
'''
import pandas as pd

# 설치된 pandas 버전 확인
print(pd.__version__)

######################################################################################################
# 자료구조
# Series
'''
인덱스(라벨)이 붙은 1차원 배열
    - 1차원 배열 구조(벡터 구조)
    - 각 데이터에 대해 인덱스(라벨) 부여 가능
        - Numpy 배열은 인덱스가 정수 0, 1, 2, ... 이지만, Series는 문자열 등 임의의 인덱스 가능
    - Numpy 배열과 비슷하게 다양한 연산 지원
    - 데이터와 인덱스(index)가 함께 저장됨
    - 동일 타입 : 하나의 Series 안의 모든 데이터는 같은 타입임


* Series의 3가지 핵심 구성요소:
    
    1. Value (값)
       - 실제 데이터가 저장되는 부분
       - Numpy 배열로 내부 저장됨
       - 빠른 수치 연산 가능
    
    2. Index (인덱스)
       - 각 값을 식별하는 레이블 (행 번호)
       - 기본값: 0, 1, 2, ... (정수)
       - 사용자 정의 가능 (문자열, 날짜 등)
       - 데이터 검색과 정렬의 기준
    
    3. Name (이름)
       - Series 전체를 설명하는 이름
       - 선택사항 (없어도 작동함)
       - DataFrame 결합 시 컬럼명으로 사용됨

* pd.Series() 함수의 매개변수:
    
    pd.Series(data=None, index=None, dtype=None, name=None)
    
    - data: 실제 데이터 (필수)
            리스트, 딕셔너리, 스칼라값, Numpy 배열 가능
    
    - index: 인덱스 레이블 (선택)
             기본값은 0, 1, 2, ...
             리스트, 배열 등으로 사용자 지정 가능
    
    - dtype: 데이터 타입 (선택)
             자동 추론되지만 명시적으로 지정 가능
    
    - name: Series 이름 (선택)
            메타데이터로 활용

* 주요 속성
속성            설명
.values         Series의 실제 데이터(Numpy 배열)
.index          인덱스 객체(index)
.dtype          데이터 타입
.size           원소 개수
.shape          배열의 형태(튜플)
.name           Series의 이름
.ndim           차원(Series는 항상 1)

* dtype이 중요한 이유:
    1. 메모리 사용량 결정
       - int8: 1바이트 (-128~127)
       - int64: 8바이트 (-9경~9경)
    
    2. 연산 가능 여부
       - 숫자 타입: 사칙연산 가능
       - 문자열 타입: 연결, 분할 가능
    
    3. 성능에 영향
       - 적절한 타입 선택으로 속도 향상
'''
# 데이터 타입
# 정수형 Series
int_series = pd.Series([1, 2, 3, 4, 5])
print(f'[3-1] Integer Series dtype: {int_series.dtype}')
print(int_series)
print()

# 실수형 Series
float_series = pd.Series([1.1, 2.2, 3.3, 4.5, 5.6])
print(f'[3-2] Float Series dtype: {float_series.dtype}')
print(float_series)
print()

# 문자열 Series (object 타입으로 저장됨)
str_series = pd.Series(['Apple', 'Banana', 'Cherry'])
print(f'[3-3] String Series dtype: {str_series.dtype}')
print(str_series)
print()

# 불린형 Series
bool_series = pd.Series([True, False, True])
print(f'[3-4] Boolean Series dtype: {bool_series.dtype}')
print(bool_series)
print()

# 혼합형 Series (자동으로 float로 변환)
mixed_series = pd.Series([1, 2.5, 3])
print(f'[3-5] Mixed Series dtype: {mixed_series.dtype} (자동 변환)')
print(mixed_series)
print()

# 리스트로 생성
# 파이썬 리스트를 이용한 Series 생성
data = [10, 20, 30, 40]
s = pd.Series(data)
print(s)
# 0    10
# 1    20
# 2    30
# 3    40
# dtype: int64
'- 기본 인덱스(정수형)이 자동부여됨'

# 모든 구성요소를 포함한 Series
data_series = pd.Series(
    data=[10, 20, 30, 40, 50],                              # 값: 실제 저장된 데이터
    index=['Alice', 'Bob', 'Charlie', 'David', 'Eve'],      # 인덱스: 각 값의 레이블
    name='Test_Score'                                       # 이름: Series 전체의 이름
)

# 리스트 + 인덱스 지정
# 인덱스(index)를 직접 지정
s2 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(s2)
# a    10
# b    20
# c    30
# d    40
# dtype: int64
'- 인덱스를 원하는 값(문자열 등)으로 지정 가능'

# 날짜 인덱스
temp_list = [15.5, 17.2, 18.9, 19.1, 20.1]
temp = pd.Series(temp_list, name='4월_기온')

date = pd.date_range('2025-04-01', periods=5)  # 5일간의 날짜 생성
print("생성된 날짜 인덱스:")
print(date)
# DatetimeIndex(['2025-04-01', '2025-04-02', '2025-04-03', '2025-04-04',
#                '2025-04-05'],      
#               dtype='datetime64[ns]', freq='D')

temp_date = pd.Series(temp_list, index=date, name='4월_기온')
print("날짜 인덱스를 가진 기온 데이터:")
print(temp_date)
# 2025-04-01    15.5
# 2025-04-02    17.2
# 2025-04-03    18.9
# 2025-04-04    19.1
# 2025-04-05    20.1
# Freq: D, Name: 4월_기온, dtype: float64

# 딕셔너리로 생성
# 딕셔너리를 이용한 Series 생성
# 키-인덱스, 값-데이터
d = {'서울': 100, '부산':200, '대구':300}
s3 = pd.Series(d)
print(s3)
# 서울    100
# 부산    200
# 대구    300
# dtype: int64
'- 딕셔너리의 키가 인덱스, 값이 데이터가 됨'

# 스칼라 값 + 인덱스
# 하나의 값으로 Series 전체를 채우고 싶을 때
s4 = pd.Series(
    7, # 모든 값을 7로 초기화
    index=['a', 'b', 'c']
)
print(s4)
# a    7
# b    7
# c    7
# dtype: int64

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print("values:", s.values)      # 실제 데이터 배열
print("index:", s.index)        # 인덱스 객체
print("dtype:", s.dtype)        # 데이터 타입
print("size:", s.size)          # 데이터 개수
print("shape:", s.shape)        # 배열의 형태
print("name:", s.name)          # Series 이름(기본은 None)

# values: [10 20 30]
# index: Index(['a', 'b', 'c'], dtype='object')
# dtype: int64
# size: 3
# shape: (3,)
# name: None

# ============================================================================
# 6. 인덱싱 (Indexing) - 특정 데이터 선택
# ============================================================================
"""
인덱싱이란?
    - Series에서 특정 데이터를 선택하는 방법
    
두 가지 방식:
    1. 위치 기반 (Position-based): 0, 1, 2, ... (정수)
       - iloc[] 사용
       - 항상 0부터 시작하는 정수 인덱스
    
    2. 레이블 기반 (Label-based): 인덱스 이름으로 접근
       - loc[] 사용
       - 사용자가 지정한 인덱스 이름 사용
"""

sales = pd.Series(
    [100, 200, 150, 300],
    index=['Mon', 'Tue', 'Wed', 'Thu'],
    name="Daily_Sales"
)

print("=" * 80)
print("[6] 인덱싱 - 특정 데이터 선택")
print("=" * 80)
print("\n원본 데이터:")
print(sales)
print()

# 레이블 기반 인덱싱
print("[6-1] 레이블 기반 인덱싱")
wed_sales = sales['Wed']
print(f"sales['Wed'] = {wed_sales}")

wed_sales_loc = sales.loc['Wed']
print(f"sales.loc['Wed'] = {wed_sales_loc}")
print()

# 위치 기반 인덱싱
print("[6-2] 위치 기반 인덱싱 (0부터 시작)")
wed_sales_iloc = sales.iloc[2]  # 세 번째 요소 (0, 1, 2)
print(f"sales.iloc[2] = {wed_sales_iloc}")
print()

# 여러 개 선택
print("[6-3] 여러 개 선택 (리스트 사용)")
selected_days = sales[['Mon', 'Wed', 'Thu']]
print(selected_days)
print()

# ============================================================================
# 7. 슬라이싱 (Slicing) - 범위 선택
# ============================================================================
"""
슬라이싱이란?
    - 연속된 여러 개의 데이터를 선택하는 방법
    
주의사항:
    - loc[시작:끝]: 끝 포함 (inclusive)
    - iloc[시작:끝]: 끝 제외 (exclusive)
"""

print("=" * 80)
print("[7] 슬라이싱 - 범위 선택")
print("=" * 80)

print("\n[7-1] 레이블 기반 슬라이싱 (끝 포함)")
print("처음부터 수요일까지:")
print(sales.loc[:'Wed'])
print()

print("[7-2] 수요일부터 끝까지:")
print(sales.loc['Wed':])
print()

print("[7-3] 위치 기반 슬라이싱")
print("전체 선택:")
print(sales.iloc[:])
print()

print("[7-4] 역순으로 선택:")
print(sales.iloc[::-1])
print()

# ============================================================================
# 8. Boolean 인덱싱 - 조건으로 선택
# ============================================================================
"""
Boolean 인덱싱이란?
    - 조건을 만족하는 데이터만 선택하는 방법
    - SQL의 WHERE 절과 유사
    
작동 원리:
    1. 조건식을 작성 (예: sales >= 200)
    2. True/False로 구성된 Boolean Series 생성
    3. True인 위치의 값만 선택
"""

print("=" * 80)
print("[8] Boolean 인덱싱 - 조건으로 선택")
print("=" * 80)

sales = pd.Series(
    [100, 200, 150, 300],
    index=['Mon', 'Tue', 'Wed', 'Thu'],
    name="Daily_Sales"
)

print("\n원본 데이터:")
print(sales)
print()

# 조건 생성
print("[8-1] 조건 생성 (sales >= 200)")
condition = sales >= 200
print(condition)
print()

# 조건에 맞는 데이터 선택
print("[8-2] 조건에 맞는 데이터 선택")
result = sales[condition]
print(result)
print()

# ============================================================================
# 9. 비교 연산자
# ============================================================================
"""
비교 연산자:
    ==  : 같음
    !=  : 다름
    >   : 크다
    <   : 작다
    >=  : 크거나 같다
    <=  : 작거나 같다

논리 연산자:
    &   : AND (그리고)
    |   : OR (또는)
    ~   : NOT (부정)
    
주의: Python의 and, or가 아닌 &, | 사용
"""

print("=" * 80)
print("[9] 비교 연산자와 논리 연산자")
print("=" * 80)

print("\n[9-1] 같음 (==)")
print(sales[sales == 200])
print()

print("[9-2] AND 연산 (&) - 두 조건 모두 만족")
print("150 이상 350 이하:")
print(sales[(sales >= 150) & (sales <= 350)])
print()

print("[9-3] OR 연산 (|) - 둘 중 하나라도 만족")
print("150 미만 또는 300 이상:")
print(sales[(sales < 150) | (sales >= 300)])
print()

print("[9-4] 다름 (!=)")
print("200이 아닌 값:")
print(sales[sales != 200])
print()

# ============================================================================
# 10. 복합 조건
# ============================================================================
"""
복합 조건:
    - 여러 조건을 조합하여 사용
    - 괄호를 사용하여 우선순위 명확히 표시
"""

print("=" * 80)
print("[10] 복합 조건")
print("=" * 80)

sales = pd.Series(
    [100, 200, 150, 300, 250],
    index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    name="Daily_Sales"
)

print("\n원본 데이터:")
print(sales)
print()

# 예제 1: 평일 중 200 이상
print("[10-1] 평일 중 매출 200 이상")
weekday_high = sales[(sales >= 200) & (sales.index != 'Fri')]
print(weekday_high)
print()

# 예제 2: isin() 메서드 사용
print("[10-2] 특정 요일 또는 매출 200 미만")
weekend_or_low = sales[(sales < 200) | sales.index.isin(['Mon', 'Fri'])]
print(weekend_or_low)
print()

# ============================================================================
# 11. 벡터화 연산 (Vectorized Operations)
# ============================================================================
"""
벡터화 연산이란?
    - 반복문 없이 전체 데이터에 한 번에 연산 적용
    - Numpy 기반으로 매우 빠른 속도
    - 코드가 간결하고 읽기 쉬움

장점:
    1. 속도: 반복문보다 10~100배 빠름
    2. 간결성: 코드가 짧고 명확
    3. 가독성: 의도가 명확하게 드러남
"""

print("=" * 80)
print("[11] 벡터화 연산")
print("=" * 80)

prices = pd.Series(
    [3000, 1500, 4000, 2000],
    index=['apple', 'banana', 'orange', 'grape'],
    name='Price'
)

print("\n원본 가격:")
print(prices)
print()

print("[11-1] 덧셈: 모든 가격에 500원 추가")
print(prices + 500)
print()

print("[11-2] 뺄셈: 모든 가격에서 1000원 할인")
print(prices - 1000)
print()

print("[11-3] 곱셈: 20% 할인 (0.8 곱하기)")
print(prices * 0.8)
print()

print("[11-4] 나눗셈: 반값")
print(prices / 2)
print()

# ============================================================================
# 12. Series 간 연산
# ============================================================================
"""
Series 간 연산:
    - 같은 인덱스끼리 자동으로 매칭되어 연산
    - 인덱스가 다르면 NaN (Not a Number) 반환
    
정렬 방식:
    - 인덱스를 기준으로 자동 정렬 (Alignment)
    - SQL의 JOIN과 유사한 개념
"""
# Series 연산
s1 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
s2 = pd.Series([1, 2, 3], index=['b', 'c', 'd'])

# 덧셈(같은 인덱스끼리 연산, 일치하지 않으면 Nan)
result = s1 + s2
print(result)
# a     NaN
# b    21.0
# c    32.0
# d     NaN
# dtype: float64
'- 인덱스가 일치하는 값만 연산, 순서가 달라도 인겟스 기준 자동 정렬 후 연산'
'- 일치하지 않는 인덱스는 NaN(Not a Number, 결측값)으로 표시됨'

s = pd.Series([5, 10, 15], index=['x', 'y', 'z'])

# 모든 원소에 3을 더함
print(s + 3)
# x     8
# y    13
# z    18
# dtype: int64

# 모든 원소에 2배 곱함
print(s * 2)
# x    10
# y    20
# z    30
# dtype: int64

'- Series에 스칼라 값을 연산하면 각 원소에 일괄 적용됨'

# ============================================================================
# 13. NaN (결측값) 처리하며 연산하기
# ============================================================================
"""
NaN (Not a Number) 처리 방법:
    
    1. fill_value 사용
       - 없는 값을 특정 값으로 채워서 연산
    
    2. reindex() 사용
       - 인덱스를 미리 맞춘 후 연산
    
    3. dropna() 사용
       - 결측값을 제거한 후 연산
"""

print("=" * 80)
print("[13] NaN (결측값) 처리")
print("=" * 80)

# 방법 1: fill_value 사용
print("\n[13-1] fill_value로 없는 값을 0으로 채워서 연산")
price_diff_filled = store_b.sub(store_a, fill_value=0)
print(price_diff_filled)
print("설명: Grape는 2500 - 0으로 계산됨")
print()

# 방법 2: reindex로 먼저 맞추기
print("[13-2] reindex로 인덱스를 먼저 맞추기")
store_a_reindexed = store_a.reindex(store_b.index, fill_value=0)
print("인덱스를 맞춘 Store A:")
print(store_a_reindexed)
print()

price_diff_reindexed = store_b - store_a_reindexed
print("재계산된 가격 차이:")
print(price_diff_reindexed)
print()

# 방법 3: dropna로 결측값 제거
print("[13-3] dropna()로 NaN 제거")
price_diff_cleaned = price_diff.dropna()
print(price_diff_cleaned)
print("설명: NaN이 있던 Banana와 Grape가 제거됨")
print()

# ============================================================================
# 14. 비교 연산과 조건부 선택
# ============================================================================
"""
where() 메서드:
    - 조건에 따라 값을 선택적으로 유지하거나 대체
    - Series.where(조건, 대체값)
    - 조건이 True인 값만 유지, False는 대체값으로
"""

print("=" * 80)
print("[14] 비교 연산과 조건부 선택")
print("=" * 80)

store_a = pd.Series(
    [1000, 2000, 1500],
    index=['Apple', 'Pear', 'Orange'],
    name='Store_A'
)

store_b = pd.Series(
    [900, 2200, 1400],
    index=['Apple', 'Pear', 'Orange'],
    name='Store_B'
)

print("\nStore A 가격:")
print(store_a)
print()

print("Store B 가격:")
print(store_b)
print()

# Store A가 더 비싼 경우 찾기
print("[14-1] B상점이 더 저렴한 제품 찾기")
is_b_cheaper = store_a > store_b
print(is_b_cheaper)
print()

# 더 저렴한 매장의 가격만 선택
print("[14-2] 각 제품별 최저가 선택")
best_prices = store_a.where(is_b_cheaper, store_b)
print(best_prices)
print("설명:")
print("  - Apple: B가 더 저렴 (900 < 1000)")
print("  - Pear: A가 더 저렴 (2000 < 2200)")
print("  - Orange: B가 더 저렴 (1400 < 1500)")
print()

######################################################################################################
# 실습 1 Series 연습
'''
1. 파이썬 리스트 [5, 10, 15, 20]을 이용해 Series를 생성하세요.
'''
list = [5, 10, 15, 20]
s = pd.Series(list)
print(s)
# 0     5
# 1    10
# 2    15
# 3    20
# dtype: int64

'''
2. 값 [90, 80, 84, 70]에 대해 인덱스를 각각 '국어', '영어', '수학', '과학' 으로 지정한 Series를 만드세요.
'''
s = pd.Series([90, 80, 84, 70], index=['국어', '영어', '수학', '과학'])
print(s)
# 국어    90
# 영어    80
# 수학    84
# 과학    70
# dtype: int64

'''
3. {'서울':950, '부산':340, '인천':520} 딕셔너리를 이용해 Series를 만들고, 인천의 값을 출력하세요.
'''
s = pd.Series({'서울':950, '부산':340, '인천':520})
print(s)
# 서울    950
# 부산    340
# 인천    520
# dtype: int64

'''
4. Series [1, 2, 3, 4]를 만들고, 데이터 타입(dtype)을 출력하세요.
'''
s = pd.Series([1, 2, 3, 4])
print("datatype:", s.dtype)
# datatype: int64

'''
5. 아래 두 Series의 합을 구하세요.
    - s1 = pd.Series([3, 5, 7], index=['a', 'b', 'c'])
    - s2 = pd.Series([10, 20, 30], index=['b', 'c', 'd'])
'''
s1 = pd.Series([3, 5, 7], index=['a', 'b', 'c'])
s2 = pd.Series([10, 20, 30], index=['b', 'c', 'd'])

print(s1 + s2)
# a     NaN
# b    15.0
# c    27.0
# d     NaN
# dtype: float64

'''
6. Series [1, 2, 3, 4, 5]의 각 값에 10을 더한 Series를 만드세요.
'''
s1 = pd.Series([1, 2, 3, 4, 5])
s2 = s1 + 10
print(s2)
# 0    11
# 1    12
# 2    13
# 3    14
# 4    15
# dtype: int64

######################################################################################################
# 통계 함수
# 데이터의 특징을 숫자로 요약하는 것

# 한 달간 일일 매출 데이터
daily_sales = pd.Series([
    302, 423, 123, 437, 890,
    124, 781, 920, 478, 901,
    241, 891, 123, 678, 912,
    367, 894, 355, 123, 674,
    891, 234, 678, 943, 524,
    782, 394, 327, 891, 237
],
    index=pd.date_range('2025-09-01', periods=30),
    name='Sales'
)
# 평균(mean) : 모든 값의 합 / 개수
mean_value = daily_sales.mean()
print(f'1. 평균 (Mean): {mean_value:.2f}만원')

# 중앙값(Median) : 정렬헀을 때 가운데 값
median_value = daily_sales.median()
print(f'2. 중앙값 (Median): {median_value}만원')

# 최빈값 (Mode) : 가장 자주 나타나는 값
mode_value = daily_sales.mode()
print(f'3. 최빈값 (Mode):\n {mode_value}만원')
print()

# 산포도 측정
# 데이터가 얼마나 퍼져있는지 알려주는 통계량
print('=== 산포도 측정 ===')
max_value = daily_sales.max()
min_value = daily_sales.min()

print(f'1. 최댓값: {max_value}')
print(f'2. 최솟값: {min_value}')

# 평균(mean) : 모든 값의 합 / 개수
mean_value = daily_sales.mean()
print(f'1. 평균 (Mean): {mean_value:.2f}만원')

# 범위 (Range): 최댓값 - 최솟값
range_value = max_value - min_value
print(f'3. 범위 (Range): {range_value}')

# 분산 (Variance) :평균으로부터 떨어진 정도의 제곱의 평균
variance = daily_sales.var()
print(f'4. 분산 (Variance): {variance:.2f}')

# 표준편차 (Standard Deviation): 분산의 제곱근
std_dev = daily_sales.std()
print(f'4. 표준편차 (Std Dev): {std_dev:.2f}')

# 표준편차 해석
print('표준편차 해석:')
print(f'평균 표준편차: {mean_value - std_dev:.2f} ~ {mean_value + std_dev:.2f}')
print()

# 한번에 모든 통계
print(daily_sales.describe())

######################################################################################################
# 자료구조
# DataFrame
'''
행과 열로 구성된 2차원 라벨 데이터 구조
    - 2차원 테이블 구조(행(Row)-열(Column))
    - 각 열은 서로 다른 자료형 가능 (예: 숫자 + 문자열 혼합)
    - 행 인덱스와 열 이름으로 데이터 접근
    - 엑셀 표, SQL 테이블과 유사
    - NumPy의 2차원 배열보다 더 강력한 라벨링 및 데이터 관리 기능
    - Series의 집합
    - 이름(rabel) 기반
    - 혼합 타입 가능

* DataFrame의 3가지 핵심 구성 요소:

    1. 데이터 (Values/Data)
       - 실제 저장된 값들
       - 2차원 배열(행렬) 형태
       - Numpy 배열로 내부 저장
    
    2. 행 인덱스 (Index)
       - 각 행을 식별하는 레이블
       - 기본값: 0, 1, 2, 3, ...
       - 사용자 정의 가능: 'E001', 'E002', ...
       - 행 데이터를 찾는 데 사용
    
    3. 열 이름 (Columns)
       - 각 열을 식별하는 레이블
       - 필드명, 속성명으로 사용
       - 예: 'name', 'age', 'salary'
       - 열 데이터를 찾는 데 사용

시각적 구조:
    
                   Columns (열 이름)
              ┌─────────┬─────┬────────┐
              │  name   │ age │ salary │
    ┌─────────┼─────────┼─────┼────────┤
    │  E001   │  김철수  │ 27  │  4500  │ ← Row (행)
Index├─────────┼─────────┼─────┼────────┤
(행   │  E002   │  이영희  │ 23  │  4800  │ ← Row (행)
인덱스)└─────────┴─────────┴─────┴────────┘
                    ↑       ↑      ↑
                 Column  Column Column

* 주요 속성/메서드
속성/메서드         설명
.shape             (행 개수, 열 개수)
.columns            컬럼명(index 객체)
.index              행 인덱스(index 객체)
.dtypes             각 컬럼의 데이터 타입
.info()             DataFrame 전체 정보(행/열, 타입 등)
.head()             상위 5개 행 미리보기
.tail()             하위 5개 행 미리보기
.values             실제 데이터(Numpy 2차원 배열)
.describe()         수치형 컬럼에 대한 요약 통계량

* Series vs DataFrame 비교
┌─────────────────┬──────────────────────┬──────────────────────┐
│     특징        │       Series         │      DataFrame       │
├─────────────────┼──────────────────────┼──────────────────────┤
│ 차원            │ 1차원                │ 2차원                │
│ 구조            │ 값 + 인덱스          │ 값 + 인덱스 + 열이름 │
│ 비유            │ Excel의 한 개 열     │ Excel의 전체 시트    │
│ 데이터 타입     │ 단일 타입            │ 열마다 다른 타입     │
│ 생성            │ pd.Series()          │ pd.DataFrame()       │
│ 인덱싱          │ s[0], s['index']     │ df['col'], df.loc[]  │
└─────────────────┴──────────────────────┴──────────────────────┘

관계:
    DataFrame = 여러 개의 Series를 열로 결합한 것
    DataFrame의 한 개 열 = Series
'''
# 딕셔너리로 생성
# 딕셔너리의 key가 컬럼명, value가 각 컬럼의 값 리스트가 됨
data = {
    '이름': ['홍길동', '김철수', '이영희'],
    '나이': [28, 31, 24],
    '도시': ['서울', '부산', '대구']
}
df = pd.DataFrame(data)
print(df)
#     이름  나이  도시
# 0  홍길동  28  서울
# 1  김철수  31  부산
# 2  이영희  24  대구

# 리스트의 리스트로 생성(각 내부 리스트가 한 행(행 기준))
df2 = pd.DataFrame(
    [[1, 'A'], [2, 'B'], [3, 'C']],
    columns=['번호', '코드']
)
print(df2)
#    번호 코드
# 0   1  A
# 1   2  B
# 2   3  C
'- 컬럼명을 지정하지 않을 시 정수로 넘버링됨'

# 딕셔너리 리스트로 생성(각 행이 딕셔너리/JSON 구조와 유사)
# 각 행을 하나의 딕셔너리로 표현
data = [
    {'이름': '홍길동', '나이': 28, '도시': '서울'},
    {'이름': '김철수', '나이': 31, '도시': '부산'}
]
df3 = pd.DataFrame(data)
print(df3)
#     이름  나이  도시
# 0  홍길동  28  서울
# 1  김철수  31  부산
'- key : 컬럼명, value : 해당 컬럼의 값'

# Series의 딕셔너리로 생성(Series 결합/각 열이 별도의 Series)
# 각 Series가 컬럼으로 들어감(index 자동 정렬)
s1 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
s2 = pd.Series([40, 50, 60], index=['a', 'b', 'c'])
df4 = pd.DataFrame({'col1': s1, 'col2': s2})
print(df4)
'- 각 Series가 컬럼으로 들어감 (index 자동 정렬)'
#    col1  col2
# a    10    40
# b    20    50
# c    30    60

# Numpy 배열로 생성
import numpy as np

data_array = np.array([
    [27, 4500],
    [23, 4800],
    [35, 5200]
])

employees_numpy = pd.DataFrame(
    data_array,
    columns=['age', 'salary'],
    index=['E001', 'E002', 'E003']
)

print(employees_numpy)

# 직원 정보를 담은 DataFrame
test_data = pd.DataFrame(
    # 1. 데이터 (Value) - 2차원 리스트
    data=[
        ['김철수', 27, "Dev", 4500],
        ['이영희', 23, "HR", 4800],
    ],
    # 2. 행 인덱스(index) - 각 행의 레이블 (사원 번호)
    index=['E001', 'E002'],
    # 3. 열 이름 (columns) - 각 열의 레이블 (필드명)
    columns=['name', 'age', 'department', 'salary']
)

print("\n생성된 DataFrame:")
print(test_data)

# CSV, 엑셀 등 파일로부터 생성
# CSV 파일 불러오기 예시
df_csv = pd.read_csv('sample.csv')
print(df_csv.head())
'- read_csv() : 파일에서 DataFrame 생성'
'- CSV(Comma-Separated Values) : 데이터를 쉼표(,)로 구분하여 저장하는 텍스트 기반의 표 형식 파일'

# 사용 예제 - DataFrame의 주요 속성/메서드
df = pd.DataFrame({
    '이름' : ['홍길동', '김철수', '이영희'],
    '나이' : [28, 31, 24], 
    '도시' : ['서울', '부산', '대구']
})

print("shape", df.shape)          # (행, 열) 튜플 반환
print("columns", df.columns)      # 컬럼명(index)
print("index", df.index)          # 행 인덱스(index)
print("dtypes", df.dtypes)        # 각 컬럼 데이터 타입
print("values", df.values)        # Numpy 2차원 배열

# shape (3, 3)
# columns Index(['이름', '나이', '도시'], dtype='object')
# index RangeIndex(start=0, stop=3, step=1)

# dtypes 이름    object
# 나이     int64
# 도시    object
# dtype: object

# values [['홍길동' 28 '서울']       
#  ['김철수' 31 '부산']
#  ['이영희' 24 '대구']]

# 4-1. 행 인덱스 (Index)
print("\n[2-1] 행 인덱스 (Index)")
print(f"      타입: {type(test_data.index)}")
print(f"      값: {test_data.index.tolist()}")
print(f"      설명: 각 행(직원)을 구분하는 고유 식별자")
print()

# 4-2. 열 이름 (Columns)
print("[2-2] 열 이름 (Columns)")
print(f"      타입: {type(test_data.columns)}")
print(f"      값: {test_data.columns.tolist()}")
print(f"      설명: 각 열(속성)의 이름")
print()

# 4-3. 데이터 형태 (Shape)
print("[2-3] 데이터 형태 (Shape)")
print(f"      값: {test_data.shape}")
print(
    f"      의미: (행 개수, 열 개수) = ({test_data.shape[0]}행, {test_data.shape[1]}열)")
print(f"      설명: 2명의 직원, 4개의 속성")
print()

# 4-4. 행 개수
print("[2-4] 행 개수")
print(f"      값: {test_data.shape[0]}")
print(f"      또는: {len(test_data)}")
print(f"      설명: 총 {test_data.shape[0]}명의 직원 데이터")
print()

# 4-5. 열 개수
print("[2-5] 열 개수")
print(f"      값: {test_data.shape[1]}")
print(f"      또는: {len(test_data.columns)}")
print(f"      설명: 각 직원마다 {test_data.shape[1]}개의 정보")
print()

# 4-6. 전체 셀 개수
print("[2-6] 전체 셀(데이터) 개수")
print(f"      값: {test_data.size}")
print(
    f"      계산: {test_data.shape[0]} × {test_data.shape[1]} = {test_data.size}")
print(f"      설명: 총 {test_data.size}개의 데이터 포인트")

# 7-1. head() - 처음 n개 행
print("\n[5-1] head() - 처음 5개 행 (기본값)")
print(df.head())
print()

print("[5-2] head(2) - 처음 2개 행")
print(df.head(2))
print()

# 7-2. tail() - 마지막 n개 행
print("[5-3] tail() - 마지막 5개 행 (기본값)")
print(df.tail())
print()

print("[5-4] tail(2) - 마지막 2개 행")
print(df.tail(2))
print()

# 7-3. info() - 전체 정보 요약
print("[5-5] info() - DataFrame 전체 정보")
df.info()
print()

# 7-4. describe() - 수치형 데이터 통계
print("[5-6] describe() - 수치형 열의 통계 요약")
print(df.describe())

# ============================================================================
# 9. 실무 예제 - 직원 데이터 분석
# ============================================================================

print("=" * 80)
print("[7] 실무 예제 - 직원 데이터 분석")
print("=" * 80)

# 더 현실적인 직원 데이터
employee_data = pd.DataFrame({
    'employee_id': ['E001', 'E002', 'E003', 'E004', 'E005'],
    'name': ['김철수', '이영희', '박민수', '정수진', '최지훈'],
    'age': [27, 23, 35, 29, 31],
    'department': ['Dev', 'HR', 'Sales', 'Dev', 'Sales'],
    'position': ['Junior', 'Senior', 'Manager', 'Senior', 'Junior'],
    'salary': [4500, 4800, 5200, 4700, 4600],
    'join_year': [2020, 2021, 2018, 2019, 2020]
})

print("\n직원 데이터:")
print(employee_data)
print()

print("=" * 80)
print("데이터 요약:")
print(f"• 총 직원 수: {len(employee_data)}명")
print(f"• 데이터 항목: {employee_data.shape[1]}개")
print(f"• 평균 연봉: {employee_data['salary'].mean():.0f}만원")
print(f"• 평균 나이: {employee_data['age'].mean():.1f}세")
print(f"• 최고 연봉: {employee_data['salary'].max()}만원")
print(f"• 최저 연봉: {employee_data['salary'].min()}만원")
print("=" * 80)

######################################################################################################
# 실습 2 DataFrame 연습

'''
1. 다음 데이터로 DataFrame을 생성하고, 컬럼명을 '이름', '나이', '도시'로 지정하세요.
    - [['홍길동', 28, '서울'], ['김철수', 33, '부산'], ['이영희', 25, '대구']]
'''
df = pd.DataFrame(
    [['홍길동', 28, '서울'], ['김철수', 33, '부산'], ['이영희', 25, '대구']],
    columns=['이름', '나이', '도시']
)
print(df)
#     이름  나이  도시
# 0  홍길동  28  서울
# 1  김철수  33  부산
# 2  이영희  25  대구

'''
2. 아래와 같은 딕셔너리로 DataFrame을 생성하세요.
    - {'A': [1, 2, 3], 'B': [4, 5, 6]}
'''
df = pd.DataFrame(
    {'A': [1, 2, 3], 'B': [4, 5, 6]}
)
print(df)
#    A  B
# 0  1  4
# 1  2  5
# 2  3  6

'''
3. 아래 데이터를 사용해 DataFrame을 만드세요.
    - [{'과목': '수학', '점수': 90}, {'과목': '영어', '점수': 85}, {'과목': '과학', '점수': 95}]
'''
df = pd.DataFrame(
    [{'과목': '수학', '점수': 90}, {'과목': '영어', '점수': 85}, {'과목': '과학', '점수': 95}]
)
print(df)
#    과목  점수
# 0  수학  90
# 1  영어  85
# 2  과학  95

'''
4. 아래 데이터를 사용해 DataFrame을 생성하되, 인덱스를 ['학생1', '학생2', '학생3']으로 지정
하세요.
    - {'이름': ['민수', '영희', '철수'], '점수': [80, 92, 77]}
'''
df = pd.DataFrame(
    {'이름': ['민수', '영희', '철수'], '점수': [80, 92, 77]},
    index=['학생1', '학생2', '학생3']
)
print(df)
#      이름  점수
# 학생1  민수  80
# 학생2  영희  92
# 학생3  철수  77

'''
5. 아래 Series 객체 2개를 이용해 DataFrame을 만드세요.
    - kor = pd.Series([90, 85, 80], index=['a', 'b', 'c'])
    - eng = pd.Series([95, 88, 82], index=['a', 'b', 'c'])
'''
kor = pd.Series([90, 85, 80], index=['a', 'b', 'c'])
eng = pd.Series([95, 88, 82], index=['a', 'b', 'c'])

df = pd.DataFrame({
    'kor': kor,
    'eng': eng
})
print(df)
#    kor  eng
# a   90   95
# b   85   88
# c   80   82

'''
6. 아래 딕셔너리로 DataFrame을 만들고, 컬럼 순서를 ['B', 'A']로 지정해 출력하세요.
    - {'A': [1, 2], 'B': [3, 4]}
'''
df = pd.DataFrame(
    {'A': [1, 2], 'B': [3, 4]},
    columns=['B', 'A']
)
print(df)
#    B  A
# 0  3  1
# 1  4  2

'''
7. 데이터를 DataFrame으로 만들고, 컬럼명을 ['product', 'price', 'stock']으로 변경하세요.
    - [['펜', 1000, 50], ['노트', 2000, 30]]
'''
df = pd.DataFrame(
    [['펜', 1000, 50], ['노트', 2000, 30]],
    columns=['product', 'price', 'stock']
)
print(df)
#   product  price  stock
# 0       펜   1000     50
# 1      노트   2000     30

'''
8. 아래 DataFrame을 생성한 뒤, '국가' 컬럼만 추출하세요.
    - {'국가': ['한국', '일본', '미국'], '수도': ['서울', '도쿄', '워싱턴']}
'''
df = pd.DataFrame(
    {'국가': ['한국', '일본', '미국'], '수도': ['서울', '도쿄', '워싱턴']}
)
print(df.get('국가'))
# 0    한국
# 1    일본
# 2    미국
# Name: 국가, dtype: object

######################################################################################################
# 데이터 입출력
'''
데이터 분석은 다양한 데이터 소스에서 데이터를 불러오고, 가공한 데이터를 다시 파일로 저장하는 과정을 거침
    - Pandas는 CSV, Excel, JSON, Google sheet 등 여러 포맷의 입출력 기능을 지원
    - 쉼표(,)로 구분 가능한 파일 처리
    - 가볍고 빠름

* csv 파일 불러오기
    pd.read_csv('파일경로/파일명.csv', 옵션...)

    * 주요 옵션
        - sep : 구분자 지정(기본값, )
        - encoding : 문자 인코딩 지정(예:'utf-8', 'cp949')
        - header : 헤더(열 이름) 지정
        - index_col : 특정 열을 인덱스로 사용

* csv 파일로 저장
    df.to_csv('저장경로/파일명.csv', 옵션...)

    * 주요 옵션
        - index : 인덱스 포함 여부(기본값 : True)
        - encoding : 문자 인코딩
        - sep : 구분자 지정
'''
# csv 파일 불러오기
df = pd.read_csv('sample.csv')
print(df.head())
'- read_csv() : 파일에서 DataFrame 생성'

# csv 파일로 저장 예시
# 인덱스 포함 저장
df.to_csv('result_csv')

# 인덱스없이 저장
df.to_csv('result_noindex.csv', index=False)

# 한글 포함 파일 저장(인코딩 저장)
df.to_csv('result_kor.csv', encoding='cp949')

# 사용 예제
sample_data = pd.DataFrame(
    {
        'name': ['kim', 'lee', 'park'],
        'age': [21, 30, 27],
        'city': ['Seoul', 'Busan', 'Daegu'],
        'salary': [3000, 5000, 4500]
    }
)

sample_data.to_csv('sample_data.csv', index=False)
sample_data.to_csv('sample_data_index.csv', index=True)

df = pd.read_csv('sample_data.csv')
print(df)
print(f'데이터 타입:\n{df.dtypes}')
print(f'데이터 배열 크기: {df.shape}')

# 데이터 타입:
# name      object
# age        int64
# city      object
# salary     int64
# dtype: object
# 데이터 배열 크기: (3, 4)

sample_data_kor = pd.DataFrame(
    {
        'name': ['kim', 'lee', 'park'],
        'age': [21, 30, 27],
        'city': ['서울', '부산', '대구'],
        'salary': [3000, 5000, 4500]
    }
)

sample_data_kor.to_csv('sample_data_kor.csv', index=False, encoding='utf-8-sig')

df_kor = pd.read_csv('sample_data_kor.csv')
print(df_kor)

# seq 구분자 설정
sample_data.to_csv('sample_data_seq.txt', sep='\t', index=False)

df_tab = pd.read_csv('sample_data_seq.txt', sep='\t', index=False)
print(df_tab)

'''
* Excel 파일 불러오기
    df = pd.read_excel('파일경로/파일명.xlsx', 옵션...)

    * 주요 옵션
        - sheet_name : 불러올 시트 이름 또는 번호(기본값 0)
        - header, index_col, usecols 등
    
    * 특징
        - 마이크로소프트의 스프레드시트 프로그램
        - 여러 시트(sheet) 지원
        - 서식, 수식 포함 가능
        - 확장자 : 최신(.xlsx)/구버전(.xls)

    * openpyxl 설치
        # pip로 설치
        pip install openpyxl

        # conda 환경에서 설치
        # 가상환경 진입 후
        conda install openpyxl
    
    * 기본 문법
    # Excel 파일의 첫 번째 시트 불러오기
    df = pd.read_excel('sample.xlsx')

    # 특정 시트 불러오기
    df_sheet = pd.read_excel('sample.xlsx', sheet_name='매출데이터')

    # 여러 시트 불러오기(딕셔너리 형태로 반환)
    df_dict = pd.read_excel('sample.xlsx', sheet_name=['Sheet1', 'Sheet2'])

    - sheet_name= : 해당 시트만 불러옴
    - 여러 시트를 동시에 불러오면 딕셔너리로 반환됨

* Excel 파일로 저장
    df.to_excel('저장경로/파일명.xlsx', 옵션...)

    * 주요 옵션
        - index : 인덱스 포함 여부
        - sheet_name : 저장할 시트 이름
    
    * 기본 문법
    # 기본 사용법
    df.to_excel('result.xlsx')

    # 인덱스 없이 시트명 지정
    df.to_excel('result_sheet.xlsx', index=False, sheet_name='분석결과')
'''
# 엑셀 데이터 생성
sample_data.to_excel('sample_data.xlsx', index=False, sheet_name='sample')

excel_data = pd.read_excel('sample_data.xlsx')
print(excel_data)

# 엑셀 데이터 생성 - with 사용하여 여러 sheet 생성하기
with pd.ExcelWriter('multi_sheet.xlsx') as writer:
    sample_data.to_excel(writer, sheet_name='Defalut', index=Fasle)
    sample_data['name'].to_excel(writer, sheet_name='Name', index=False)

'''
JSON 파일 입출력

    * 특징
        - JavaScript Object Notation
        - 웹에서 주로 사용

    - 불러오기 : pd.read_json()

    - 저장하기 : df.to_json('result.json', orient='records', force_ascii=False)
        - orient: JSON 구조 지정(예: 'records', 'split', 'index')
        - force_ascii=False: 한글 등 비ASCII 문자 유지
'''
sample_data.to_json('sampe_json', orient='records', indent=2)
print('JSON 파일 저장')

df_json = pd.read_json('sampe_json.json')
print(df_json)

######################################################################################################
# 데이터 탐색과 요약
'''
데이터 미리보기(head, tail)
    - DataFrame.head(n=5)
        - 첫 번째 n개 행을 반환(기본값: n=5)
        - 데이터의 전체적인 구조, 컬럼명, 값의 분포를 빠르게 확일할 때 사용
        - 데이터가 정상적으로 로드되었는지, 컬럼 타입이 예상과 맞는지 등을 체크하는 첫 단계
    - DataFrame.tail(n=5)
        - 마지막 n개 행을 반환(기본값: n=5)
        - 데이터의 마지막 부분을 확인할 때 유용
        - 인덱스가 제대로 매겨졌는지, 결측값이나 잘못된 데이터가 뒤에 섞여 있는지 확인 가능


    * 기본 문법
    df = pd.read_csb("example.csv")
    
    print(df.head())    # 앞에서 5개 행을 출력(기본값)
    print(df.head(10))  # 앞에서 10개 행을 출력

    print(df.tail())    # 뒤에서 5개 행을 출력(기본값)
    print(df.tail(3))   # 뒤에서 3개 행을 출력
'''
# 사용 예제
data = {
    "이름": ["홍길동", "이순신", "김유신", "강감찬", "장보고", "이방원"],
    "나이": [23, 35, 31, 40, 28, 34],
    "직업": ["학생", "군인", "장군", "장군", "상인", "왕자"]
}

df = pd.DataFrame(data)

# 데이터 앞부분 미리보기
print(df.head(3))

# 데이터 뒷부분 미리보기
print(df.tail(2))

'''
데이터 요약정보

* info
    DataFrame.info(verbose=None, buf=None, max_cols=None, memory_usage=None, show_counts=None)

    - 전체 데이터의 행/열 개수
    - 각 컬럼의 데이터 타입(dtype)
    - 결측값(non-null)의 개수
    - 메모리 사용량 등

* describe
    DataFrame.describe(percentiles=None, include=None, exclude=None, datetime_is_numeric=False)
 
    - 수치형 데이터: 평균, 표준편차, 최솟값/최댓값, 사분위수등 요약 통계값 제공
    - 문자열/범주형 데이터: 고유값 개수, 최빈값 등
'''
# 수치형 데이터 퉁계 요약
print(df.describe())

# 범주형(문자열) 데이터 통계 요약
print(df.describe(include="object"))

######################################################################################################
# 데이터 선택
'''
인덱싱/슬라이싱
'''
# 사용 예제 - 인덱싱
df["이름"]  # '이름' 컬럼 전체 선택
df[["이름", "나이"]]    # 여러 컬럼을 리스트로 선택

# 사용 예제 - 슬라이싱
# 1~3번 인덱스의 행 선택(1이상 4미만 즉 1,2,3 번)
print(df[1:4])
# 인덱스 -3부터 끝까지
print(df[-3:])

# 1~4번 인덱스 행에서 '이름' 컬럼만 선택
print(df[1:5]["이름"])

'- DataFrame의 슬라이싱은 행(row)기준으로 동작하며, 열 단위 슬라이싱은 명시적으로 지정해야 함'

######################################################################################################
# iloc/loc
'''
iloc
    df.iloc[행, 열]
    
    - integer location의 줄임말로, 정수 위치 기반 인덱싱/슬라이싱
    - 행, 열의 순서(0, 1, 2, ...)를 사용하여 데이터 선택
    - Numpy 슬라이싱과 유사하게 동작
'''
# 단일 행/열 선택
print(df.iloc[0])       # 0번(첫 번째) 행 전체 출력
print(df.iloc[:, 1])    # 모든 행의 1번(두 번째) 출력

# 여러 행/열 동시에 선택(슬라이싱, 리스트)
print(df.iloc[1:4])     # 1~3번 행 전체 출력(슬라이싱, 끝 인덱스 제외)
print(df.iloc[:, 0:2])  # 모든 행, 0~1번 컬럼 출력 ('이름', '나이')
print(df.iloc[[0, 2, 4], [1, 2]])   # 0, 2, 4번 행의 1, 2번 컬럼 출력 ('나이', '직업')

# 행/열 모두 슬라이싱
print(df.iloc[1:5, 0:2])    # 1~4번 행, 0~1번 컬럼 ('이름', '나이')

# 음수 인덱스 사용
print(df.iloc[-1])      # 마지막 행
print(df.iloc[:, -2:])  # 모든 행, 뒤에서 2개 컬럼 ('나이', '직업')

'''
loc
    df.loc[행, 열]

    - location의 줄임말로, 라벨명(인덱스. 컬럼명)을 이용한 인덱싱/슬라이싱
    - 행/열의 이름(라벨)을 기준으로 데이터 선택
    - 시작과 끝을 모두 포함
    - 음수 인덱스 사용은 불가
'''
# 단일 행/열 선택
print(df.loc[0])            # 인덱스 0번 행 전체
print(df.loc[:, "이름"])    # 모든 행의 '이름' 컬럼

# 여러 행/열 동시에 선택(슬라이싱, 리스트)
print(df.loc[2:4])                 # 2~3번 행 전체 출력(슬라이싱, 끝 인덱스 포함)
print(df.loc[:, ["이름", "직업"]])  # 모든 행, ('이름', '나이') 컬럼만
print(df.loc[[1, 3, 5], ["이름", "나이"]])  # 1, 3, 5번 행, ('이름', '나이') 컬럼만

# 행/열 모두 슬라이싱
print(df.loc[1:3, "이름":"직업"])   # 1~3번 행, '이름'부터 '직업'까지 연속 컬럼

######################################################################################################
# 실습 3 iloc/loc 연습

data = {
"이름": ["홍길동", "이순신", "김유신", "강감찬", "장보고", "이방원", "최무선", "정도전"],
"나이": [23, 35, 31, 40, 28, 34, 42, 29],
"직업": ["학생", "군인", "장군", "장군", "상인", "왕자", "과학자", "정치가"],
"점수": [85, 90, 75, 88, 92, 95, 87, 83]
}
df = pd.DataFrame(data)

'''
1. iloc을 사용해 인덱스 2~5(포함 안함) 행, 1~3(포함 안함) 열만 선택해 출력하세요.
'''
print(df.iloc[2:5, 1:3])

'''
2. loc을 사용해 인덱스 3~6(포함!) 행, '이름'과 '점수' 컬럼만 출력하세요.
'''
print(df.loc[3:6, ["이름", "점수"]])

'''
3. iloc을 사용해, 마지막 3개 행의 '직업'과 '점수' 컬럼만 선택해 출력하세요.
'''
print(df.iloc[-1:-4, ["직업", "점수"]])

'''
4. iloc을 사용해, 홀수번째(1, 3, 5, 7번 인덱스) 행, 모든 열을 선택하세요.
'''
print(df.iloc[[1, 3, 5, 7], :])

'''
5. loc을 사용해, 인덱스 4~7번 행, '나이', '점수' 컬럼만 출력하세요.
'''
print(df.loc[4:8, ["나이", "점수"]])

'''
6. iloc을 사용해, 짝수번째(0,2,4,6) 행과 짝수번째(0,2) 열만 선택하세요.
'''
print(df.iloc[[0, 2, 4, 6], [0, 2]])

######################################################################################################
# 통계 함수
'''
* 주요 통계 함수
함수            의미/역할
mean()          평균(산술평균)
median()        중앙값(중위수)
std()           표준편차(산포도 측정)
var()           분산(산포도 측정)
count()         결측값을 제외한 데이터 개수
min()/max()     최솟값/최댓값
sum()           합계
'''
# 통계 데이터
data = {
    "상품명": ["무선 이어폰", "스마트 워치", "텀블러", "노트북", "블루투스 스피커", "무드등"],
    "가격": [129000, 250000, 15000, 1200000, 85000, 22000],
    "재고": [23, 12, 54, 5, 17, 31]
}
df = pd.DataFrame(data)

# 주요 통계 함수
print("평균(가격):", df["가격"].mean())
print("평균(재고):", df["재고"].mean())

print("중앙값(가격):", df["가격"].median())
print("중앙값(재고):", df["재고"].median())

print("가격 값 개수:", df["가격"].count())
print("재고 값 개수:", df["재고"].count())

print("표준편차(가격):", df["가격"].std())
print("표준편차(재고):", df["재고"].std())

print("분산(가격):", df["가격"].var())
print("분산(재고):", df["재고"].var())

print("최솟값(가격):", df["가격"].min())
print("최댓값(재고):", df["재고"].max())
print("합계(재고):", df["재고"].sum())

######################################################################################################
# 결측값 처리
'''
결측값(Missing Value, NA, Null) : 데이터에 값이 기록되지 않은 상태
    - Pandas에서는 보통 NaN(Not a Number, float), None(object), NA 등으로 처리

    * 결측값이 있는 데이터의 문제점
        - 통계/분석/모델링 시 오류 또는 왜곡이 발생할 수 있음
        - 따라서, 탐색 및 전처리 단계에서 반드시 결측값 처리 필요
        - 결측값 처리
            - 삭제 : 결측값이 있는 행/열 제거
            - 대체 : 다른 값으로 채우기
            - 예측 : 앞 뒤 값이나 패턴으로 추정

    * 결측값 탐지 : isnull(), notnull()

        df.isnull()
            - 각 요소가 결측값이면 True, 아니면 False 반환
        df.notnull()
            - 각 요소가 결측값이 아니면 True, 결측값은 False 반환

    * 결측값 제거 : dropna()

        df.dropna(axis=0, how='any', inplace=False)
            - axis=0 : 결측값이 있는 행 삭제(기본값)
            - axis=1 : 결측값이 있는 열 삭제
            - how='any' : 하나라도 결측값 있으면 삭제
            - how='all' : 모두 결측값인 행(열) 삭제
            - inplace=True : 원본 데이터프레임에서 바로 삭제(반환값 없음)
    
    * 결측값 대체(채우기) : fillna()

        df.fillna(value, method=None, inplace=False)
            - value : 특정 값(예:0, 평균, 문자열 등)으로 결측값 대체
            - method='ffill' : 이전 값으로 채움(forward fill)
            - method='bfill' : 다음 값으로 채움(backward fill)
            - inplace=True : 원본에 적용
'''
# 결측값 데이터
data = {
    "이름": ["서준", np.nan, "민준", "서연", "하은", "지민"],
    "나이": [22, 28, np.nan, 31, np.nan, 24],
    "점수": [89, np.nan, 83, 90, 88, np.nan],
    "성별": ["남", "여", "남", np.nan, "여", "여"]
}
df = pd.DataFrame(data)

# 결측값 개수 계산
df.isnull().sum()       # 각 컬럼별 결측값 개수
df.isnull().sum().sum() # 전체 결측값 개수

# 결측값 제거
# 결측값있는 행 전체 삭제
df2 = df.dropna()

# 결측값있는 열 삭제
df3 = df.dropna(asix=1)

# 모두 결측값인 행만 삭제
df4 = df.dropna(how='all')

# 결측값 채우기
# 모든 결측값을 0으로 채움
df_filled = df.fillna(0)

# 각 컬럼별 평균값으로 결측값 대체
df_mean = df.fillna(df.mean(numeric_only=True))

# 이전 값으로 채움
df_fill = df.fillna(method='ffill')

# 사용 예제
missing_types = pd.DataFrame({
    'none_type': [1, 2, None, 4],           # Python None
    'nan_type': [1, 2, np.nan, 4],         # NumPy NaN
    'empty_string': ['A', 'B', '', 'D'],   # 빈 문자열
    'whitespace': ['A', 'B', ' ', 'D'],    # 공백
    'special_value': [1, 2, -999, 4]       # -999를 결측값으로 사용하는 경우
})


# 결측값이 있는 샘플 데이터
sales_data = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=7),
    'sales': [100, 120, np.nan, 150, np.nan, 180, 200],
    'customers': [20, 25, 22, np.nan, 30, 35, 40],
    'region': ['Seoul', 'Busan', np.nan, 'Daegu', 'Seoul', np.nan, 'Busan']
})

######################################################################################################
# 실습 4 통계함수/결측값 처리 연습

data = {
"도시": ["서울", "부산", "광주", "대구", np.nan, "춘천"],
"미세먼지": [45, 51, np.nan, 38, 49, np.nan],
"초미세먼지": [20, np.nan, 17, 18, 22, 19],
"강수량": [0.0, 2.5, 1.0, np.nan, 3.1, 0.0]
}
df = pd.DataFrame(data)


'''
1. ‘미세먼지’ 컬럼의 평균과 중앙값을 구하세요.
'''
print("미세먼지 평균:", df["미세먼지"].mean())      # 미세먼지 평균: 45.75
print("미세먼지 중앙값:", df["미세먼지"].median())  # 미세먼지 중앙값: 47.0

'''
2. ‘초미세먼지’ 컬럼의 최댓값과 최솟값을 구하세요.
'''
print("초미세먼지 최댓값:", df["초미세먼지"].max()) # 초미세먼지 최댓값: 22.0
print("초미세먼지 최솟값:", df["초미세먼지"].min()) # 초미세먼지 최솟값: 17.0

'''
3. 각 컬럼별 결측값 개수를 구하세요.
'''
print("결측값 개수:\n", df.isnull().sum())
# 결측값 개수:
#  도시       1
# 미세먼지     2
# 초미세먼지    1        
# 강수량      1
# dtype: int64

'''
4. 결측값이 하나라도 있는 행을 모두 삭제한 뒤, 남은 데이터의 ‘초미세먼지’ 평균을 구하세요.
'''
drop_null = df.dropna(how='any')
# print("결측값 삭제:\n", drop_null)
# 결측값 삭제:
#     도시  미세먼지  초미세먼지  강수량
# 0  서울  45.0   20.0  0.0
print("초미세먼지 평균:", drop_null["초미세먼지"].mean())   # 초미세먼지 평균: 20.0

'''
5. 결측값을 모두 0으로 채운 뒤, ‘미세먼지’와 ‘초미세먼지’의 합계를 각각 구하세요.
'''
zero_filled = df.fillna(0)
print("미세먼지 합계:", zero_filled["미세먼지"].sum())  # 미세먼지 합계: 183.0
print("초미세먼지 합계:", zero_filled["초미세먼지"].sum())  # 초미세먼지 합계: 96.0

'''
6. ‘미세먼지’ 컬럼의 결측값을 평균값으로 채운 뒤, 그 표준편차를 구하세요.
'''
print("표준편차:", df["미세먼지"].fillna(df["미세먼지"].mean()).std())  # 표준편차: 4.444097208657794

######################################################################################################
# 실습 1 조건 필터링 연습

# 사용 데이터
df = pd.DataFrame({
'이름': ['민준', '서연', '지후', '서준', '지민'],
'점수': [78, 92, 85, 60, 88],
'반': [1, 2, 1, 2, 1]
})

'''
1. 점수(score)가 80점 이상인 학생만 추출하세요.
'''
print(df[df['점수'] >= 80])

'''
2. 1반(반==1) 학생들 중, 점수가 85점 이상인 학생만 추출하세요.
'''
df[(df['반'] == 1) & (df['점수'] >= 85)]

'''
3. 이름이 '서연' 또는 '지민'인 학생만 추출하세요.
'''
print(df[(df['이름'] == '서연') | (df['이름'] == '지민')])

'''
4. 문제 3에서 추출한 결과에서 인덱스를 0부터 재정렬하여 출력하세요.
'''
print(df[(df['이름'] == '서연') | (df['이름'] == '지민')])

'''
5. 점수가 80점 미만이거나 2반인 학생만 추출하세요.
'''
print(df[(df['반'] == 2) | (df['점수'] < 80)])

'''
6. 문제 5의 결과에서 '점수' 컬럼이 70점 이상인 학생만 다시 추출하고, 인덱스를 재정렬하여 출력하세요.
'''
print(df[(df['반'] == 2) | (df['점수'] < 80) & (70 <= df['점수'])])

######################################################################################################
# 실습 2 행/열 추가·수정·삭제

# 사용 데이터
df = pd.DataFrame({
'이름': ['김철수', '이영희', '박민수'],
'국어': [90, 80, 70]
})

'''
1. '수학' 점수 [95, 100, 88]을 새 열로 추가하세요.
'''
df['수학'] = [95, 100, 88]
print(df)

'''
2. 1번 문제의 DataFrame에서 '이름' 열을 삭제하세요.
'''
df = df.drop('이름', axis=1)
print(df)

# 사용 데이터
df = pd.DataFrame({
'제품': ['A', 'B'],
'가격': [1000, 2000]
})

'''
3. 제품 'C', 가격 1500인 새 행을 추가하세요.
'''
new_row = pd.DataFrame([{'제품':'C', '가격':1500}])
df = pd.concat([df, new_row], ignore_index=True)
print(df)

'''
4. 3번 문제의 DataFrame에서 첫 번째 행(제품 'A')을 삭제하세요.
'''
drop_df = df.drop(0)
print(drop_df)

# 사용 데이터
df = pd.DataFrame({
'과목': ['국어', '영어', '수학'],
'점수': [85, 90, 78]
})

'''
5. '점수'가 80 미만인 행을 모두 삭제하세요.
'''
print(df[df['점수'] > 80])

'''
6. '학년' 열(값은 모두 1)을 추가하세요.
'''
df['학년'] = 1
print(df)

# 사용 데이터
df = pd.DataFrame({
'이름': ['A', 'B'],
'나이': [20, 22]
})

'''
7. 이름이 'C', 나이가 25, 키가 NaN(결측값)인 새 행을 추가하세요.
(단, '키'라는 새 열이 자동으로 추가되어야 함)
'''
new_row = pd.DataFrame([{'이름': 'C', '나이' : 25, '키' : np.nan}])
df = pd.concat([df, new_row], ignore_index=True)
print(df)

# 사용 데이터
df = pd.DataFrame({
'부서': ['영업', '기획', '개발', '디자인'],
'인원': [3, 2, 5, 1]
})

'''
8. 인원이 2명 이하인 행을 모두 삭제하고,
'''
print(df[df['인원'] > 2])

'''
9. '평가' 열을 새로 추가해 모든 값을 '미정'으로 채우세요.
'''
df['평가'] = '미정'
print(df)

######################################################################################################
# 실습 3 정렬

# 사용 데이터
df = pd.DataFrame({
'name': ['Alice', 'Bob', 'Charlie', 'David'],
'score': [88, 95, 70, 100]
})
'''
1. 주어진 DataFrame에서, score 컬럼 기준으로 오름차순 정렬한 결과를 출력하세요.
'''
print(df.sort_values(by='score'))

'''
2. score 컬럼 기준 내림차순으로 정렬한 후, 정렬된 인덱스를 무시하고 0부터 재정렬한 결과를 
출력하세요.
'''
print(df.sort_values(by='score', ascending=False, ignore_index=True))

# 사용 데이터
df = pd.DataFrame({
'이름': ['가', '나', '다', '라', '마'],
'반': [2, 1, 1, 2, 1],
'점수': [90, 85, 80, 95, 85]
})
'''
3. 주어진 DataFrame에서,반(class) 기준 오름차순, 같은 반 내에서는 점수(score) 기준 내림차순으로 정렬한 결
과를 출력하세요.
'''
print(df.sort_values(by='반').sort_values(by='점수', ascending=False))

'''
4. 열(컬럼) 이름을 알파벳순으로 정렬해서 출력하세요.
'''
print(df.sort_index(axis=1))

# 사용 데이터
df = pd.DataFrame({
'value': [10, 20, 30, 40]
}, index=[3, 1, 4, 2])
'''
5. 인덱스 기준으로 오름차순 정렬한 결과를 출력하세요.
'''
print(df.sort_index())

'''
6. 인덱스 기준 내림차순 정렬, value 컬럼 기준 오름차순 정렬 두 가지 정렬 결과를 각각 출력하
세요.
'''
print(df.sort_index(ascending=False))
print(df.sort_values(by='value'))

######################################################################################################
# 실습 4 groupby 정렬문제

'''
1. 각 학년(grade)별 평균 국어 점수(kor)를 구하세요.
'''
df = pd.DataFrame({
'grade': [1, 2, 1, 2, 1, 3],
'name': ['Kim', 'Lee', 'Park', 'Choi', 'Jung', 'Han'],
'kor': [85, 78, 90, 92, 80, 75]
})

print(df.groupby('grade')['kor'].mean())

'''
2. 아래 DataFrame에서 반(class)별, 과목(subject)별로 시험에 응시한 학생 수(count)와 평균 점수(avg)를 구하세요.
'''
df = pd.DataFrame({
'class': [1, 1, 1, 2, 2, 2],
'subject': ['Math', 'Math', 'Eng', 'Math', 'Eng', 'Eng'],
'score': [80, 90, 85, 70, 95, 90]
})

print(df.groupby(['class', 'subject']).count())
print(df.groupby(['class', 'subject']).mean())

'''
3. 아래 DataFrame에서 지역(region)별 판매자(seller)별로 판매액(sales)의 합계와 최대값을 구하세요.
'''
df = pd.DataFrame({
'region': ['Seoul', 'Seoul', 'Busan', 'Busan', 'Daegu'],
'seller': ['A', 'B', 'A', 'B', 'A'],
'sales': [100, 200, 150, 120, 130]
})

print(df.groupby(['region', 'seller'])['sales'].agg(['sum', 'max']))

'''
4. 아래 DataFrame에서 팀(team)별, 포지션(position)별로 결측치(NaN)를 포함한 점수(score)의 평균을 구하세요.
'''
df = pd.DataFrame({
'team': ['A', 'A', 'B', 'B', 'A', 'B'],
'position': ['FW', 'DF', 'FW', 'DF', 'DF', 'FW'],
'score': [3, 2, None, 1, 4, 2]
})

print(df.groupby(['team', 'position'], dropna=False)['score'].mean())

'''
5. 아래 DataFrame에서 부서(dept)별로 성별(gender)별 인원 수와, 총 연봉(salary) 합계를 구하세요.
'''
df = pd.DataFrame({
'dept': ['HR', 'HR', 'IT', 'IT', 'Sales', 'Sales'],
'gender': ['M', 'F', 'F', 'M', 'F', 'F'],
'salary': [3500, 3200, 4000, 4200, 3000, 3100]
})

print(df.groupby(['dept', 'gender']).count())
print(df.groupby(['dept', 'gender']).sum('salary'))