# 자료형
'''
변수에 저장되는 데이터의 종류(동적 타이핑(자동으로 자료형 결정))
정수, 실수, 문자, 문자열, 불리언 ...
- 정수 : 2, 3, 12, 25 ...
- 실수 : 1.1, 41.123, 3.1415
- 문자 : 'a', 'B'
- 문자열: "aaa", "hello"
'''

'''
- 숫자형 : int - 정수(크기 제한 X, 값이 커지면 메모리 자동 할당 / C++, JAVA 등에서는 정수형 저장 범위 고정적), float - 실수(부동소수점 숫자), complex - 복소수
- 문자형 : str
- 불리언형 : True - 0 이외 모든 값, False - 1
- 시퀀스형 : list, tuple, range
- 집합형 : set, frozenset
- 매핑형 : dict
- None : NoneType - 아무 값도 없음

'''

print('"파이썬"은 가장 널리 사용되는 프로그래밍 언어입니다.')     # "파이썬"은 가장 널리 사용되는 프로그래밍 언어입니다.
print("'파이썬'은 가장 널리 사용되는 프로그래밍 언어입니다.")     # '파이썬'은 가장 널리 사용되는 프로그래밍 언어입니다.

true = True
false = False

######################################################################
# 자료형 확인 함수 : type()
a = 'a'
b = 1
c = 3.14

print(type(a))    # <class 'str'>
print(type(b))    # <class 'int'>
print(type(c))    # <class 'float'>
print(type(true))  # <class 'bool'>
print(type(false))      # <class 'bool'>

#####################################################################
# 형 변환(Type case)
'''
하나의 자료형을 다른 자료형으로 변경

int(x) : 정수형으로 변환
flaot(x) : 실수형으로 변환
str(x) : 문자형으로 변환
'''

print("c = ", int(c), type(int(c)))  # c =  3 <class 'int'>
print("b = ", float(b), type(float(b)))   # b =  1.0 <class 'float'>
print("b = ", str(b), type(str(b)))  # b =  1 <class 'str'>

###################################################################
# 문자열 포매팅 : f-string
'''
문자열 내에 중괄호 {} 사용
변수나 표현식의 값을 직접 삽입할 수 있는 문자열 포매팅 방식
'''

name = "Codingon"
age = 5
print(f'{name} is {age} years old.')      # Codingon is 5 years old.

#####################################################################
# 실습1
'''
영화정보 출력하기
f-string을 사용하여 1줄 작성
변수 : 영화이름(title), 감동(director), 개봉년도(year), 장르(genre)
'''
title = 'Inception'
director = 'Christopher Nolan'
year = 2010
Genre = 'Sci-Fi'

print(f'Title: {title} Director: {director} Year: {year} Genre: {Genre}')
# Title: Inception Director: Christopher Nolan Year: 2010 Genre: Sci-Fi

#####################################################################
# 실습2
'''
f-string을 사용하여 자기소개하기
print 한번만 사용하여 여러줄의 문장이 나오게 하기
변수 : 이름, 나이, MBTI
'''
name = '배경은'
age = 32
mbti = 'ENTJ'

print(f'안녕하세요. \n제 이름은 {name}이고, \n{age}살입니다. \n제 MBTI는 {mbti}에요.')
# 안녕하세요.
# 제 이름은 배경은이고,
# 32살입니다.
# 제 MBTI는 ENTJ에요.

print('안녕하세요.', f'제 이름은 {name}이고,', f'{age}살입니다.',
      f'제 MBTI는 {mbti}에요.', sep='\n')
# 안녕하세요.
# 제 이름은 배경은이고,
# 32살입니다.
# 제 MBTI는 ENTJ에요.

print(f"""안녕하세요.
제 이름은 {name}이고,
{age}살입니다.
제 MBTI는 {mbti}에요.""")
# 안녕하세요.
# 제 이름은 배경은이고,
# 32살입니다.
# 제 MBTI는 ENTJ에요.
