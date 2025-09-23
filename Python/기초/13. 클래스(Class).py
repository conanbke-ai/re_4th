# 객체 지향 프로그래밍(OOP, Object-Oriented Programming)

'''
OOP(Object-Oriented Programming, 객체 지향 프로그래밍)
    : 객체를 기반으로 프로그램을 설계하는 프로그래밍 패러다임
    ref) C++은 대표적인 객체 지향 언어
'''
######################################################################################################
# 객체(Object)란?

'''
객체(Object)는 데이터와 데이터를 조작하는 기능(메서드)를 하나로 묶은 독립적인 실행 단위
객체는 실제 세계의 사물이나 개념을 프로그래밍적으로 모델링한 것

* 객체의 특징
    - 상태(State) : 객체의 속성(데이터, 변수)
    - 행동(Behavior) : 객체의 기능(메서드, 함수)
    - 식별성(Identity) : 객체 고유의 존재
'''
'''
객체 : "속성과 행동" 을 함께 묶어서 현실 세계의 개념을 표현할 수 있도록 함
모델링 : 현실 세계의 복잡한 개념을 프로그래밍에서 다룰 수 있도록 단순화하는 과정
'''
'''
OOP 이전에는 절차적 프로그래밍이 널리 사용되었음

* 절차적 프로그래밍(Procedural Programming)
    - 프로그램을 순차적인 절차(Flow)와 함수(Procedure)로 구성하는 방식
    - 함수 (또는 프로시저) 단위로 코드가 실행되며, 데이터를 함수가 직접 처리
    
    * 문제점
        - 데이터와 함수가 분리되어 있음
        - 함수가 많아지면 코드가 복잡해짐
        - 코드 재사용성이 낮음
        - 유지보수가 어려움
'''
'''
1. 캡슐화(ENcapsulation) : 객체 내부 데이터를 외부에서 직접 접근하지 못하도록 보호
    - 데이터 보호(Data Hiding)을 통해 잘못된 값이 저장되지 않도록 방지
    - 내부 동작을 숨겨 코드 변경이 있어도 외부에서 영향없이 사용 가능(모듈화)
2. 상속(Inheritance) : 기존 클래스를 확장하여 새로운 기능을 추가할 수 있음
    - 코드의 재사용성을 높이고 유지보수를 쉽게 만듦
    - 기존 클래스를 기반으로 새로운 기능을 추가하는 것이 용이함
3. 다형성(Polymorphism) : 같은 함수를 서로 다른 방식으로 실행할 수 있음
    - 새로운 클래스 추가 시 기존 코드를 변경할 필요 없음
    - 같은 인터페이스를 사용해 다양한 기능을 쉽게 추가할 수 있음
4. 추상화(Abstrction) : 필요한 정보만 보여주고, 불필요한 내부 구현은 숨기는 개념
    - 불필요한 세부 사항 없이 핵심 기능만 제공하여 코드 관리가 쉬워짐
    - 공통적인 동작을 정의하고, 세부 구현은 각 클래스에서 따로 처리 가능
'''
'''
OOP가 중요한 이유

    1. 코드 재사용성 증가
        같은 클래스를 여러 개의 객체로 생성하여 사용 가능
    2. 유지보수 및 확장 용이
        클래스 단위로 개발하면 새로운 기능을 추가하기 쉬움
        기존 클래스를 수정하면 관련된 모든 객체에 반영됨
    3. 현실 세계 모델링 가능
        현실 세계의 개념을 코드로 직접 표현할 수 있음
    4. 코드 구조화
        복잡한 프로그램을 체계적으로 구성
'''

######################################################################################################
# 클래스(Class)
'''
데이터(속성)과 기능(메서드)를 하나로 묶는 구조

* 기본 문법
    class ClassName:
        # 클래스 변수
        ...

        # 클래스 생성자
        def __init__(self, ...):
            # 인스턴스 변수 초기화
            ...
        # 메서드 정의
        def method_name(self, ...):
            ...
        
    - class : 클래스 정의 키워드
    - 클래스 이름 : 주로 PascalCase 사용
    - 생성자 (__init__) : 객체가 생성될 때 자동 호출되는 초기화 메서드
    - self : 생성되는 객체 자신을 가리킴
    - 클래스 변수 : 모든 객체가 공유하는 변수
    - 인스턴스 변수 : 객체마다 독립적으로 유지되는 변수(self.변수명)
    - 메서드 : 클래스 내부에 정의된 함수. 첫 번째 인자로 self를 사용
'''
'''
클래스와 객체

- 클래스(Class) : 객체를 만들기 위한 설계도
- 객체(Object) : 클래스로부터 만들어진 실제 데이터(→ 인스턴스)

클래스는 공통적인 속성과 동작을 정의하고, 객체는 이를 기반으로 실제 데이터를 가지는 객체
'''


from abc import ABC, abstractmethod
class Person:
    def __init__(self, name, age):
        # 인스턴스 변수
        self.name = name
        self.age = age

    def introduce(self):
        print(f'안녕하세요. 저는 {self.name}, {self.age}살입니다.')


'''
객체(인스턴스) 생성
    클래스를 기반으로 실제 동작 가능한 실체(객체)를 만드는 것을 인스턴스 생성이라고 함
    객체는 클래스이름() 형식으로 생성하며, 생성자에 정의된 매개변수를 전달해야 함
'''

# 객체 생성
person1 = Person("지민", 25)
person2 = Person("민준", 30)

# 메서드 호출
person1.introduce()  # 안녕하세요. 저는 지민, 25살입니다.
person2.introduce()  # 안녕하세요. 저는 민준, 30살입니다.

# Car 클래스 생성


class Car:
    def __init__(self, brand, model, color):
        self.brand = brand  # 브랜드
        self.model = model  # 모델명
        self.color = color  # 색상
        self.speed = 0      # 현재 속도

    def accelerate(self, increase):
        "속도를 증가시키는 메서드"
        self.speed += min(150, increase)  # 최대 속도 150 미만이어야 함
        print(f'속도가 {increase}km/h 증가했습니다. 현재 속도 : {self.speed}km/h')

    def brake(self, decrease):
        "속도를 감소시키는 메서드"
        self.speed = max(0, self.speed - decrease)  # 속도는 0 미만이 될 수 없다.
        print(f'속도가 {decrease}km/h 감소했습니다. 현재 속도 : {self.speed}km/h')

    def info(self):
        "차량 정보를 출력하는 메서드"
        print(f'브랜드: {self.brand}')
        print(f'모델명: {self.model}')
        print(f'색상: {self.color}')
        print(f'현재 속도: {self.speed}km/h')


# 객체(인스턴스) 생성
my_car = Car('tesla', 'model 3', '빨간색')
# 객체 정보 출력
my_car.info()
my_car.accelerate(80)
my_car.brake(30)
my_car.info()

# 브랜드: tesla
# 모델명: model 3
# 색상: 빨간색
# 현재 속도: 0km/h

# 속도가 80km/h 증가했습니다. 현재 속도 : 80km/h

# 속도가 30km/h 감소했습니다. 현재 속도 : 50km/h

# 브랜드: tesla
# 모델명: model 3
# 색상: 빨간색
# 현재 속도: 50km/h

'''
생성자 __init__() 함수

    - 생성자(Constructor)
        - 클래스로부터 객체(인스턴스)를 생성할 때 자동으로 호출되는 초기화 함수
        - 객체 생성 시 필요한 속성 초기화 및 기본 상태 설정에 사용
        - __init__() 메서드로 생성자 정의
        - 하나의 클래스에 하나의 __init__()만 정의 가능함

    - self : 생성되는 객체 자신을 가리킴
    - self.속성 = 매개변수 형태로 인스턴스 속성 초기화

    - 소멸자
        - 객체가 메모리에서 삭제될 떄 호출되는 메서드
        - def __del__(self):
'''


class Student:
    def __init__(self, name, age, student_id):
        "생성자 : 학생 객체를 초기화"
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []    # 성적 리스트 초기화
        print(f'학생 {name}의 정보가 등록되었습니다.')

    def add_grade(self, grade):
        "성적 추가 메서드"
        self.grades.append(grade)
        print(f'{self.name}의 성적 {grade}점이 추가되었습니다.')

    def get_averate(self):
        "평균 성적 계산 메서드"
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

    def __del__(self):
        print(f'학생 {self.name} 의 정보가 삭제되었습니다.')


# 객체(인스턴스) 생성
student1 = Student("김철수", 20, "20230001")    # 학생 김철수의 정보가 등록되었습니다.
print()
student1.add_grade(30)  # 김철수의 성적 30점이 추가되었습니다.
student1.add_grade(70)  # 김철수의 성적 70점이 추가되었습니다.
print(f'평균 점수 : {student1.get_averate()}')  # 평균 점수 : 50.0
print()
student2 = Student("이영희", 22, "20220112")    # 학생 이영희의 정보가 등록되었습니다.
del student2    # 학생 이영희 의 정보가 삭제되었습니다.
# 학생 김철수 의 정보가 삭제되었습니다.
'- 인스턴스 생성 시마다, 생성자 호출됨'
'- 함수 종료 시, 전체 객체가 사라지므로 정보가 삭제되었습니다 출력됨'

######################################################################################################
# 실습 1 class 기본 문법 연슴

'''
1. 책 클래스 만들기
    Book 클래스를 정의하세요.
    인스턴스 변수로 title, author, total_pages, current_page를 가집니다.
    메서드
        - read_page(pages): 현재 페이지를 읽음, 총 페이지 수를 넘지 않도록 처리
        - progress(): 전체에서 얼마나 읽었는지를 퍼센트(%)로 소수점 1자리까지 출력
'''

# Book 클래스 정의


class Book:

    def __init__(self, title, author, total_pages, current_page):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.currunt_page = current_page

    # 메서드 정의 - 현재 페이지를 읽음
    def read_page(self, pages):
        if pages < 0:
            return
        else:
            self.currunt_page = min(
                self.total_pages, self.currunt_page + pages)
        print(f'현재 {self.currunt_page} 페이지입니다.')

    # 메서드 정의 - 독서 진행률
    def progress(self):

        # 진행률 계산
        pct = self.currunt_page / self.total_pages * 100
        # 소수점자리 1번째까지
        print(f'현재 {round(pct, 1)} % 읽었습니다.')

    # 객체 출력 혹은 디버깅 시, 사용됨(문자열로 표현할 때 호출
    def __repr__(self):
        return f'<Book {self.title} by {self.author}> 현재 {self.currunt_page} / 총 {self.total_pages} 페이지>'


my_book = Book('파이썬 클린코드', '홍길동', 200, 0)
print(my_book)          # <Book 파이썬 클린코드 by 홍길동> 현재 0 / 총 200 페이지>
my_book.read_page(50)   # 현재 50 페이지입니다.
my_book.progress()      # 현재 25.0 % 읽었습니다.
my_book.read_page(100)  # 현재 150 페이지입니다.
my_book.progress()      # 현재 75.0 % 읽었습니다.

'''
2. Rectangle 클래스 구현
    - 인스턴스 변수 : width, height
    - 메서드
        area() : 사각형의 넓이 반환
    - 사용자 입력 : 
        프로그램 실행 시 사용자로부터 가로(width)와 세로(heingt) 값을 입력 받아 객체를 생성하고 area() 메서드를 호출하여 넓이를 출력
'''

# 클래스 생성


class Rectangle:

    # 생성자
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 넓이 구하기 공식
    def area(self):
        return self.width * self.height

    def __repr__(self):
        return f"(도형의 가로 길이 : {self.width}, 세로 길이 : {self.height})"


# 가로와 세로 길이를 입력하세요. : 7 4
width, height = input("가로와 세로 길이를 입력하세요. : ").split()
my_rectangle = Rectangle(int(width), int(height))
print(my_rectangle)         # (도형의 가로 길이 : 7, 세로 길이 : 4)
print(my_rectangle.area())  # 28

######################################################################################################
# 인스턴스 변수, 메서드 변수 vs 클래스 변수, 메서드 변수

'''
인스턴스 변수
    각 인스턴스(객체)가 개별적으로 소유하는 변수
        - self.변수이름 형태로 정의하며, 생성자(__init__)안에서 초기화
        - 객체마다 서로 다른 값을 가짐
        - 인스턴스이름.변수이름으로 접근
'''


class Dog:
    def __init__(self, name):
        self.name = name    # 인스턴스 변수


dog1 = Dog("초코")
dog2 = Dog("밀크")

print(dog1.name)    # 초코
print(dog2.name)    # 밀크

'''
클래스 변수
    클래스 자체에 소속된 변수
        - 모든 인스턴스가 공통적으로 공유
        - 클래스 블록 내부, 메서드 바깥에서 선언함
        - 클래스이름.변수이름으로 접근
    → 공유해야 하는 값을 클래스 변수로 사용
'''


class Dog:
    kind = "포유류"  # 클래스 변수

    def __init__(self, name):
        self.name = name    # 인스턴스 변수


dog1 = Dog("초코")
dog2 = Dog("콩이")

print(dog1.kind)    # 포유류
print(dog2.kind)    # 포유류
print(Dog.kind)     # 포유류

'''
인스턴스 메서드
    클래스 인스턴스를 통해 호출되는 메서드
        - 첫번째 인자는 self, 호출한 객체 자신을 의미
        - 인스턴스이름.메서드이름()으로 접근
'''


class MyClass:
    def instance_method(self, arg):
        print(f'self는 {self}, 인자는 {arg}')


class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f'안녕하세요. 저는 {self.name}입니다.')


p = Person("이안")
p.say_hello()   # 안녕하세요. 저는 이안입니다.

'''
클래스 메서드(@classmethod)
    클래스 자체를 대상으로 동작하는 메서드
        - 첫 번째 인자 cls, 클래스 자신을 참조(self는 인스턴스, cls는 클래스 자신)
        - 클래스 변수를 조작할 때 주로

    클래스 메서드는 인스턴스가 아닌 클래스 이름으로 호출
'''


class MyClass:
    @classmethod
    def class_method(cls, arg):
        print(f'cls는 {cls}, 인자는 {arg}')


class Book:
    count = 0  # 클래스 변수

    def __init__(self):
        Book.count += 1

    @classmethod
    def get_count(cls):
        print(f'총 {cls.count}권의 책이 생성되었습니다.')


b1 = Book()
b2 = Book()
Book.get_count()    # 총 2권의 책이 생성되었습니다.


'''
정적 메서드(@staticmethod)
    일반적인 유틸리티 함수를 클래스 내부에 정의할 때 사용
        self나 cls를 사용하지 않는 유틸리티 함수
        클래스와 관련은 있지만 클래스나 인스턴스 상태에 의존하지 않는 기능을 제공
    클래스 안에 포함되어 있지만, 클래스나 객체와 무관하게 사용할 수 있음
'''


class MyClass:
    @staticmethod
    def static_method(arg):
        print(f'정적 메서드입니다. {arg}')


class MathTool:
    @staticmethod
    def add(a, b):
        return a + b


print(MathTool.add(3, 5))   # 8

'''
* 메서드 비교 요약
            인스턴스 메서드         클래스 메서드          정적 메서드
데코레이터  없음                    @classmethod            @staticmethod
첫 인자     self(객체)              cls(클래스)             없음
호출 방식   인스턴스.메서드()       클래스.메서드()         클래스.메서드()
주 용도     인스턴스 상태 조작      클래스 상태 조작        일반 함수(유틸리티 등)


'''


class BankAccount:
    # 클래스 변수
    # 은행 이름
    bank_name = "파이썬 은행"
    # 총 계좌 개수
    total_acoounts = 0
    # 이자율
    interest_rate = 0.02

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.account_number = BankAccount.total_acoounts + 1
        # 클래스 변수 업데이트
        BankAccount.total_acoounts += 1

    def deposit(self, amount):
        "입금 메서드"
        if amount > 0:
            self.balance += amount
            print(f'{amount}원이 입급되었습니다. 잔액 : {self.balance}원')
        else:
            print(f'입급액은 0보다 커야 합니다.')

    def withdraw(self, amount):
        "출금 메서드"
        if self.balance >= amount:
            self.balance -= amount
            print(f'{amount}원이 출금되었습니다. 잔액 : {self.balance}원')
        else:
            print(f'잔액이 부족합니다.')

    def apply_interest(self):
        "이자 적용"
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        print(f'이자 {interest}원이 적용되었습니다. 잔액 : {self.balance}원')

    @classmethod
    def change_interest_rate(cls, new_rate):
        "클래스 메서드: 이자율 변경"
        cls.interest_rate = new_rate
        print(f'이자율 {new_rate % 100} %로 변경되었습니다.')

    def __del__(self):
        # 클래스 변수 업데이트
        BankAccount.total_acoounts -= 1
        print(f'{self.owner}의 계좌가 삭제되었습니다.')
        print(f'총 계좌 수는 {BankAccount.total_acoounts}')


account1 = BankAccount("홍길동", 10000)
print(account1.account_number)      # 1

account2 = BankAccount("김철수", 15000)
print(account2.account_number)      # 2

print(f'은행 이름 : {BankAccount.bank_name}')   # 은행 이름 : 파이썬 은행
print(f'총 계좌 수 : {BankAccount.total_acoounts}')  # 총 계좌 수 : 2

account1.deposit(20000)             # 20000원이 입급되었습니다. 잔액 : 30000원
account1.withdraw(15000)            # 15000원이 출금되었습니다. 잔액 : 15000원
account1.apply_interest()           # 이자 300.0원이 적용되었습니다. 잔액 : 15300.0원
BankAccount.change_interest_rate(0.04)  # 이자율 0.04 %로 변경되었습니다.
del account1    # 홍길동의 계좌가 삭제되었습니다.
# 총 계좌 수는 1
# 김철수의 계좌가 삭제되었습니다.
# 총 계좌 수는 0

'- self.account_number = BankAccount.total_acoounts + 1 자체가 클래스 변수를 변화시키지 않으므로 따로 증가해주어야 함'
'- del account1 하지 않아도 프로그램 종료 시, 전체 객체 삭제됨'


class Calculator:
    # 클래스 변수
    calculation_count = 0

    def __init__(self, name):
        self.name = name
        self.history = []

    # 인스턴스 메서드
    def add_to_history(self, operation, result):
        "계산 기록 저장"
        self.history.append(f'{operation} = {result}')
        Calculator.calculation_count += 1

    @classmethod
    def get_total_calculations(cls):
        return cls.calculation_count

    @staticmethod
    def add(a, b):
        "두 수의 합"
        return a + b

    @staticmethod
    def multiply(a, b):
        "두 수의 곱"
        return a * b

    @staticmethod
    def is_even(number):
        "짝수 판별"
        return number % 2 == 0

    def calculate_and_save(self, a, b, operation):
        "계산하고 기록 저장"
        if operation == 'add':
            result = self.add(a, b)
            self.add_to_history(f'{a} + {b}', result)
        elif operation == 'multiply':
            result = self.multiply(a, b)
            self.add_to_history(f'{a} x {b}', result)
        return result


# 객체 생성
cal1 = Calculator("계산기1")
cal2 = Calculator("계산기2")

# 정적 메서드 사용(인스턴스 없이도 호출 가능)
print(Calculator.add(5, 3))     # 8
print(Calculator.multiply(5, 3))  # 15
print(Calculator.is_even(10))   # True

# 인스턴스 메서드
result = cal1.calculate_and_save(10, 20, "add")
print(f'결과 : {result}')   # 결과 : 30

result = cal1.calculate_and_save(10, 20, "multiply")
print(f'결과 : {result}')   # 결과 : 200

# 클래스 메서드 사용
print(f'총 계산 횟수 : {Calculator.get_total_calculations()}')  # 총 계산 횟수 : 2


######################################################################################################
# 실습 2 클래스 변수, 메서드 연습

'''
User 클래스 구현
    - User 클래스를 정의하세요.
    - 인스턴스 변수 : username, points(초기값은 0)
    - 클래스 변수 : total_users(생성된 유저 수 저장)
    - 메서드
        - add_points(amount) : 포인트 증가
        - get_level() : 포인트 기준으로 레벨 반환
            0-99: Bronze, 100~499 : Silver, 500 이상 : Gold
        - 클래스 메서드
            - get_total_users() : 총 유저 수 출력
'''


class User:
    # 생성된 유저 수
    total_users = 0

    def __init__(self, username):
        self.username = username
        self.points = 0

        User.total_users += 1

    def add_points(self, amount):
        self.points += amount

    def get_level(self):

        if 0 <= self.points < 100:
            return "Bronze"
        elif 100 <= self.points < 500:
            return "Silver"
        else:
            return "Gold"

    @classmethod
    def get_total_users(cls):
        print(f'총 유저 수 : {cls.total_users}명')

    @classmethod
    def __del__(cls):
        cls.total_users -= 1


user1 = User("김철수")
print(f'{user1.username} : {user1.get_level()}')    # 김철수 : Bronze
user1.add_points(500)
print(f'{user1.username} : {user1.get_level()}')    # 김철수 : Gold

user2 = User("이영희")
print(f'{user2.username} : {user2.get_level()}')    # 이영희 : Bronze

User.get_total_users()  # 총 유저 수 : 2명


######################################################################################################
# 접근 제어와 정보 은닉

'''
정보 은닉
    - 객체의 내부 상태(데이터)를 외부에서 직접 접근하지 못하도록 막고, 공개된 메서드를 통해서만 접근하도록 제한하는 것
    - 데이터 무결성 보호, 코드 안정성 향상에 기여
캡슐화
    - 객체가 자신의 속성과 메서드를 하나로 묶고, 외부에는 필요한 부분만 공개하는 것
    - 정보 은닉은 캡슐화의 하위 개념으로 실현 방법 중 하나임

* 파이썬의 접근 수준 구분

접근 수준       문법 예     의미
public(공개)    name        어디서나 접근 가능
protected(보호) _name       클래스 내부 및 자식 클래스에서 사용 권장
private(비공개) __name      클래스 외부 접근 금지(이름 맹글링 적용됨)

    - 파이썬은 접근 제어 키워드가 없음 → 접두어 명명 규칙을 따름
    - 이름 맹글링(name mangling) : 파이썬 클래스에서 변수 이름을 일부 자동 변경하는 규칙
                                클래스 내부에서 변수의 접근 범위를 제한하기 위해 사용
                                상속 시 변수 충돌 방지
                                진짜 private 변수는 아니고 단순한 네이밍 규칙
    
'''
'''
접근 제어자
    객체 지향 프로그래밍에서 클래스의 멤버(속성, 메서드)에 대한 접근 권한을 제어하는 매커니즘
'''
'''
    * 파이썬의 철학
        프로그래머를 신뢰하는 철학을 가짐
        강제적 제한보다는 컨벤션과 문서화를 중시
        필요하다면 모든 것에 접근 가능(하지말아야 할 것을 명확히 표시)
'''


class MyClass:
    def __init__(self):
        self.__secret = 42  # 이름 맹글링 발생


obj = MyClass()
# print(obj.__secret)  # ❌ AttributeError 발생
print(obj._MyClass__secret)


class Parent:
    def __init__(self):
        self.__value = 100


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__value = 200  # Parent.__value와 충돌하지 않음


c = Child()
print(c._Parent__value)  # 100
print(c._Child__value)   # 200


'''
public 멤버
    클래스 외부에서 자유롭게 접근 가능
    파이썬에서 일반적으로 정의한 인스턴스 변수는 기본적으로 모두 public
'''


class Person:
    def __init__(self, name, age):
        self.name = name    # public
        self.age = age      # public


p = Person("지민", 25)
print(p.name)   # 지민
print(p.age)    # 25

p.name = "철수"
print(p.name)   # 철수  # 직접 수정 가능


class Car:
    def __init__(self, brand, model):
        self.brand = brand  # public 속성
        self.model = model  # public 속성
        self.speed = 0  # public 속성

    def accelerate(self, amount):  # public 메서드
        '''외부에서 자유롭게 호출 가능'''
        self.speed += amount
        return f'속도가 {self.speed}km/h가 되었습니다.'

    def get_info(self):  # public 메서드
        return f'{self.brand} {self.model}'


print()
# 객체 생성
car = Car('tesla', 'model 3')
print(car.model)  # 정상 접근
print(car.brand)  # 정상 접근
print(car.get_info())  # 정상 호출
car.speed = 200  # 직접 수정 가능

'''
protected 멤버
    외부에서는 직접 접근하지 않는 것을 권장
        _변수명으로 표현
        보호 수준을 명시적으로 표현하기 위한 개발자 간 약속
        외부에서의 직접 접근은 가능 → 캡슐화를 깨뜨리는 행위로 간주되며 권장되지 않음
'''


class User:
    def __init__(self, name):
        self._nickname = name   # protected


class Admin(User):
    def show_nickname(self):
        print(self._nickname)


a = Admin("관리자")
a.show_nickname()   # 관리자
print(a._nickname)  # 기능은 하지만 권장되지 않음

'''
private 멤버
    클래스 외부에서 직접 접근 불가
        __변수명으로 표현(underscore 두 번)
        네임 맹글링(name mangling)
            - 내부적으로 _{클래스명}__변수명으로 이름이 변경되어 접근을 어렵게 함
            - _{클래스명}__변수명으로 접근할 수 있지만 권장되지 않음
'''


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance    # private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


acc = BankAccount("지민", 10000)
print(acc.get_balance())    # 10000
# print(acc.__balance)    # AttributeError 발생
print(acc._BankAccount__balance)    # 기능은 하지만 권장 X


class SecuritySystem:
    def __init__(self, password):
        self.__password = password
        self.__security_level = 'High'
        self.__failed_attmepts = 0

    # private method
    def __encrypt_password(self, pwd):
        "내부적으로만 사용되는 암호화 메서드"
        return pwd[::1] + 'encrypted'

    # private method
    def __check_security(self):
        "내부 보안 체크"
        return self.__failed_attmepts < 3

    # public method
    def authenticate(self, password):
        if not self.__check_security():  # private 메서드 호출
            return "계정이 잠겼습니다."

        # 인자로 받은 password를 암호화
        encrypted = self.__encrypt_password(password)

        # 이미 암호화된 password 비교
        if encrypted == self.__encrypt_password(self.__password):
            self.__failed_attmepts = 0
            return "인증 성공"
        else:
            self.__failed_attmepts += 1
            return f'인증 실패 {self.__failed_attmepts}/3'


security = SecuritySystem("1234")
# print(security.__password)  # 에러 발생
# security.__check_security() # 에러발생

print(security.authenticate("1212"))    # 인증 실패 1/3
print(security.authenticate("1212"))    # 인증 실패 2/3
print(security.authenticate("1212"))    # 인증 실패 3/3
print(security.authenticate("1234"))    # 계정이 잠겼습니다.

print(security._SecuritySystem__password)   # 기능은 하지만 권장하지 않음

'''
@property 데코레이터
    메서드를 속성처럼 사용할 수 있도록 만들어주는 파이썬의 내장 데코레이터
        주로 캡슐화된(private) 인스턴스 변수에 접근하거나 수정할 때, 메서드 호출처럼 보이지 않게 하면서 내부 로직을 수정할 수 있도록 도와줌
        외부에는 속성처럼 보이게 하면서, 내부에서는 함수 호출을 통한 유효성 검사 또는 부가처리를 하고 싶을 때 사용
'''


class ClassName:
    def __init__(self):
        self._value = 0  # 내부 변수

    @property
    def value(self):    # getter 역할
        return self._value

    @value.setter       # setter 역할
    def value(self, val):
        if val < 0:
            raise ValueError("음수는 허용되지 않습니다.")
        self._value = val


class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):  # getter
        return self.__celsius

    @celsius.setter
    def celsius(self, value):   # setter
        if value < -273.15:
            raise ValueError("절대 0도 이하일 수 없습니다.")
        self.__celsius = value


t = Temperature(25)
print(t.celsius)    # 25 (getter 호출)
t.celsius = 30
print(t.celsius)    # 30
# t.celsius = -300    # ValueError 발생


class Circle1:
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):  # 메서드로 접근
        return 3.14 * self.__radius ** 2

    def set_radius(self, radius):
        self.__radius = radius


class Circle2:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def area(self):  # 메서드로 접근
        return 3.14 * self.__radius ** 2

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius


c1 = Circle1(5)
print(c1.get_area())    # 78.5 # 메서드 호출하여 접근 : 괄호있음
c1.set_radius(10)
print(c1.get_area())    # 341.0

c2 = Circle2(4)
print(c2.area)  # 50.24 # 속성 접근: 괄호없음


######################################################################################################
# 게터(Getter) 와 세터(Setter)

'''
게터(Getter) : 객체 내부의 속성 값을 읽을 수 있도록 외부에 제공하는 메서드
세터(Setter) : 객체 내부의 속성 값을 변경할 수 있도록 외부에 제공하는 메서드

→ 외부에서 직접 변수에 접근하지 못하도록 하고, 메서드를 통해 접근할 때 사용
'''


class Temperature:
    def __init__(self):
        self.__celsius = 0

    # setter
    def set_celsius(self, value):
        if value < -273.15:
            raise ValueError("절대 0도 이하일 수 없습니다.")
        self.__celsius = value
    # getter

    def get_celsius(self):
        return self.__celsius

    '- 실수로 잘못된 값을 설정하지 않도록 검증 로직 포함 가능'


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        "print() 함수 호출 시"
        return f'Vector (x = {self.x} y = {self.y})'

    def __repr__(self):
        "개발자를 위한 문자열 표현"
        return f'Vector (x = {self.x} y = {self.y})'

    # 오버로딩
    def __add__(self, other):
        "+연산 오버로딩"
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __eq__(self, other):
        return self.x == other.x or self.y == other.y

    def __len__(self):
        "len() 함수 호출 시"
        return int((self.x ** 2 + self.y ** 2) ** 0.5)


v1 = Vector(3, 4)
v2 = Vector(1, 4)

print(v1)       # Vector (x = 3 y = 4) # __str__ 호출
print(repr(v1))   # Vector (x = 3 y = 4) # __str__ 호출

v3 = v1 + v2
print(v3)   # Vector (x = 4 y = 8)

print(len(v1))  # 5

v4 = v1 - v2
print(v4)   # Vector (x = 2 y = 0)

print(v1 == v2)  # True

######################################################################################################
# 실습 3 접근 제어와 정보은닉 연습
'''
1. UserAccount 클래스 : 비밀번호 보호
    - UserAccount 클래스를 정의하세요.
    - 인스턴스 변수 
        - username : 사용자 이름
        - __password : private 변수, 비밀번호
    - 생성자에서 사용자 이름과 비밀번호를 초기화하세요.
    - 다음 메서드를 정의하세요.
        - change_password(old_pw, new_pw) : 현재 비밀번호가 old_pw와 같을 때만 변경 허용, 틀리면 "비밀번호 불일치" 출력
        - check_password(password) : 비밀번호 일치 여부를 반환(True/False)
'''


class UserAccount:

    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def change_password(self, old_pw, new_pw):
        if self.check_password(old_pw):
            self.__password = new_pw
            return "비밀번호가 변경되었습니다."
        else:
            return "비밀번호 불일치"

    def check_password(self, password):
        if self.__password == password:
            return True
        return False


user1 = UserAccount("김철수", "1234")
print(user1.check_password("1212"))     # False
print(user1.check_password("1234"))     # True
print(user1.change_password("1234", "4567"))    # 비밀번호가 변경되었습니다.


'''
2. Student 클래스 : 성적 검증(@property 사용)
    - Student 클래스를 정의하세요.
    - 인스턴스 변수 __score는 private로 선언합니다.
    - score에 대한 getter/setter를 @property를 사용하여 정의하세요.
        - 점수는 0이상 100이하만 허용되며, 범위를 벗어나면 ValueError를 발생시킵니다.(raise ValueError 사용)
'''


class Student:

    def __init__(self, score):
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score_setter(self, score):
        if 0 <= self.score <= 100:
            self.__score = score
        else:
            raise ValueError("0이상 100이하의 점수만 허용됩니다.")

    # def get_score(self):
    #     return self.__score

    # def set_score(self, score):
    #     if 0 <= score <= 100:
    #         self.__score = score
    #     else:
    #         raise ValueError("0이상 100이하의 점수만 허용됩니다.")

######################################################################################################
# 상속과 오버라이딩


'''
상속(Inheritance)의 개념과 필요성
    기존에 정의된 클래스의 속성과 메서드를 물려받아 새로운 클래스를 만드는 것
        - 코드의 재사용성을 높임
        - 공통된 기능은 부모 클래스에 정의하고, 자식 클래스에서 확장하거나 수정

        - 자식클래스는 부모클래스의 모든 것을 물려받음
        - 부모의 모든 속성과 메서드 사용 가능
        - 부모클래스가 자식클래스를 사용할 순 없음

    * 기본 문법
    class Parent:
        # 부모 클래스 정의
        ...
    class Child(Parent):
        # 자식 클래스, Parent로부터 상속
        ...
'''


class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")


class Dog(Animal):
    pass


d = Dog()
d.speak()   # 동물이 소리를 냅니다.

'''
super()를 사용한 부모 생성자 호출

    super() : 부모 클래스의 메서드나 생성자를 호출할 수 있도록 해주는 내장 함수
        - 자식 클래스에서 부모 클래스의 메서드, 생성자, 속성을 명시적 클래스명없이 호출할 때 사용
        - 코드의 유연성과 유지보수성 향상
    * 기본 문법
        super().메서드명()

        - 자식 클래스 안에서 super() 호출
            → 상속 계층에서 다음 클래스의 메서드를 자동으로 찾아서 호출
        - 보통은 생성자에서 super().__init__() 형태로 많이 사용
    * 사용 시 주의사항
        - super()는 반드시 클래스 내부 메서드에서 사용해야 함
        - 생성자에서 super().__init__()를 호출하지 않으면 부모 생성자가 생략됨
        - super().__init__()는 Parent.__init__(self)를 직접 호출하는 것과 유사하지만
            상속 구조가 변경되어도 자동 추적되므로 안전함
'''


class Parent:
    def __init__(self):
        print("부모 생성자 호출")


class Child(Parent):
    def __init__(self):
        super().__init__()  # 부모 생성자 호출
        print("자식 생성자 호출")


c = Child()  # 부모 생성자 호출
# 자식 생성자 호출


class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")


class Dog(Animal):
    def speak(self):
        super().speak()  # 부모 메서드 호출
        print("멍멍!")


d = Dog()
d.speak()   # 동물이 소리를 냅니다.
# 멍멍!

'''
매서드 오버라이딩(Overriding)
    - 부모 클래스의 메서드를 자식 클래스에서 동일한 이름으로 다시 정의하는 것(상속 관계)
    - 런타임(동적 바인딩)
    - 기존 기능을 새로운 방식으로 변경하거나 특화된 동작을 구현할 수 있음
    - 조건
        메서드 이름 같음
        매개변수 목록 같음
        리턴 타입이 같거나 부모보다 더 구체적일 수 있음
        접근 제어자는 부모보다 좁아질 수 없음
        JAVA에선 @Override 애너테이션 권장
'''


class Animal:
    def speak(self):
        print("동물이 소리를 냅니다.")


class Cat(Animal):
    def speak(self):    # 오버라이딩
        print("야옹!")


c = Cat()
c.speak()   # 야옹!

'- Cat 클래스는 Animal의 speak()을 덮어씀(override)'

'''
메서드 오버로딩(Overloading)
    - 같은 이름의 메서드를 여러 개 정의하는 것(매개변수 개수 혹은 타입이 다름)
    - 컴파일 타임(정적 바인딩)
    - 조건
        메서드 이름이 같음
        매개변수의 개수 또는 타입이 달라야 함
        리턴 타입만 다른 것은 불가능함
'''

# 사용 예제 - (JAVA 예시)
# class Calculator {
#     int add(int a, int b) {
#         return a + b;
#     }

#     double add(double a, double b) {  // 같은 이름, 다른 매개변수 타입
#         return a + b;
#     }

#     int add(int a, int b, int c) {    // 같은 이름, 다른 매개변수 개수
#         return a + b + c;
#     }
# }

'- Python은 전통적인 오버로딩 개념이 없음'
'   동적 타입 언어이기 때문에 같은 이름의 함수를 여러 개 정의할 시, 마지막 정의만 남기 때문'

'''
1️⃣ 기본 인자(Default Arguments) 활용
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

c = Calculator()
print(c.add(2, 3))      # 2 + 3 = 5
print(c.add(2, 3, 4))   # 2 + 3 + 4 = 9
print(c.add(5))         # 5 + 0 + 0 = 5


👉 매개변수 개수에 따라 다른 방식으로 동작 → 오버로딩 효과

2️⃣ 가변 인자(*args, **kwargs) 활용
class Calculator:
    def add(self, *args):
        return sum(args)

c = Calculator()
print(c.add(1, 2))            # 3
print(c.add(1, 2, 3, 4, 5))   # 15


👉 매개변수 개수를 자유롭게 받아 처리 → 자바의 오버로딩과 비슷한 효과

3️⃣ functools.singledispatch (표준 라이브러리) 활용

👉 매개변수 타입에 따라 다른 함수 실행 가능

from functools import singledispatch

@singledispatch
def process(value):
    raise NotImplementedError("지원하지 않는 타입입니다.")

@process.register(int)
def _(value):
    return f"정수 처리: {value * 2}"

@process.register(str)
def _(value):
    return f"문자열 처리: {value.upper()}"

@process.register(list)
def _(value):
    return f"리스트 처리: 길이 {len(value)}"

print(process(10))         # 정수 처리: 20
print(process("hello"))    # 문자열 처리: HELLO
print(process([1, 2, 3]))  # 리스트 처리: 길이 3


👉 자바/씨++의 오버로딩과 가장 유사한 방식
'''


'''
* 오버로딩 vs 오버라이딩

구분	    오버로딩(Overloading)	    오버라이딩(Overriding)
관계	    같은 클래스 내	            상속 관계 (부모 ↔ 자식)
조건	    매개변수 다름	            매개변수 동일
리턴 타입	달라도 무방
            (단, 매개변수만으로 
            구분 가능해야 함)	        같거나 더 구체적
시점	    컴파일 타임	런타임
목적	    메서드 이름 재사용	        부모 메서드 기능 재정의
'''

######################################################################################################
# 실습 4 상속과 오버라이딩 연습

'''
1. Shape 클래스 오버라이딩
[Shape 클래스 조건]
- 생성자를 통해 다음 두 값을 초기화하세요
    - sides : 변의 개수
    - base : 밑변의 길이
- printInfo() 메서드를 정의하여 다음과 같이 출력
    - 변의 개수 : 4
    - 밑변의 길이 : 10
- area() 메서드를 정의하여 "넓이 계산이 정의되지 않았습니다." 라는 메시지 출력
    → 자식 클래스에서 이 메서드를 오버라이딩해야 합니다.

[Rectangle 클래스 조건]
- Shape을 상속받습니다.
- 생성자에서 sides, base, height을 모두 초기화합니다.
- area() 메서드를 오버라이딩하여 base * height 값을 출력합니다.

[Triangle 클래스 조건]
- Shape을 상속받습니다.
- 생성자에서 sides, base, height을 모두 초기화합니다.
- area() 메서드를 오버라이딩하여 base * height / 2 값을 출력합니다.
'''


class Shape:
    def __init__(self, sides, base):
        self.sides = sides
        self.base = base

    def printInfo(self):
        return f'변의 개수 : {self.sides}\n밑변의 길이 : {self.base}'
    '- print() return 시, 함수는 None을 리턴하여 출력된다.'

    def area(self):
        return "넓이 계산이 정의되지 않았습니다."


class Rectangle(Shape):
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height

    def area(self):
        return int(self.height) * int(self.base)


class Triagle(Shape):
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height

    def area(self):
        return int(self.height) * int(self.base) / 2


r = Rectangle(3, 4, 5)
print(r.printInfo())    # 변의 개수 : 3
# 밑변의 길이 : 4
print(r.area())  # 20

t = Triagle(3, 4, 5)
print(t.printInfo())    # 변의 개수 : 3
# 밑변의 길이 : 4
print(t.area())  # 10.0
print(super(Triagle, t).area())  # 넓이 계산이 정의되지 않았습니다.
print(Shape.area(t))            # 넓이 계산이 정의되지 않았습니다.

######################################################################################################
# 추상 클래스

'''
직접 인스턴스(객체)를 만들 수 없으며, 반드시 자식 클래스에서 구현을 완성해야 하는(미완성) 클래스
    공통적인 구조는 정의하되, 구체적인 동작은 상속받은 클래스에서 구현하도록 강제하는 용도로 사용

* 추상 클래스의 목적
    - 공통 인터페이스 정의 : 모든 하위 클래스가 따라야 할 메서드 구조 정의
    - 일관성 유지 : API나 프레임워크의 통일된 동작 보장
    - 구현 강제 : 필수 메서드를 구현하지 않으면 오류 발생
    - 코드 재사용 + 설계 명확화 : 일부 구현을 제공하면서도 확장 가능하도록 설계\

* 기본 문법
    from abc import ABC, abstractmethod

    class AbstractClassName(ABC):
    
        @abstractmethod
        def method_name(self):
            pass
    
    - 추상 클래스를 만들기 위해 abc(Abstract Base Classes) 모듈 사용
    - ABC를 반드시 상속해야 함
    - @abstractmethod가 붙은 메서드는 자식 클래스에서 반드시 구현해야 함
    
    ※ 추상 클래스는 직접 인스턴스화 불가능
'''
# 구현 구상 중 - 일반 상속만 하려고 했을 때


class Animal:
    def make_sound(self):
        pass    # 비어있음 - 구현을 깜빡할 수 있음


class Dog(Animal):
    def eat(self):
        print("강아지가 밥을 먹습니다.")


dog = Dog()
dog.make_sound()    # 아무것도 안 일어남 - 버그


# 구현 구상 중 - 추상 클래스 사용
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("멍멍!")


class Cat(Animal):
    def sound(self):
        print("야옹!")


animal = Animal()   # 에러 발생(추상 클래스이기 때문에 객체 생성 안됨)
dog = Dog()         # 추상 메서드를 구현했기 때문에 객체 생성됨
cat = Cat()         # 추상 메서드를 구현했기 때문에 객체 생성됨

dog.sound()  # 멍멍!
cat.sound()  # 야옹!

# 구현 구상 중 - 추상 클래스 사용 / 하위 클래스에서 구현하지 않을 시


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def __init__(self):
        print("멍멍!")


class Cat(Animal):
    def __init__(self):
        print("야옹!")


animal = Animal()   # 에러 발생 (추상 클래스이기 때문에 객체 생성 안됨)
dog = Dog()         # 에러 발생 (sound() 구현이 안되었기 때문)
cat = Cat()         # 에러 발생 (sound() 구현이 안되었기 때문)

'- Animal은 공통 인터페이스를 정의하고, 실제 구현은 하위 클래스에서 이루어짐'
'- 반드시 자식 클래스에서 추상 메서드를 구현해야 함'
'- 추상 클래스는 직정 객체 생성이 불가함'


class Shape(ABC):
    "추상 클래스"
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        # super().__init__()
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


# shape = Shape()   # 에러 발생
circle = Circle(5)
print(circle.area())    # 78.5


class Animal(ABC):
    "추상 클래스"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 일반 메서드 - 모든 동물이 공통으로 사용
    def sleep(self):
        print(f'{self.name}이(가) 잠을 잡니다.')

    def eat(self)
    print(f'{self.name}이(가) 먹이를 먹습니다.')

    # 추상 메서드 - 각 동물마다 다르게 구현
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):

    def make_sound(self):
        print(f'{self.name} : 멍멍!')

    def move(self):
        print(f'{self.name}이(가) 뛰어다닙니다.')


class Bird(Animal):

    def make_sound(self):
        print(f'{self.name} : 짹짹!')

    def move(self):
        print(f'{self.name}이(가) 날아다닙니다.')


dog = Dog("바둑이", 3)
bird = Bird("참새", 1)

dog.eat()       # 바둑이이(가) 먹이를 먹습니다.
bird.sleep()    # 참새이(가) 잠을 잡니다.

dog.make_sound()    # 바둑이 : 멍멍!
bird.move()         # 참새이(가) 날아다닙니다.

######################################################################################################
# 실습 5 추상 클래스 연습 문제

'''
추상 클래스 Payment 구현

- 추상 클래스 Payment를 정의하고, pay(amount)를 추상 메서드로 선언하세요. (abc 모듈 사용)
- CardPayment 클래스와 CashPayment 클래스는 Payment를 상속받아 pay() 메서드를 오버라이딩하세요.
    - Cardpayment : 카드로 {amount}원을 결제합니다. 출력
    - CashPayment : 현금으로 {amount}원을 결제합니다. 출력
'''


class Payment:

    @abstractmethod
    def pay(self):
        pass


class CardPayment(Payment):

    def __init__(self, amount):
        super().__init__()
        self.amount = amount

    def pay(self):
        return f'카드로 {self.amount}원을 결제합니다.'


class CashPayment(Payment):

    def __init__(self, amount):
        super().__init__()
        self.amount = amount

    def pay(self):
        return f'현금으로 {self.amount}원을 결제합니다.'


card = CardPayment(10000)
cash = CashPayment(30000)

print(card.pay())   # 카드로 10000원을 결제합니다.
print(cash.pay())   # 현금으로 30000원을 결제합니다.
