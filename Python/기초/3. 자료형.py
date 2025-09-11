# 자료형(Data Types)
'''
변수에 저장되는 데이터의 종류(동적 타이핑(자동으로 자료형 결정))
정수, 실수, 문자, 문자열, 불리언 ...

1. 정수(int): 소수점이 없는 숫자 → 2, 3, 12, 25, -10
2. 실수(float): 소수점이 있는 숫자 → 1.1, 41.123, 3.1415
3. 문자(char): 한 글자 → 'a', 'B', '가' (Python에서는 길이 1인 문자열)
4. 문자열(str): 여러 글자의 조합 → "hello", "안녕하세요"
5. 불린(bool): 참/거짓 값 → True, False
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

# 1. 정수형 (Integer)
student_count = 30              # 학생 수
temperature = -5                # 기온
year = 2024                    # 연도

# 2. 실수형 (Float)
pi = 3.14159                   # 원주율
average_score = 85.5           # 평균 점수
body_temperature = 36.5        # 체온

# 3. 문자열 (String)
greeting_message = "안녕하세요!"  # 인사말
programming_language = "Python"  # 프로그래밍 언어명

# 4. 불린 (Boolean)
is_student = True              # 학생인가? (참)
is_adult = False              # 성인인가? (거짓)

# ========================================
# 불린(Boolean) 자료형 상세
# ========================================

# 불린 변수명은 is_, has_, can_ 등으로 시작하는 것이 관례
is_raining = True              # 비가 오고 있나요?
has_license = False           # 면허증이 있나요?
can_drive = True             # 운전할 수 있나요?

print(f'비가 오나요? {is_raining}, 타입: {type(is_raining)}')
print(f'면허증이 있나요? {has_license}, 타입: {type(has_license)}')

# ========================================
# 문자열에서 따옴표 사용하기
# ========================================

# 문자열 안에 따옴표를 포함시키는 방법들:

# 방법 1: 큰따옴표 안에 작은따옴표 사용
message1 = '"파이썬"은 가장 널리 사용되는 프로그래밍 언어 입니다.'
print(message1)

# 방법 2: 작은따옴표 안에 큰따옴표 사용
message2 = "'파이썬'은 가장 널리 사용되는 프로그래밍 언어 입니다."
print(message2)

# 방법 3: 이스케이프 문자(\) 사용
message3 = "\"파이썬\"은 최고의 언어입니다."
message4 = '\'파이썬\'은 최고의 언어입니다.'
print(message3)
print(message4)

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

print(f"student_count의 타입: {type(student_count)}")       # <class 'int'>
print(f"pi의 타입: {type(pi)}")                           # <class 'float'>
print(f"greeting_message의 타입: {type(greeting_message)}")  # <class 'str'>
print(f"is_student의 타입: {type(is_student)}")           # <class 'bool'>

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


# ========================================
# 자료형 변환 (Type Conversion)
# ========================================

"""
때로는 한 자료형을 다른 자료형으로 변환해야 할 때가 있습니다.
int(), float(), str() 함수를 사용하여 변환할 수 있습니다.
"""

# 문자열을 숫자로 변환
string_number = "123"           # 문자열 "123"
converted_int = int(string_number)     # 정수 123으로 변환
converted_float = float(string_number)  # 실수 123.0으로 변환

print(f"원본: {string_number} (타입: {type(string_number)})")
print(f"정수 변환: {converted_int} (타입: {type(converted_int)})")
print(f"실수 변환: {converted_float} (타입: {type(converted_float)})")

# 숫자를 문자열로 변환
number = 456
converted_string = str(number)   # "456"으로 변환
print(f"원본: {number} (타입: {type(number)})")
print(f"문자열 변환: {converted_string} (타입: {type(converted_string)})")

# 주의: 변환할 수 없는 경우 에러 발생
# a = "1a"  # 문자가 섞여 있어서 숫자로 변환 불가능
# a1 = int(a)  # ValueError 발생!

###################################################################
# 문자열 포매팅 : f-string
'''
문자열 내에 중괄호 {} 사용
변수나 표현식의 값을 직접 삽입할 수 있는 문자열 포매팅 방식
'''

name = "Codingon"
age = 5
print(f'{name} is {age} years old.')      # Codingon is 5 years old.

"""
f-string (f-문자열)은 Python 3.6부터 도입된 강력한 문자열 포매팅 방법입니다.
문자열 앞에 f를 붙이고, 중괄호 {} 안에 변수나 표현식을 넣어 사용합니다.
"""

student_age = 20
student_grade = 85.7

# f-string 사용법
print(f'학생의 나이는 {student_age}세이고, 성적은 {student_grade}점입니다.')

# 중괄호 안에서 계산도 가능
print(f'내년 나이: {student_age + 1}세')
print(f'성적 반올림: {round(student_grade)}점')


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
