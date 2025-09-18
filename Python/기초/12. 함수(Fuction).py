# 함수(Function)

'''
특정 작업을 수행하는 코드 블록(묶음)
한 번 정의하면 필요할 때마다 호출하여 재사용할 수 있음

* 함수의 필요성
    - 코드 재사용(재활용성)
        동일한 작업을 반복할 때 매번 코드를 다시 작성할 필요없음
        한 번 정의한 함수는 여러 번 호출 가능
    - 코드의 가독성 향상
        기능 단위로 묶어서 코드가 논리적으로 명확해짐
        다른 사람이 읽고 이해하기 쉬워짐
    - 유지보수 용이성
        수정이 필요한 부분이 생기면 함수 내부만 고치면 됨
        중복 코드 수정의 부담 감소
    - 프로그램의 구조화(모듈화)
        큰 프로그램을 여러 개의 작은 작업으로 나누어 체계적으로 관리
        각 함수는 하나의 "기능"만 담당하게 설계하는 것이 원칙(단일 책임 원칙 - SRP)
    - 협업과 확장성
        개발자끼리 작업 분담이 쉬움
        작은 단위의 함수가 쌓여 큰 기능을 설계(계층적 설계)
    - 추상화
        복잡한 로직을 단순한 인터페이스로 제공

* 내장함수와 사용자 정의 함수
    - 내장 함수 : 파이썬이 기본적으로 제공하는 함수
                별도의 정의없이 바로 사용 가능
                ex) print(), len(), type(), sum(), max(), sorted() 등
    - 사용자 정의 함수 : 사용자가 def 키워드를 사용하여 직접 만든 함수

* 기본 문법
    def 함수이름(매개변수1, 매개변수2, ...):

        실행할 코드

        return 반환값

    - def : 함수 정의 키워드(define)
    - 함수이름 : 함수를 식별하는 이름 - 파이썬은 주로 snake_case 사용
    - 매개변수(Parameters) : 함수가 받은 입력값(선택적 사용)
    - 콜론(:) : 코드 블록 시작을 알림
    - 들여쓰기 : 들여쓰기 한 코드 블록이 함수 본문이 됨
    - return : 결과값 반환(선택적 사용), 없으면 None 반환
                return을 만나는 즉시 함수 종료

* 함수 호출 문법
    # 함수에 매개변수가 없을 시
    함수이름()
    # 함수에 매개변수가 있을 시
    함수이름(인자값1, 인자값2, ...)

    - 괄호 : 함수에 전달할 값이 없더라도 실행 시 괄호 반드시 필요
    - 인자 : 함수 호출 시 전달하는 값
'''

# 사용 예제 - 함수 호출


def say_hello():
    print("안녕하세요!")


# 매개변수 없이 호출
say_hello()

# return 없는 경우
# greet 함수 생성


def greet(name):
    print(f'Hello, {name]}!')

# 매개변수 호출
# return이 없으므로 None 반환
greet("CodingOwl")

# return 있는 경우
# add 함수 생성
def add(a, b):
    return a + b
# return값 변수에 할당
result = add(3, 5)
print(result)   # 8

# 사용 예제 - 재사용, 단순화
print('첫 번째 섹션')
print('두 번째 섹션')

def print_section(title):
    print(f'{title} 섹션')

print_section("첫 번째")
print_section("두 번째")

# 사용 예제 - 사각형 넓이
def calculate_area(width, height):
    """
    직사각형의 넓이를 계산합니다.
    Parameters
        - width(float) : 직사각형의 너비
        - height(float) : 직사각형의 높이
    Return
        - (float) : 직사각형의 넓이
    """
    return width * height

print(calculate_area(10, 20))   # 200

# 문서화 (함수 내부의 주석을 출력) - Docstring
print(calculate_area.__doc__)

# 직사각형의 넓이를 계산합니다.
# Parameters
#     - width(float) : 직사각형의 너비
#     - height(float) : 직사각형의 높이
# Return
#     - (float) : 직사각형의 넓이


######################################################################################################
# 실습 1 사칙연산 계산기 함수 만들기
'''
두 개의 숫자와 연산자를 인자로 받아 해당 연산 결과를 반환하는 함수를 작성하세요.

    * 요구사항
        - 함수 이름은 calculate로 합니다.
        - 매개변수는 a, b, operator 세 개입니다.
        - operator는 문자열이며, 다음 중 하나입니다. ("+", "-, "*", "/")
        - 나눗셈은 결과를 실수(float)로 반환합니다.
        - 올바르지 않은 연산자가 들어오면 "지원하지 않는 연산입니다."라는 문자열을 반환하세요.
'''

# 사칙연산 계산 함수 생성
def calculate(a, b, operator):
    # 변수 초기화
    result = ""

    # 더하기
    if operator == "+":
        result = a + b
    # 빼기
    elif operator == "-":
        result = a - b
    # 곱하기
    elif operator == "*":
        result = a * b
    # 나누기
    elif operator == "/":
        # 결과 값 실수로 변환
        result = float(a / b)
    # 기타
    else :
        result = "지원하지 않는 연산입니다."
    
    # 결과값 반환
    return result

print(calculate(1, 5, "+"))
print(calculate(1, 5, "-"))
print(calculate(1, 5, "*"))
print(calculate(1, 5, "/"))
print(calculate(1, 5, "**"))

######################################################################################################
# 매개변수와 인자

'''
- 매개변수(Parameter) : 함수를 정의할 때 사용자가 입력할 값을 받기 위해 설정하는 변수
- 인자(Argument) : 함수를 호출할 때 매개변수로 전달하는 실제 값
'''

# 위치 인자(Positional Arguments)
def add(a, b):
    return a + b
result = add(3, 5)  # a = 3, b = 5로 매칭

'- 인자의 순서대로 매개변수에 대응되는 방식'
'- 매개변수 개수와 인자 개수가 일치하지 않을 시, TypeError 발생'

# 키워드 인자(Keyword Arguments)
def introduce(name, age):
    print(f'{name}님은 {age}살입니다.')

introduce(age=30, name="홍길동")

'- 인자의 이름을 명시하여 전달하는 방식'
'- 순서와 무관하게 매개변수에 대응 가능'
'   인자의 순서를 헷갈릴 때 안전하게 사용'

# 기본값 인자(Default Arguments)
def greet(name, message="안녕하세요"):
    print(f'{name}님, {message}')

# 기본값 사용
greet("홍길동")
# 기본값 무시하고 새 인자 전달
greet("홍길동", "반갑습니다")

'- 함수 정의 시 매개변수에 기본값 지정'
'- 호출 시 인자를 생략하면 기본값 사용'
'- 기본값 매개변수는 반드시 뒤 쪽에 위치해야 함'
'   ex) def func(a=1, b): 오류'
'       def func(a, b=1): 가능'

# 위치 가변 인자 (*args)
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3, 4))  # 10

'- 여러 개의 위치 인자를 튜플 형태로 받음'
'- 함수 정의 시 *args로 표기'

# 키워드 가변 인자(**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}:{value}')

print_info(name="홍길동", age=30, city="서울")

'- 여러 개의 키워드 인자를 딕셔너리 형태로 받음'
'- 함수 정의 시 **kwargs로 표기'
'- 위치 인자 → 기본값 인자 → *args → **kwargs 순서로 정의해야 함'

def example(a, b=0, *args, **kwargs):
    pass

# 매개변수 전달 방식

'''
파이썬은 값 전달(Call by Value)가 아닌, 객체 참조에 의한 전달(Call by Object Reference) 방식
    - 변경 가능한 객체(mutable) : 함수 내 변경 → 외부에도 영향
    - 변경 불가능한 객체(immutable) : 함수 내 변경 → 외부 영향 없음
'''

def modify_list(my_list):
    my_list.append(100)

lst = [1, 2, 3]
modify_list(lst)
print(lst)  # [1, 2, 3, 100]    (mutable 영향 받음)

######################################################################################################
# 실습 2 가변인자 연습하기

'''
1. *args 사용 연습
    a. 숫자 여러 개의 평균 구하기
        숫자를 몇 개든 받을 수 잇는 average() 함수를 만들어보세요.
    b. 가장 긴 문자열 찾기(max 함수에 대해 찾아보고 풀기)
        여러 개의 문자열을 받아, 가장 긴 문자열을 반환하는 함수를 만들어보세요.
'''

# 평균값을 계산하는 함수
def average(*args):
    # 인자가 없는 경우 처리
    if not args:
        return None
    # 평균 값 반환
    return sum(args) / len(args)


# 인자가 없는 경우
print(average())
# 인자가 있는 경우
print(average(1, 2, 3))

# 가장 긴 문자열 찾는 함수
def logest_string(*args):
    return max(*args)

print(logest_string("apple", "banana", "cherry", "pinapple"))

'''
2. **kwargs 사용 연습
    c. 사용자 정보 출력 함수
        사용자의 이름, 나이, 이메일 등의 정보를 받아 출력하는 함수를 **kwargs로 구현하세요.
        정보가 몇 개가 들어오든 모두 출력해야 합니다.
    d. 할인 계산기
        상품 가격 목록을 **kwargs로 받아, 각각 10%씩 할인된 가격을 출력하는 함수를 작성하세요.
'''

# 사용자 정보 출력 함수
def info(**kwargs):
    for num, (key, value) in enumerate(kwargs.items(), start=1):
        print(f'{num}. {key} : {value}', end=", ")

info(name="배경은", age=32, email="1234@example.com")

# 10% 할인된 가격 출력 함수
def calculate_sail(**kwargs):
    for num, (key, value) in enumerate(kwargs.items(), start=1):
        value *= 0.9
        print(f'{num}. {key}의 가격은 10% 할인된 {int(value)} 원입니다.')


calculate_sail(가방=200000, 신발=150000, 치마=10000)

######################################################################################################
# 지역변수와 전역변수

# 파이썬의 메모리 구조
'''
- 스택 영역
    지역 변수(local variable), 매개 변수(parameter) 등이 저장되는 공간
- 힙 영역
    파이썬에서 생성되는 모든 객체(숫자, 문자열, 리스트, 딕셔너리, 클래스 인스턴스 등)가 저장되는 공간
'''

# 변수의 유효 범위(Scope)
'''
Scope(스코프) : 어떤 이름(변수, 함수 등)을 참조할 수 있는 코드의 범위

* 파이썬의 이름 탐색 규칙 : LEGB Rule
    - Local : 지역 스코프(함수 내)
    - Enclosing : 내포된 함수의 스코프
    - Global : 모듈 단위
    - Built-in : 내장 이름들 ex) len, sum 등
'''

# 지역 변수(Local Variable) : 함수 내부에서 선언된 변수
'- 함수가 호출될 때 생성되고, 함수가 끝나면 소멸됨'

def greet():
    message = "안녕하세요" # 지역 변수
    print(message)

greet() 
print(message) # 오류 발생: message는 지역 변수

'- message는 greet() 함수 내부에서만 유효함'
'- 함수 바깥에서 접근 시, NameError 발생'

# 전역 변수(Global Variable) : 함수 외부에서 선언된 변수
'- 프로그램 전체에서 접근 가능(단, 함수 내부에서 값 변경은 제한됨)'

# 전역변수
count = 0

def show_count():
    print(f'count = {count}')

show_count()    # count: 0

# 함수 내부에서 전역 변수 수정 시 문제 발생
x = 10

def change_x():
    x = x + 5   # UnboundLocalError 발생
    print(x)

change_x()

'- 함수 내에서 x = x + 5 로 할당하려는 순간, 파이썬은 x를 지역 변수로 간주'
'- 할당 전에 값을 참조하려고 했기 때문에 UnboundLocalError 발생'

# Global 키워드 사용 : 함수 내부에서 전역 변수 수정이 필요할 때
def change_x():
    global x    # 전역 변수임을 암시
    x = x + 5
    print(f'[함수 내부] x: {x}')    # x = 15

change_x()
print(f'[함수 외부] x: {x}')    # x = 15

'* 주의점'
'- 전역 상태를 지나치게 사용하는 코드는 유지보수가 어렵고, 에러 발생 가능성 증가'
'- 전역 변수는 가급적 읽기만 하고, 수정이 필요하다면 매개변수와 반환값으로 전달하는 구조 권장'

# nonlocal 키워드(심화, 중첩 함수에서 사용)
def outer():
    a = 10
    def inner():
        nonlocal a
        a += 5
        print(f'[inner] a : {a}')
    inner()
    print(f'[outer] a : {a}')

outer()

'- 내부 함수가 바깥 함수의 지역 변수에 접근하고 수정할 수 있게 함'

######################################################################################################
# 실습 3 전역 변수 연습하기

'''
로그인/로그아웃 전역 상태 관리
    전역 변수로 로그인한 사용자 저장 및 로그아웃 기능 구현

    * 요구 사항
        - 전역 변수 current_user는 로그인한 사용자의 이름을 저장합니다.
        - login(name) 함수는 사용자를 로그인시키고, logout() 함수는 로그아웃 상태로 만듭니다.
        - 이미 로그인된 상태에서 다시 로그인하면, "이미 로그인되어 있습니다."를 출력합니다.
        - 로그아웃하지 않고 로그인을 여러 번 시도할 수 없도록 합니다.
'''
# 전역 변수 - 사용자 이름 저장
current_user = ""
condition = False

# 로그인 함수
def login(name):
    global current_user

    # 저장된 변수가 있을 때
    if current_user:
        print("이미 로그인되었습니다.")
    # 저장된 변수가 없을 때
    else:
        current_user = name
        print(f'{name}님 로그인 성공')

# 로그아웃 함수
def logout():
    global current_user

    # 저장된 변수가 있을 때
    if current_user:
        current_user = ""
        print("로그아웃되었습니다.")


login("Ian")
login("CodingOwl")
logout()
login("CodingOwl")
print(current_user)

######################################################################################################
# 재귀함수(Recursive Function)

'''
함수가 자기 자신을 호출하는 함수
반복문 없이 특정 작업을 반복 수행할 수 있음

* 기본 구조
def 함수이름():
    if 종료조건:
        return 결과
    else : 
        return 자기자신호출(작은 입력)

* 작동 원리
    - 함수가 자기 자신을 호출하면서 문제를 더 작은 문제로 나눔
    - 기본 조건(Base Case)이 충족될 때까지 재귀 호출을 반복
    - 기본 조건을 만나면 재귀 호출이 종료되고, 함수가 차례로 반환됨

    ※ 재귀 호출이 끝나려면 반드시 기본 조건(Base Case)이 필요!
        → 없으면 무한 루프 발생

* 장점
    - 코드가 직관적이고 간결함 : 복잡한 문제를 간결하게 표현 가능하여 코드의 가독성이 높아짐
    - 문제 해결을 논리적으로 표현 가능 : 반복문(for, while)보다 문제의 개념을 더 자연스럽게 코드로 표현 가능(예: DFS, 트리 탐색, 하노이의 탑 등)
    - 일부 알고리즘에 적합 : 분할 정복(Dvide & Conquer), 백트래킹(Backtracking), 트리 탐색(Tree Traversal)과 같은 문제에서 재귀가 유용함
    - 데이터 구조 탐색에 용이 : 연결 리스트, 그래프, 트리와 같은 재귀적 구조를 가진 데이터 구조 탐색에 적합함

* 단점
        # 스택 오버플로우 : 함수 호출이 너무 깊어져 스택 메모리가 초과되면서 프로그램이 비정상적으로 종료되는 현상
    - 스택 오버플로우(Stack Overflow) 위험 : 너무 깊은 재귀 호출이 발생하면 스택 메모리가 초과되어 프로그램이 종료될 수 있음
    - 반복문보다 성능이 낮을 수 있음 : 함수 호출마다 스택 프레임이 생성되므로, 반복문보다 성능이 떨어질 수 있음
    - 메모리 사용량 증가 : 각 함수 호출마다 메모리가 추가로 필요하므로, 메모리 사용량이 증가할 수 있음
    - 중복 연산이 발생할 가능성 : 피보나치 수열처럼 같은 값을 여러 번 계산하는 경우 불필요한 연산이 많아짐
    - 디버깅이 어려울 수 있음 : 반복문보다 실행 흐름을 추적하기 어려울 수 있음

* 반복문과 비교
                    재귀                         반복문
사용방식        함수가 자기 자신을 호출         for, while 사용
코드 가독성     논리적으로 간결                 더 직관적이고 이해하기 쉬움
메모리 사용     스택 메모리 사용                메모리 사용량이 적음
                (함수 호출 스택 증가)
속도           재귀 깊이가 깊어지면 비효율적    일반적으로 더 빠름
추천 상황       문제를 작은 문제로 나눌 경우    일반적인 반복 작업(배열 순회 등)
'''
# 기본 구조
def recursive_func(n):

    if n == 0:
        return  # 기본 조건(Base Case)
    print("재귀 호출")

    recursive_func(n-1) # 자기 자신 호출

######################################################################################################
# 실습 4 거듭 제곱

'''
자연수 a와 b가 주어졌을 때, a의 b 제곱을 계산하는 재귀 함수 만들기

거듭제곱의 정의
    a**b = a * (a**(b-1))
'''

def n_th_power(a, b):

    if b == 0:
        return 1

    return a * n_th_power(a, b-1)


print(n_th_power(2, 5)) # 32

######################################################################################################
# 실습 5 팩토리얼(Factorial)

'''
1. 반복문을 활용하여 팩토리얼을 구현한다.
2. 1번을 바탕으로 작동 원리를 파악하고, 재귀함수를 이용해서 팩토리얼을 구현한다.
3. 디버거를 이용해 재귀함수의 작동을 확인합니다.
    n! = n * (n-1) * (n-2) * ... * 1
'''

def pactorial(n):

    if n == 0:
        return 1

    return n * pactorial(n-1)


print(pactorial(5))

######################################################################################################
# 실습 6 피보나치 수열(Fibonacci Numbers)

'''
1. 먼저 반복문을 활용해서 피보나치 수열을 구현합니다.
2. 1번을 바탕으로 작동 원리를 파악하고, 재귀함수를 이용해서 피보나치 수열을 구현합니다.

    0 이하의 수가 입력될 시 0 리턴
'''

n = 3

0 1 2
1 1 2

lst=[]

lst = [x+=x for x in range(n)]

print(lst)

    


    



def fivonacci(n):

    if n < 0:
        return 0
    
    return n + fivonacci(n) 
        