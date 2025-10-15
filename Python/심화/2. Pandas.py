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

* CSV의 주요 특징:
    1. 쉼표(,)로 값을 구분 - 각 열(컬럼)이 쉼표로 분리됨
    2. 텍스트 파일이라 메모장, 에디터 등 어디서나 열람 가능
    3. 파일 크기가 가볍고 읽기/쓰기가 빠름
    4. Excel, Google Sheets, 데이터베이스 등 다양한 프로그램과 호환
    5. 서식이나 수식은 포함되지 않고 순수 데이터만 저장

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

* CSV 파일 예시 내용 (실제 파일 내부 모습)
name,   age,    city,   salary
John,   25,     Seoul,  50000
Jane,   30,     Busan,  60000
Park,   35,     Daegu,  55000
'''
# 샘플 데이터프레임 생성
# DataFrame: 엑셀 시트처럼 행(row)과 열(column)로 구성된 2차원 테이블 구조
sample_data = pd.DataFrame({
    'name': ['John', 'Jane', 'Park'],      # 이름 열
    'age': [25, 30, 35],                   # 나이 열
    '도시': ['서울', '부산', '대구'],        # 도시 열 (한글 컬럼명 사용 가능)
    'salary': [50000, 60000, 55000]        # 급여 열
})

# UTF-8로 CSV 저장 (가장 권장되는 방식)
sample_data.to_csv('sample_data.csv',
                   # index=False: 행 번호(0,1,2...)를 파일에 저장하지 않음
                   index=False,
                   # utf-8-sig: UTF-8 + BOM (Byte Order Mark)
                   encoding='utf-8-sig')
# BOM을 추가하면 Excel에서 한글이 깨지지 않고 정상적으로 표시됨

# CP949로 저장 (Windows 한글 인코딩)
# 구형 Windows 시스템이나 특정 프로그램에서 필요할 때 사용
# sample_data.to_csv('sample_data.csv', index=False, encoding='cp949')

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

# CSV는 기본적으로 쉼표(,)로 구분하지만, 다른 구분자도 사용 가능합니다.
# 예: 탭(\t), 세미콜론(;), 파이프(|) 등

sample_data = pd.DataFrame({
    'name': ['John', 'Jane', 'Park'],
    'age': [25, 30, 35],
    '도시': ['서울', '부산', '대구'],
    'salary': [50000, 60000, 55000]
})

# sep='\t': 탭(Tab) 문자로 구분된 파일 저장
# 주로 .txt 확장자와 함께 사용되며, 탭으로 구분된 값(TSV)이라고 부름
sample_data.to_csv('tab_separated.txt',
                   sep='\t',               # 구분자를 탭으로 설정
                   index=False)

# 탭으로 구분된 파일 읽기
df_tab = pd.read_csv('tab_separated.txt',
                     sep='\t')             # 읽을 때도 동일한 구분자 지정

print('=== CSV sep=탭 파일 읽기 ===')
print(df_tab)
print()
print(df_tab.head())  # head(): 처음 5개 행만 출력 (데이터 미리보기에 유용)
# head(10)처럼 숫자를 지정하면 해당 개수만큼 출력

'''
* Excel 파일 불러오기
    df = pd.read_excel('파일경로/파일명.xlsx', 옵션...)

    * 주요 옵션
        - sheet_name : 불러올 시트 이름 또는 번호(기본값 0)
        - header, index_col, usecols 등
    
    * 특징
        - 마이크로소프트의 스프레드시트 프로그램
        - 여러 시트(Sheet) 지원 - 하나의 파일에 여러 테이블 저장 가능
        - 서식(색상, 폰트, 정렬 등), 수식, 차트 포함 가능
        - 확장자: .xlsx (Excel 2007 이후, 최신 버전), .xls (구버전)
        - 비즈니스 환경에서 가장 많이 사용되는 형식

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
    sample_data.to_excel(writer, sheet_name='Defalut', index=False)
    sample_data['name'].to_excel(writer, sheet_name='Name', index=False)

# excel 파일 저장
sample_data = pd.DataFrame({
    'name': ['John', 'Jane', 'Park'],
    'age': [25, 30, 35],
    '도시': ['서울', '부산', '대구'],
    'salary': [50000, 60000, 55000]
})

# to_excel(): DataFrame을 Excel 파일로 저장
sample_data.to_excel('sample_data.xlsx',
                     index=False,              # 행 번호 제외
                     sheet_name='Default')     # 시트 이름 지정
print('샘플 엑셀 파일 생성 완료')

# excel 파일 읽기
# read_excel(): Excel 파일을 읽어서 DataFrame으로 변환
df_excel = pd.read_excel('sample_data.xlsx')
# 시트 이름을 지정하지 않으면 첫 번째 시트를 자동으로 읽음

print('=== Excel 파일 읽기 ===')
print(df_excel)

# 여러 시트를 가진 excel 파일 만들기
sample_data = pd.DataFrame({
    'name': ['John', 'Jane', 'Park'],
    'age': [25, 30, 35],
    '도시': ['서울', '부산', '대구'],
    'salary': [50000, 60000, 55000]
})

# ExcelWriter: 여러 시트를 하나의 Excel 파일에 저장할 때 사용
# with 문을 사용하면 파일이 자동으로 저장되고 닫힘
with pd.ExcelWriter('multi_sheet.xlsx') as writer:
    # 첫 번째 시트: 전체 데이터
    sample_data.to_excel(writer,
                         sheet_name='Default1',   # 시트 이름
                         index=False)

    # 두 번째 시트: 이름 열만 저장
    sample_data['name'].to_excel(writer,
                                 sheet_name='name',
                                 index=False)

print('2개의 시트를 가진 엑셀 파일 생성 완료')

# 특정 시트 읽기 예시:
# df = pd.read_excel('multi_sheet.xlsx', sheet_name='Default1')
# 모든 시트 읽기 예시:
# all_sheets = pd.read_excel('multi_sheet.xlsx', sheet_name=None)  # 딕셔너리 형태로 반환

'''
JSON 파일 입출력

    * 특징
        - JavaScript Object Notation
        - 웹에서 주로 사용
        - 웹 API, 설정 파일, 데이터 교환에 널리 사용되는 텍스트 기반 형식
    
    * JSON의 주요 특징:
    1. 가볍고 읽기 쉬운 텍스트 형식
    2. 웹 개발에서 가장 많이 사용 (REST API 등)
    3. 중첩된 구조(nested structure) 표현 가능
    4. 키-값 쌍(key-value pair)으로 데이터 저장
    5. JavaScript뿐만 아니라 거의 모든 프로그래밍 언어에서 지원

    - 불러오기 : pd.read_json()

    - 저장하기 : df.to_json('result.json', orient='records', force_ascii=False)
        - orient: JSON 구조 지정(예: 'records', 'split', 'index')
        - force_ascii=False: 한글 등 비ASCII 문자 유지
'''
sample_data.to_json('sampe_json', orient='records', indent=2)
print('JSON 파일 저장')

df_json = pd.read_json('sampe_json.json')
print(df_json)

# JSON 파일 저장
sample_data = pd.DataFrame({
    'name': ['John', 'Jane', 'Park'],
    'age': [25, 30, 35],
    '도시': ['서울', '부산', '대구'],
    'salary': [50000, 60000, 55000]
})

# to_json(): DataFrame을 JSON 파일로 저장
sample_data.to_json('sample_data.json',
                    orient='records',      # orient: JSON 구조 방식 지정
                    # 'records': [{}, {}, {}] 형태 (레코드 배열)
                    # 'columns': {컬럼명: {인덱스: 값}} 형태
                    # 'index': {인덱스: {컬럼명: 값}} 형태
                    indent=2)             # indent=2: 들여쓰기 2칸 (가독성 향상)
print('JSON 파일 저장')

# JSON 파일 읽기
# read_json(): JSON 파일을 읽어서 DataFrame으로 변환
df_json = pd.read_json('sample_data.json')
print('=== JSON 파일 읽기 ===')
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
df["이름"]  # '이름' 컬럼 전체 선택/단일 열 선택: Series 형태로 반환
df[["이름", "나이"]]    # 여러 열 선택: DataFrame 형태로 반환 (2차원 테이블 유지)

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

'''
═══════════════════════════════════════════════════════════════
iloc vs loc 차이점 정리
═══════════════════════════════════════════════════════════════

┌─────────────┬──────────────────┬──────────────────┐
│             │ iloc             │ loc              │
├─────────────┼──────────────────┼──────────────────┤
│ 인덱싱 방식  │ 정수 위치 (0, 1..)│ 라벨/이름        │
│ 끝 범위     │ 포함 안 됨        │ 포함됨           │
│ 열 선택     │ 정수만 가능       │ 이름 사용 가능    │
│ 조건 필터   │ 불가능           │ 가능             │
└─────────────┴──────────────────┴──────────────────┘

예시:
df.iloc[1:3, 0:2]  → 1, 2번 행 / 0, 1번 열
df.loc[1:3, '이름':'나이']  → 1, 2, 3번 행 / 이름부터 나이까지 모든 열

권장 사용법:
- iloc: 위치 기반 슬라이싱, 순차적 접근
- loc: 조건부 필터링, 명시적 열 이름 사용
'''

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
# 데이터 정제(Data Cleaning)
# 실제 현업에서 수집한 데이터는 완벽하지 않습니다.
# 데이터 분석의 80%는 데이터 정제 작업이라고 할 정도로 중요한 과정입니다.

# ─────────────────────────────────────────────────────────────
# 1. 현실의 "더러운 데이터" 예시
# ─────────────────────────────────────────────────────────────

dirty_data = pd.DataFrame({
    # 중복된 이름, 결측값(None) 존재
    'name': ['John Doe', 'Jane Smith', 'John Doe', 'Jane Smith', None, 'Bob Wilson'],

    # 형식 불일치: 숫자, 문자열, None 혼재 / 이상값: 250살
    'age': ['25', '30 years', 28, 'thirty', None, 250],

    # 중복 이메일, 형식 오류(@뒤 도메인 누락), None
    'email': ['john@email.com', 'jane@email', 'john@email.com',
              'jane@email.com', 'invalid@', None],

    # 날짜 형식이 제각각: YYYY-MM-DD, YYYY.MM.DD, MM/DD/YYYY 혼재
    # 날짜 오류: 13월 45일은 존재하지 않음
    'join_date': ['2024-01-01', '2024.01.15', '01/20/2024',
                  '2024-01-15', None, '2024-13-45']
})

print(dirty_data)

'''
    데이터 품질 문제점:
    1. 중복 데이터 - 동일한 사람이 여러 번 기록됨
    2. 결측값 - None, NaN 등 비어있는 데이터
    3. 형식 불일치 - age가 숫자/문자 혼재, 날짜 형식 다양
    4. 이상값 - age가 250살처럼 비현실적인 값
    5. 무결성 위반 - 존재할 수 없는 날짜(13월 45일)
'''

# 결측값 처리
'''
결측값(Missing Value, NA, Null) : 데이터에 값이 기록되지 않은 상태
    - Pandas에서는 보통 NaN(Not a Number, float), None(object), NA 등으로 처리

    * 결측값이 있는 데이터의 문제점
        - 통계/분석/모델링 시 오류 또는 왜곡이 발생할 수 있음
        - 따라서, 탐색 및 전처리 단계에서 반드시 결측값 처리 필요
        - 결측값 처리
            1. 삭제 (Deletion)
                - 결측값이 있는 행/열 제거
                - 장점: 간단하고 빠름
                - 단점: 데이터 손실, 샘플 수 감소
                - 사용 시기: 결측값이 소수이고 무작위일 때
                
            2. 대체 (Imputation)
                - 통계값(평균, 중앙값, 최빈값)으로 채우기
                - 장점: 데이터 보존
                - 단점: 편향 발생 가능
                - 사용 시기: 결측값이 일정 패턴 없이 분포할 때
                
            3. 예측 (Prediction)
                - 앞뒤 값이나 다른 변수로 추정
                - 장점: 정확도 높음
                - 단점: 복잡함
                - 사용 시기: 시계열 데이터, 결측값이 많을 때
    
    * 결측값의 종류와 표현 방식:
    
    1. None - Python의 기본 빈 객체
       - 객체형(object) 데이터에 주로 사용
       - 예: 문자열 컬럼의 결측값
    
    2. np.nan (Not a Number) - NumPy의 결측값 표현
       - 숫자형 데이터에 주로 사용
       - 수학 연산에서 nan 전파 (nan + 1 = nan)
    
    3. pd.NA - Pandas의 범용 결측값 (최신 버전)
       - 모든 데이터 타입에 사용 가능
       - Boolean 연산 개선
    
    4. 빈 문자열 - '', " " (공백)
       - 기술적으로는 결측값이 아니지만 의미 없는 데이터
       - 명시적으로 처리 필요
    
    5. 특수 값 - -999, 99999, -1 등
       - 도메인 지식에 따라 결측값으로 처리해야 할 수 있음
       - 예: 나이 -999는 실제로는 결측값을 의미

    * 결측값 탐지(Detection) : isna() / isnull(), notna() / notnull()

        df.isna() / df.isnull()
            - 각 요소가 결측값이면 True, 아니면 False 반환
        df.notna() / df.notnull()
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

# 다양한 결측값 타입 예시
missing_types = pd.DataFrame({
    'none_type': [1, 2, None, 4],           # Python None
    'nan_type': [1, 2, np.nan, 4],          # NumPy NaN (숫자형 결측값)
    'empty_string': ['A', 'B', '', 'D'],    # 빈 문자열 (결측값 아님!)
    'whitespace': ['A', 'B', ' ', 'D'],     # 공백 (결측값 아님!)
    'special_value': [1, 2, -999, 4]        # 특수 값 (도메인에 따라 결측값 처리)
})

print(missing_types)

# 결측값 탐지
# isna() / isnull() - 결측값이면 True 반환
# 두 메서드는 완전히 동일한 기능 (isna가 더 최신 권장)
print('=== isna() ===')
print(missing_types.isna())    # 결측값 위치를 True/False로 표시
print(missing_types.isnull())  # isna()와 동일
print()

# notna() / notnull() - 값이 있으면 True 반환 (isna의 반대)
print('=== notna() ===')
print(missing_types.notna())   # 값이 있는 위치를 True로 표시
print(missing_types.notnull())  # notna()와 동일

# 결측값 통계 확인
# 열별 결측값 개수 계산
# .isna()로 True/False 생성 → .sum()으로 True 개수 집계
print('=== 열별 결측값 개수 ===')
print(missing_types.isna().sum())
# 결과:
# none_type        1  (3번 행에 None)
# nan_type         1  (3번 행에 NaN)
# empty_string     0  (빈 문자열은 결측값으로 인식 안 됨)
# whitespace       0  (공백도 결측값으로 인식 안 됨)
# special_value    0  (-999는 실제 숫자로 인식)

# 전체 결측값 개수 (모든 열의 결측값 합계)
print('전체 결측값:', missing_types.isna().sum().sum())
# .sum() 첫 번째: 각 열의 결측값 개수
# .sum() 두 번째: 그 개수들의 합

# ─────────────────────────────────────────────────────────────
# 결측값 처리 실습용 샘플 데이터
# ─────────────────────────────────────────────────────────────

sales_data = pd.DataFrame({
    # 2024년 1월 1일부터 7일간의 날짜
    'date': pd.date_range('2024-01-01', periods=7),

    # 매출: 3번, 5번 행에 결측값
    'sales': [100, 120, np.nan, 150, np.nan, 180, 200],

    # 고객수: 4번 행에 결측값
    'customers': [20, 25, 22, np.nan, 30, 35, 40],

    # 지역: 3번, 6번 행에 결측값
    'region': ['Seoul', 'Busan', np.nan, 'Daegu', 'Seoul', np.nan, 'Busan']
})

print('=== 원본 데이터 ===')
print(sales_data)
print()

# ─────────────────────────────────────────────────────────────
# 전략 1: 삭제 (Deletion)
# ─────────────────────────────────────────────────────────────

# 1-1. 결측값이 있는 행 전체 삭제
# dropna(): 결측값이 하나라도 있는 행을 모두 제거
drop_rows = sales_data.dropna()
print('결측값이 있는 행 삭제:')
print(drop_rows)
# 결과: 7개 행 중 결측값 없는 0, 1, 6번 행만 남음 (3개 행만 유지)
# 주의: 데이터가 대폭 줄어듦!
print()

# 1-2. 결측값이 있는 열 전체 삭제
# axis=1: 열(column) 방향으로 삭제
drop_cols = sales_data.dropna(axis=1)
print('결측값이 있는 열 삭제:')
print(drop_cols)
# 결과: sales, customers, region 열이 모두 삭제됨
# date 열만 남음 (날짜 정보만으로는 분석 불가!)
print()

# 1-3. 특정 열 기준으로만 삭제
# subset=['sales']: sales 열에 결측값이 있는 행만 삭제
drop_sales = sales_data.dropna(subset=['sales'])
print('sales 열 기준으로만 삭제:')
print(drop_sales)
# 결과: sales가 NaN인 3번, 5번 행만 제거됨
# customers, region의 결측값은 무시됨
print()

# ─────────────────────────────────────────────────────────────
# 전략 2: 대체 (Imputation) - 통계값 사용
# ─────────────────────────────────────────────────────────────

# 2-1. 평균값으로 대체
# 주의: 원본 데이터를 보존하기 위해 .copy() 사용!
fill_mean = sales_data.copy()
# fillna(평균값): 결측값을 평균으로 채움
fill_mean['sales'] = fill_mean['sales'].fillna(fill_mean['sales'].mean())
print('평균값으로 대체:')
print(fill_mean)
# sales 평균: (100+120+150+180+200) / 5 = 150
# 3번, 5번 행의 NaN → 150으로 채워짐
print()

# 2-2. 중앙값으로 대체 (이상값이 있을 때 유용!)
# median(): 데이터를 정렬했을 때 중간 값
fill_median = sales_data.copy()
fill_median['sales'] = fill_median['sales'].fillna(
    fill_median['sales'].median()
)
print('중앙값으로 대체:')
print(fill_median)
# sales 중앙값: [100, 120, 150, 180, 200] 정렬 → 중간값 150
# 평균과 달리 극단값(outlier)의 영향을 덜 받음
# 예: 데이터가 [100, 120, 150, 180, 10000]이면
#     평균 = 2110 (왜곡됨)
#     중앙값 = 150 (안정적)
print()

# ─────────────────────────────────────────────────────────────
# 전략 3: 시계열 대체 (Time Series Imputation)
# ─────────────────────────────────────────────────────────────
# 시간 순서가 있는 데이터에서 앞뒤 값으로 결측값을 채웁니다.
# 주가, 온도, 판매량처럼 연속적인 패턴이 있는 데이터에 적합합니다.

# 3-1. Forward Fill (앞의 값으로 채우기)
# method='ffill': 결측값 바로 이전 값으로 채움
fill_forward = sales_data.copy()
fill_forward['customers'] = fill_forward['customers'].fillna(method='ffill')
print('Forward Fill (앞 값으로 채우기):')
print(fill_forward)
# customers 4번 행 NaN → 3번 행의 22로 채워짐
# 논리: "어제 고객수가 22명이었으면 오늘도 비슷할 것"
print()

# 3-2. Backward Fill (뒤의 값으로 채우기)
# method='bfill': 결측값 바로 다음 값으로 채움
fill_backward = sales_data.copy()
fill_backward['customers'] = fill_backward['customers'].fillna(
    method='bfill'
)
print('Backward Fill (뒤 값으로 채우기):')
print(fill_backward)
# customers 4번 행 NaN → 5번 행의 30으로 채워짐
# 논리: "내일 고객수가 30명이면 오늘도 비슷할 것"
print()

# ═══════════════════════════════════════════════════════════════
# 실전 예제: 환경 데이터 정제
# ═══════════════════════════════════════════════════════════════

data = {
    "도시": ["서울", "부산", "광주", "대구", np.nan, "춘천"],
    "미세먼지": [45, 51, np.nan, 38, 49, np.nan],         # PM10
    "초미세먼지": [20, np.nan, 17, 18, 22, 19],           # PM2.5
    "강수량": [0.0, 2.5, 1.0, np.nan, 3.1, 0.0]          # mm
}

df = pd.DataFrame(data)

print('=== 환경 데이터 원본 ===')
print(df)
print()

# 결측값 현황 파악
print('=== 결측값 개수 ===')
print(df.isna().sum())
print()

# 처리 전략 수립:
# 1. 도시명 결측 → 삭제 (도시를 모르면 데이터 무의미)
# 2. 미세먼지 결측 → 평균값 대체 (대기질은 인근 지역과 유사)
# 3. 초미세먼지 결측 → 중앙값 대체 (극단값 영향 최소화)
# 4. 강수량 결측 → 0으로 대체 (기록 없음 = 비 안 옴)

# 1. 도시명 결측 행 제거
df_clean = df.dropna(subset=['도시'])
print('=== 도시명 결측 제거 후 ===')
print(df_clean)
print()

# 2. 미세먼지 평균값으로 대체
pm10_mean = df_clean['미세먼지'].mean()  # (45+51+38+49)/4 = 45.75
df_clean['미세먼지'] = df_clean['미세먼지'].fillna(pm10_mean)
print('=== 미세먼지 평균 대체 후 ===')
print(df_clean)
print()

# 3. 초미세먼지 중앙값으로 대체
pm25_median = df_clean['초미세먼지'].median()  # [17, 18, 20, 22] → 19
df_clean['초미세먼지'] = df_clean['초미세먼지'].fillna(pm25_median)
print('=== 초미세먼지 중앙값 대체 후 ===')
print(df_clean)
print()

# 4. 강수량 0으로 대체
df_clean['강수량'] = df_clean['강수량'].fillna(0)
print('=== 최종 정제 데이터 ===')
print(df_clean)
print()

# 최종 결측값 확인
print('=== 최종 결측값 확인 ===')
print(df_clean.isna().sum())
# 모든 결측값이 처리되어야 함!

'''
═══════════════════════════════════════════════════════════════
결측값 처리 의사결정 가이드
═══════════════════════════════════════════════════════════════

┌──────────────────┬─────────────────┬──────────────────┐
│ 상황             │ 권장 방법        │ 이유             │
├──────────────────┼─────────────────┼──────────────────┤
│ 식별자 결측      │ 삭제            │ 행 추적 불가     │
│ 결측 <5%        │ 삭제            │ 영향 미미        │
│ 결측 5-40%      │ 평균/중앙값 대체│ 데이터 보존      │
│ 결측 >40%       │ 열 삭제 고려    │ 신뢰도 낮음      │
│ 시계열 데이터    │ ffill/bfill    │ 연속성 유지      │
│ 범주형 데이터    │ 최빈값 대체     │ 가장 흔한 값     │
│ 이상값 존재      │ 중앙값 대체     │ 평균 왜곡 방지   │
└──────────────────┴─────────────────┴──────────────────┘

주의사항:
- 결측값 처리 전 반드시 원본 백업 (.copy() 사용)
- 처리 이유를 문서화 (재현 가능성)
- 도메인 지식 활용 (통계만으로 판단 금지)
- 여러 방법 시도 후 결과 비교
'''

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
# 조건 필터링(Conditional Filtering)
# Boolean Indexing을 사용하여 원하는 조건의 데이터만 선택

'''
조건 필터링 핵심 정리:
┌─────────────┬──────────────┬─────────────────┐
│ 연산자      │ 의미         │ 예시            │
├─────────────┼──────────────┼─────────────────┤
│ &           │ AND (그리고) │ (조건1) & (조건2)│
│ |           │ OR (또는)    │ (조건1) | (조건2)│
│ ~           │ NOT (부정)   │ ~(조건1)        │
│ ==          │ 같음         │ df['A'] == 10   │
│ !=          │ 다름         │ df['A'] != 10   │
│ >  >=  <  <=│ 크기 비교    │ df['A'] >= 80   │
│ isin()      │ 목록 포함    │ df['A'].isin([])│
└─────────────┴──────────────┴─────────────────┘

주의사항:
- 조건마다 괄호() 필수!
- and/or 대신 &/| 사용 (Python 예약어는 사용 불가)
- 여러 값 비교 시 isin() 사용 권장
'''

######################################################################################################
# 실습 1 조건 필터링 연습

# 사용 데이터
df = pd.DataFrame({
'이름': ['민준', '서연', '지후', '서준', '지민'],
'점수': [78, 92, 85, 60, 88],
'반': [1, 2, 1, 2, 1]
})

'''
# 문제 1: 단일 조건 필터링
1. 점수(score)가 80점 이상인 학생만 추출하세요.
'''
print(df[df['점수'] >= 80])
# 점수가 80점 이상인 학생만 추출
# df['점수'] >= 80 → Boolean Series [False, True, True, False, True]
# df[Boolean Series] → True인 행만 선택

'''
# 문제 2: 다중 조건 필터링 (AND 연산)
2. 1반(반==1) 학생들 중, 점수가 85점 이상인 학생만 추출하세요.
'''
df[(df['반'] == 1) & (df['점수'] >= 85)]
# & 연산자: 두 조건을 모두 만족 (AND)
# 주의: 각 조건을 괄호()로 묶어야 함!
# (df['반'] == 1) AND (df['점수'] >= 85)
# 결과: 지후(1반, 85점), 지민(1반, 88점)

'''
# 문제 3: 다중 조건 필터링 (OR 연산)
3. 이름이 '서연' 또는 '지민'인 학생만 추출하세요.
'''
print(df[(df['이름'] == '서연') | (df['이름'] == '지민')])
# | 연산자: 둘 중 하나만 만족 (OR)

print("3-2. 이름이 '서연' 또는 '지민' (isin 사용):")
print(df[df['이름'].isin(['서연', '지민'])])
# isin(['서연', '지민']) → ['서연', '지민'] 리스트에 포함된 값 찾기
# isin() 메서드: 여러 값 중 하나라도 포함되면 True
# OR 연산보다 간결하고 가독성이 좋음

'''
# 문제 4: 인덱스 재정렬 (reset_index)
4. 문제 3에서 추출한 결과에서 인덱스를 0부터 재정렬하여 출력하세요.
'''
print(df[(df['이름'] == '서연') | (df['이름'] == '지민')])
# 필터링 후 인덱스가 불연속적일 때 0부터 재정렬

df_isin = df[df['이름'].isin(['서연', '지민'])]
print("4-1. 필터링 후 (인덱스 불연속):")
print(df_isin)  # 인덱스: 1, 4

# reset_index(): 인덱스를 0부터 재정렬
# 기존 인덱스는 'index'라는 새 컬럼으로 추가됨
df_isin = df_isin.reset_index()
print("4-2. reset_index() 후:")
print(df_isin)  # 인덱스: 0, 1 / 기존 인덱스는 'index' 컬럼에 저장

# reset_index(drop=True): 기존 인덱스를 버리고 재정렬
# 일반적으로 이 방법을 더 많이 사용
df_isin_dropped = df[df['이름'].isin(['서연', '지민'])].reset_index(drop=True)
print("4-3. reset_index(drop=True) 후:")
print(df_isin_dropped)  # 인덱스: 0, 1 / 기존 인덱스 제거됨

'''
# 문제 5: 복합 조건 (OR)
5. 점수가 80점 미만이거나 2반인 학생만 추출하세요.
'''
print(df[(df['반'] == 2) | (df['점수'] < 80)])

# 결과: 민준(78점), 서연(2반), 서준(2반, 60점)

'''
# 문제 6: 연속 필터링 (Chaining)
6. 문제 5의 결과에서 '점수' 컬럼이 70점 이상인 학생만 다시 추출하고, 인덱스를 재정렬하여 출력하세요.
'''
print(df[(df['반'] == 2) | (df['점수'] < 80) & (70 <= df['점수'])].reset_index(drop=True))
# 결과: 민준(78점), 서연(92점)
# 서준(60점)은 제외됨

######################################################################################################
# 행/열 추가·수정·삭제

'''
행 추가 방법 비교:
┌─────────────┬────────────┬────────────────┐
│ 방법        │ 장점       │ 단점           │
├─────────────┼────────────┼────────────────┤
│ concat()    │ 안전, 명확 │ 코드 길이 김   │
│ loc[]       │ 간결       │ 컬럼 순서 주의 │
│ append()    │ 직관적     │ deprecated됨   │
└─────────────┴────────────┴────────────────┘
권장: concat() 또는 loc[] 사용
'''
'''
행 추가(concat)
    pd.concat(objs, axis=0, join='outer', ignore_index=False, ...)
    결합시 열 이름이 기존과 다르면 NaN 값이 들어감
    - objs: 결합할 Series, DataFrame 또는 이들의 리스트/튜플 (필수)
    - axis: 결합 방향
        - 0 (기본값): 행 방향(아래로 붙임, row-wise, index 증가)
        - 1: 열 방향(옆으로 붙임, column-wise, column 증가)
    - ignore_index: 인덱스 재설정 여부 (기본값: False)
        - True로 설정 시 결과의 인덱스를 0부터 재부여(재정렬)
'''

######################################################################################################
# 실습 2 행/열 추가·수정·삭제

# 사용 데이터
df = pd.DataFrame({
'이름': ['김철수', '이영희', '박민수'],
'국어': [90, 80, 70]
})

'''
# 문제 1: 열(Column) 추가
1. '수학' 점수 [95, 100, 88]을 새 열로 추가하세요.
'''
df['수학'] = [95, 100, 88]  # 리스트 길이는 행 개수와 동일해야 함
print(df)

# 새 열 추가: df['새열이름'] = 값
# 값: 리스트, 단일값, Series 등 가능

'''
# 문제 2: 열(Column) 삭제
2. 1번 문제의 DataFrame에서 '이름' 열을 삭제하세요.
'''
df = df.drop('이름', axis=1)
print(df)

# drop(컬럼명, axis=1): 열 삭제
# axis=1: 열 방향, axis=0: 행 방향
# 주의: drop()은 원본을 변경하지 않음 → 재할당 필요
# 또는 df.drop('이름', axis=1, inplace=True) 사용

# 사용 데이터
df = pd.DataFrame({
'제품': ['A', 'B'],
'가격': [1000, 2000]
})

'''
# 문제 3: 행(Row) 추가 방법 1 - concat()
# 문제 3: 행(Row) 추가 방법 2 - loc[]
3. 제품 'C', 가격 1500인 새 행을 추가하세요.
'''
new_row = pd.DataFrame([{'제품':'C', '가격':1500}])
df = pd.concat([df, new_row], ignore_index=True)
print(df)

# concat(): 여러 DataFrame을 합치기
# ignore_index=True: 인덱스를 0부터 재정렬

# loc[인덱스번호] = [값들]: 특정 위치에 행 추가
# len(df): 현재 행 개수 → 다음 인덱스 번호
df.loc[len(df)] = ['D', 2500]
# len(df) = 3 → df.loc[3] = ['D', 2500]

'''
4. 3번 문제의 DataFrame에서 첫 번째 행(제품 'A')을 삭제하세요.
'''
drop_df = df.drop(0)    # 인덱스 0번 행 삭제
print(drop_df)

# 사용 데이터
df = pd.DataFrame({
'과목': ['국어', '영어', '수학'],
'점수': [85, 90, 78]
})

'''
# 문제 4: 행(Row) 삭제
5. '점수'가 80 미만인 행을 모두 삭제하세요.
'''
df = df.drop(df[df['점수'] < 80].index)
print(df)

# drop(인덱스번호): 특정 행 삭제
# axis=0 (기본값): 행 삭제
# df[df['점수'] < 80].index → 조건에 맞는 행의 인덱스 번호
# drop(인덱스 리스트) → 해당 인덱스 행들 삭제

'''
# 문제 6: 모든 행에 같은 값을 가진 열 추가
6. '학년' 열(값은 모두 1)을 추가하세요.
'''
df['학년'] = 1  # 스칼라 값은 모든 행에 자동으로 브로드캐스팅됨
print(df)

# 사용 데이터
df = pd.DataFrame({
'이름': ['A', 'B'],
'나이': [20, 22]
})

'''
# 문제 7: 새 열과 함께 행 추가 (결측값 포함)
7. 이름이 'C', 나이가 25, 키가 NaN(결측값)인 새 행을 추가하세요.
(단, '키'라는 새 열이 자동으로 추가되어야 함)
'''

# 기존 DataFrame에 없던 열('키')을 포함한 행 추가
# 기존 행의 '키' 열은 자동으로 NaN으로 채워짐
new_row = pd.DataFrame({
    '이름': ['C'],
    '나이': [25],
    '키': [np.nan]  # np.nan: NumPy의 결측값
})
df = pd.concat([df, new_row], ignore_index=True)
print(df)
# 결과:
#   이름  나이   키
# 0  A   20  NaN  ← 기존 행, '키' 자동 추가됨
# 1  B   22  NaN  ← 기존 행
# 2  C   25  NaN  ← 새 행

# 사용 데이터
df = pd.DataFrame({
'부서': ['영업', '기획', '개발', '디자인'],
'인원': [3, 2, 5, 1]
})

'''
# 문제 8: 조건 필터링으로 행 삭제
8. 인원이 2명 이하인 행을 모두 삭제하고,
'''
print(df[df['인원'] > 2])   # 인원이 3명 이상인 행만 남김
# 결과: 영업(3명), 개발(5명)만 남음

'''
# 문제 9: 열 추가 (모든 값 동일)
9. '평가' 열을 새로 추가해 모든 값을 '미정'으로 채우세요.
'''
df['평가'] = '미정' # 문자열도 브로드캐스팅 가능
print(df)

######################################################################################################
# 문자열 데이터 처리
'''
* 문자열 데이터 처리 함수
메서드                  설명                            예시
.str.lower()        소문자로 변환                 "Hello" → "hello"
.str.upper()        대문자로 변환                 "Hello" → "HELLO"
.str.strip()        양쪽 공백 제거                " hi " → "hi"
.str.lstrip()       왼쪽 공백 제거                " hi" → "hi"
.str.rstrip()       오른쪽 공백 제거              "hi " → "hi"
.str.replace()      문자열 치환                   "2024-01" → "2024/01"
.str.contains()     특정 패턴(문자열) 포함 여부     "abc123" → True (if "abc" 포함 시)
.str.startswith()   특정 접두사로 시작 여부         "Python" → True (if "Py"로 시작)
.str.endswith()     특정 접미사로 끝남 여부         "main.py" → True (if ".py"로 끝남)
.str.len()          문자열 길이 반환                "apple" → 5
.str.split()        구분자로 분할하여 리스트 반환   "a,b,c" → ["a", "b", "c"]
.str.get(i)         i번째 원소 추출 (split 등에서) ["a","b","c"] → "a" (i=0)
.str.cat()          문자열 결합(Series끼리, 구분자) SeriesA.str.cat(SeriesB, sep=":")
'''
# 사용 예제
# 이름의 좌우 공백을 제거하고 모두 소문자로 변환
df['name_clea '] = df['name'].str.strip().str.lower()

# 이메일을 '@'로 분할 후 도메인(뒤쪽)만 추출
df['domain'] = df['email'].str.split('@').str.get(1)

# 이메일이 'gmail.com'을 포함하는지 True/False 반환
df['is_gmail'] = df['email'].str.contanins('gamil.com')

# info에서 ','로 분할 후, 앞쪽 (도시)와 뒷쪽 (나이) 추출
df['city'] = df['info'].str.split(',').str.get(0)
df['age'] = df['info'].str.split(',').str.get(1).str.strip().str.replate('세', '')

# 이름의 글자 수 확인 (공백 제거 후)
df['name_length'] = df['name'].str.strip().str.len()

'- 반드시 Series에서만 사용 가능 (DataFrame 전체에는 바로 적용 불가, 개별 열 선택 필요)'

######################################################################################################
# 정렬
# DataFrame의 행이나 열을 특정 기준으로 정렬
'''
정렬 메서드 정리:
┌──────────────────┬─────────────────────────────┐
│ 메서드           │ 용도                        │
├──────────────────┼─────────────────────────────┤
│ sort_values()    │ 열(컬럼) 값 기준 정렬       │
│ sort_index()     │ 행 인덱스 또는 열 이름 정렬 │
│ ascending        │ True=오름차순, False=내림차순│
│ by               │ 정렬 기준 열 지정           │
│ axis             │ 0=행, 1=열                  │
│ inplace          │ True=원본 변경              │
│ reset_index()    │ 인덱스 재정렬               │
└──────────────────┴─────────────────────────────┘

정렬 후 인덱스 처리:
- 정렬 후 인덱스가 불규칙해짐
- reset_index(drop=True)로 0부터 재정렬 권장
'''
'''
* 값 기준 정렬(sort_values)
 DataFrame.sort_values(by, axis=0, ascending=True, inplace=False)
    - by: 정렬 기준이 되는 컬럼명(또는 리스트)
    - axis: 0=행을 기준(기본), 1=열을 기준
    - ascending: 오름차순 여부(True=오름차순, False=내림차순)
    - inplace: 원본 변경 여부(False=새로운 객체 반환, True=원본 수정)
'''
'''
* 인덱스 기준 정렬(sort_index)
 DataFrame.sort_index(axis=0, ascending=True, inplace=False)
    - axis: 0=행 인덱스 기준, 1=열 이름 기준
    - ascending: 오름차순/내림차순
    - inplace: 원본 변경 여부
'''
'''
* reset_index()
    - DataFrame의 인덱스를 기본값(0, 1, 2, ...)으로 되돌리는 함수
        - 인덱스가 중간에 비연속적이거나, 삭제/추출/필터링 등으로 어긋났을 때 정렬된 기본 인덱스를 다시 부여함
        - 행 삭제, 조건 필터링 등 후에는 reset_index(drop=True) 습관화
    - drop
        - True : 기존 인덱스 값을 새로운 열로 남기지 않고 완전히 버림
        - False(기본값) : 기존 인덱스 값을 새 열로 DataFrame에 남김
    - inplace
        - True : 원본을 직접 변경
        - False(기본값) : 변경된 DataFrame을 반환(원본은 그대로)
'''

######################################################################################################
# 실습 3 정렬

# 사용 데이터
df = pd.DataFrame({
'name': ['Alice', 'Bob', 'Charlie', 'David'],
'score': [88, 95, 70, 100]
})
'''
# 문제 1: 단일 열 기준 오름차순 정렬
1. 주어진 DataFrame에서, score 컬럼 기준으로 오름차순 정렬한 결과를 출력하세요.
'''
# sort_values(by='컬럼명'): 특정 열을 기준으로 정렬
# 기본값: ascending=True (오름차순)
print(df.sort_values(by='score'))
# 결과: 70 → 88 → 95 → 100

# 주의: sort_values()는 원본을 변경하지 않음
# 변경하려면: df = df.sort_values(...) 또는 inplace=True
print(df)

'''
# 문제 2: 내림차순 정렬 + 인덱스 재정렬
2. score 컬럼 기준 내림차순으로 정렬한 후, 정렬된 인덱스를 무시하고 0부터 재정렬한 결과를 
출력하세요.
'''
# ascending=False: 내림차순 정렬
# reset_index(drop=True): 인덱스를 0부터 재정렬
print(df.sort_values(by='score', ascending=False).reset_index(drop=True))
# 결과: 100 → 95 → 88 → 70 (인덱스: 0, 1, 2, 3)

# 사용 데이터
df = pd.DataFrame({
'이름': ['가', '나', '다', '라', '마'],
'반': [2, 1, 1, 2, 1],
'점수': [90, 85, 80, 95, 85]
})
'''
# 문제 3: 다중 열 기준 정렬
3. 주어진 DataFrame에서,반(class) 기준 오름차순, 같은 반 내에서는 점수(score) 기준 내림차순으로 정렬한 결
과를 출력하세요.
'''
# sort_values(by=['열1', '열2']): 여러 열 기준 정렬
# ascending=[True, False]: 각 열마다 다른 정렬 방향
print(df.sort_values(by='반').sort_values(by='점수', ascending=False))
print(df.sort_values(by=['반', '점수'], ascending=[True, False]))
# 정렬 순서:
# 1) 먼저 '반'을 오름차순 (1반 → 2반)
# 2) 같은 반 내에서 '점수'를 내림차순
# 결과:
# 1반: 나(85), 마(85), 다(80) ← 점수 내림차순
# 2반: 라(95), 가(90)        ← 점수 내림차순

'''
# 문제 4: 열(컬럼) 이름 정렬
4. 열(컬럼) 이름을 알파벳순으로 정렬해서 출력하세요.
'''
# sort_index(axis=1): 열 이름을 알파벳순으로 정렬
# axis=0: 행 인덱스 정렬, axis=1: 열 이름 정렬
print(df.sort_index(axis=1))
# 결과: '이름', '점수', '반' → '반', '이름', '점수'

# 사용 데이터
df = pd.DataFrame({
'value': [10, 20, 30, 40]
}, index=[3, 1, 4, 2])  # 불규칙한 인덱스
'''
# 문제 5: 인덱스 기준 정렬
5. 인덱스 기준으로 오름차순 정렬한 결과를 출력하세요.
'''
# sort_index(): 행 인덱스를 기준으로 정렬
print(df.sort_index())

'''
# 문제 6: 다양한 정렬 방법
6. 인덱스 기준 내림차순 정렬, value 컬럼 기준 오름차순 정렬 두 가지 정렬 결과를 각각 출력하
세요.
'''
print(df.sort_index(ascending=False))
# 결과: 인덱스 4, 3, 2, 1 순서
print(df.sort_values(by='value'))
# 결과: 10, 20, 30, 40 순서 (인덱스는 원래대로)

######################################################################################################
# groupby(Grouping and Aggregation)
'''
groupby
 - 데이터프레임에서 특정 컬럼(또는 조건)에 따라 데이터를 그룹화하는 기능
 - 각 그룹별로 집계(합계, 평균 등), 변환, 필터링 등의 연산을 적용할 수 있도록 함
 - 집계 함수와 함께 사용
    - sum(), mean(), count(), size(), min(), max(), median(), std(), var(), first(), last(), agg(), 

DataFrame.groupby(by=None, axis=0, as_index=True)
    - by: 그룹화 기준 컬럼 또는 컬럼의 리스트(혹은 함수)
    - as_index: 결과의 그룹키를 인덱스로 할지 여부 (기본값: True)
    - axis: 그룹화 기준 방향 (보통 0=행, 기본값)
    
'''
'''
1. 기본 패턴:
   df.groupby('기준열')['집계열'].집계함수()

2. 다중 그룹:
   df.groupby(['열1', '열2'])['집계열'].집계함수()

3. 다중 집계:
   df.groupby('기준열')['집계열'].agg(['함수1', '함수2'])

4. 컬럼별 다른 집계:
   df.groupby('기준열').agg({
       '열1': '함수1',
       '열2': ['함수2', '함수3']
   })

5. 명명된 집계(가독성 최고):
   df.groupby('기준열').agg(
       새이름1=('열1', '함수1'),
       새이름2=('열2', '함수2')
   )

6. 결측값 처리:
   - dropna = True (기본): 결측값 제외
   - dropna = False: 결측값 포함

7. 인덱스 제어:
   - as_index = True (기본): 그룹 키가 인덱스
   - as_index = False: 그룹 키가 일반 컬럼
'''
# 데이터를 특정 기준으로 묶어서 분석하는 핵심 기법입니다.
# SQL의 GROUP BY와 유사하며, 데이터 분석의 필수 도구입니다.

# ─────────────────────────────────────────────────────────────
# 1. GroupBy의 필요성
# ─────────────────────────────────────────────────────────────

'''
    그룹화가 필요한 이유:
    
    ❌ 전체 평균만으로는 부족한 경우가 많음
       예: 전체 평균 연봉 5,000만원
       → 하지만 부서별로는 큰 차이가 있을 수 있음
    
    ✅ 그룹화를 통해 얻는 인사이트:
       - 카테고리별 패턴 발견 (부서별, 지역별, 시간별)
       - 세그먼트별 비교 분석
       - 숨겨진 트렌드 파악
       
    실무 예시:
    - 부서별 평균 연봉 비교
    - 월별 매출 추이 분석
    - 지역별 고객 수 집계
    - 제품 카테고리별 판매량
'''

# 직원 데이터 예시
employee_data = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry'],
    'department': ['Dev', 'Dev', 'Sales', 'Sales', 'Dev', 'HR', 'HR', 'Sales'],
    'years': [3, 5, 2, 7, 10, 4, 6, 3],  # 근속연수
    'salary': [4500, 5500, 4000, 6500, 8000, 4800, 5800, 4200]  # 연봉(만원)
})

print('전체 직원 데이터')
print(employee_data)
print()

# ─────────────────────────────────────────────────────────────
# 2. 전체 분석 vs 그룹별 분석 비교
# ─────────────────────────────────────────────────────────────

# 전체 평균 - 모든 직원의 평균 연봉
print('전체 분석')
overall_avg = employee_data['salary'].mean()
print(f'전체 평균 연봉: {overall_avg:.2f}만원')
# 결과: 5,412.5만원 → 부서별 차이가 보이지 않음!
print()

# 그룹별 평균 - 부서별로 나누어 분석
print('그룹별 분석')
dept_avg = employee_data.groupby('department')['salary'].mean()
print(dept_avg)
# 결과:
# Dev      6000.0  (개발팀이 가장 높음)
# HR       5300.0
# Sales    4900.0  (영업팀이 가장 낮음)
# → 부서별 연봉 격차가 명확하게 드러남!
print()

# ═══════════════════════════════════════════════════════════════
# GroupBy의 핵심 개념: Split-Apply-Combine
# ═══════════════════════════════════════════════════════════════

'''
    GroupBy의 3단계 프로세스:
    
    1. Split (분할)
       - 데이터를 그룹으로 나누기
       - 예: 부서별로 직원 데이터 분리
    
    2. Apply (적용)
       - 각 그룹에 독립적으로 함수 적용
       - 예: 각 부서의 평균 연봉 계산
    
    3. Combine (결합)
       - 결과를 하나의 DataFrame/Series로 합치기
       - 예: 부서별 평균을 하나의 테이블로 정리
    
    시각적 표현:
    ┌─────────────────┐
    │  전체 데이터     │
    └────────┬────────┘
             │ Split
    ┌────────┴────────┐
    │ Dev │ HR │Sales │ ← 그룹별로 분할
    └────┬───┬───┬────┘
         │   │   │ Apply (각 그룹에 함수 적용)
    ┌────┴───┴───┴────┐
    │   결과 테이블     │ ← Combine
    └─────────────────┘
'''

print('=== Split - Apply - Combine 단계별 확인 ===')
simple_data = pd.DataFrame({
    'category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'value': [10, 20, 15, 25, 12, 22]
})
print('원본 데이터')
print(simple_data)
print()

# ─────────────────────────────────────────────────────────────
# 1단계: Split (분할) - 데이터를 그룹으로 나누기
# ─────────────────────────────────────────────────────────────
print('【1단계: Split】')
for category, group in simple_data.groupby('category'):
    print(f'\n{category} 그룹:')
    print(group)
# A 그룹: 0, 2, 4번 행 (value: 10, 15, 12)
# B 그룹: 1, 3, 5번 행 (value: 20, 25, 22)
print()

# ─────────────────────────────────────────────────────────────
# 2단계: Apply (적용) - 각 그룹에 함수 적용
# ─────────────────────────────────────────────────────────────
print('【2단계: Apply】')
for category, group in simple_data.groupby('category'):
    avg = group['value'].mean()
    print(f'{category} 그룹 평균: {avg}')
# A 그룹 평균: (10+15+12) / 3 = 12.33
# B 그룹 평균: (20+25+22) / 3 = 22.33
print()

# ─────────────────────────────────────────────────────────────
# 3단계: Combine (결합) - 결과를 하나로 합치기
# ─────────────────────────────────────────────────────────────
print('【3단계: Combine】')
result = simple_data.groupby('category')['value'].mean()
print(result)
# category
# A    12.333333
# B    22.333333
# Name: value, dtype: float64
print()

# ═══════════════════════════════════════════════════════════════
# groupby() 메서드의 주요 매개변수
# ═══════════════════════════════════════════════════════════════

'''
    groupby() 함수 시그니처:
    groupby(by=None, axis=0, level=None, as_index=True, sort=True, ...)
    
    주요 매개변수:
    - by: 그룹화 기준 (컬럼명 또는 컬럼명 리스트)
    - as_index: 그룹 키를 인덱스로 설정할지 여부 (기본=True)
    - sort: 그룹 키를 정렬할지 여부 (기본=True)
    - axis: 0=행, 1=열 기준 그룹화 (거의 항상 0 사용)
'''

# ─────────────────────────────────────────────────────────────
# 3. groupby() 사용법 - 컬럼 선택 방법
# ─────────────────────────────────────────────────────────────

employee_data = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry'],
    'department': ['Dev', 'Dev', 'Sales', 'Sales', 'Dev', 'HR', 'HR', 'Sales'],
    'years': [3, 5, 2, 7, 10, 4, 6, 3],
    'salary': [4500, 5500, 4000, 6500, 8000, 4800, 5800, 4200]
})

print('=== 컬럼 선택 방법 ===')

# 방법 1 - 대괄호 접근 (권장)
result1 = employee_data.groupby('department')['salary'].mean()
print('방법 1: groupby("부서")["연봉"]')
print(result1)
print()

# 방법 2 - 점(.) 접근 (간결하지만 컬럼명에 공백 있으면 사용 불가)
result2 = employee_data.groupby('department').salary.mean()
print('방법 2: groupby("부서").salary')
print(result2)
print()

# 방법 3 - 여러 컬럼 선택 (이중 대괄호 사용)
result3 = employee_data.groupby('department')[['salary', 'years']].mean()
print('방법 3: 여러 컬럼 선택')
print(result3)
# 결과: salary와 years 모두 평균 계산
print()

# ─────────────────────────────────────────────────────────────
# 4. as_index 매개변수 - 인덱스 설정 제어
# ─────────────────────────────────────────────────────────────

print('=== as_index 매개변수 ===')

# as_index=True (기본값) - 그룹 키가 인덱스로 설정됨
result_indexed = employee_data.groupby(
    'department', as_index=True)['salary'].mean()
print('as_index=True (기본값):')
print(result_indexed)
print(f'타입: {type(result_indexed)}')  # Series
print(f'인덱스: {result_indexed.index.tolist()}')  # ['Dev', 'HR', 'Sales']
# 장점: 인덱싱으로 빠른 접근 가능 (result_indexed['Dev'])
# 단점: DataFrame으로 변환 필요한 경우 불편
print()

# as_index=False - 그룹 키가 일반 컬럼으로 유지됨
result_no_indexed = employee_data.groupby(
    'department', as_index=False)['salary'].mean()
print('as_index=False:')
print(result_no_indexed)
print(f'타입: {type(result_no_indexed)}')  # DataFrame
# 장점: 바로 DataFrame 형태, 추가 처리 용이
# 단점: 인덱스 접근 불가
print()

'''
    as_index 선택 가이드:
    - True: 빠른 조회, 시각화에 적합
    - False: 추가 분석, 병합(merge) 작업에 적합
'''

# ─────────────────────────────────────────────────────────────
# 5. sort 매개변수 - 정렬 제어
# ─────────────────────────────────────────────────────────────

print('=== sort 매개변수 ===')

# sort=True (기본값) - 그룹 키를 알파벳/숫자 순으로 정렬
result_sorted = employee_data.groupby(
    'department', sort=True)['salary'].mean()
print('sort=True (기본값):')
print(result_sorted)
# 결과: Dev, HR, Sales 순서 (알파벳순)
print()

# sort=False - 데이터 등장 순서대로 유지
result_no_sorted = employee_data.groupby(
    'department', sort=False)['salary'].mean()
print('sort=False:')
print(result_no_sorted)
# 결과: Dev, Sales, HR 순서 (데이터에 나타난 순서)
# 장점: 대용량 데이터에서 정렬 비용 절약 (속도 향상)
print()

# ═══════════════════════════════════════════════════════════════
# 6. 집계 함수 (Aggregation Functions)
# ═══════════════════════════════════════════════════════════════

'''
    주요 집계 함수:
    
    기본 통계:
    - count()   : 개수 (결측값 제외)
    - sum()     : 합계
    - mean()    : 평균
    - median()  : 중앙값 (중간값)
    - min()     : 최솟값
    - max()     : 최댓값
    
    분산 관련:
    - var()     : 분산 (데이터의 퍼진 정도²)
    - std()     : 표준편차 (데이터의 퍼진 정도)
    
    기타:
    - first()   : 첫 번째 값
    - last()    : 마지막 값
    - size()    : 그룹 크기 (결측값 포함)
'''

print('=== 집계 함수 예시 ===')
print(f"count: {employee_data.groupby('department')['salary'].count()}")
print(f"sum: {employee_data.groupby('department')['salary'].sum()}")
print(f"min: {employee_data.groupby('department')['salary'].min()}")
print(f"max: {employee_data.groupby('department')['salary'].max()}")
print()

# ─────────────────────────────────────────────────────────────
# 7. describe() - 종합 통계 한 번에 확인
# ─────────────────────────────────────────────────────────────

# describe(): 여러 통계를 한 번에 계산하는 편리한 메서드
result = employee_data.groupby('department')['salary'].describe()
print('=== describe() 종합 통계 ===')
print(result)
# 결과: count, mean, std, min, 25%, 50%, 75%, max 모두 출력
# 데이터 분포를 한눈에 파악 가능!
print()

# ═══════════════════════════════════════════════════════════════
# 8. 다중 그룹화 (Multiple Grouping)
# ═══════════════════════════════════════════════════════════════
# 여러 컬럼을 기준으로 계층적 그룹화

employee_detail = pd.DataFrame({
    'department': ['Dev', 'Dev', 'Dev', 'Sales', 'Sales', 'Sales', 'HR', 'HR'],
    'position': ['Junior', 'Mid', 'Senior', 'Junior', 'Mid', 'Senior', 'Mid', 'Senior'],
    'gender': ['M', 'F', 'M', 'F', 'M', 'M', 'F', 'F'],
    'salary': [4000, 4500, 5500, 3800, 4300, 5200, 4500, 5300]
})

print('=== 다중 그룹화 ===')

# 부서 → 직급 순서로 그룹화
multi_group1 = employee_detail.groupby(
    ['department', 'position'])['salary'].mean()
print('부서 → 직급 순 그룹화:')
print(multi_group1)
# 결과: 계층적 인덱스 (MultiIndex)
# Dev
#   Junior    4000
#   Mid       4500
#   Senior    5500
# HR
#   Mid       4500
#   Senior    5300
# ...
print()

# 직급 → 부서 순서로 그룹화 (순서가 다르면 결과 구조가 달라짐!)
multi_group2 = employee_detail.groupby(
    ['position', 'department'])['salary'].mean()
print('직급 → 부서 순 그룹화:')
print(multi_group2)
# 결과:
# Junior
#   Dev      4000
#   Sales    3800
# Mid
#   Dev      4500
#   HR       4500
#   Sales    4300
# ...
print()

'''
    다중 그룹화 팁:
    - 첫 번째 기준이 상위 레벨, 두 번째가 하위 레벨
    - unstack()으로 피벗 테이블처럼 변환 가능
    - reset_index()로 일반 DataFrame으로 변환
'''

# ═══════════════════════════════════════════════════════════════
# 9. agg() - 다양한 집계 동시 수행
# ═══════════════════════════════════════════════════════════════
# agg() = aggregate (집계하다)
# 여러 집계 함수를 한 번에 적용할 수 있는 강력한 메서드

monthly_sales = pd.DataFrame({
    'month': [1, 1, 2, 2, 3, 3, 1, 2, 3],
    'store': ['A', 'B', 'A', 'B', 'A', 'B', 'C', 'C', 'C'],
    'sales': [100, 80, 120, 90, 150, 100, 110, 95, 130],  # 매출
    'customers': [50, 40, 60, 45, 75, 50, 55, 48, 65]     # 고객수
})

print('=== agg() 다양한 사용법 ===')

# ─────────────────────────────────────────────────────────────
# 방법 1: 함수 이름 리스트 (가장 간단)
# ─────────────────────────────────────────────────────────────
result1 = monthly_sales.groupby('store')['sales'].agg(['mean', 'sum', 'std'])
print('방법 1: 함수 이름 리스트')
print(result1)
# 결과: 각 매장의 평균, 합계, 표준편차가 열로 표시됨
print()

# ─────────────────────────────────────────────────────────────
# 방법 2: 함수 객체 사용 (NumPy 함수 등)
# ─────────────────────────────────────────────────────────────
result2 = monthly_sales.groupby(
    'store')['sales'].agg([np.mean, np.sum, np.std])
print('방법 2: 함수 객체 사용')
print(result2)
# 결과: 컬럼명이 <ufunc 'mean'> 같은 형태로 나옴 (권장하지 않음)
print()

# ─────────────────────────────────────────────────────────────
# 방법 3: 딕셔너리로 컬럼별 다른 함수 적용 (가장 유연)
# ─────────────────────────────────────────────────────────────
result3 = monthly_sales.groupby('store').agg({
    'sales': ['mean', 'sum'],        # 매출: 평균, 합계
    'customers': ['mean', 'max']      # 고객수: 평균, 최댓값
})
print('방법 3: 딕셔너리로 컬럼별 다른 함수')
print(result3)
# 결과: 계층적 컬럼명 (MultiIndex)
#        sales              customers
#         mean   sum         mean  max
# store
# A      123.33  370         61.67  75
# B       90.00  270         45.00  50
# C      111.67  335         56.00  65
print()

# ─────────────────────────────────────────────────────────────
# 방법 4: 사용자 정의 함수 (람다 또는 def)
# ─────────────────────────────────────────────────────────────
result4 = monthly_sales.groupby('store')['sales'].agg([
    ('평균', 'mean'),
    ('합계', 'sum'),
    ('범위', lambda x: x.max() - x.min())  # 최댓값 - 최솟값
])
print('방법 4: 사용자 정의 함수와 이름 지정')
print(result4)
# 결과: 컬럼명을 한글로 지정 가능, 복잡한 계산 가능
print()

'''
═══════════════════════════════════════════════════════════════
GroupBy 실무 활용 패턴
═══════════════════════════════════════════════════════════════

1. 기본 집계
   df.groupby('부서')['연봉'].mean()

2. 다중 집계
   df.groupby('부서').agg({'연봉': 'mean', '근속연수': 'max'})

3. 다중 그룹화
   df.groupby(['부서', '직급'])['연봉'].mean()

4. 필터링과 결합
   df.groupby('부서').filter(lambda x: x['연봉'].mean() > 5000)

5. 변환(Transform)
   df['부서_평균'] = df.groupby('부서')['연봉'].transform('mean')

자주 사용되는 조합:
- as_index=False → 병합(merge) 작업 전
- sort=False → 대용량 데이터 성능 최적화
- agg(['mean', 'std']) → 평균과 분산 동시 확인
'''

# ═══════════════════════════════════════════════════════════════
# 실전 예제: 월별 매장 성과 분석
# ═══════════════════════════════════════════════════════════════

print('=== 종합 실전 예제 ===')

# 월별, 매장별 통합 분석
comprehensive = monthly_sales.groupby(['month', 'store']).agg({
    'sales': ['sum', 'mean'],
    'customers': ['sum', 'mean']
})

print('월별/매장별 종합 분석:')
print(comprehensive)
print()

# 매장별 총합 (월 구분 없이)
store_total = monthly_sales.groupby('store', as_index=False).agg({
    'sales': ['sum', 'mean'],
    'customers': 'sum'
})
print('매장별 총합:')
print(store_total)

######################################################################################################
# 실습 4 groupby 정렬문제

'''
# 문제 1: 단일 그룹, 단일 집계
1. 각 학년(grade)별 평균 국어 점수(kor)를 구하세요.
'''
df = pd.DataFrame({
'grade': [1, 2, 1, 2, 1, 3],
'name': ['Kim', 'Lee', 'Park', 'Choi', 'Jung', 'Han'],
'kor': [85, 78, 90, 92, 80, 75]
})

print(df.groupby('grade')['kor'].mean())
# 결과:
# grade
# 1    85.0  (85+90+80)/3
# 2    85.0  (78+92)/2
# 3    75.0

'''
# 문제 2: 다중 그룹, 다중 집계 + 열 이름 변경
2. 아래 DataFrame에서 반(class)별, 과목(subject)별로 시험에 응시한 학생 수(count)와 평균 점수(avg)를 구하세요.
'''
df = pd.DataFrame({
'class': [1, 1, 1, 2, 2, 2],
'subject': ['Math', 'Math', 'Eng', 'Math', 'Eng', 'Eng'],
'score': [80, 90, 85, 70, 95, 90]
})

print(df.groupby(['class', 'subject']).count())
print(df.groupby(['class', 'subject']).mean())

result = df.groupby(['class', 'subject'])['score'].agg(['count', 'mean'])
print(result)
# agg(['count', 'mean']): 두 집계 함수를 동시에 적용
# 결과 컬럼명: 'count', 'mean'

# rename(): 컬럼명 변경
# columns={'기존이름': '새이름'}
# inplace=True: 원본 변경
result.rename(columns={'mean': 'avg'}, inplace=True)
print(result)
# 결과:
#                count  avg
# class subject
# 1     Eng          1   85.0
#       Math         2   85.0  (80+90)/2
# 2     Eng          2   92.5  (95+90)/2
#       Math         1   70.0

'''
# 문제 3: 다중 그룹, 다중 집계
3. 아래 DataFrame에서 지역(region)별 판매자(seller)별로 판매액(sales)의 합계와 최대값을 구하세요.
'''
df = pd.DataFrame({
'region': ['Seoul', 'Seoul', 'Busan', 'Busan', 'Daegu'],
'seller': ['A', 'B', 'A', 'B', 'A'],
'sales': [100, 200, 150, 120, 130]
})

print(df.groupby(['region', 'seller'])['sales'].agg(['sum', 'max']))
# 결과:
#                sum  max
# region seller
# Busan  A       150  150
#        B       120  120
# Daegu  A       330  200  (130+200, max=200)
# Seoul  A       100  100
#        B       200  200

'''
# 문제 4: 결측값 포함 그룹화
4. 아래 DataFrame에서 팀(team)별, 포지션(position)별로 결측치(NaN)를 포함한 점수(score)의 평균을 구하세요.
'''
df = pd.DataFrame({
'team': ['A', 'A', 'B', 'B', 'A', 'B'],
'position': ['FW', 'DF', 'FW', 'DF', 'DF', 'FW'],
'score': [3, 2, None, 1, 4, 2]
})

# dropna=False: 결측값도 그룹화에 포함
# 기본값(dropna=True)은 결측값이 있는 행을 제외함
print(df.groupby(['team', 'position'], dropna=False)['score'].mean())
# 결과:
# team  position
# A     DF          3.0  (2+4)/2
#       FW          3.0
# B     DF          1.0
#       FW          2.0  (None+2)/1 = 2.0 (None은 평균 계산 시 제외)

'''
# 문제 5: agg() 딕셔너리 방식 + 이름 지정
5. 아래 DataFrame에서 부서(dept)별로 성별(gender)별 인원 수와, 총 연봉(salary) 합계를 구하세요.
'''
df = pd.DataFrame({
'dept': ['HR', 'HR', 'IT', 'IT', 'Sales', 'Sales'],
'gender': ['M', 'F', 'F', 'M', 'F', 'F'],
'salary': [3500, 3200, 4000, 4200, 3000, 3100]
})
# 방법 1: 기본 agg() (컬럼명 자동)
result1 = df.groupby(['dept', 'gender'])['salary'].agg(['count', 'sum'])
print(result1)

# 방법 2: 명명된 집계 (권장)
# 새컬럼명=('집계대상컬럼', '집계함수')
result2 = df.groupby(['dept', 'gender']).agg(
    count=('salary', 'count'),       # 새 컬럼: count
    total_salary=('salary', 'sum')   # 새 컬럼: total_salary
)
print(result2)
# 결과:
#               count  total_salary
# dept  gender
# HR    F           1          3200
#       M           1          3500
# IT    F           1          4000
#       M           1          4200
# Sales F           2          6100  (3000+3100)

# ═══════════════════════════════════════════════════════════════
# 추가 실전 예제 및 고급 팁
# ═══════════════════════════════════════════════════════════════

print("=" * 60)
print("추가 실전 예제")
print("=" * 60)

# ─────────────────────────────────────────────────────────────
# 예제 1: 조건 필터링 종합
# ─────────────────────────────────────────────────────────────

students = pd.DataFrame({
    '이름': ['철수', '영희', '민수', '지영', '동현'],
    '학년': [1, 2, 1, 2, 3],
    '성별': ['남', '여', '남', '여', '남'],
    '수학': [85, 92, 78, 95, 88],
    '영어': [90, 88, 85, 92, 94]
})

print("\n[원본 데이터]")
print(students)
print()

# 복합 조건 1: 1학년 남학생
print("[복합 조건 1] 1학년 남학생:")
result = students[(students['학년'] == 1) & (students['성별'] == '남')]
print(result)
print()

# 복합 조건 2: 수학 90점 이상 OR 영어 90점 이상
print("[복합 조건 2] 수학 90점 이상 OR 영어 90점 이상:")
result = students[(students['수학'] >= 90) | (students['영어'] >= 90)]
print(result)
print()

# 복합 조건 3: 부정 조건 (NOT)
# ~ 연산자: 조건의 반대
print("[복합 조건 3] 1학년이 아닌 학생:")
result = students[~(students['학년'] == 1)]
# 또는: students[students['학년'] != 1]
print(result)
print()

# 복합 조건 4: 범위 조건
# between(최소값, 최대값): 특정 범위 내의 값
print("[복합 조건 4] 수학 점수 80~90점:")
result = students[students['수학'].between(80, 90)]
# 또는: students[(students['수학'] >= 80) & (students['수학'] <= 90)]
print(result)
print()

# 복합 조건 5: 문자열 포함 검색
# str.contains('문자열'): 문자열 포함 여부
students_copy = students.copy()
students_copy['이름'] = ['김철수', '이영희', '박민수', '최지영', '정동현']
print("[복합 조건 5] 이름에 '영'이 포함된 학생:")
result = students_copy[students_copy['이름'].str.contains('영')]
print(result)
print()

# ─────────────────────────────────────────────────────────────
# 예제 2: 행/열 추가 삭제 종합
# ─────────────────────────────────────────────────────────────

scores = pd.DataFrame({
    '이름': ['A', 'B', 'C'],
    '점수1': [80, 90, 85]
})

print("\n[행/열 추가 삭제 종합]")
print("원본:")
print(scores)
print()

# 1. 여러 열 동시 추가
print("1. 여러 열 동시 추가:")
scores['점수2'] = [85, 88, 90]
scores['점수3'] = [82, 91, 87]
print(scores)
print()

# 2. 계산된 값으로 열 추가
print("2. 평균 열 추가 (계산):")
scores['평균'] = (scores['점수1'] + scores['점수2'] + scores['점수3']) / 3
# 또는: scores['평균'] = scores[['점수1', '점수2', '점수3']].mean(axis=1)
print(scores)
print()

# 3. 조건부 열 추가
print("3. 합격 여부 열 추가 (조건부):")
# np.where(조건, 참일때값, 거짓일때값)
scores['합격'] = np.where(scores['평균'] >= 85, '합격', '불합격')
print(scores)
print()

# 4. 여러 열 동시 삭제
print("4. 점수1, 점수2 열 삭제:")
scores = scores.drop(['점수1', '점수2'], axis=1)
# 또는: scores = scores.drop(columns=['점수1', '점수2'])
print(scores)
print()

# 5. 여러 행 동시 삭제
print("5. 불합격 학생 모두 삭제:")
scores = scores[scores['합격'] == '합격']
# 또는: scores = scores.drop(scores[scores['합격'] == '불합격'].index)
print(scores)
print()

# ─────────────────────────────────────────────────────────────
# 예제 3: 정렬 고급 활용
# ─────────────────────────────────────────────────────────────

employees = pd.DataFrame({
    '부서': ['영업', '개발', '영업', '개발', '인사'],
    '이름': ['김', '이', '박', '최', '정'],
    '급여': [4500, 5500, 4800, 6000, 4200],
    '경력': [3, 5, 4, 7, 2]
})

print("\n[정렬 고급 활용]")
print("원본:")
print(employees)
print()

# 1. 부서별 정렬 후 급여 내림차순
print("1. 부서 오름차순 → 급여 내림차순:")
result = employees.sort_values(
    by=['부서', '급여'],
    ascending=[True, False]  # 부서는 오름차순, 급여는 내림차순
)
print(result)
print()

# 2. 정렬 후 순위 컬럼 추가
print("2. 급여순 순위 추가:")
employees_ranked = employees.copy()
# rank(): 순위 계산 (기본: 평균 순위, method='min'으로 최소 순위)
employees_ranked['급여순위'] = employees_ranked['급여'].rank(
    ascending=False,  # 높은 급여가 1위
    method='min'      # 동점은 최소 순위
)
print(employees_ranked.sort_values('급여순위'))
print()

# 3. 상위 N개 추출 (정렬 + 슬라이싱)
print("3. 급여 상위 3명:")
top3 = employees.nlargest(3, '급여')  # nlargest(개수, 기준컬럼)
# 또는: employees.sort_values('급여', ascending=False).head(3)
print(top3)
print()

# 4. 하위 N개 추출
print("4. 경력 하위 2명:")
bottom2 = employees.nsmallest(2, '경력')  # nsmallest(개수, 기준컬럼)
print(bottom2)
print()

# ─────────────────────────────────────────────────────────────
# 예제 4: GroupBy 고급 활용
# ─────────────────────────────────────────────────────────────

sales_data = pd.DataFrame({
    '지역': ['서울', '서울', '부산', '부산', '서울', '부산'],
    '분기': ['Q1', 'Q2', 'Q1', 'Q2', 'Q3', 'Q3'],
    '매출': [100, 120, 80, 90, 130, 95],
    '비용': [60, 70, 50, 55, 75, 60]
})

print("\n[GroupBy 고급 활용]")
print("원본:")
print(sales_data)
print()

# 1. 그룹별 통계 + 새 컬럼 계산
print("1. 지역별 매출 통계:")
result = sales_data.groupby('지역').agg({
    '매출': ['sum', 'mean', 'count'],
    '비용': 'sum'
})
print(result)
print()

# 2. transform으로 그룹 평균 추가
# transform(): 원본과 같은 크기로 결과 반환
print("2. 지역별 평균 매출 컬럼 추가:")
sales_with_avg = sales_data.copy()
sales_with_avg['지역평균매출'] = sales_data.groupby('지역')['매출'].transform('mean')
print(sales_with_avg)
# transform의 특징: 각 행에 해당 그룹의 집계 값이 채워짐
print()

# 3. 그룹별 누적합
print("3. 지역별 매출 누적합:")
sales_with_cumsum = sales_data.copy()
sales_with_cumsum['누적매출'] = sales_data.groupby('지역')['매출'].cumsum()
print(sales_with_cumsum)
print()

# 4. 그룹별 필터링
# filter(함수): 조건을 만족하는 그룹만 반환
print("4. 총 매출 300 이상인 지역만:")
result = sales_data.groupby('지역').filter(
    lambda x: x['매출'].sum() >= 300
)
print(result)
# 서울의 총 매출: 100+120+130 = 350 (포함)
# 부산의 총 매출: 80+90+95 = 265 (제외)
print()

# 5. 사용자 정의 집계 함수
print("5. 지역별 매출 범위 (최대-최소):")
result = sales_data.groupby('지역')['매출'].agg(
    범위=lambda x: x.max() - x.min()
)
print(result)
print()

# 6. 피벗 테이블처럼 활용
print("6. 지역/분기별 매출 (unstack):")
result = sales_data.groupby(['지역', '분기'])['매출'].sum().unstack(fill_value=0)
# unstack(): MultiIndex를 피벗 테이블 형태로 변환
print(result)
print()

# ─────────────────────────────────────────────────────────────
# 예제 5: 종합 실전 문제
# ─────────────────────────────────────────────────────────────

print("\n[종합 실전 문제]")

# 고객 구매 데이터
purchases = pd.DataFrame({
    '고객ID': ['A001', 'A001', 'A002', 'A003', 'A002', 'A001', 'A003'],
    '상품': ['노트북', '마우스', '키보드', '모니터', '노트북', '키보드', '마우스'],
    '금액': [1200000, 30000, 80000, 300000, 1300000, 85000, 35000],
    '수량': [1, 2, 1, 1, 1, 1, 3],
    '날짜': ['2024-01-15', '2024-01-20', '2024-02-10',
           '2024-02-15', '2024-03-05', '2024-03-10', '2024-03-20']
})

print("원본 구매 데이터:")
print(purchases)
print()

# 문제 1: 고객별 총 구매금액과 구매횟수
print("문제 1: 고객별 총 구매금액과 구매횟수")
result = purchases.groupby('고객ID').agg(
    총구매금액=('금액', 'sum'),
    구매횟수=('금액', 'count'),
    평균구매금액=('금액', 'mean')
).round(0)  # 소수점 반올림
print(result)
print()

# 문제 2: 100만원 이상 구매한 고객만 추출
print("문제 2: 100만원 이상 구매 내역:")
high_value = purchases[purchases['금액'] >= 1000000]
print(high_value)
print()

# 문제 3: 고객별 총 구매금액이 150만원 이상인 고객
print("문제 3: 총 구매금액 150만원 이상 고객:")
customer_total = purchases.groupby('고객ID')['금액'].sum()
vip_customers = customer_total[customer_total >= 1500000]
print(vip_customers)
print()

# 문제 4: 상품별 판매현황
print("문제 4: 상품별 판매현황:")
product_sales = purchases.groupby('상품').agg(
    판매횟수=('수량', 'count'),
    총판매수량=('수량', 'sum'),
    총판매금액=('금액', 'sum')
).sort_values('총판매금액', ascending=False)
print(product_sales)
print()

# 문제 5: 날짜를 datetime으로 변환하고 월별 집계
print("문제 5: 월별 매출:")
purchases['날짜'] = pd.to_datetime(purchases['날짜'])
purchases['월'] = purchases['날짜'].dt.month
monthly_sales = purchases.groupby('월')['금액'].sum()
print(monthly_sales)
print()

'''
═══════════════════════════════════════════════════════════════
핵심 메서드 체크리스트
═══════════════════════════════════════════════════════════════

□ 조건 필터링:
  - df[조건]
  - df[(조건1) & (조건2)]  # AND
  - df[(조건1) | (조건2)]  # OR
  - df[~조건]              # NOT
  - df['열'].isin([값들])
  - df['열'].between(최소, 최대)
  - df['열'].str.contains('문자')

□ 행/열 추가:
  - df['새열'] = 값
  - df.loc[인덱스] = [값들]
  - pd.concat([df, new_df], ignore_index=True)

□ 행/열 삭제:
  - df.drop('열', axis=1)
  - df.drop(인덱스)
  - df.drop(['열1', '열2'], axis=1)
  - df[조건]  # 필터링으로 간접 삭제

□ 정렬:
  - df.sort_values(by='열')
  - df.sort_values(by=['열1', '열2'], ascending=[True, False])
  - df.sort_index()
  - df.nlargest(n, '열')
  - df.nsmallest(n, '열')

□ 그룹화:
  - df.groupby('열')['집계열'].함수()
  - df.groupby('열').agg({'열1': '함수1', '열2': '함수2'})
  - df.groupby('열').agg(이름=('열', '함수'))
  - df.groupby('열')['열'].transform('함수')
  - df.groupby('열').filter(lambda x: 조건)

□ 인덱스 관리:
  - df.reset_index(drop=True)
  - df.set_index('열')
  - df.index

□ 데이터 타입:
  - pd.to_datetime('날짜')
  - df['열'].astype('타입')
'''

# ═══════════════════════════════════════════════════════════════
# 실무 팁과 주의사항
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("실무 팁과 주의사항")
print("=" * 60)

print("""
1. 조건 필터링 시:
   ✅ 조건마다 괄호() 필수
   ✅ and/or 대신 &/| 사용
   ✅ 여러 값 비교는 isin() 사용
   ❌ df[df.score >= 80 and df.name == 'A']  # 오류!
   ✅ df[(df.score >= 80) & (df.name == 'A')]  # 정상

2. 원본 보존:
   ✅ 원본 변경: df.drop(..., inplace=True)
   ✅ 새 변수: new_df = df.drop(...)
   ❌ 주의: 대부분의 메서드는 원본을 변경하지 않음!

3. 인덱스 관리:
   ✅ 필터링/삭제 후 reset_index(drop=True)
   ✅ concat 시 ignore_index=True
   ❌ 인덱스 불연속 방치 → 접근 오류 발생

4. 정렬 후:
   ✅ inplace=True 또는 재할당
   ✅ reset_index(drop=True)로 인덱스 정리
   ❌ 정렬만 하고 저장 안 함 → 원본 그대로

5. GroupBy 활용:
   ✅ as_index=False → 병합 작업 전
   ✅ 명명된 집계로 가독성 향상
   ✅ transform으로 원본 크기 유지
   ❌ 너무 많은 그룹 → 성능 저하

6. 성능 최적화:
   ✅ 큰 데이터는 필터링 먼저
   ✅ 불필요한 정렬 피하기 (sort=False)
   ✅ 필요한 열만 선택
   ❌ 전체 데이터에서 무거운 연산

7. 데이터 검증:
   ✅ df.info() → 데이터 타입 확인
   ✅ df.isnull().sum() → 결측값 확인
   ✅ df.describe() → 통계 요약
   ✅ df.duplicated().sum() → 중복 확인
""")

# ═══════════════════════════════════════════════════════════════
# 자주 하는 실수와 해결법
# ═══════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("자주 하는 실수와 해결법")
print("=" * 60)

print("""
실수 1: SettingWithCopyWarning
문제: df_filtered = df[df.score > 80]
     df_filtered['grade'] = 'A'  # 경고 발생!
해결: df_filtered = df[df.score > 80].copy()

실수 2: 조건문 괄호 누락
문제: df[df.age > 20 & df.city == 'Seoul']  # 오류!
해결: df[(df.age > 20) & (df.city == 'Seoul')]

실수 3: 인덱스 불일치
문제: df1과 df2를 병합했는데 인덱스가 꼬임
해결: reset_index(drop=True) 사용

실수 4: inplace 오해
문제: result = df.sort_values('col', inplace=True)
     print(result)  # None 출력됨!
해결: inplace=True면 반환값이 None
     df.sort_values('col', inplace=True)
     또는
     result = df.sort_values('col')

실수 5: 문자열 컬럼에 수치 연산
문제: df['age'].mean()  # 오류 (age가 문자열)
해결: df['age'] = df['age'].astype(int)
     df['age'].mean()

실수 6: 날짜 형식 미변환
문제: df['date'] > '2024-01-01'  # 문자열 비교
해결: df['date'] = pd.to_datetime(df['date'])
     df['date'] > '2024-01-01'  # 날짜 비교
""")