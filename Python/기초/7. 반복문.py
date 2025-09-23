# ===========================
# for문 - 정해진 횟수만큼 반복
# ===========================

# print('안녕하세요')  # 단순 출력

# range(5) → 0부터 4까지 총 5번 반복

import random
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

# 예시1)
# num = [num * 2 for num in numbers]

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

# 예시1)
# lens = [len(word) for word in words]

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

# 예시1)
# x_values = [x for x, y in coordinates]
# y_values = [y for x, y in coordinates]

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
# 중첩 for문
'''
하나의 for문 블록 안에 또 다른 for문이 들어있는 구조
- 2차원 이상의 데이터 구조나 반복 패턴 처리 시, 사용됨
'''

# 기본 문법
for i in outer_iterable:
    for j in inner_iterable:
        print(i, j)  # 내부 반복에서 실행할 코드

# 이중 for문 사용 예시
colors = ['red', 'blue']
fruits = ['apple', 'banana']

for color in colors:
    for fruit in fruits:
        print(f'{color} {fruit}')

# red apple
# red banana
# blue apple
# blue banana

'- 바깥 루프 1번 당 안쪽 루프는 전체 반복'
'- 총 반복 횟수 : len(colors) * len(fruits) = 2 * 2 = 4'

######################################################################################################
# 실습 2 for문과 range()

'''
1. 입력받은 수의 합 구하기
    for문과 range()를 사용하여 1부터 사용자가 입력한 수까지의 합 구하기
'''
# 정수 입력값 받기
n = int(input("정수를 입력하여 주십시오. : "))
# range를 이용한 반복문
for num in range(1, n+1):
    num += num
# 결과값 출력
print(num)

'''
2. 4단 생성하기
'''
print("[구구단 - 4단]")
# 1~9까지 곱셈
for i in range(1, 10):
    # 결과값 출력
    print(f'4 x {i} = {4 * i}')

'''
3. 구구단 전체 생성하기
'''
print("[구구단 만들기]")
# 1~9 단 반복
for i in range(1, 10):
    print('##########')
    print(f'## {i} 단 ##')
    print('##########')
    # 1~9 까지 곱셈
    for j in range(1, 10):
        # 결과값 출력
        print(f'{i} x {j} = {i * j}')

'''
4. 3의 배수의 합 구하기
    for문과 range()룰 사용하여 1부터 100까지의 수 중 3의 배수만 골라 합 출력
'''
# 변수 초기화
sum = 0
# 1~100 까지 반복
for x in range(1, 101):
    # 3의 배수인 경우
    if x % 3 == 0:
        # 합산
        sum += x
# 결과값 출력
print(f'3의 배수 합 = {sum}')

# 예시1)
# total = 0
# for i in range(3, 101, 3):
#     total += i

'''
5. 짝수이면서 5의 배수인 수 출력하기
    사용자로부터 숫자 n을 입력 받아
    1부터 n까지의 수 중 짝수이면서 5의 배수인 수 출력
'''
# 사용자 정수 입력
n = int(input("정수 값을 입력해주세요. : "))
# 1부터 n까지 반복
for x in range(1, n+1):
    # 2와 5의 배수인 경우
    if x % 2 == 0 and x % 5 == 0:
        # 결과값 출력
        print(x)

# 예시1)
# for i in range(1, n+1):
#       # 2의 배수인 경우 0 이므로 False → not False = True
#       # 5의 배수인 경우 0 이므로 False → not False = True
#     if (not i % 2) and (not i % 5):
#         print(i)

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

'''
왼쪽/가운데/오른쪽 정렬로 구현해보기
'''

count = int(input("몇 줄? \n : "))

print("########################################")
print("[ 왼쪽 정렬 ]")

# 왼쪽 정렬
for i in range(1, count + 1):
    print("*" * i)

print("########################################")

print("########################################")
print("[ 가운데 정렬 ]")

# 가운데 정렬
for i in range(1, count + 1):
    print(" " * (count - i + 1), "*" * (i * 2 - 1))
print("########################################")

print("########################################")
print("[ 오른쪽 정렬 ]")

# 오른쪽 정렬
for i in range(1, count + 1):
    print(" " * (count - i + 1), "*" * i)

print("########################################")

# 몇 줄?
#  : 5
# ########################################
# [ 왼쪽 정렬 ]
# *
# **
# ***
# ****
# *****
# ########################################
# ########################################
# [ 가운데 정렬 ]
#       *
#      ***
#     *****
#    *******
#   *********
# ########################################
# ########################################
# [ 오른쪽 정렬 ]
#       *
#      **
#     ***
#    ****
#   *****
# ########################################

# 에단 리더 답변

n = int(input('몇 줄 ? >'))

print('[왼쪽 정렬]')
for i in range(1, n + 1):
    for j in range(i):
        print('*', end='')
    print()


print('[가운데 정렬]')
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end='')
    # (i - 1) * 2 + 1 = 2i - 1
    for k in range(2 * i - 1):
        print('*', end='')
    print()

print('[오른쪽 정렬]')
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end='')
    for k in range(i):
        print('*', end='')
    print()

######################################################################################################
# 컴프리헨션(Comprehension)
'''
리스트 컴프리헨션(리스트 내포)
    for문을 사용한 반복문을 한 줄로 축약하여 새 리스트를 생성하는 문법

* 기본 문법
    [표현식 for 변수 in 반복대상 if 조건]

* 장단점
    - 장점
        간결성 : 반복문을 한 줄로 표현 가능
        가독성 : 조건과 결과를 동시에 확인 가능
        성능 : 일반 루프보다 약간 빠른 경우도 있음
    - 단점
        복잡한 로직 : 중첩이 깊거나 조건이 많아지면 오히려 가동성 저하
        디버깅 어려움 : 중간 값을 출력하거나 추적하기 어려움
'''

# 사용 예시
# for문과 비교
'일반적인 for문'
squares = []
for x in range(1, 6):
    squares.append(x**2)
print(squares)  # [1, 4, 9, 16, 25]

'컴프리헨션 방식'
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

'- 동일한 결과를 훨씬 짧고 읽기 쉬운 코드로 표현 가능'

# 예제 - 1~10 사이에서 짝수만 추출
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)    # [2, 4, 6, 8, 10]
'- 조건문은 끝에 위치하며, 해당 조건을 만족하는 값만 리스트에 포함됨'
'- 조건이 복잡해질 시, 가독성 저하 우려됨'

# 예제 - 2개의 리스트에서 모든 조합 만들기 (바깥 for문 / 안쪽 for문)
pairs = [(c, f) for c in colors for f in fruits]
print(pairs)
# [('red', 'apple'), ('red', 'banana'), ('blue', 'apple'), ('blue', 'banana')]

'''
딕셔너리/집합 컴프리헨션
'''

# 딕셔너리 컴프리헨션
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 셋 컴프리헨션
unique_lengths = {len(word) for word in ["apple", "banana", "cherry"]}
print(unique_lengths)   # {5, 6}

######################################################################################################
# 실습 4 리스트 컴프리헨션 연습 문제
'''
1. 제곱값 리스트 만들기
    - 1부터 10까지의 숫자에 대해, 각 수의 제곱값을 요소로 갖는 리스트를 리스트 컴프리헨션으로 생성하세요.
'''
compNum = [x**2 for x in range(1, 11)]
print(compNum)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

'''
2. 3의 배수만 리스트로 만들기
    - 1부터 50까지의 숫자에 대해, 3의 배수만 포함된 리스트를 리스트 컴프리헨션으로 생성하세요.
'''

tripNum = [x for x in range(1, 51) if x % 3 == 0]
print(tripNum)  # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]

'''
3. 문자열 리스트에서 길이가 5 이상인 단어만 뽑기
    - 아래의 리스트에서 글자 수가 5 이상인 단어들만 리스트 컴프리헨션으로 생성하세요.
     fruits = ["apple", "fig", "banana", "plum", "cherry", "pear", "orange"]
'''

fruits = ["apple", "fig", "banana", "plum", "cherry", "pear", "orange"]

fiveWord = [x for x in fruits if len(x) >= 5]
print(fiveWord)  # ['apple', 'banana', 'cherry', 'orange']

######################################################################################################
# 루프 제어문(break, continue, pass)
'''
1. break : 반복 즉시 중단
        반복문 실행 중 break를 만나면 반복문을 즉시 종료함
'''

for i in range(10):
    # i 가 5인 경우
    if i == 5:
        # 반복문 즉시 탈출
        break
    print(i)

# 0
# 1
# 2
# 3
# 4

# 사용 예제 - 특정 조건에서 검색 중단
numbers = [1, 3, 5, 7, 9, 11, 13]
target = 7

for num in numbers:
    print(f'검색중... {num}')
    if num == target:
        print(f'{target}을 찾았어요!')
        break  # 찾았으니 더 이상 검색할 필요 없음

'''
2. continue : 현재 반복만 건너뛰고 다음 반복 수행
        반복문 실행 중 continue를 만나면 다음 반복으로 넘어감
'''

for i in range(5):
    # i 가 2인 경우
    if i == 2:
        # 다음 반복으로 넘김
        continue
    print(i)

# 0
# 1
# 3
# 4

# 사용 예제 - 특정 값 제외하고 처리
# 음수 제외하고 출력하기
scores = [85, -1, 92, 78, -999, 88]  # -1과 -999는 오류값

for score in scores:
    if score < 0:  # 음수는 오류값이니까
        print(f'{score}는 잘못된 점수, 건너뜀')
        continue  # 이번 점수는 무시하고 다음 점수로
    print(f'  유효한 점수: {score}점')

'''
3. pass : 아무 동작 하지 않고 자리만 차지
'''

for i in range(3):
    pass    # 추후 구현 예정인 자리 → 프로그램에 영향 X

for i in range(10):
    pass      # 그냥 통과~ (아무 일도 안 일어남)
    print(i)  # 0~9 모두 정상 출력
print()

# 사용 예제 - 나중에 구현할 코드 자리 채우기


def process_data(data):
    if data > 100:
        pass  # TODO: 나중에 여기 특별 처리 코드 넣을 예정
    else:
        print(f'데이터 처리: {data}')


process_data(50)   # 정상 처리
process_data(150)  # pass라서 아무 일 안 일어남

'''
4. for - else 구문 : 반복이 정상적으로 모두 수행된 경우 else 블록 실행
'''

# 정상 종료
for i in range(5):
    print(i)
else:
    print("루프 정상 종료")  # 실행됨


# break 종료 - else 구문 실행 X
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("루프 정상 종료")  # 실행되지 않음

# 사용 예제 - 검색 실패 감지

items = ['사과', '바나나', '딸기']
search_item = '수박'

for item in items:
    if item == search_item:
        print(f'{search_item}을 찾았습니다!')
        break
else:
    # break가 안 됐다 = 못 찾았다
    print(f'{search_item}을 찾을 수 없습니다.')


# ==========================================
#      💡 break vs continue vs pass 비교
# ==========================================
print('='*50)
print('💡 break vs continue vs pass 한눈에 비교')
print('='*50)

# break 예시
print('🛑 break: 1~5 중에 3에서 멈추기')
for i in range(1, 6):
    if i == 3:
        print('  → break! 여기서 끝!')
        break
    print(f'  숫자: {i}')
print()

# continue 예시
print('⏭️ continue: 1~5 중에 3만 건너뛰기')
for i in range(1, 6):
    if i == 3:
        print('  → continue! 3은 건너뜀')
        continue
    print(f'  숫자: {i}')
print()

# pass 예시
print('🤷 pass: 1~5 모두 출력 (pass는 아무 영향 없음)')
for i in range(1, 6):
    if i == 3:
        pass  # 아무것도 안 함
    print(f'  숫자: {i}')
print()

# 사용 예제 - 활용
# 실전 1: 비밀번호 검증 (break 활용)
print('\n📝 비밀번호 검증')
passwords = ['1234', 'abcd', 'secret', 'python']
correct_pass = 'secret'

for idx, pwd in enumerate(passwords, 1):
    print(f'시도 {idx}: {pwd}', end=' ')
    if pwd == correct_pass:
        print('✅ 맞았습니다!')
        break
    print('❌ 틀렸습니다')

# 실전 2: 유효한 데이터만 처리 (continue 활용)
print('\n📊 성적 평균 구하기 (잘못된 데이터 제외)')
scores = [85, -1, 92, 200, 78, -999, 88]  # -1, 200, -999는 오류
valid_scores = []

for score in scores:
    if score < 0 or score > 100:  # 잘못된 점수
        print(f'  ⚠️ {score}는 무시 (0~100 범위 벗어남)')
        continue
    valid_scores.append(score)
    print(f'  ✅ {score}점 추가')

if valid_scores:
    average = sum(valid_scores) / len(valid_scores)
    print(f'평균: {average:.1f}점')

'''
🛑 break
  - 반복문을 완전히 종료
  - "찾았으니 그만 찾자"
  - 사용처: 검색, 조건 만족시 종료

⏭️ continue  
  - 현재 반복만 건너뛰고 다음 반복 진행
  - "이건 패스하고 다음거"
  - 사용처: 특정 조건 제외, 필터링

🤷 pass
  - 아무것도 하지 않음 (빈 자리 채우기용)
  - "일단 비워두고 나중에"
  - 사용처: 미완성 코드, 예외 무시

🎯 for-else
  - break 없이 정상 종료시 else 블록 실행
  - "끝까지 다 돌았는데 못 찾았네"
  - 사용처: 검색 실패 감지
'''

######################################################################################################
# While 문

'''
조건이 True인 동안 루프 안의 코드를 반복 실행하는 반복문
조건식이 False가 되면 반복을 멈추고 루프를 빠져나옴

* 기본 문법
    while 조건식 : 
        실행할 코드1
        실행할 코드2
        ...

    - 조건식 : boolean 표현식, 참(True)일 동안 반복 실행됨
    - : (콜론) : 블록 시작나타냄
    - 들여쓰기 : 블록 범위 정의

* 실행 흐름
    1. 조건식 평가
        조건식 True : 블록 내부 코드 실행
        조건식 False : 반복 종료
    2. 블록 실행 후 다시 조건 평가
        조건이 여전히 True일 시 다시 반복
    3. 조건이 False 될 때까지 반복

* 필요
    - 반복 횟수가 정해지지 않았을 때
        ex) 사용자가 'exit'를 입력할 때까지 계속 입력 받기
    - 조건 기반 루프가 필요할 때
        ex) 파일이 존재하는 동안 반복 처리
    - 무한 루프 + 조건 분기 구조에 유용
        ex) 게임 루프, 서버 대기 루프 등

*                   while문                vs              for문

반복 조건 : 조건이 True일 동안 반복            시퀀스나 반복 가능한 객체의 각 항목 순회
반복 횟수 : 명확하지 않음(조건에 따라 달라짐)   명확함(range, 리스트 등)
주요 용도 : 조건 기반 반복, 무한 루프           반복 대상이 명확한 경우(반복 횟수 등)
예시      : 사용자 입력, 센서값 모니터링        리스트 요소 출력, 숫자 카운트
'''

# 사용 예시

# 변수 초기화
i = 1

# i가 5 이하일 동안 반복
while i <= 5:
    print(i)    # i 출력
    i += 1      # i 에 1을 더하여 갱신


'''
While문 사용 시 주의점
    - 조건식의 갱신 반드시 필요
    - 조건을 갱신하지 않을 시, 무한 루프에 빠질 수 있음
'''

# 무한 루프 (조건 갱신 누락)
i = 1
while i <= 5:
    print(i)

# 사용 예제 - 올바른 나이 입력받기
# 사람 나이는 0~150살 사이여야 해
age = -1  # 일부러 잘못된 값 넣기 (반복문 들어가려고)

while age < 0 or age > 150:  # 나이가 이상하면 다시 물어봐
    age = int(input('나이를 입력하세요(0-150): '))

    if age < 0 or age > 150:  # 또 이상한 값 입력했네?
        print('😅 그런 나이는 없어요! 다시 입력해주세요!')

print(f'✅ 입력된 나이: {age}세')

# 사용 예제 - 비밀번호 3번 입력기회
correct_password = 'python123'  # 정답 비밀번호
attempt = 0                      # 지금까지 몇 번 시도했나
max_attempts = 3                 # 총 3번만 기회 줄거야

while attempt < max_attempts:  # 아직 3번 안됐으면 계속
    password = input('🔐 비밀번호를 입력하세요: ')
    attempt = attempt + 1  # 시도 횟수 1 증가

    if password == correct_password:  # 맞췄다!
        print('✅ 로그인 성공!')
        break  # 여기서 반복문 탈출! (더 이상 물어보지 마)
    else:  # 틀렸네...
        remaining = max_attempts - attempt  # 몇 번 남았나 계산
        if remaining > 0:  # 아직 기회가 있으면
            print(f'❌ 틀렸습니다. {remaining}번 남았습니다.')
        else:  # 기회 다 썼으면
            print(f'🚫 로그인 실패! 계정이 잠겼습니다.')

######################################################################################################
# 실습 1 While문 연습문제
'''
1. 비밀 코드 맞추기
    비밀 모임에 입장 시, 비밀 코드 입력해야 함. 아래의 요구사항에 만족하는 코드를 작성하세요.
    - 변수 secret_code에는 "codingonre4"라는 문자열이 저장되어 있음.
    - 사용자에게 "비밀 코드를 입력하세요."라고 안내 문구 출력함.
    - 사용자가 입력한 코드가 secret_code 와 다를 경우, 계속해서 다시 입력받음.
    - 코드가 맞으면, "입장이 허용되었습니다!" 를 출력하고 프로그램 종료.
'''
# 비밀 코드 선언
secret_code = "codingonre4"

# 비밀 코드 사용자 입력
code = input("비밀 코드를 입력하세요. \n : ")
# 반복
# 사용자 입력 코드와 비밀 코드 불일치 시,
while secret_code != code:
    code = input("비밀 코드를 입력하세요. \n : ")
# 사용자 입력 코드와 비밀 코드 일치 시,
print("입장이 허용되었습니다!")

# 비밀 코드를 입력하세요.
#  : ㅇㄴㅁㄹ
# 비밀 코드를 입력하세요.
#  : ㅇㅇ
# 비밀 코드를 입력하세요.
#  : codingonre4
# 입장이 허용되었습니다.


'''
2. 업다운 게임
    컴퓨터가 1부터 100 사이의 무작위 정수 하나를 미리 정해 놓았습니다. 사용자는 이 수를 맞출 때까지 입력해야 합니다.
    - 입력한 숫자가 정답보다 크면, "입력한 숫자보다는 작아요." 출력함.
    - 입력한 숫자가 정답보다 작으면, "입력한 숫자보다는 커요." 출력함.
    - 숫자를 맞히면, "{입력 횟수}번 만에 정답을 맞췄습니다." 출력함.
'''
# random 메소드 import

# 변수 초기화
i = 0

com = random.randrange(1, 100)
num = int(input("숫자를 맞춰주세요. \n : "))
# 반복
while com != num:
    # 변수 카운트
    i += 1
    if com > num:
        print("입력한 숫자보다는 커요.")
    else:
        print("입력한 숫자보다는 작아요.")
    num = int(input("숫자를 맞춰주세요. \n : "))

print(f'{i}번 만에 정답을 맞췄습니다.')

# 숫자를 맞춰주세요.
#  : 30
# 입력한 숫자보다는 커요.
# 숫자를 맞춰주세요.
#  : 50
# 입력한 숫자보다는 커요.
# 숫자를 맞춰주세요.
#  : 70
# 입력한 숫자보다는 작아요.
# 숫자를 맞춰주세요.
#  : 60
# 입력한 숫자보다는 작아요.
# 숫자를 맞춰주세요.
#  : 56
# 입력한 숫자보다는 커요.
# 숫자를 맞춰주세요.
#  : 58
# 5번 만에 정답을 맞췄습니다.


######################################################################################################
# 무한 루프와 종료 제어
'''
무한 루프 만들기(while True:)
    조건이 항상 참(Ture)이므로 루프가 무한히 반복됨
    주로 반복을 외부 이벤트로 제어할 때 사용
    루프 내에 종료 조건(break 등)을 반드시 포함해야 함

* 기본 문법
    while True:
        실행할 코드
        ...
'''

# break 문으로 루프 탈출
# 사용 예제 - 1부터 증가하면서 10보다 크면 종료
i = 1
while True:
    print(i)
    if i > 10:
        break   # i가 10보다 크면 루프 종료
    i += 1

# 사용 예제 - 사용자 입력으로 종료(0 입력 시 종료)
while True:
    num = int(input("숫자를 입력하세요 (0 입력 시 종료):"))
    if num == 0:
        print("종료합니다.")
        break
    print(f'입력한 숫자: {num}')

# continue
# 사용 예제 - 1부터 10까지 중 홀수만 출력
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue    # 짝수는 건너뜀
    print(i)    # 홀수만 출력

# while -else 구문
'''
break 없이 정상 종료되었는 지 확인할 때 사용
'''
# 사용 예제
i = 10
while i < 15:  # i가 15보다 작으면 반복
    print(i)
    if i == 11:  # i가 11이 되면
        break    # 강제 종료! (else 실행 안됨)
    i = i + 1
else:  # break 없이 조건이 False가 되어 종료되면 실행
    print('정상적으로 끝났어요!')
    # 위 예제는 i=11에서 break 되므로 이 줄은 출력 안됨

# 사용 예제
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("while 루프가 정상적으로 종료되었습니다.")

'- while 루프가 정상적으로 종료되었을 때만 else 블록이 실행'
'- break로 루프가 종료되면 else는 실행되지 않음'

# 사용 예제 - 계산기
while True:  # 계속 계산할 수 있게 무한 반복
    num1 = float(input("첫 번째 숫자: "))

    if num1 == 0:  # 0 입력하면 계산기 끄기
        print("계산기를 종료합니다.")
        break

    num2 = float(input("두 번째 숫자: "))
    operator = input('연산자 (+, -, *, /): ')

    # 어떤 계산을 할지 정하기
    if operator == '+':  # 더하기
        result = num1 + num2
    elif operator == '-':  # 빼기
        result = num1 - num2
    elif operator == '*':  # 곱하기
        result = num1 * num2
    elif operator == '/':  # 나누기
        if num2 != 0:  # 0으로는 못 나눠!
            result = num1 / num2
        else:
            print('⚠️ 0으로 나눌 수 없어요!')
            continue  # 이번 계산은 건너뛰고 다시 처음부터
    else:  # +, -, *, / 가 아닌 다른 걸 입력했네?
        print('❌ 잘못된 연산자입니다.')
        continue  # 이번 계산은 건너뛰고 다시 처음부터

    print(f'📊 결과: {result}')

######################################################################################################
# 실습 2 While문 연습문제
'''
1. 비밀 코드 맞추기
    비밀 모임에 입장 시, 비밀 코드 입력해야 함. 아래의 요구사항에 만족하는 코드를 작성하세요.
    정답을 입력할 때까지 무한히 반복되며, 정확한 코드를 입력하면 루프를 탈출합니다.
    - 변수 secret_code에는 "codingonre4"라는 문자열이 저장되어 있음.
    - 사용자에게 "비밀 코드를 입력하세요."라고 안내 문구 출력함.
    - 사용자가 입력한 코드가 secret_code 와 다를 경우, "비밀 코드가 틀렸습니다. 다시 시도하세요." 출력 후, 계속해서 루프 진행함.
    - 코드가 맞으면, "입장이 허용되었습니다!" 를 출력하고 break로 프로그램 종료.
'''
# 비밀 코드 선언
secret_code = "codingonre4"

# 비밀 코드 사용자 입력
code = input("비밀 코드를 입력하세요. \n : ")
# 반복
# 사용자 입력 코드와 비밀 코드 불일치 시,
while True:
    if secret_code == code:
        break
    else:
        print("비밀 코드가 틀렸습니다. 다시 시도하세요. \n")
        code = input("비밀 코드를 입력하세요. \n : ")
print("입장이 허용되었습니다!")

# 비밀 코드를 입력하세요.
#  : dkdse
# 비밀 코드가 틀렸습니다. 다시 시도하세요.

# 비밀 코드를 입력하세요.
#  : halo
# 비밀 코드가 틀렸습니다. 다시 시도하세요.

# 비밀 코드를 입력하세요.
#  : codingonre4
# 입장이 허용되었습니다!

'''
2. 유효한 나이만 평균 내기
    사용자에게 총 5명의 나이를 입력받아, 유효한 나이들만 평균을 내어 출력하세요.
    - 변수 times는 유효한 입력의 개수를 셈.
    - 변수 sum_age 는 나이의 합계를 저장함.
    - 나이는 정수로 입력받음.
    - 나이가 0이하이거나 120보다 크면 무시하고, 반복을 건너뜀
    - 5개의 유효한 나이를 입력받으면 루프를 종료하고, 총합과 평균을 출력함.
'''

# 5명의 사용자 입력 나이 리스트
ageList = input("5명의 나이를 입력해주십시오.(구분자 : \" \") \n : ").split()

# 변수 초기화
times, sum_age = 0, 0

# 무한 반복문
while True:
    # ageList 길이만큼 반복
    for x in range(0, len(ageList)):
        # 0 이하이거나 120보다 큰 나이 무시
        if int(ageList[x]) <= 0 or int(ageList[x]) > 120:
            continue
        else:
            # 유효한 나이 개수 카운트
            times += 1
            # 유효한 나이 합계 계산
            sum_age += int(ageList[x])
    # while 반복 멈춤
    break

print(f'times = {times}, sum_age = {sum_age}, avg = {sum_age / times}')

# 5명의 나이를 입력해주십시오.(구분자 : " ")
# : 121 50 -5 10 20
# times = 3, sum_age = 80, avg = 26

######################################################################################################
# 중첩 While문

'''
While문 안에 또 다른 While문을 포함하는 구조
반복문 안에서 또 다른 반복이 필요할 때 사용

* 기본 문법
    while 바깥 조건식 :
        # 바깥 루프의 실행 코드
        while 안쪽 조건식 : 
            # 안쪽 루프의 실행 코드
'''

# 사용 예제 - 구구단 만들기

dan = 2

# 바깥 루프 : 단(dan)을 2 ~ 9까지 증가시키며 반복
while dan <= 9:
    su = 1
    # 안쪽 루프 : 각 단마다 1 ~ 9 곱셈 수행
    while su <= 9:
        print(f'{dan} x {su} = {dan * su}')
        # 안쪽 루프 조건 갱신
        su += 1
    # 단위 구분을 위한 빈 줄 출력
    print()
    # 바깥 루프 조건 갱신
    dan += 1

# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18

# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27

# 4 x 1 = 4
# 4 x 2 = 8
# 4 x 3 = 12
# 4 x 4 = 16
# 4 x 5 = 20
# 4 x 6 = 24
# 4 x 7 = 28
# 4 x 8 = 32
# 4 x 9 = 36

# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45

# 6 x 1 = 6
# 6 x 2 = 12
# 6 x 3 = 18
# 6 x 4 = 24
# 6 x 5 = 30
# 6 x 6 = 36
# 6 x 7 = 42
# 6 x 8 = 48
# 6 x 9 = 54

# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63

# 8 x 1 = 8
# 8 x 2 = 16
# 8 x 3 = 24
# 8 x 4 = 32
# 8 x 5 = 40
# 8 x 6 = 48
# 8 x 7 = 56
# 8 x 8 = 64
# 8 x 9 = 72

# 9 x 1 = 9
# 9 x 2 = 18
# 9 x 3 = 27
# 9 x 4 = 36
# 9 x 5 = 45
# 9 x 6 = 54
# 9 x 7 = 63
# 9 x 8 = 72
# 9 x 9 = 81

######################################################################################################
# 실습 3 중첩 While문 연습문제
'''
로그인 시스템 구현

    로그인 시스템을 만들고 있습니다.
    순서대로 ID와 비밀번호를 입력받고, ID와 비밀번호 모두 일치 시, 로그인 성공 메시지를 출력하세요.

    - 임의의 ID와 비밀번호를 세팅합니다.
    - 잘못된 ID일 경우 "ID가 존재하지 않습니다." 를 출력하고, 다시 ID를 입력받습니다.
    - ID가 맞으면 비밀번호를 입력받고, 비밀번호가 틀리면 "비밀번호가 틀렸습니다." 를 출력하고 다시 입력 받습니다.
    - 둘 다 맞으면, "로그인 성공!" 을 출력하고 프로그램을 종료합니다.
'''

id, password = "codingon", "1234"

inputStr = input("ID와 비밀번호를 입력해주세요. (구분자 : \" \") \n : ").split()
inputId = inputStr[0]
inputPassword = inputStr[1]

while True:
    if inputId != id:
        print("ID가 존재하지 않습니다.")
        inputId = input("ID를 다시 입력해주세요. \n : ")
        if inputPassword != password:
            print("비밀번호가 틀렸습니다.")
            inputPassword = input("비밀번호를 다시 입력해주세요. \n : ")
    print("로그인 성공!")
    break

# ID와 비밀번호를 입력해주세요. (구분자 : " ")
#  : baekee 1212
# ID가 존재하지 않습니다.
# ID를 다시 입력해주세요.
#  : cordingon
# 비밀번호가 틀렸습니다.
# 비밀번호를 다시 입력해주세요.
#  : 1234
# 로그인 성공!
