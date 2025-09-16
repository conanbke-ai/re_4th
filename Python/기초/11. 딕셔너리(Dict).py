# 딕셔너리(Dict)

'''
하나의 키(Key)와 값(Value)을 쌍으로 묶어 데이터를 저장하는 자료형
    
    * 특징
        - 키-값 쌍 구조(Key-Value)
        - 키는 유일해야 함(고유성), 값은 중복 가능
        - 순서 보장(Python 3.7이상 부터)
        - 변경 가능 : 요소 추가, 수정, 삭제 가능
    * 장점
        - 빠른 검색 : 키를 통해 값을 매우 빠르게 찾을 수 있음(해시 테이블 기반)(O(1))
        - 명확한 구조 : 각 항목이 어떤 의미를 가지는지 명확함(Key로 의미 부여 가능)
        - 확장성과 유연성 : JSON과의 호환성이 뛰어나고, 다양한 자료구조 표현 가능
'''

######################################################################################################
# Dict 기본 문법

# 딕셔너리를 사용하지 않는 경우 - 두 개의 리스트로 관리 (비효율적)
import copy
student_ids = ["20230001", "20230002", "20230003"]
student_names = ["김철수", "이영희", "박민수"]

print("리스트로 관리하는 경우:")
print(f"학번 리스트: {student_ids}")
print(f"이름 리스트: {student_names}")

# 특정 학번의 이름을 찾으려면? (비효율적 - O(n) 시간복잡도)
target_id = "20230002"
if target_id in student_ids:  # 전체 리스트를 순차 검색
    index = student_ids.index(target_id)  # 또 다시 순차 검색 O(n)
    name = student_names[index]
    print(f"학번 {target_id}의 이름: {name}")

# 딕셔너리를 사용하는 경우 - 직관적이고 빠름 (O(1) 시간복잡도)
students = {
    "20230001": "김철수",
    "20230002": "이영희",
    "20230003": "박민수"
}

print(f"\n딕셔너리로 관리: {students}")
print(f"학번 20230002의 이름: {students['20230002']}")  # O(1) - 즉시 접근!

# 특징 확인 예시
sample_dict = {"a": 1, "b": 2, "a": 3}  # 중복 키 - 마지막 값으로 덮어씀
print(f"\n중복 키 처리: {sample_dict}")  # {'a': 3, 'b': 2}

# 순서 보장 확인 (Python 3.7+)
ordered_dict = {"첫번째": 1, "두번째": 2, "세번째": 3}
# 순서 보장 확인: ['첫번째', '두번째', '세번째']
print(f"순서 보장 확인: {list(ordered_dict.keys())}")

# 딕셔너리 생성방법
# 방법 1 중괄호 {} 사용 / 리터럴 방식

person = {
    "name": "Alice",
    "age": 25
}

'- 키는 문자열일 필요는 없으나, 문자열이 가장 일반적'
'- 키에는 불변 자료형만 사용할 수 있음(문자열, 숫자, 튜플 등)'

# 방법 2 dict() 생성자 사용 / 키워드 인자
person = dict(name="Alice", age=25)

'- 함수 호출 방식으로 딕셔너리를 생성'
'- 키는 문자열이어야 하고, 변수 이름처럼 쓸 수 있는 형식이어야함'

# 방법 3 리스트/튜플 쌍으로부터 생성
pairs = [('a', 1), ('b', 2), ('c', 3)]  # 리스트의 튜플들
dict_from_pairs = dict(pairs)
print(f"쌍에서 생성된 딕셔너리: {dict_from_pairs}")

# 튜플의 튜플로도 가능
tuple_pairs = (('x', 10), ('y', 20), ('z', 30))
dict_from_tuples = dict(tuple_pairs)
print(f"튜플 쌍에서 생성: {dict_from_tuples}")

# 방법 4 zip()을 이용한 생성 (매우 유용!)
keys = ['name', 'age', 'city']
values = ['박민수', 21, '대전']
person3 = dict(zip(keys, values))  # 두 리스트를 쌍으로 묶어서 딕셔너리 생성
print(f"zip으로 생성: {person3}")

# 방법 5 Dictionary Comprehension (고급 기법)
squares = {x: x**2 for x in range(1, 6)}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(f"comprehension으로 생성: {squares}")

# 조건부 comprehension
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"조건부 comprehension: {even_squares}")

# 방법 6 fromkeys() 메서드 - 같은 기본값으로 초기화
keys = ['a', 'b', 'c']
default_dict = dict.fromkeys(keys, 0)  # 모든 키에 0으로 초기화
# fromkeys로 생성: {'a': 0, 'b': 0, 'c': 0}
print(f"fromkeys로 생성: {default_dict}")

# 주의: 가변 객체를 기본값으로 사용할 때
# wrong_way = dict.fromkeys(['a', 'b'], [])  # 모든 키가 같은 리스트를 참조!
# 올바른 방법은 comprehension 사용
right_way = {key: [] for key in ['a', 'b']}  # 각각 다른 리스트 생성
print(f"올바른 초기화: {right_way}")    # 올바른 초기화: {'a': [], 'b': []}

# key로 사용 가능한 데이터 타입
# Hashable(해시 가능한) 타입만 key로 사용 가능 - 불변 타입들
valid_dict = {
    1: "정수",
    3.14: "실수",
    '문자열': 'string',
    (1, 2): "튜플",
    True: '불리언',  # True는 1과 같으므로 정수 키와 충돌 주의
    frozenset([1, 2]): "frozenset"
}
print(f"유효한 키 타입들: {valid_dict}")

# 키 충돌 예시 (True와 1은 같은 키로 취급)
collision_example = {1: "정수", True: "불리언"}
print(f"키 충돌 예시: {collision_example}")  # True가 1을 덮어씀

# Unhashable(해시 불가능한) 타입은 key로 사용 불가 - 가변 타입들
print("사용 불가능한 키 타입들:")
print("- 리스트: [1, 2]")
print("- 딕셔너리: {'a': 1}")
print("- 집합: {1, 2}")

# 다음 코드들은 TypeError를 발생시킵니다:
# invalid_dict = {[1, 2]: "리스트"}  # TypeError
# invalid_dict = {{1, 2}: "집합"}   # TypeError
# invalid_dict = {{'a': 1}: "딕셔너리"}  # TypeError

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
        - 대괄호 []를 사용하는 방식(일반적) - KeyError 발생 위험
        - get() 메서드를 사용하는 방식(안전) - 존재하지 않는 키 None 반환 / 기본값 지정 가능
        - setdefault() - 키가 없을 시, 기본값 설정하고 반환
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

# del 키워드 사용 - 값 반환 안함
person = {
    "name": "Alice",
    "age": 30,
    "city": "Seoul"
}

person_backup = person.copy()  # 백업 생성

del person["age"]   # age 항목 삭제
del person["email"]  # KeyError: 'email'
print(person)   # {'name': 'Alice', 'city': 'Seoul'}

del person  # person 객체 자체 삭제

# pop() 메서드 사용 - 값을 반환하면서 삭제
person = {"name": "Bob", "age": 25}

age = person.pop("age")
print(age)  # 25
print(person)   # {'name': 'Bob'}
print(person.pop("email", "해당 키 없음"))  # 해당 키 없음

'- 지정한 키를 삭제하고 삭제된 값을 반환'
'- 존재하지 않는 키를 삭제하면 KeyError 발생 → 두번째 인자에 값을 넣으면 기본값 출력 가능'

# popitem() 메서드 사용 - 마지막 항목 제거 (LIFO : Last In First Out)
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

# clear() 메서드 사용 - 모든 요소 제거
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

# fromkeys() - value 값 지정
keys = ['a', 'b', 'c']
default_dict = dict.fromkeys(keys, 'A')
# default_dict {'a': 'A', 'b': 'A', 'c': 'A'}
print('default_dict', default_dict)

# setdefault() - key가 없으면 추가, 있으면 기존 값
person.setdefault("name", "Tom")    # 기존 값 변경
person.setdefault("city", "Seoul")  # 새로 추가
print(person)

# copy() - 얕은 복사 / 원본 값에 영향을 받음(원본 값 수정될 시 변함)
person_copy = person.copy()
person_copy["name"] = "Jerry"
person_copy["city"] = "Jinju"
print('person', person)
print('person_copy', person_copy)

# deepcopy() - 깊은 복사 / 원본 값에 영향을 받지 않음(원본 값 수정되어도 불변)
nested_dict = {
    # 팀 값을 딕셔너리로, 키 leader는 문자열을 값으로, 키 members는 리스트를 값으로 가짐
    "team1": {'leader': '김철수', 'members': ['이영희', '박민수']},
    "team2": {'leader': '정수진', 'members': ['최동훈', '강미나']}
}

# 얕은 복사
shallow = nested_dict.copy()
# 깊은 복사
deep = copy.deepcopy(nested_dict)

# 원본 값에 추가
nested_dict['team1']['members'].append('신입')

print('얕은 복사', shallow['team1']['members'])  # ['이영희', '박민수', '신입']
print('깊은 복사', deep['team1']['members'])  # ['이영희', '박민수']

# 순회
scores = {
    '김철수': 85,
    '이영희': 92,
    '박민수': 72
}

# 기본적인 키만 순회
for key in scores:
    print(f'{key}: {scores[key]}')

# 김철수: 85
# 이영희: 92
# 박민수: 72

# 명시적 키만 순회
for key in scores.keys():
    print(f'{key}: {scores[key]}')

# 김철수: 85
# 이영희: 92
# 박민수: 72

# 값만 순회
for value in scores.values():
    print(f'value: {value}')

# value: 85
# value: 92
# value: 72

# 평균값 계산
average = sum(scores.values()) // len(scores)
print(f'average = {average}')   # average = 83

# 키 - 값 쌍 순회 - 가장 일반적
for key, value in scores.items():
    print(f'{key}: {value}')

# 김철수: 85
# 이영희: 92
# 박민수: 72

# enumerate(start: int=0) - 인덱스와 함께 순회
for idx, (key, value) in enumerate(scores.items(), 1):
    print(f'{idx}번째 {key} : {value} 점')

# 1번째 김철수 : 85 점
# 2번째 이영희 : 92 점
# 3번째 박민수 : 72 점

# 중첩 딕셔너리
students_db = {
    "20230001": {
        "name": "김철수",
        "age": 20,
        "grades": {"수학": 90, "영어": 85, "과학": 92}
    },
    "20230002": {
        "name": "이영희",
        "age": 19,
        "grades": {"수학": 95, "영어": 88, "과학": 90}
    }
}

# 중첩 딕셔너리 접근
student_id = "20230001"
student_name = students_db[student_id]["name"]
math_grade = students_db[student_id]["grades"]["수학"]
print(f"학생 {student_id}의 이름: {student_name}")  # 학생 20230001의 이름: 김철수
print(f"수학 점수: {math_grade}")                   # 수학 점수: 90

# 안전한 중첩 접근
english_grade = students_db.get(student_id, {}).get(
    "grades", {}).get("영어", "점수 없음")
print(f"영어 점수: {english_grade}")                # 영어 점수: 85

# 딕셔너리 병합 (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
# merged = dict1 | dict2  # Python 3.9+
merged = {**dict1, **dict2}  # 이전 버전에서도 동작
# 딕셔너리 병합: {'a': 1, 'b': 3, 'c': 4}
print(f"딕셔너리 병합: {merged}")

# 조건부 딕셔너리 생성
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = {num: num**2 for num in numbers if num % 2 == 0}
# 짝수의 제곱: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
print(f"짝수의 제곱: {even_squares}")

# 딕셔너리 뒤집기 (키-값 교환)
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {value: key for key, value in original.items()}
# 뒤집힌 딕셔너리: {1: 'a', 2: 'b', 3: 'c'}
print(f"뒤집힌 딕셔너리: {reversed_dict}")

# 사용 예제
# 1) 카운터 구현
text = "hello world"
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
# 문자 카운터: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
print(f"문자 카운터: {char_count}")

# 더 간단한 방법 (setdefault 사용)
char_count2 = {}
for char in text:
    char_count2.setdefault(char, 0)
    char_count2[char] += 1
# setdefault 사용: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
print(f"setdefault 사용: {char_count2}")

# 2) 그룹화
students_list = [
    {"name": "김철수", "grade": 1},
    {"name": "이영희", "grade": 2},
    {"name": "박민수", "grade": 1},
    {"name": "최지영", "grade": 2}
]

grouped_by_grade = {}
for student in students_list:
    grade = student["grade"]
    if grade not in grouped_by_grade:
        grouped_by_grade[grade] = []
    grouped_by_grade[grade].append(student["name"])

# 학년별 그룹화: {1: ['김철수', '박민수'], 2: ['이영희', '최지영']}
print(f"학년별 그룹화: {grouped_by_grade}")

# 3) 캐시 구현
cache = {}


def expensive_function(n):
    if n in cache:
        print(f"캐시에서 반환: {n}")
        return cache[n]

    print(f"계산 중: {n}")
    result = n ** 2  # 복잡한 계산이라고 가정
    cache[n] = result
    return result


print(f"첫 번째 호출: {expensive_function(5)}")
# 계산 중: 5
# 첫 번째 호출: 25

print(f"두 번째 호출: {expensive_function(5)}")
# 캐시에서 반환: 5
# 두 번째 호출: 25

# 4) 설정 관리
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp"
    },
    "api": {
        "timeout": 30,
        "retry_count": 3
    }
}

db_host = config["database"]["host"]
api_timeout = config.get("api", {}).get("timeout", 60)  # 기본값 60
print(f"DB 호스트: {db_host}")
print(f"API 타임아웃: {api_timeout}")
# DB 호스트: localhost
# API 타임아웃: 30


print("\n" + "=" * 60)
print("딕셔너리 vs 다른 자료구조 비교")
print("=" * 60)

print("딕셔너리 사용이 좋은 경우:")
print("- 키-값 관계의 데이터를 저장할 때")
print("- 빠른 검색이 필요할 때")
print("- 데이터의 구조화가 필요할 때")
print("- 고유 식별자로 데이터에 접근할 때")

print("\n리스트 사용이 좋은 경우:")
print("- 순서가 중요한 데이터")
print("- 인덱스 기반 접근이 필요할 때")
print("- 중복 데이터를 허용해야 할 때")

print("\n성능 비교:")
print("- 검색: 딕셔너리 O(1) vs 리스트 O(n)")
print("- 삽입: 딕셔너리 O(1) vs 리스트 O(1) (끝에 추가)")
print("- 삭제: 딕셔너리 O(1) vs 리스트 O(n) (중간 삭제)")

print("\n" + "=" * 60)
print("딕셔너리 사용 시 주의사항")
print("=" * 60)

print("1. 키는 불변 타입만 사용 가능")
print("2. 키의 순서는 Python 3.7+ 에서만 보장")
print("3. 중첩 딕셔너리 복사 시 깊은 복사 고려")
print("4. 키 존재 여부 확인 후 접근하는 습관")
print("5. 메모리 사용량이 리스트보다 많음")

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
# del user[]"email"]
# user.setdefault('signup_date', '2025-07-10')

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
# 1. 원래 점수 : {'Charlie': 90, 'Bob': 85, 'Alice': 95}
print(f'1. 원래 점수 : {students}')

# 정보 수정
students.update(David=80)
students.update(Alice=88)
del students["Bob"]

# students["David"] = 80
# students["Alice"] = 88

# 최종 결과 출력
# 2. 수정된 점수 : {'Charlie': 90, 'Alice': 88, 'David': 80}
print(f'2. 수정된 점수 : {students}')


######################################################################################################
# ==========================================
# 딕셔너리 중요 메서드들과 순회 완전 가이드
# ==========================================


print("=" * 60)
print("1. setdefault() 메서드 - 안전한 키 생성")
print("=" * 60)

scores = {
    '김철수': 85,
    '이영희': 92,
    '박민수': 78
}
print(f"초기 점수: {scores}")

# setdefault(key, default_value)
# - 키가 없으면: 새 키-값 쌍을 추가하고 default_value 반환
# - 키가 있으면: 기존 값을 그대로 유지하고 기존 값 반환

# 새로운 학생 추가
new_score = scores.setdefault('정수진', 88)  # 키가 없으므로 새로 추가
print(f"정수진 점수 설정: {new_score}")
print(f"점수 추가 후: {scores}")

# 기존 학생의 점수는 변경되지 않음
existing_score = scores.setdefault('김철수', 100)  # 기존 값(85) 유지
print(f"김철수 기존 점수 유지: {existing_score}")
print(f"최종 점수: {scores}")

# setdefault() 활용 예시 - 그룹화할 때 매우 유용
students_by_grade = {}
student_data = [
    ('김철수', 1), ('이영희', 2), ('박민수', 1),
    ('정수진', 2), ('최동훈', 1)
]

print(f"\n학년별 그룹화 예시:")
for name, grade in student_data:
    # 학년 키가 없으면 빈 리스트 생성, 있으면 기존 리스트 사용
    students_by_grade.setdefault(grade, []).append(name)

# 학년별 학생: {1: ['김철수', '박민수', '최동훈'], 2: ['이영희', '정수진']}
print(f"학년별 학생: {students_by_grade}")

# setdefault 없이 구현하면 (더 복잡함)
students_manual = {}
for name, grade in student_data:
    if grade not in students_manual:
        students_manual[grade] = []
    students_manual[grade].append(name)
print(f"수동 구현 결과: {students_manual}")

print("\n" + "=" * 60)
print("2. copy() vs deepcopy() - 복사 방법의 차이")
print("=" * 60)

# 얕은 복사(Shallow Copy) vs 깊은 복사(Deep Copy)
scores = {
    '김철수': 85,
    '이영희': 92,
    '박민수': 78
}

# copy() - 얕은 복사: 딕셔너리 자체만 복사, 내부 객체는 참조 공유
scores_copy = scores.copy()
scores_copy['최동훈'] = 95  # 새 키 추가
scores_copy['김철수'] = 10  # 기존 키 수정

print(f"원본 scores: {scores}")           # 원본은 변경되지 않음
print(f"복사본 scores_copy: {scores_copy}")  # 복사본만 변경됨

print(f"\n단순 딕셔너리에서는 copy()로 충분합니다.")

# 중첩 딕셔너리에서의 얕은 복사 vs 깊은 복사
nested_dict = {
    "team1": {
        'leader': '김철수',
        'members': ['이영희', '박민수']  # 리스트는 가변 객체
    },
    "team2": {
        'leader': '정수진',
        'members': ['최동훈', '강미나']
    }
}
print(f"\n원본 중첩 딕셔너리: {nested_dict}")

# 얕은 복사: 내부의 리스트들은 여전히 같은 객체를 참조
shallow = nested_dict.copy()

# 깊은 복사: 모든 내부 객체까지 새로 복사
deep = copy.deepcopy(nested_dict)

# 원본의 내부 리스트 수정
nested_dict['team1']['members'].append('신입사원')
print(f"\n원본에 '신입사원' 추가 후:")
print(f"원본: {nested_dict['team1']['members']}")
print(f"얕은 복사(영향 받음): {shallow['team1']['members']}")  # 같은 리스트를 참조하므로 변경됨
print(f"깊은 복사(영향 없음): {deep['team1']['members']}")    # 별도 리스트이므로 변경 안됨

# 또 다른 테스트
shallow['team2']['leader'] = '새로운 리더'  # 딕셔너리 자체는 독립적
print(f"\n얕은 복사에서 리더 변경:")
print(f"원본 team2 리더: {nested_dict['team2']['leader']}")
print(f"얕은 복사 team2 리더: {shallow['team2']['leader']}")

# 메모리 관리 관점에서의 설명
print(f"\n메모리 참조 확인:")
# is(==)
print(
    # 원본과 얕은 복사의 team1 members가 같은 객체인가?: True
    f"원본과 얕은 복사의 team1 members가 같은 객체인가?: {nested_dict['team1']['members'] is shallow['team1']['members']}")
print(
    # 원본과 깊은 복사의 team1 members가 같은 객체인가?: False
    f"원본과 깊은 복사의 team1 members가 같은 객체인가?: {nested_dict['team1']['members'] is deep['team1']['members']}")

print("\n" + "=" * 60)
print("3. 딕셔너리 순회(Iteration) 방법들")
print("=" * 60)

scores = {
    '김철수': 85,
    '이영희': 92,
    '박민수': 78,
    '정수진': 88
}

# 방법 1: 키만 순회 (기본 방식)
print("1) 키만 순회 (기본 방식):")
for key in scores:  # 기본적으로 키를 순회
    print(f'{key}: {scores[key]}점')

print("\n2) 키만 순회 (명시적 방식):")
for key in scores.keys():  # 명시적으로 keys() 메서드 사용
    print(f'{key}: {scores[key]}점')

# 방법 2: 값만 순회
print("\n3) 값만 순회:")
for value in scores.values():
    print(f'점수: {value}점')

# 값들로 통계 계산
total_score = sum(scores.values())
average_score = total_score / len(scores)
max_score = max(scores.values())
min_score = min(scores.values())

print(f"\n점수 통계:")
print(f"총점: {total_score}점")
print(f"평균: {average_score:.1f}점")
print(f"최고점: {max_score}점")
print(f"최저점: {min_score}점")

# 방법 3: 키-값 쌍 순회 (가장 일반적이고 유용)
print("\n4) 키-값 쌍 순회:")
for key, value in scores.items():
    print(f'{key}: {value}점')

# 방법 4: 인덱스와 함께 순회
print("\n5) 인덱스와 함께 순회:")
for idx, (key, value) in enumerate(scores.items()):
    print(f'{idx+1}번째 - {key}: {value}점')

# 순회하면서 조건부 처리
print("\n6) 조건부 순회:")
print("90점 이상인 학생들:")
for name, score in scores.items():
    if score >= 90:
        print(f'  {name}: {score}점 (우수)')

print("\n80점 미만인 학생들:")
for name, score in scores.items():
    if score < 80:
        print(f'  {name}: {score}점 (보충 필요)')

print("\n" + "=" * 60)
print("4. 고급 순회 기법들")
print("=" * 60)

# 딕셔너리 정렬하여 순회
print("1) 점수 순으로 정렬하여 순회:")
# key 함수를 사용하여 값(점수)으로 정렬
for name, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
    print(f'  {name}: {score}점')

print("\n2) 이름순으로 정렬하여 순회:")
# 키(이름)로 정렬
for name, score in sorted(scores.items()):
    print(f'  {name}: {score}점')

# 딕셔너리 컴프리헨션과 순회
print("\n3) 조건에 맞는 새 딕셔너리 생성:")
high_scores = {name: score for name, score in scores.items() if score >= 85}
print(f"85점 이상: {high_scores}")

# 값 변환하며 새 딕셔너리 생성
grade_dict = {name: 'A' if score >= 90 else 'B' if score >= 80 else 'C'
              for name, score in scores.items()}
print(f"등급 변환: {grade_dict}")

print("\n" + "=" * 60)
print("5. 실용적인 순회 활용 예시")
print("=" * 60)

# 예시 1: 학급 성적 분석
scores = {
    '김철수': 85, '이영희': 92, '박민수': 78, '정수진': 88,
    '최동훈': 95, '강미나': 83, '윤서준': 76, '한지원': 89
}

print("1) 학급 성적 분석:")
grade_distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

for name, score in scores.items():
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    else:
        grade = 'D'

    grade_distribution[grade] += 1
    print(f"  {name}: {score}점 ({grade}등급)")

print(f"\n등급별 분포: {grade_distribution}")

# 예시 2: 재고 관리 시스템
inventory = {
    '노트북': {'재고': 15, '가격': 1200000},
    '마우스': {'재고': 50, '가격': 25000},
    '키보드': {'재고': 3, '가격': 80000},
    '모니터': {'재고': 8, '가격': 300000}
}

print("\n2) 재고 관리 시스템:")
total_value = 0
low_stock_items = []

for item, details in inventory.items():
    stock = details['재고']
    price = details['가격']
    item_value = stock * price
    total_value += item_value

    print(f"  {item}: 재고 {stock}개, 가격 {price:,}원, 총액 {item_value:,}원")

    if stock < 10:
        low_stock_items.append(item)

print(f"\n총 재고 가치: {total_value:,}원")
print(f"재고 부족 품목: {low_stock_items}")

# 예시 3: 단어 빈도 분석
text = "python is great python is easy python programming is fun"
words = text.split()

print("\n3) 단어 빈도 분석:")
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# 빈도순으로 정렬하여 출력
for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
    print(f"  '{word}': {count}번")

print("\n" + "=" * 60)
print("6. 순회 시 주의사항과 팁")
print("=" * 60)

print("주의사항:")
print("1. 순회 중 딕셔너리 크기 변경 금지")
print("   - 순회 중 키 추가/삭제하면 RuntimeError 발생 가능")

print("\n2. 안전한 수정 방법:")
scores_to_modify = {'A': 10, 'B': 20, 'C': 30}

# 잘못된 방법 (순회 중 수정)
# for key in scores_to_modify:
#     if scores_to_modify[key] < 15:
#         del scores_to_modify[key]  # RuntimeError 위험!

# 올바른 방법 1: 별도 리스트에 키 저장 후 삭제
keys_to_delete = []
for key, value in scores_to_modify.items():
    if value < 15:
        keys_to_delete.append(key)

for key in keys_to_delete:
    del scores_to_modify[key]
print(f"안전한 삭제 후: {scores_to_modify}")

# 올바른 방법 2: 딕셔너리 컴프리헨션 사용
original = {'A': 10, 'B': 20, 'C': 30}
filtered = {k: v for k, v in original.items() if v >= 15}
print(f"컴프리헨션으로 필터링: {filtered}")

print("\n성능 팁:")
print("1. 큰 딕셔너리에서는 .items() 사용")
print("2. 키만 필요하면 기본 순회 사용")
print("3. 값만 필요하면 .values() 사용")
print("4. 조건부 순회 시 컴프리헨션 고려")

print("\n" + "=" * 60)
print("7. 메모리 효율적인 순회 방법")
print("=" * 60)

large_dict = {f'key_{i}': i**2 for i in range(10)}

print("1) 기본 순회 (메모리 효율적):")
for key in large_dict:  # 키를 하나씩 생성
    print(f"{key}: {large_dict[key]}")
    if key == 'key_3':  # 예시를 위해 일부만 출력
        print("  ... (나머지 생략)")
        break

print("\n2) list() 변환은 메모리 사용량 증가:")
print(f"keys() 객체 크기: 작음 (뷰 객체)")
print(f"list(keys()) 크기: 큼 (실제 리스트 생성)")

# 메모리 사용량 비교 (개념적 설명)
print("\n메모리 사용 패턴:")
print("- dict.keys(): 뷰 객체 - 메모리 효율적")
print("- list(dict.keys()): 실제 리스트 - 메모리 사용량 증가")
print("- 일반적으로 list() 변환은 필요할 때만 사용")
