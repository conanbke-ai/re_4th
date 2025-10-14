import pandas as pd
import numpy as np

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

print(df.groupby(['team', 'position'])['score'].apply(lambda x: x.mean(skipna=False)))

'''
5. 아래 DataFrame에서 부서(dept)별로 성별(gender)별 인원 수와, 총 연봉(salary) 합계를 구하세요.
'''
df = pd.DataFrame({
'dept': ['HR', 'HR', 'IT', 'IT', 'Sales', 'Sales'],
'gender': ['M', 'F', 'F', 'M', 'F', 'F'],
'salary': [3500, 3200, 4000, 4200, 3000, 3100]
})

print(df.groupby(['dept', 'gender']).agg(
    count = ('salary', 'count'),
    total_salary = ('salary', 'sum')
))
