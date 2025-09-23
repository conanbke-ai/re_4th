# 모듈(Module)

'''
여러 기능들이 뭉쳐진 하나의 .py 파일
    함수, 변수, 클래스 등을 담아 코드의 재사용성과 관리 효율을 높임

* 모듈을 사용하는 이유
    - 코드의 분할 및 재사용
    - 유지보수 용이성
    - 네임스페이스 분리로 충돌 방지
'''

# 사용 예제 - 모듈 생성
# hello.py
import os
import time
import sys
from datetime import datetime
from random import choices
from random import randint
from my_math import operations
import datetime
import random
import calculator
import math as m
from math import *
from math import sprt
import math
import hello    # hello.py 파일을 불러옴


def greeting(name):
    print(f'Hello, {name}!')


# main.py
hello.greeting("Python")    # Hello, Python!

'- import 키워드로 모듈을 불러옴'
'- 모율이름.함수이름() 형태로 접근'

# 사용 예제 - 다양한 import 방식
# 방법 1. 모듈 전체 불러오기

# 방법 2. 특정 함수만 불러오기

# 방법 3. 모든 함수/변수 불러오기 (비추천)

# 방법 4. 모듈에 별칭 사용

'- import 모듈명 또는 from 모듈 import 이름 방식 사용 권장'


# 작성되어있는 모듈

result = calculator

######################################################################################################
# 실습 1 계산기 모듈 만들어보기

'''
1. calc.py라는 파일을 생성하여 사칙연산 함수(덧셈, 뺄셈, 곱셈, 나눗셈)을 각각 구현하세요.
2. 함수명 : add(a, b), substract(a, b), multiply(a, b), divide(a, b)
3. 같은 폴더에 main.py 파일을 생성하고, calc 모듈을 import 하여 각 함수의 결과를 출력하세요.

* 요구 사항
    나눗셈 함수에서 0으로 나누는 경우 "0으로 나눌 수 없습니다."를 출력하고 None을 반환하세요.
'''

######################################################################################################
# 패키지(Package)

'''
여러 모듈(.py파일)을 폴더(디렉터리) 단위로 묶은 것
    - 대규모 프로젝트, 라이브러리 제작 시 사용
    - (python 3.3이전) 파이썬의 패키지로 인식되려면 __init__.py를 포함

* 패키지 폴더 구조 예시

my_package/
    __init__.py
    module_a.py
    module_b.py
    sub_package/
        __init__.py
        module_c.py
'''
# 패키지 생성
# my_math 패키지 생성 후
# operations.py


def mul(a, b):
    return a * b


# 패키지 불러오기(임포트) 및 사용
print(operations.mul(3, 4))  # 12

'- my_math라는 패키지에서 operations 모듈을 import하여 사용'


'''
외부 패키지 다운받아 불러오기

* pip 사용

파이썬 패키지 관리자

1. 설치 전, 가상환경 생성
    python -m venv 이름(myenv)

2. 가상환경 활성화(Window)
    ex) myenv\Script\activate
    가상환경 활성화(Mac/Linux)
        ex) source myenv/bin/activate

만약, pip가 최신이 아니라면 
    python -m pip install --upgrade pip

전체 pip 설치 리스트 확인
    pip list

가상환경 비활성화
    deactivate

pip install numpy 
pip install pandas

→ pip install numpy pandas
'''

######################################################################################################
# 파이썬 표준 모듈(라이브러리)

'''
파이썬 표준 라이브러리
    파이썬이 설치될 때 기본적으로 포함되어 있는 모듈들의 집합
        - 외부 설치(pip 등)없이 바로 사용할 수 있음

* 파이썬 내장 모듈의 종류
모듈        설명
math        수학 계산과 관련된 모듈
random      난수를 발생시키는 모듈
datetime    날짜 및 시간과 관련된 모듈
time        시간과 관련된 모듈
sys         변수와 함수를 직접 제어할 수 있게 해주는 모듈
os          환경변수나 디렉터리, 파일 등의 OS 자원을 제어할 수 있게 해주는 모듈
'''

'''
math 모듈
    수학적 연산에 사용되는 모듈
        - 주요 기능 : 수학 상수, 삼각함수, 로그, 제곱근 등

* 대표 함수
함수명              용도
sqrt(x)             x의 제곱근
pow(x,y)            x의 y제곱
factorial(x)        x! (팩토리얼)
ceil(x)             올림
floor(x)            내림
trunc(x)            절삭(버림)
fabs(x)             절댓값
gcd(x, y)           최대공약수
lcm(x, y)           최소공배수
pi                  수학 상수
e                   수학 상수
sin(x)              삼각함수(단위:라디안)
cos(x)              삼각함수(단위:라디안)
tan(x)              삼각함수(단위:라디안)
log(x)              로그함수
log10(x)            로그함수
exp(x)              지수함수
'''

######################################################################################################
# 실습 2 math 모듈 사용해보기

'''
1. 실제 거리 계산 : 좌표 두 점 사이 거리 구하기
    두 점(x1, y1), (x2, y2)의 좌표를 입력받아 두 점 사이의 실제 거리를 소수 둘째 자리까지 구하세요.

* 피타고라스 정리 : 거리 = sqrt((x2-x1)^2 + (y2-y1)^2)
* math.sqrt(), math.pow() 함수 활용
'''

x1, y1 = input("(x1, y1) 좌표를 입력해주세요(입력예) (1,2)) : ").split(",")
x2, y2 = input("(x2, y2) 좌표를 입력해주세요(입력예) (1,2)) : ").split(",")

l = math.sqrt(math.pow(math.fabs(int(x2)-int(x1)), 2) +
              math.pow(math.fabs(int(y2)-int(y1)), 2))
print(round(l, 2))  # 3.61


'''
2. 상품 나누기 : 최소 공배수와 최대 공약수
    어떤 학급에 학생이 18명, 선생님이 24명 있습니다.
    두 집단이 모두 공평하게 나눠 가질 수 있는 최대의 간식 개수(최대 공약수)와
    포장 단위별로 동시에 맞게 나누어 떨어지는 최소 간식 개수(최소 공배수)를 구하는 코드를 작성하세요.

* math.gcd(), math.lcm() (lcm은 Python 3.9+)
'''

print(f'최대 공약수 : {math.gcd(18, 24)}', f'최소 공배수 : {math.lcm(18, 24)}', sep="\n")

# 최대 공약수 : 6
# 최소 공배수 : 72

######################################################################################################
'''
random 모듈
    랜덤 값(난수) 생성 시, 사용
        - 주요 기능 : 난수, 임의 선택, 섞기

* 대표 함수
함수명                          용도
random()                        0.0~1.0 사이의 실수 난수
random(a, b)                    a~b 범위 내 정수 난수
uniform(a, b)                   a~b 범위 내 실수 난수
randrange(start, stop, step)    범위 내 정수 난수
choices(seq, k)                 시퀀스에서 k개 임의 선택(중복 가능)
sample(seq, k)                  시퀀스에서 k개 임의 선택(중복 불가)
shuffle(seq)                    시퀀스 무작위 섞기(리스트만 가능)
seed(a)                         난수 생성 초기값 설정
'''

######################################################################################################
# 실습 3 로또 번호 뽑기

'''
1. 1~45 까지의 수 중에서 랜덤으로 6개의 숫자를 뽑는다.
2. 6개의 숫자 중 중복되는 숫자가 없도록 한다.
3. 오름차순으로 정렬한 결과를 출력한다.
'''


# 리스트 초기화
x = []

# 임의의 수만큼 반복
for i in range(100):
    # 1~45 사이의 난수 할당
    r = randint(1, 45)
    # 리스트에 값이 없을 시, append
    if r not in x:
        x.append(r)
        # 리스트의 길이가 6이면 종료
        if len(x) == 6:
            break

# 결과값 결과값 오름차순 출력
print(sorted(x))

'''
예시1)
import random

# 1~45 사이에서 중복 없이 6개 난수 뽑기
numbers = random.sample(range(1, 46), 6)

# 오름차순 정렬
print(sorted(numbers))
'''

######################################################################################################
# 실습 4 가위 바위 보 게임 만들기
'''
1. 컴퓨터는 "가위", "바위", "보" 중 하나를 무작위로 선택합니다.
2. 사용자는 키보드로 "가위", "바위", "보" 중 하나를 직접 입력합니다.
3. 둘의 결과를 비교해 승, 무, 패를 판단하여 출력하세요.

* 요구 사항
    random 모듈의 함수를 사용할 것
    사용자 입력은 input()으로 받을 것
    승패 판정(비교) 로직은 if/elif/else로 직접 구현할 것
'''

# 1. 컴퓨터가 무작위 선택
choices = ["가위", "바위", "보"]
computer = random.choice(choices)

# 2. 사용자 입력
user = input("가위, 바위, 보 중 하나를 입력하세요: ")

print(f"컴퓨터: {computer}, 사용자: {user}")

# 3. 승패 판정
if user == computer:
    print("무")
elif (user == "가위" and computer == "보") or \
     (user == "바위" and computer == "가위") or \
     (user == "보" and computer == "바위"):
    print("승")
elif user in choices:
    print("패배")
else:
    print("잘못된 입력입니다. '가위', '바위', '보' 중 하나만 입력하세요.")


'''
* 딕셔너리 사용 구조


import random

choices = ["가위", "바위", "보"]
computer = random.choice(choices)
user = input("가위, 바위, 보 중 하나를 입력하세요: ")

print(f"컴퓨터: {computer}, 사용자: {user}")

# 승패 규칙 딕셔너리 (key가 이기는 value)
win_rules = {
    "가위": "보",
    "바위": "가위",
    "보": "바위"
}

if user not in choices:
    print("잘못된 입력입니다.")
elif user == computer:
    print("무")
elif win_rules[user] == computer:
    print("승")
else:
    print("패")
'''

'''
* 클래스로 구현

import random

class RPSGame:
    def __init__(self):
        self.choices = ["가위", "바위", "보"]
        self.win_rules = {
            "가위": "보",
            "바위": "가위",
            "보": "바위"
        }
        self.user_score = 0
        self.computer_score = 0

    def play_round(self):
        computer = random.choice(self.choices)
        user = input("가위, 바위, 보 중 하나를 입력하세요 (종료하려면 '종료'): ")

        if user == "종료":
            return False  # 게임 종료 신호

        if user not in self.choices:
            print("잘못된 입력입니다. 다시 입력하세요.")
            return True

        print(f"컴퓨터: {computer}, 사용자: {user}")

        if user == computer:
            print("무승부!")
        elif self.win_rules[user] == computer:
            print("사용자 승리!")
            self.user_score += 1
        else:
            print("컴퓨터 승리!")
            self.computer_score += 1

        return True

    def start(self):
        print("=== 가위바위보 게임 시작 ===")
        while True:
            if not self.play_round():
                break
        print("=== 게임 종료 ===")
        print(f"최종 점수 → 사용자: {self.user_score}, 컴퓨터: {self.computer_score}")


# 실행
game = RPSGame()
game.start()
'''

######################################################################################################
'''
datetime 모듈
    날짜와 시간의 생성, 조작, 형식 변환과 같은 시간 관련 기능을 제공
        - 주요 기능 : 현재 날짜/시간, 시간 차이 계산, 포맷 변환

* 대표 함수
함수명                          용도
datetime.now()                  현재 날짜와 시간
date.today()                    오늘 날짜
datetime(year, m, d, h, m, s)   특정 날짜/시간 객체 생성
strftime(format)                날짜/시간 → 문자열로 포맷 변환
strptime(string, format)        문자열 → 날짜/시간 객체로 변환
timedelta(days, hours, ...)     날짜/시간 차이, 연산
weekday()                       요일 반환(월:0 ~ 일:6)
'''
# 사용 예제 - 지나온 날짜 계산하기

print("지금까지 몇 일?")

first_day = datetime.date(year=2025, month=9, day=3)
print(first_day)    # 2025-09-03

today = datetime.date.today()
print(today)        # 2025-09-23

passed_time = today - first_day
print(passed_time)  # 20 days, 0:00:00

print(f'개강 이후 {passed_time.days}일 지났습니다.')    # 개강 이후 20일 지났습니다.

# 사용 예제 - 날짜로 요일 알아내기
'''
weekday() -  0 : 월 ~ 6 : 일로 변환
isweekday() - 1 : 월 ~ 7 : 일로 변환
'''

days = ["월", "화", "수", "목", "금", "토", "일"]

# 오늘의 요일
weekday = datetime.date.today().weekday()
print(weekday)      # 1
print(f'오늘은 {days[weekday]}요일')    # 화

# 특정한 날의 요일
the_day = datetime.date(year=2024, month=9, day=17).weekday()
print(the_day)      # 1
print(f'추석은 {days[the_day]}요일')    # 화


######################################################################################################
'''
calendar 모듈
    날짜와 달력 관련 다양한 기능 제공
        - 주요 기능 : 달력(캘린더) 생성, 요일 계산, 윤년 판별

* 대표 함수
함수명                      용도
month(year, month)          특정 연, 월의 달력(문자열) 출력
calendar(year)              특정 연도의 달력(문자열) 출력
prmonth(year, month)        지정한 연도와 월의 달력을 콘솔에 보기 좋게 출력
weekday(year, month, day)   해당 날짜의 요일(월:0~일:6) 반환
isleap(year)                윤년 여부 판별(True/False)
monthrange(year, month)     (첫날 요일, 마지막 일)튜플 반환
setfirstweekday(n)          달력의 첫 요일 지정
'''

######################################################################################################
# 실습 5 다음 생일까지 남은 날짜 계산하기

'''
1. 사용자로부터 생일(월-일, 예: 07-25)을 입력 받으세요.
2. 오늘 날짜를 기준으로 올해 또는 내년의 생일까지 남은 날짜(일 수)를 계산해서 출력하세요.
    - 올해 생일이 지났으면 내년까지 남은 일 수로,
        아직 안 지났으면 올해 생일까지 남은 일 수로 계산

* 요구 사항
    - 날짜 연산에는 반드시 datetime 모듈을 사용할 것
'''


# 1. 사용자 입력
birth = input("생일을 입력하세요 (MM-DD 형식, 예: 07-25): ")
birth_month, birth_day = map(int, birth.split("-"))

# 오늘 날짜
today = datetime.today()

# 2. 올해 생일 날짜 만들기
this_year_birthday = datetime(today.year, birth_month, birth_day)

# 3. 생일까지 남은 일수 계산
if this_year_birthday >= today:
    # 아직 안 지난 경우 → 올해 생일까지 남은 일수
    left_day = (this_year_birthday - today).days
else:
    # 이미 지난 경우 → 내년 생일까지 남은 일수
    next_year_birthday = datetime(today.year + 1, birth_month, birth_day)
    left_day = (next_year_birthday - today).days

print(f"당신의 다음 생일까지 {left_day}일 남았습니다!")

######################################################################################################
'''
표준 모듈 - time 모듈
    시간의 측정, 지연, 변환과 같은 시간 관련 기능을 제공
        - 주요 기능 : 현재 시간, 대기(sleep), 시간 측정

* 대표 함수
함수명                      용도
time()                      현재 시각을 Unix 타임스탭프로 반환
ctime([secs])               타임스탬프(혹은 현재 시간)
sleep(seconds)              지정한 초만큼 프로그램 실행 일시 정지
localtime([secs])           타임스탬프를 struct_time(로컬)로 변환
strftie(format, t)          시간 객체를 포맷 문자열로 변환
strptime(string, format)    포맷 문자열을 시간 객체(struct_time)으로 변환
'''

# 사용 예제 - 수행 시간 측정

# 수행 시간 측정하기
start = time.time()

# 1초 간격으로 출력
for i in range(10):
    print(i)
    time.sleep(1)

end = time.time()
print("수행 시간 : " + str(end-start) + "초")


# 1초 간격으로 실행됨
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 수행 시간 : 10.008511781692505초

######################################################################################################
# 실습 6 타자 연습 게임 만들기

'''
1. 영단어 리스트 중 무작위로 단어가 제시됩니다.
2. 사용자는 해당 단어를 정확히 입력해야 다음 문제로 넘어갈 수 있습니다.
3. 10문제를 모두 맞히면, 게임이 종료되고 총 소요 시간이 출력됩니다.
4. 틀린 경우에는 "오타! 다시 도전!" 메시지를 출력하고, 같은 문제를 다시 도전하게 합니다.
5. 게임이 시작되기 전, 엔터키를 누르면 시작합니다.

* 요구 사항
    - 단어는 미리 주어진 리스트에서 random.choice()로 무작위 선택
    - input()으로 사용자 입력
    - time.time()으로 시작~종료 시간 측정, 소요 시간 계산
    - 문제마다 번호가 함께 출력
    - 통과/오타 메시지, 총 타자 시간까지 출력
'''

words = [
    "apple", "banana", "cherry", "grape", "orange",
    "peach", "pear", "plum", "melon", "lemon",
    "car", "bus", "train", "plane", "ship",
    "dog", "cat", "horse", "tiger", "lion"
]

ent = input("[타자 게임] 준비되면 엔터!")

# 엔터값 들어왔을 때 게임 시작
if ent == "":

    # 시작 시간 측정
    start_time = time.time()

    # 10문제 반복
    for i in range(1, 11):

        print(f'문제 {i}')
        # 문제 (리스트 랜덤 배열)
        q = random.choice(words)
        usr = input("")

        while True:
            # 정답을 맞출 때까지 반복
            if usr != q:
                usr = input("오타! 다시 도전! \n: ")
            else:
                print(q)
                print(usr)
                print("통과!!")
                break

    # 종료 시간 측정
    end_time = time.time()

    print(f'타자 시간 : {end_time - start_time}초')

print("[타자 게임] 종료")
######################################################################################################
'''
sys 모듈
    파이썬 인터프리터와 관련된 다양한 기능을 제공
        - 주요 기능 : 입출력, 인자 처리, 환경 정보, 종료 등

* 대표 함수
함수명                          용도
sys.version                 파이썬 버전 문자열 반환
sys.platform                실행 중인 운영체제 정보 반환
sys.argv                    명령행 인자 리스트 반환
sys.exit([arg])             프로그램 즉시 종료
sys.path                    모듈 검색 경로(리스트)
sys.stdin/stdout/stderr     표준 입출력/에러 스트림(파일 객체)
'''

'''
sys.argv : 명령 행에서 인수 전달하기

python  sys_ex1.py   dog        cat         tiger
        argv[0]      argv[1]    argv[2]     argv[3]
'''
# print(sys.argv)

args = sys.argv[1:]  # 인덱싱
print(args)

######################################################################################################
# 실습 7 sys 라이브러리 활용하여 sys.exit(0) 파이썬 프로그램 종료

x = input("수 입력 : ")
n = int(x)

if n == 0:
    print("0으로 나눌 수 없습니다.")
    sys.exit(0)

result = 10 / n

print(result)

# 수 입력 : 3
# 3.3333333333333335

# 수 입력 : 0
# 0으로 나눌 수 없습니다.

######################################################################################################
'''
os 모듈
    운영체제와 상호작용할 수 있도록 도와주는 기능 제공
        - 주요 기능 : 파일·디렉터리 관리, 환경 변수, 시스템 정보 등

* 대표 함수
함수명                  용도
os.getcwd()             현재 작업 디렉터리 경로 반환
os.listdir([path])      디렉터리 내 파일/폴더 목록 반환
os.mkdir([path])        새 디렉터리 생성
os.remove(path)         파일 삭제
os.rmdir(path)          빈 디렉터리 삭제
os.rename(src, dst)     파일/디렉터리 이름 변경
os.environ              환경 변수(딕셔너리)
os.path.join(a, b, ..)  경로들을 OS에 맞게 합침
os.path.exists(path)    경로의 존재 여부(True/False) 반환
'''

######################################################################################################
# 실습 8 os 라이브러리 활용하여 새 폴더 생성 후 파일 목록 출력하기

# 1. 현재 작업 디렉터리 확인
# 현재 작업 디렉터리 :  C:\Users\user\Documents\re-4th
print("현재 작업 디렉터리 : ", os.getcwd())

# 2. 새 폴더 생성(이미 있으면 예외 발생 가능)
folder_name = "sample_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f'{folder_name} 폴더를 생성했습니다.')    # sample_folder 폴더를 생성했습니다.
else:
    print(f'{folder_name} 폴더가 이미 존재합니다.')

# 3. 현재 디렉터리 내 파일/폴더 목록 출력
print("현재 디렉터리 내 파일 및 폴더 목록")
# ['.git', '.gitignore', 'Init_Test', 'Project1', 'Python', 'README.md', 'sample_folder', 'Study']
print(os.listdir())
