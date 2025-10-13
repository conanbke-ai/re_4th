import pandas as pd
import numpy as np

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
print("미세먼지 평균:", df["미세먼지"].mean())
print("미세먼지 중앙값:", df["미세먼지"].median())

'''
2. ‘초미세먼지’ 컬럼의 최댓값과 최솟값을 구하세요.
'''
print("초미세먼지 최댓값:", df["초미세먼지"].max())
print("초미세먼지 최솟값:", df["초미세먼지"].min())

'''
3. 각 컬럼별 결측값 개수를 구하세요.
'''
print("결측값 개수:\n", df.isnull().sum())

'''
4. 결측값이 하나라도 있는 행을 모두 삭제한 뒤, 남은 데이터의 ‘초미세먼지’ 평균을 구하세요.
'''
drop_null = df.dropna(how='any')
print("결측값 삭제:\n", drop_null)
print("초미세먼지 평균:", drop_null["초미세먼지"].mean())

'''
5. 결측값을 모두 0으로 채운 뒤, ‘미세먼지’와 ‘초미세먼지’의 합계를 각각 구하세요.
'''
zero_filled = df.fillna(0)
print("미세먼지 합계:", zero_filled["미세먼지"].sum())
print("초미세먼지 합계:", zero_filled["초미세먼지"].sum())

'''
6. ‘미세먼지’ 컬럼의 결측값을 평균값으로 채운 뒤, 그 표준편차를 구하세요.
'''
print("표준편차:", df["미세먼지"].fillna(df["미세먼지"].mean()).std())