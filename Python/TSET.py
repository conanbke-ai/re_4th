import pandas as pd

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

print("[4-1] 리스트로 Series 생성")
temp_list = [15.5, 17.2, 18.9, 19.1, 20.1]
temp = pd.Series(temp_list, name='4월_기온')
print(temp)

date = pd.date_range('2025-04-01', periods=5)  # 5일간의 날짜 생성
print("생성된 날짜 인덱스:")
print(date)

temp_date = pd.Series(temp_list, index=date, name='4월_기온')
print("날짜 인덱스를 가진 기온 데이터:")
print(temp_date)