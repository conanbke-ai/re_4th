# 딕셔너리(Dict)

'''
하나의 키(Key)와 값(Value)을 쌍으로 묶어 데이터를 저장하는 자료형
    
    * 특징
        - 키-값 쌍 구조(Key-Value)
        - 키는 유일해야 함, 값은 중복 가능
        - 순서 보장(Python 3.7이상 부터)
        - 변경 가능
    * 장점
        - 빠른 검색 : 키를 통해 값을 매우 빠르게 찾을 수 있음(해시 기반)
        - 명확한 구조 : 각 항목이 어떤 의미를 가지는지 명확함(Key로 의미 부여 가능)
        - 확장성과 유연성 : JSON과의 호환성이 뛰어나고, 다양한 자료구조 표현 가능
'''

######################################################################################################
# Dict 기본 문법

# 딕셔너리 생성방법 1
# 방법 1 중괄호 {} 사용
person = {
    "name": "Alice",
    "age": 25
}

'- 키는 문자열일 필요는 없으나, 문자열이 가장 일반적'
'- 키에는 불변 자료형만 사용할 수 있음(문자열, 숫자, 튜플 등)'

# 방법 2 dict() 생성자 사용
person = dict(name="Alice", age=25)

'- 함수 호출 방식으로 딕셔너리를 생성'
'- 키는 문자열이어야 하고, 변수 이름처럼 쓸 수 있는 형식이어야함'

# 사용 예제
# 키로 정수 사용
num_dict = {1: "one", 2: "two"}

# 키로 튜플 사용
coord_dict = {(0, 0): "origin", (1, 2): "point A"}

# 리스트를 키로 사용한 경우, 에러 발생
my_dict = {
    [1, 2, 3]: "value"  # 리스트는 변경 가능한 객체이므로 키로 사용 불가
}

# 리스트나 튜플의 쌍으로부터 생성
pairs = [("name", "Bob"), ("age", 22), ("city", "Busan")]
person = dict(pairs)
print(person)   # {'name': 'Bob', 'age': 22, 'city': 'Busan'}

'- (key, value) 형태의 쌍을 요소로 가지는 리스트 또는 튜플을 통해 딕셔너리를 만들 수 있음'
'- CSV 데이터 파싱 또는 키-값 쌍 리스트를 가공할 때 유용하게 사용됨'

# zip() 함수와 함께 사용

keys = ["name", "age", "city"]
values = ["Charlie", 28, "Incheon"]

info = dict(zip(keys, values))
print(info)  # {'name': 'Charlie', 'age': 28, 'city': 'Incheon'}

'- 서로 대응되는 두 리스트(혹은 이터러블)을 묶어서 딕셔너리 생성 가능'

'''
딕셔너리 데이터 접근(1)
    딕셔너리 값을 가져올 때는 키(Key)를 사용하여 접근함
        - 대괄호 []를 사용하는 방식(일반적)
        - get() 메서드를 사용하는 방식(안전)
'''

# 사용 예제
person = {
    "name": "Alice",
    "age": 30,
    "city": "Seoul"
}

print(person["name"])   # Alice
print(person["email"])  # 에러 발생 : KeyError: 'email'

'- 존재하는 키에 접근하여 값을 반환'
'- 존재하지 않는 키에 접근하면 KeyError 예외 발생'


print(person.get("name"))   # Alice
print(person.get("email"))  # None(에러 X)
print(person.get("email", "없음"))  # 없음(기본 값 제공)

'- get(key)는 키가 없을 경우 None을 반환'
'- get(key, default)를 사용하면 기본값을 직접 지정할 수 있어 KeyError 발생 방지 가능'
'   : 사용자의 입력이나 외부 API 데이터 등 불확실한 키 접근에 유리함'

# 사용자 입력 처리
user_data = {
    "username": "student01",
    "email": "student@example.com"
}

# 사용자가 요청한 키
key = input("확인할 정보를 입력하세요 (username, email, phone): ")

# 안전하게 접근
value = user_data.get(key, "해당 정보 없음")

print(value)

# 확인할 정보를 입력하세요 (username, email, phone): username
# student01

# 확인할 정보를 입력하세요 (username, email, phone): email
# student@example.com

# 확인할 정보를 입력하세요 (username, email, phone): phone
# 해당 정보 없음

# 딕셔너리 데이터 추가 및 수정
'''
파이썬 딕셔너리에서 데이터의 추가와 수정은 동일한 문법을 사용함
    만약 해당 키가 존재하지 않을 시, 새로운 항목 추가
    이미 존재하는 키일 시, 해당 키의 값이 수정

    * 기본 문법
        딕셔너리[키] = 값
'''

# 사용 예제
user = {
    "username": "student01",
    "email": "student@example.com"
}

# phone 이라는 새로운 키 추가
user["phone"] = "010-0000-0000"

# email의 값 수정
user["email"] = "new_email@example.com"

print(user)
# {'username': 'student01', 'email': 'new_email@example.com', 'phone': '010-0000-0000'}

# update() 메서드 사용
user.upate({
    "email": "update@example.com",
    "nickname": "codeMaster"
})

# 키가 문자열인 경우 인자 전달 가능
user.update(phone="010-1234-5678", level=3)

# 또는 딕셔너리 전달
extra = {
    "grade": "A",
    "active": True
}

user.update(extra)

print(user)
# {'username': 'student01', 'email': 'update@example.com', 'phone': '010-1234-5678', 'nickname': 'codeMaster', 'level': 3, 'grade': 'A', 'active': True}

'- 내부적으로는 각 키마다 dict[key] = value를 반복하는 것과 동일'

# del 키워드 사용
person = {
    "name": "Alice",
    "age": 30,
    "city": "Seoul"
}

del person["age"]   # age 항목 삭제
del person["email"]  # KeyError: 'email'
print(person)   # {'name': 'Alice', 'city': 'Seoul'}

del person  # person 객체 자체 삭제

# pop() 메서드 사용
person = {"name": "Bob", "age": 25}

age = person.pop("age")
print(age)  # 25
print(person)   # {'name': 'Bob'}
print(person.pop("email", "해당 키 없음"))  # 해당 키 없음

'- 지정한 키를 삭제하고 삭제된 값을 반환'
'- 존재하지 않는 키를 삭제하면 KeyError 발생 → 두번째 인자에 값을 넣으면 기본값 출력 가능'

# popitem() 메서드 사용
person = {
    "name": "Tom",
    "age": 32,
    "city": "Busan"
}

last_item = person.popitem()
print(last_item)    # ('city', 'Busan')
print(person)   # {'name': 'Tom', 'age': 32}

'- 가장 마지막에 추가된 항목을 제거하고 (key, value) 쌍 반환(Python 3.7+에서만 순서 보장)'
'- 딕셔너리가 비어있을 때 호출하면 KeyError 발생'

# clear() 메서드 사용
person = {
    "name": "Anna",
    "email": "anna@example.com"
}
person.clear()
print(person)   # {}

'- 딕셔너리 안의 모든 항목을 한번에 삭제'
'- 객체 자체는 유지됨'

######################################################################################################
# Dict 기본 메서드

# keys() - 모든 키를 반환
person = {
    "name": "Alice",
    "age": 30
}

print(person.keys())    # dict_keys(['name', 'age'])
key_list = list(person.keys())  # 리스트로 변환

'- dict_keys 객체를 반환함(리스트처럼 보이지만 실제 리스트는 X)'
'- 리스트로 변환하고 싶다면 list() 함수로 변환'

# values() - 모든 값을 반환
print(person.values())  # dict_values(['Alice', 30])
value_list = list(person.values())  # 리스트로 변환

'- dict_values 객체를 반환함(리스트처럼 보이지만 실제 리스트 X)'
'- 리스트로 변환하고 싶다면 list() 함수로 변환'

# items() - 모든 (키, 값) 쌍 반환
print(person.items())   # dict_items([('name', 'Alice'), ('age', 30)])
item_list = list(person.items())    # 리스트로 변환

'- dict_values 객체를 반환함(리스트처럼 보이지만 실제 리스트 X)'
'- 리스트로 변환하고 싶다면 list() 함수로 변환'

######################################################################################################
# 실습 1 딕셔너리 종합 연습 문제

'''
1. 딕셔너리 핵심 개념 통합 실습
    a. 빈 딕셔너리 생성 : user 라는 이름의 빈 딕셔너리를 생성하세요.
    b. 사용자 기본 정보 추가
        - "username" : "skywalker"
        - "email" : "sky@example.com"
        - "level" : 5
    c. 값 읽기 : "email" 값을 변수 email_value 저장하고 출력하세요.
    d. 값 수정 : "level" 값을 6으로 수정하세요.
    e. 안전하게 키 조회 : 딕셔너리에 "phone"키가 없다면 "미입력"이라는 문자열을 출력하도록 하세요.
        - update()를 사용해 "nickname": "sky" 항목을 추가하세요.
        - "email" 항목을 삭제하세요.
        - "signup_date" 키가 없다면 "2025-07-10" 으로 추가하세요.(setdefault() 사용)
        - 최종 user 딕셔너리를 출력하세요.
'''

# 빈 딕셔너리 생성
user = {}
# 사용자 기본 정보 추가
user = {"username": "skywalker",
        "email": "sky@example.com",
        "level": 5
        }
# email 값 할당
email_value = user.get("email")
print(email_value)  # sky@example.com

# level 값 수정
user["level"] = 6

# 키 없을 시,
user.get("phone", "미입력")
print(user.get("phone", "미입력"))  # 미입력

# update 사용하여 수정
user.update(nickname="sky")

# 요소 제거
user.pop("email")
user.update(signup_date="2025-07-10")

# 최종 결과값 출력
print(user)
# {'username': 'skywalker', 'level': 6, 'nickname': 'sky', 'signup_date': '2025-07-10'}

'''
2. 학생 점수 관리
    a. 빈 딕셔너리 students를 생성한다.
    b. "Alice", "Bob", "Charlie" 세 학생의 점수를 각가 85, 90, 95 로 추가한다.
    c. "David" 학생의 점수(80)를 추가한다.
    d. "Alice"의 점수를 88로 수정한다.
    e. "Bob"을 딕셔너리에서 삭제한다.
    f. 최종 students 딕셔너리를 출력한다.
'''

# 빈 딕셔너리 생성
students = {}

# 학생 이름
student = {"Alice", "Bob", "Charlie"}
# 학생 점수
score = {85, 90, 95}

# 딕셔너리 변환
students = dict(zip(student, score))
# 중간 결과 출력
print(f'1. 원래 점수 : {students}')

# 정보 수정
students.update(David=80)
students.update(Alice=88)
del students["Bob"]

# 최종 결과 출력
print(f'2. 수정된 점수 : {students}')
