# ===========================
# for문 - 정해진 횟수만큼 반복
# ===========================

# print('안녕하세요')  # 단순 출력

# range(5) → 0부터 4까지 총 5번 반복
for i in range(5):
    print('안녕하세요')  # 5번 반복해서 출력


# ===========================
# range 함수의 기본 구조
# ===========================

# range(끝) → 0부터 끝-1까지
range(5)  # 0, 1, 2, 3, 4

# range(시작, 끝) → 시작부터 끝-1까지
range(2, 6)  # 2, 3, 4, 5

# range(시작, 끝, 간격) → 간격만큼 증가하면서 반복
range(2, 6, 2)  # 2, 4


print('==========')
print()

# ===========================
# for문 예시 1
# ===========================
for i in range(5):  # i = 0, 1, 2, 3, 4
    print(f'i의 값 {i}')  # i 값을 출력
print('==========')
print()

# ===========================
# for문 예시 2
# ===========================
for i in range(2, 6):  # i = 2, 3, 4, 5
    print(f'i의 값 {i}')
print('==========')
print()

# ===========================
# for문 예시 3
# ===========================
for i in range(2, 6, 2):  # i = 2, 4 (2씩 증가)
    print(f'i의 값 {i}')
print('==========')
print()


# ===========================
# 구구단 만들기 (4단만 출력)
# ===========================

num = 4
print('4단')
for i in range(1, 10):  # 1부터 9까지 반복
    print(f'{num} * {i} = {num * i}')  # 곱셈 결과 출력
print('==========')
print()


# ===========================
# 구구단 전체 (1단 ~ 9단)
# ===========================
for num in range(1, 10):  # 1단부터 9단까지 반복
    print(f"=== {num} 단 === ")

    for i in range(1, 10):  # 각 단에서 1~9까지 곱하기
        print(f'{num} * {i} = {num * i}')
    print()  # 단 사이에 줄바꿈


# ===========================
# 리스트와 for문
# ===========================

# 과일 리스트 선언
fruits = ["사과", "바나나", "오렌지", "포도"]

# 리스트의 요소를 하나씩 꺼내어 출력
for fruit in fruits:
    print(f"과일 : {fruit}")


# 점수 리스트 선언
scores = [65, 27, 87, 86, 65, 27, 87,
          86, 65, 27, 87, 86, 65, 27,
          87, 86]

# 총점과 개수를 저장할 변수 초기화
total = 0
count = 0

# 점수를 하나씩 꺼내면서 총점과 개수 누적
for score in scores:
    total += score
    count += 1
    print(f"점수 : {score}")

# 최종 결과 출력
print("총점: ", total)
print("평균: ", total / count)
print()


# ===========================
# 문자열 순회 (문자 하나씩 출력)
# ===========================

print("=========")
word = "Python"

for char in word:  # 문자열도 리스트처럼 반복 가능
    print(char, end=' ')  # 줄바꿈 없이 출력 (공백으로 구분)
print()


# ===========================
# 중첩 for문 - 반복 속의 반복
# ===========================

# 별 패턴 1 : 직각삼각형
# i가 1일 때 → 별 1개
# i가 2일 때 → 별 2개
# ...
# i가 5일 때 → 별 5개
for i in range(1, 6):      # i = 1, 2, 3, 4, 5
    for j in range(i):     # j는 i번 반복
        print('*', end='')  # 별 출력 (줄바꿈 없이)
    print()                # 줄바꿈


# 별 패턴 2 : 정사각형
# 5행 5열의 별 출력
# *****
# *****
# *****
# *****
# *****
for i in range(5):          # 5번 반복 (행)
    for j in range(5):      # 5번 반복 (열)
        print('*', end='')  # 별 출력
    print()                 # 줄바꿈


# 반복문(Iteration)

'''
동일한 작업(코드 블록)을 여러 번 실행하는 구조적 프로그래밍 기법
    - python은 for 또는 while문을 사용하여 반복문 구현함

* 반복문 사용의 목적
    - 동일한 작업의 반복 실행
    - 가독성과 유지보수성 향상
    - 자동화와 대량 처리
'''

# 100번 반복
for i in range(100):
    print("Hello")

######################################################################################################
# for 문
'''
시퀀스/이터러블 객체으 항목들을 하나씩 꺼내서 실행 블록에 전달하는 반복문

* 기본 문법
    for <변수> in <이터러블> :
        반복 실행할 코드 블록

    - 변수 : 각 반복마다 이터러블 객체의 항목을 하나씩 대입받는 변수
    - 이터러블 : 순회 가능한 객체 (list, tuple, str, dict, set, range 등)
    - : 코드 블록의 시작을 알림
    - 들여쓰기를 통해 코드 블록 범위를 명확히 구분
'''

# 기본 사용 예제
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(f'I like {fruit}')

'''
1. fruits 리스트의 첫 번째 요소 'apple'이 fruit 변수에 할당됨
2. print() 문 실행
3. 다음 요소 'banana'가 fruit에 대입되어 동일한 코드 실행
4. 리스트가 끝날 때까지 반복
'''

# 문자열 반복
text = "Hello"
for ch in text:
    print(ch)   # H e l l o

# 리스트, 튜플 반복
coords = [(1, 2), (3, 4), (5, 6)]
for x, y in coords:
    print(f'x: {x}, y: {y}')

'- 튜플의 경우 구조 분해를 활용해 동시에 여러 값 unpack 가능'

# 딕셔너리 반복
# 1. key 순회
person = {"name": "Alice", "age": 30}
for key in person:
    print(key)  # person.keys() 순회 결과와 같음

# 2. value 순회
for value in person.values():
    print(f'Value: {value}')

# 3. key, value 순회
for key, value in person.items():
    print(f'{key} => {value}')

# set 반복
'''
- set은 중복이 없고 순서를 보장하지 않는 컬렉션이지만 반복은 가능함
- 단, 출력 순서는 예측 불가능
'''

unique_numbers = {3, 1, 4, 1, 5}
for num in unique_numbers:
    print(num)

######################################################################################################
# 실습 1 for문 기본 문법 문제
'''
1. 리스트의 값을 두 배로 변환하기
    - for문을 사용하여, 아래 리스트의 각 값의 두 배를 계산한 결과를 새로운 리스트에 저장한 뒤 출력
    - 주어진 리스트 : numbers = [3, 6, 1, 8, 4]
'''
numbers = [3, 6, 1, 8, 4]
dob_nums = []
for num in numbers:
    dob_nums.append(num * 2)
print(dob_nums)


'''
2. 문자열의 길이 구해서 새 리스트 만들기
    - 리스트 단어의 길이(len)을 구해서, 길이만 담긴 새로운 리스트 생성하여 출력
    - 주어진 리스트 : words = ["apple", "banana", "kiwi", "grape"]
'''

words = ["apple", "banana", "kiwi", "grape"]
lens = []

for word in words:
    lens.append(len(word))
print(lens)


'''
3. 좌표 튜플에서 x, y 좌표 나누기
    - 아래와 같은 (x, y) 형태의 좌표 튜플 리스트에서 for문 튜플 언패킹(구조 분해) 활용
    - 각 좌표의 x 값만을 x_values 리스트에 y 값만을 y_values 리스트에 저장하고 각각 출력
    - 주어진 리스트 : coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]
'''

coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]
x_values, y_values = [], []

for x, y in coordinates:
    x_values.append(x)
    y_values.append(y)
print(f'x_values = {x_values}', f'y_values = {y_values}', sep=", ",)


######################################################################################################
# for문과 range()
'''
지정된 범위의 정수 시퀀스를 생성하는 내장 함수
주로 for문과 함께 사용되어 반복 횟수를 제어함
    range(start, stop[, step])
    - start: 시작 정수
    - stop : stop -1 까지 생성
    - step : 정수 증가 간격(기본값 1)
'''

# 기본 예제
for i in range(5):
    print(i)    # 0 1 2 3 4

'- range(stop) : start 생략 시 0부터 stop -1 까지 정수 생성'

for i in range(1, 6):
    print(i)    # 1 2 3 4 5

'- range(start, stop) : start부터 stop -1 까지 정수 생성'

for i in range(0, 10, 2):
    print(i)    # 2 4 6 8

'- range(start, stop, step) : start부터 step씩 증가하여 stop -1 까지 정수 생성'

for i in range(5, 0, -1):
    print(i)    # 5 4 3 2 1
'- step을 음수로 지정 시, 역순으로 시퀀스 생성'

######################################################################################################
# 실습 2 구구단 만들기
'''
4단 생성하기
'''
print("[구구단 - 4단]")
for i in range(1, 10):
    print(f'4 x {i} = {4 * i}')


'''
전체 생성하기
'''
print("[구구단 만들기]")
for i in range(1, 10):
    print('##########')
    print(f'## {i} 단 ##')
    print('##########')
    for x in range(1, 10):
        print(f'{i} x {x} = {i * x}')


######################################################################################################
# 실습 3 별표 만들기
'''
중첩 for문을 사용하여 아래와 같이 별표 만들기
*
**
***
****
*****
'''

for i in range(1, 6):
    print(f'{'*' * i}')

for i in range(1, 6):
    for j in range(1, 6):
        print("*", end='')
    print()

'''
정사각형만들기

*****
*****
*****
*****
*****
'''

for i in range(1, 6):
    print(f'{'*' * 5}')
