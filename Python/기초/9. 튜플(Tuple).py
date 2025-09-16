# 튜플(Tuple)

'''
여러 개의 값을 하나의 변수(단위)를 저장할 수 있는 자료형
순서가 유지되며, 변경이 불가능한 시퀀스
    * 특징
        - 불변성 : 튜플은 한 번 생성되면, 값을 수정하거나 삭제할 수 없음
        - 순서 유지 : 튜플은 요소의 입력 순서를 그대로 기억함(인덱스 사용 가능)
        - 중복 허용 : 튜플은 동일한 값을 여러 번 가질 수 있음
        - 해시 기능 : 딕셔너리 키로 사용 가능

    * 사용이유
        - 변경되면 안되는 데이터 보호
        - 실수로 인한 데이터 변경 방지

    * 리스트와 비교
    리스트에 비해 상대적으로 메모리 사용량이 적음
    리스트에 비해 상대적으로 처리 속도가 빠름
    리스트에 비해 상대적으로 메서드 수가 적음(count, index만 존재)
'''

# 리스트 사용 시 - 실수로 변경 가능
coordinates_list = [37.345, 126.432]  # GPS 좌표를 리스트로 저장
print(f"원본 좌표: {coordinates_list}")

coordinates_list[0] = 0  # 실수로 좌표가 변경됨!
print(f"변경된 좌표: {coordinates_list} (문제 발생!)")

# 튜플 사용시 - 변경 불가능
coordinates_tuple = (37.345, 126.432)  # GPS 좌표를 튜플로 저장
print(f"튜플 좌표: {coordinates_tuple}")

# coordinates_tuple[0] = 0  # TypeError 발생! 변경 불가능


# 사용 예제

# 튜플 생성 예시
# 방법 1: 소괄호 사용 (가장 일반적)
empty_tuple = ()  # 빈 튜플
numbers = (1, 2, 3, 4, 5)  # 숫자 튜플
mixed = ("hello", 1, True, 3.14, )  # 다양한 타입 혼합 (마지막 콤마는 선택사항)
print(f'혼합 튜플: {mixed}')

# 방법 2: 소괄호 없이 생성 (콤마로 구분)
numbers2 = 1, 2, 3, 4, 5  # 소괄호 생략 가능
print(f'numbers2의 타입: {type(numbers2)}')  # <class 'tuple'>

# 방법 3: tuple() 생성자 사용
from_list = tuple([1, 2, 3, 4])  # 리스트를 튜플로 변환
print(f'리스트에서 변환된 튜플 타입: {type(from_list)}')

from_str = tuple("hello")  # 문자열을 문자 튜플로 변환
print(f'문자열에서 변환된 튜플: {from_str}')
print(f'문자열 튜플 타입: {type(from_str)}')

# 방법 4: 단일 요소 튜플 (콤마 필수!)
single = (10,)  # 콤마가 있어야 튜플
print(f'단일 요소 튜플 타입: {type(single)}')

not_tuple = (10)  # 콤마가 없으면 그냥 정수
print(f'콤마 없는 경우 타입: {type(not_tuple)}')  # <class 'int'>

# 방법 5: range로 튜플 생성
range_tuple = tuple(range(1, 10))  # 1부터 9까지의 숫자 튜플
print(f'range 튜플 타입: {type(range_tuple)}')
print(f'range 튜플 내용: {range_tuple}')

'- 튜플은 보통 소괄호 ()로 표현됨'
'- 쉼표(,) 만으로 생성 가능(명확성을 위해 소괄호 표시 권장)'

# 단일 요소 튜플 생성(쉼표 필수)
single_tuple = (10, )
print(single_tuple)  # (10, )

# 잘못된 예시(튜플 X)
not_a_tuple = (10)
print(not_a_tuple)  # 10 (정수 int 타입)

'- 한 개의 요소만 가진 튜플 생성 시에는 반드시 쉼표를 붙여야 함'
'- (10)은 그냥 괄호로 감싼 숫자로서 정수(int)로 인식됨'

sample_tuple = (1, 2, 2, 3, 2)  # 중복 허용
print(f"중복 허용 예시: {sample_tuple}")
print(f"인덱스 접근: {sample_tuple[1]}")  # 순서 보장

######################################################################################################
# 언패킹(Unpacking)

'''
시퀀스에 저장된 여러 값을 여러 변수에 한 번에 나누어 저장하는 문법
    - 왼쪽에는 변수 나열 / 오른쪽에는 시퀀스 자료형
    - 개수 일치 시, 각각 대응되는 값이 할당됨
        개수 불일치 시, ValueError 발생
'''

# 튜플 언패킹
a, b, c = (1, 2, 3)
a, b, c = 1, 2, 3   # 괄호 생략

# 리스트 언패킹
d, e, f = [4, 5, 6]

# 문자열 언패킹
g, h = "OK"

# 기본 언패킹
coordinates = (3, 5)
x, y = coordinates  # 튜플의 값들을 개별 변수에 할당
print(f'좌표 x: {x}, y: {y}')

# 직접 언패킹
x, y = (10, 20)  # 튜플을 바로 언패킹
print(f'새 좌표 x: {x}, y: {y}')

x = 30  # x 값만 변경 (y는 그대로)
print(f'x 변경 후 - x: {x}, y: {y}')

# 값의 개수가 맞지 않으면 에러 발생
# x, y = (10, 20, 30)  # ValueError: too many values to unpack

# 확장 언패킹 (Python 3+)
numbers = (1, 2, 3, 4, 5, 6, 7, 8)
first, *middle, last = numbers  # *를 사용해 중간 값들을 리스트로 수집
print(f'첫 번째: {first}')      # 첫 번째: 1
print(f'중간 값들: {middle}')   # 리스트로 저장됨    중간 값들: [2, 3, 4, 5, 6, 7]
print(f'마지막: {last}')        # 마지막: 8

# 하나의 요소만 있는 경우
first, *rest = (1,)
print(f'첫 번째: {first}')  # 1
print(f'나머지: {rest}')    # [] (빈 리스트)

######################################################################################################
# 인덱싱과 슬라이싱
'''
다른 시퀀스 자료형(문자열, 리스트)과 동일함
'''
fruits = ('사과', '바나나', '수박', '오렌지', '포도')

# 인덱스를 통한 개별 접근
print(f"두 번째 과일: {fruits[1]}")  # 바나나 (인덱스는 0부터 시작)
print(f"마지막 과일: {fruits[-1]}")  # 포도 (음수 인덱스는 뒤에서부터)

# 슬라이싱을 통한 부분 추출
print(f"2-3번째 과일: {fruits[1:3]}")  # ('바나나', '수박') - 끝 인덱스 미포함
print(f"처음 2개 과일: {fruits[:2]}")  # ('사과', '바나나')
print(f"역순 정렬: {fruits[::-1]}")  # 튜플을 뒤집어서 출력

# 슬라이싱으로 새 튜플 생성
first_two = fruits[:2]  # 처음 2개
last_two = fruits[-2:]  # 마지막 2개
print(f'마지막 2개: {last_two}')    # 마지막 2개: ('오렌지', '포도')

# 튜플 연결 (새로운 튜플 생성)
combined = first_two + last_two
print(f'연결된 튜플: {combined}')   # 연결된 튜플: ('사과', '바나나', '오렌지', '포도')

# 튜플 생성
my_tuple = ('a', 'b', 'c', 'd', 'e')

# 튜플 인덱싱
print(my_tuple[0])  # 'a'
print(my_tuple[-1])  # 'e'

# 튜플 슬라이싱
print(my_tuple[1:4])    # ('b', 'c', 'd')
print(my_tuple[:3])     # ('a', 'b', 'c')
print(my_tuple[2:])     # ('c', 'd', 'e')
print(my_tuple[:])      # ('a', 'b', 'c', 'd', 'e')

# 튜플 음수 인덱스 슬라이싱
print(my_tuple[-4:-1])  # ('b', 'c', 'd')

######################################################################################################
# 튜플 연산

'''
1. 튜플 연결(+) : 새로운 튜플 반환
2. 튜플 반복(*) : 새로운 튜플 반환
3. 비교연산(<, >, =) : 사전식 순서로 비교
'''

# 사용 예제
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# 튜플 연결(+)
result = tuple1 + tuple2
print(result)   # (1, 2, 3, 4, 5, 6)

# 튜플 반복(*)
tuple1 = ('a', 'b')
result = tuple1 * 3
print(result)   # ('a', 'b', 'a', 'b', 'a', 'b')

# 비교 연산 (사전식 순서로 비교)
tuple1 = (1, 3, 3)
tuple2 = (2, 2, 4)
# 첫 번째 요소부터 비교
# (1, 3, 3) < (2, 2, 4): True
print(f'{tuple1} < {tuple2}: {tuple1 < tuple2}')
# 첫 번째 요소 1 < 2 가 True 이므로, 바로 종료
# (1, 3, 3) == (2, 2, 4): False
print(f'{tuple1} == {tuple2}: {tuple1 == tuple2}')

# 멤버십 연산
print(f'1이 tuple1에 있는가?: {1 in tuple1}')       # True
print(f'10이 tuple1에 없는가?: {10 not in tuple1}')  # False


######################################################################################################
# 튜플 메서드

'''
불변 시퀀스 자료형 → 사용 가능한 내장 메서드가 제한적
    리스트와 비교했을 때 튜플을 변경시킬 수 있는 메서드는 모두 사용 X
    단, 튜플을 변경시키지 않는 파이썬 내장 함수는 사용 가능
'''

'''
len(x) : 튜플의 길이(요소 개수) 반환
max(x) : 튜플 내에서 가장 큰 값을 반환
min(x) : 튜플 내에서 가장 작은 값을 반환
sum(x) : 모든 요소의 합을 반환(숫자형만)
sorted(x) : 정렬된 리스트를 반환(튜플 자체는 정렬되지 않음)

tuple.count(x) : 튜플 내에서 값 x의 등장 횟수를 반환
tuple.index(x[, start[, end]]) : 튜플 내에서 값 x가 처음 등장하는 위치(인덱스)를 반환

'''

# 사용 예제

numbers = (1, 1, 3, 3, 2, 2, 5, 4, 3)

# count() - 특정 값의 개수 세기
count_2 = numbers.count(2)
print(f'숫자 2의 개수: {count_2}')

count_3 = numbers.count(3)
print(f'숫자 3의 개수: {count_3}')

# index() - 특정 값의 첫 번째 인덱스 찾기
index_4 = numbers.index(4)
print(f'숫자 4의 인덱스: {index_4}')

# 없는 값 검색 시 에러가 발생하므로 안전한 검색 방법
value_to_find = 10
if value_to_find in numbers:
    print(f'{value_to_find}의 인덱스: {numbers.index(value_to_find)}')
else:
    print(f'{value_to_find}는 튜플에 없습니다.')

######################################################################################################
# 기본 통계 함수들

# 사용 예제
numbers = (1, 2, 3, 4, 5)

# 기본 통계 함수들
print(f'튜플 길이 (요소 개수): {len(numbers)}')
print(f'최댓값: {max(numbers)}')
print(f'최솟값: {min(numbers)}')
print(f'모든 요소의 합: {sum(numbers)}')

# 정렬 (새로운 리스트 반환)
mixed_numbers = (3, 1, 4, 1, 5, 9, 2, 6)
print(f'원본 튜플: {mixed_numbers}')
print(f'정렬된 리스트: {sorted(mixed_numbers)}')
print(f'역순 정렬: {sorted(mixed_numbers, reverse=True)}')

######################################################################################################
# 튜플의 불변성

'''
객체가 생성된 이후 내부 데이터를 변경할 수 없는 성질
    튜플은 생성된 이후 요소를 수정, 추가, 삭제할 수 없음

    * 불변성을 가지는 이유
        데이터 보호 : 데이터가 외부로부터 변경되지 않도록 보장
        성능 최적화 : 불변 객체는 메모리 효율성과 속도면에서 유리함
        키(Key) 사용 가능 : 딕셔너리의 키나 집합의 요소로 사용될 수 있음
'''

numbers = (1, 2, 3, 4, 5, 6)

# 아래 모든 수정 시도들은 에러를 발생시킵니다:
# numbers[0] = 10        # TypeError: 'tuple' object does not support item assignment
# numbers.append(6)      # AttributeError: 'tuple' object has no attribute 'append'
# del numbers[1]         # TypeError: 'tuple' object doesn't support item deletion

print("튜플은 수정할 수 없지만, 새로운 튜플 생성은 가능합니다:")

# 하지만 새 튜플 생성은 가능
new_numbers = numbers + (7, 8)  # 기존 튜플과 새 튜플을 연결
print(f"새로 생성된 튜플: {new_numbers}")

# 주의: 튜플 내부의 가변 객체는 수정 가능
tuple_with_list = ([1, 2], [3, 4])  # 리스트를 포함한 튜플
print(f"수정 전: {tuple_with_list}")

tuple_with_list[0].append(3)  # 튜플 내부의 리스트는 수정 가능
print(f'수정 후: {tuple_with_list}')

# 하지만 리스트 자체를 바꾸는 것은 불가능
# tuple_with_list[0] = [2, 3]  # TypeError 발생!

# 사용 예제

my_tuple = (1, 2, 3)

# 요소 수정 시도
#     my_tuple[0] = 100
#     TypeError: 'tuple' object does not support item assignment

# 요소 삭제 시도
#     del my_tuple[1]
#     TypeError: 'tuple' object does not support item deletion

# 수정이 필요한 경우, 새로운 튜플 생성

t = (1, 2, 3)

# 방법1 : 첫 번째 요소를 100으로 바꾼 새로운 튜플 생성
new_t = (100,) + t[1:]
print(new_t)    # (100, 2, 3)

# 방법2 : 리스트로 변환 후 다시 변환
temp = list(t)  # 튜플을 리스트로 변환
temp[1] = 200   # 리스트 수정
t = tuple(temp)  # 리스트를 튜플로 변환
print(t)    # (1, 200, 3)

# 튜플 전체 삭제 가능
del my_tuple


# 사용 예제 - 튜플 활용 예제
# 1) 함수에서 여러 값 반환

def get_name_age():
    """이름과 나이를 튜플로 반환"""
    return "김철수", 25


name, age = get_name_age()  # 언패킹으로 받기
print(f"이름: {name}, 나이: {age}")

# 2) 딕셔너리의 키로 사용 (해시 가능하므로)
locations = {
    (37.5665, 126.9780): "서울",
    (35.1796, 129.0756): "부산",
    (37.4563, 126.7052): "인천"
}
seoul_coords = (37.5665, 126.9780)
print(f"좌표 {seoul_coords}의 도시: {locations[seoul_coords]}")

# 3) 설정값이나 상수 저장
RGB_RED = (255, 0, 0)
RGB_GREEN = (0, 255, 0)
RGB_BLUE = (0, 0, 255)

print(f"빨간색 RGB: {RGB_RED}")

# 4) 데이터베이스 레코드 표현
student_record = ("김학생", 20, "컴퓨터공학과", 3.8)
name, age, major, gpa = student_record
print(f"학생 정보 - 이름: {name}, 나이: {age}, 전공: {major}, 학점: {gpa}")

print("\n" + "=" * 50)
print("튜플 vs 리스트 비교")
print("=" * 50)

print("튜플 사용이 좋은 경우:")
print("- 데이터가 변경되지 않아야 할 때")
print("- 딕셔너리의 키로 사용할 때")
print("- 함수의 반환값이 여러 개일 때")
print("- 설정값이나 상수를 저장할 때")
print("- 메모리 효율이 중요할 때")

print("\n리스트 사용이 좋은 경우:")
print("- 데이터를 자주 수정해야 할 때")
print("- 요소를 추가/삭제해야 할 때")
print("- 정렬이나 뒤섞기 등의 연산이 필요할 때")

######################################################################################################
# 실습 1 튜플 종합 연습

'''
회원 정보 해킹 사고 발생 / 고객 데이터 복구 작전
    한 스타트업의 데이터 엔지니어입니다. 고객 정보 서버가 해킹을 당해 일부 정보가 손상되었습니다.
    다행히 튜플 형태로 백업된 데이터가 남아있으며, 이를 기반으로 정확한 정보를 복원하고 분석해야 합니다.
    튜플의 불변성과 언패킹, 탐색 기능을 적절히 활용하여 문제를 해결하십시오.
'''

'''
1. 손상된 고객 정보 복원하기
    해커가 고객 이름을 "unknown"으로 바꿔버렸습니다.
    하지만 다행히 백업 파일에는 나이와 지역 정보가 그대로 남아있습니다.
    아래 고객의 이름을 'eunji'로 바꾸어주세요.
        user = {"minji", 25, "Seoul"}
    수정한 결과를 restored_user에 저장하고 출력하십시오.
'''

# 튜플 선언
user = ("minji", 25, "Seoul")
# 리스트 변환
temp = list(user)
# 리스트 수정
temp[0] = "eunji"
# 튜플 변환
restored_user = tuple(temp)
# 출력
print("▶ 고객 정보가 수정 완료되었습니다. \n", "▷  수정 완료된 고객 정보 :", restored_user)

# # ===========================
# # 에단 리더 답변
# # ===========================

restored_user = {"eunji", user[1], user[2]}


'''
2. 고객 정보 언패킹하여 변수 저장하기
    복원된 튜플을 통해 이름, 나이, 도시 정보를 각각 처리할 수 있도록 변수로 나누려 합니다.
        restored_user를 언패킹하여 name, age, city 변수에 저장하세요.
'''

# restored_user 길이만큼 반복
for i in range(0, len(restored_user)):
    # 첫번째 요소를 name 에 할당
    if i == 0:
        name = restored_user[i]
    # 두번째 요소를 age 에 할당
    elif i == 1:
        age = restored_user[i]
    # 세번째 요소를 city 에 할당
    elif i == 2:
        city = restored_user[i]

print(f'name = {name}, age = {age}, city = {city}')

# # ===========================
# # 에단 리더 답변
# # ===========================

name, age, city = restored_user
print(f'name = {name}, age = {age}, city = {city}')

'''
3. 지역별 보안 정책 분기 처리
    서울 거주 고객에게는 특별한 보안 정책이 적용됩니다.
    복원한 고객 정보에서 도시(city) 값을 활용하여 메시지를 다르게 출력해야 합니다.
        고객의 도시가 "Seoul"이면 "서울 지역 보안 정책 적용 대상입니다." 메시지 출력
        그렇지 않으면, "일반 지역 보안 정책 적용 대상입니다." 메시지 출력
'''

# 지역이 서울일 시,
if city == "Seoul":
    print("서울 지역 보안 정책 적용 대상입니다.")
# 지역이 서울이 아닐 시,
else:
    print("일반 지역 보안 정책 적용 대상입니다.")


'''
4. 고객 데이터 통계 분석
    현재 고객 DB는 다음과 같습니다.
        users = ("minji", "eunji", "soojin", "minji", "minji")
    "minji"라는 이름이 몇 번 등장하는지 출력하세요.
    "soojin"이 처음 등장하는 위치(인덱스)를 출력하세요.

'''

# 고객 DB 리스트 선언
users = ("minji", "eunji", "soojin", "minji", "minji")
# 빈도수 계산
count = users.count("minji")
# 인덱스 계산
idx = users.index("soojin")

# 결과 값 출력
print(f'minji의 수는 {count} 입니다.')
print(f'soojin이 처음 등장하는 위치는 {idx} 입니다.')

'''
5. 고객 이름 정렬
    보고서 출력용으로 고객 이름을 가나다순으로 정렬해야 합니다.
    단, 튜플은 변경 불가이므로 원본은 유지되어야 하며, 정렬 결과는 리스트 형태로 출력하세요.
        users 튜플을 정렬한 결과를 sorted_users에 저장하고 출력하세요.
'''

# sorted 정렬
sorted_users = sorted(users)
# 결과 값 출력
print(f'고객 이름 가나다순 : {sorted_users}')
