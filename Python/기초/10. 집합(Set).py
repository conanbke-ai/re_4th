# 집합(Set)
'''
중복을 허용하지 않고, 순서가 없는 컬렉션 자료형
    - 수학에서의 집합 개념을 프로그래밍에 적용한 자료형
    - 합집합, 교집합, 차집합 등의 집합 연산을 빠르게 수행할 수 있음

* 특징
    - 중복된 값을 자동으로 제거
    - 요소의 순서를 보장하지 않음
    - 리스트나 튜플처럼 인덱싱이 불가능
    - 요소는 해시 가능한(immutable) 객체여야 함
    - in, not in 사용
    - 빠른 검색 가능 (시간복잡도 : O(1))
    - 집합 연산 : |, &, -, ^

* 기본 문법
    s1 = {1, 2, 3}
    s1 = {1, 1, 2, 2, 2, 3, 3, 3, 3}
    print(s1)   # {1, 2, 3}

    - 중괄호 {} 안에 값을 나열하면 바로 집합 생성
    - 중복된 값은 자동으로 제거됨

    s2 = set({1, 2, 3, 2})
    print(s2)   # {1, 2, 3}

    - 리스트, 튜플, 문자열 등을 전달할 수 있음
    - 중복된 값은 자동으로 제거됨
'''

# 빈 집합 생성
s = {}
print(type(s))  # <class 'dict'>

s_empty = set()
print(type(s_empty))    # <class 'set'>

'- 빈 중괄호 {} 는 dict로 해석됨'
'- 빈 집합을 만드려면 반드시 set()을 사용해야 함'

# 순서 없음
s = {10, 20, 30}
print(s)    # TypeError: 'set' object is not subscriptable

s = {10, 20, 30}
s_list = list(s)
print(s_list[0])    # 가능하지만, 순서는 예측 불가(내부적으로 해시값 기반 저장)

'- set은 순서가 없는 컬렉션이기 때문에 인덱싱, 슬라이싱 불가능'
'- 만약 순서를 보장하고 싶다면, list로 변환해서 사용해야 함'

# 자료형 제한
s = {1, 2, (3, 4)}
s = {[1, 2]}    # TypeError: unhashable

######################################################################################################
# 집합이 필요한 경우

# 중복 제거가 필요한 상황 예시
visitors = ['철수', '영희', '철수', '민수', '영희', '철수']
print(f"원본 방문자 리스트: {visitors}")

# 방법 1: 리스트로 중복 제거 (비효율적 - O(n²) 시간복잡도)
unique_visitors_list = []
for visitor in visitors:
    if visitor not in unique_visitors_list:  # 매번 전체 리스트를 검색 O(n)
        unique_visitors_list.append(visitor)
print(f"리스트로 중복 제거: {unique_visitors_list}")

# 방법 2: Set으로 중복 제거 (효율적 - O(n) 시간복잡도)
unique_visitors_set = set(visitors)  # 한 번에 중복 제거
print(f"Set으로 중복 제거: {unique_visitors_set}")

######################################################################################################
# Set 생성방법

# 방법 1: 빈 set 생성
# 주의: {} 는 딕셔너리이므로 set()을 사용해야 함!
empty_dict = {}  # 이것은 딕셔너리
empty_set = set()  # 이것이 빈 set
print(f"빈 딕셔너리 타입: {type(empty_dict)}")
print(f"빈 set 타입: {type(empty_set)}")

# 방법 2: 값이 있는 set 생성 (중괄호 사용)
numbers = {11, 2, 3, 5, 4, 3, 2, 4}  # 중복 자동 제거
fruits = {'사과', '바나나', '오렌지'}
print(f"숫자 set: {numbers}")
print(f"과일 set: {fruits}")

# 방법 3: 리스트/튜플에서 set 생성
list_numbers = [11, 2, 13, 5, 4, 3, 2, 4]
set_numbers = set(list_numbers)  # 리스트를 set으로 변환
print(f"리스트에서 변환된 set: {set_numbers}")

tuple_numbers = (1, 2, 3, 2, 1)
set_from_tuple = set(tuple_numbers)
print(f"튜플에서 변환된 set: {set_from_tuple}")

# 방법 4: 문자열에서 set 생성 (각 문자가 요소가 됨)
chars = set('hello')  # 문자별로 분리되어 set 생성
print(f"문자열에서 생성된 set: {chars}")

######################################################################################################
# Set Comprehension (집합 표현식)

# 기본 반복문과 비교
print("기본 반복문:")
for i in range(5):
    print(f"  {i}", end="")
print()

# Set Comprehension 사용법
com_set = {i for i in range(10)}  # 0부터 9까지의 숫자 set
print(f"기본 comprehension: {com_set}")

com_set1 = {i * 2 for i in range(10)}  # 0, 2, 4, ..., 18
print(f"2배 곱셈: {com_set1}")

com_set2 = {i ** 2 + 1 for i in range(10)}  # 1, 2, 5, 10, 17, ...
print(f"제곱 + 1: {com_set2}")

com_set3 = {i * 3 + 2 - 1 for i in range(10)}  # 1, 4, 7, 10, ...
print(f"복합 연산: {com_set3}")

# Comprehension과 동일한 기능을 반복문으로 구현
com_set4 = set()
for i in range(10):
    com_set4.add(i * 3 + 2 - 1)
print(f"반복문으로 동일 결과: {com_set4}")

# 리스트 comprehension과 비교
com_list = [i for i in range(2, 10, 2)]  # 리스트: [2, 4, 6, 8]
print(f"리스트 comprehension: {com_list}")

# 중복이 있는 리스트에서 set comprehension
new_list = [1, 2, 5, 1, 5]
com_set5 = {i for i in new_list}  # 중복 자동 제거
print(f"중복 제거 comprehension: {com_set5}")

# 조건부 comprehension
even_squares = {i**2 for i in range(10) if i % 2 == 0}
print(f"짝수의 제곱: {even_squares}")

print("\n" + "=" * 60)
print("5. Set에 저장 가능한 데이터 타입")
print("=" * 60)

# Hashable(해시 가능한) 타입만 set에 저장 가능 - 불변 타입들
valid_set = {1, "문자열", (1, 2), 3.14, True, False, None}
print(f"저장 가능한 타입들: {valid_set}")

# Unhashable(해시 불가능한) 타입은 저장 불가 - 가변 타입들
# 다음 코드들은 TypeError를 발생시킵니다:
# invalid_set = {[1, 2]}  # 리스트는 불가
# invalid_set = {{'key': 'value'}}  # 딕셔너리는 불가
# invalid_set = {{1, 2}}  # set 자체도 불가

print("저장 불가능한 타입: 리스트, 딕셔너리, set (가변 타입들)")

# 중첩 set을 만들려면 frozenset() 사용
nested_set = {frozenset([1, 2]), frozenset([3, 4])}
print(f"중첩 set (frozenset 사용): {nested_set}")

# frozenset은 불변(immutable) 집합
fs1 = frozenset([1, 2, 3, 3, 4])  # 중복 제거되어 생성
print(f"frozenset: {fs1}")
print(f"타입: {type(fs1)}")

# frozenset은 불변이므로 수정 메서드들이 모두 에러 발생
# fs1.add(5)        # AttributeError
# fs1.remove(1)     # AttributeError
# fs1.discard(2)    # AttributeError
# fs1.clear()       # AttributeError

# 하지만 집합 연산은 가능 (새로운 frozenset 반환)
fs2 = frozenset([3, 4, 5, 6])
print(f"fs1: {fs1}")
print(f"fs2: {fs2}")
print(f"합집합: {fs1 | fs2}")
print(f"교집합: {fs1 & fs2}")

# frozenset은 해시 가능하므로 set의 요소나 딕셔너리 키로 사용 가능
nested_sets = {fs1, fs2}  # frozenset을 포함하는 set
print(f"frozenset을 포함하는 set: {nested_sets}")

fs_dict = {fs1: "첫 번째 집합", fs2: "두 번째 집합"}
print(f"frozenset을 키로 하는 딕셔너리: {fs_dict}")


######################################################################################################
# set 주요 연산 및 메서드

'''
- 합집합(union()) : | 두 집합의 모든 원소   ex) A|B
- 교집합 (intersection()) : & 공통원소      ex) A&B
- 차집합(difference()) : - A에는 있고 B에는 없는 원소   ex)A-B
- 대칭 차집합(symmetric_difference()) : ^ A와 B에 하나만 있는 원소  ex) A^B
- 부분집합
    - issubset() : 부분집합인지 검사            ex) A.issubset(B)
    - issuperset() : 상위집합인지 검사          ex) A.issuperset(B)
    - isdisjoint()  : 공통 원소가 없는지 검사   ex) A.isdisjoint(B)
'''

# 사용 예제
A = {1, 2, 3}
B = {3, 4, 5}

# 합집합
print(A | B)  # {1, 2, 3, 4, 5}
print(A.union(B))   # {1, 2, 3, 4, 5}

# 교집합
print(A & B)    # {3}
print(A.intersection(B))    # {3}

# 차집합
print(A - B)    # {1, 2}
print(A.difference(B))  # {1, 2}

# 대칭 차집합
print(A ^ B)    # {1, 2, 4, 5}
print(A.symmetric_difference(B))    # {1, 2, 4, 5}

# 부분집합
print(A.issubset(B))    # True
print(B.issuperset(A))  # False
print(A.isdisjoint({4}))  # True(공통 원소 없음)


A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(f"집합 A: {A}")
print(f"집합 B: {B}")

# 교집합 (Intersection) - 공통 요소
intersection1 = A & B  # 연산자 사용
intersection2 = A.intersection(B)  # 메서드 사용
print(f"교집합 (A ∩ B): {intersection1}")
print(f"메서드로 교집합: {intersection2}")

# 합집합 (Union) - 모든 요소 (중복 제거)
union1 = A | B  # 연산자 사용
union2 = A.union(B)  # 메서드 사용
print(f"합집합 (A ∪ B): {union1}")
print(f"메서드로 합집합: {union2}")

# 차집합 (Difference) - A에만 있는 요소
difference1 = A - B  # 연산자 사용
difference2 = A.difference(B)  # 메서드 사용
print(f"차집합 (A - B): {difference1}")
print(f"메서드로 차집합: {difference2}")

# 대칭 차집합 (Symmetric Difference) - 공통 요소 제외한 모든 요소
sym_diff1 = A ^ B  # 연산자 사용
sym_diff2 = A.symmetric_difference(B)  # 메서드 사용
print(f"대칭 차집합 (A ⊕ B): {sym_diff1}")
print(f"메서드로 대칭 차집합: {sym_diff2}")

print("\n" + "=" * 60)
print("8. 집합 연산으로 업데이트하기")
print("=" * 60)

A = {1, 2, 3}
B = {3, 4, 5}
print(f"원본 A: {A}, B: {B}")

# 교집합으로 업데이트 (A를 A∩B로 변경)
A_copy = A.copy()
A_copy.intersection_update(B)  # A = A ∩ B
print(f"A.intersection_update(B): {A_copy}")

A_copy = A.copy()
A_copy &= B  # 동일한 연산
print(f"A &= B: {A_copy}")

# 차집합으로 업데이트
A_copy = A.copy()
A_copy.difference_update(B)  # A = A - B
print(f"A.difference_update(B): {A_copy}")

A_copy = A.copy()
A_copy -= B  # 동일한 연산
print(f"A -= B: {A_copy}")

# 대칭차집합으로 업데이트
A_copy = A.copy()
A_copy.symmetric_difference_update(B)  # A = A ⊕ B
print(f"A.symmetric_difference_update(B): {A_copy}")

A_copy = A.copy()
A_copy ^= B  # 동일한 연산
print(f"A ^= B: {A_copy}")

# 합집합으로 업데이트
A_copy = A.copy()
A_copy.update(B)  # A = A ∪ B
print(f"A.update(B): {A_copy}")

A_copy = A.copy()
A_copy |= B  # 동일한 연산
print(f"A |= B: {A_copy}")

print("\n" + "=" * 60)
print("9. 집합 관계 확인")
print("=" * 60)

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {6, 7, 8}
print(f"A: {A}")
print(f"B: {B}")
print(f"C: {C}")

# 부분집합 확인 (subset)
print(f"A가 B의 부분집합인가? A.issubset(B): {A.issubset(B)}")  # True
print(f"A <= B: {A <= B}")  # True (부분집합 연산자)
print(f"B가 A의 부분집합인가? B.issubset(A): {B.issubset(A)}")  # False

# 상위집합 확인 (superset)
print(f"A가 B의 상위집합인가? A.issuperset(B): {A.issuperset(B)}")  # False
print(f"B가 A의 상위집합인가? B.issuperset(A): {B.issuperset(A)}")  # True
print(f"B >= A: {B >= A}")  # True (상위집합 연산자)

# 진부분집합/진상위집합 확인 (proper subset/superset)
print(f"A가 B의 진부분집합인가? A < B: {A < B}")  # True
print(f"B가 A의 진상위집합인가? B > A: {B > A}")  # True
print(f"A가 A의 진부분집합인가? A < A: {A < A}")  # False (자기 자신은 진부분집합 아님)

# 서로소 집합 확인 (disjoint sets) - 교집합이 없는 집합들
print(f"A와 C가 서로소인가? A.isdisjoint(C): {A.isdisjoint(C)}")  # True
print(f"A와 B가 서로소인가? A.isdisjoint(B): {A.isdisjoint(B)}")  # False

######################################################################################################
# 요소 추가 / 삭제 메서드

'''
- add : 하나의 요소 추가                    # s.add(4)
- update : 여러 요소 추가                   # s.update([5, 6])
- remove : 해당 요소 제거 (없으면 에러 발생) # s.remove(2)
- discard : 해당 요소 제거 (없으면 무시)    # s.discard(2)
- pop() : 임의의 요소 제거 후 반환          # s.pop()
- clear() : 모든 요소 제거                  # s.clear()
'''

# 사용 예제
s = {1, 2, 3}   # {1, 2, 3, 4}
s.add(4)        # {1, 2, 3, 4, 5, 6}
s.update([5, 6])    # {1, 3, 4, 5, 6}
s.remove(2)         # KeyError
s.remove(100)       # 존재하지 않아도 에러없음
s.discard(100)      # 임의의 값 하나 제거
s.pop()

colors = {"빨강", "노랑", "파랑"}
print(f"초기 colors: {colors}")

# add() - 단일 요소 추가
colors.add("초록")
print(f"add('초록') 후: {colors}")

# 중복 추가 시 변화 없음
colors.add("초록")  # 이미 있으므로 변화 없음
print(f"add('초록') 재시도 후: {colors}")

# update() - 여러 요소 한 번에 추가 (iterable 객체 사용)
colors.update(['보라', '주황'])  # 리스트로 추가
print(f"update(['보라', '주황']) 후: {colors}")

colors.update(['검정'], {"하양", "회색"})  # 여러 iterable 동시 추가
print(f"multiple update 후: {colors}")

# remove() - 특정 요소 제거 (없으면 KeyError)
colors.remove('검정')
print(f"remove('검정') 후: {colors}")

# colors.remove('검정')  # KeyError! 이미 제거된 요소
# print("두 번째 remove 시도 - 에러 발생!")

# discard() - 특정 요소 제거 (없어도 에러 없음)
colors.discard('검정')  # 없어도 에러 없음
print(f"discard('검정') 후: {colors}")

colors.discard('주황')  # 있는 요소 제거
print(f"discard('주황') 후: {colors}")

# pop() - 임의의 요소 제거하고 반환 (순서 보장 안됨)
popped = colors.pop()
print(f"pop()으로 제거된 요소: {popped}")
print(f"pop() 후 colors: {colors}")

# clear() - 모든 요소 제거
colors_copy = colors.copy()  # 백업
colors.clear()
print(f"clear() 후: {colors}")


# 사용 예제 - 집합 Set 활용
# 1) 중복 제거
print("1) 중복 제거:")
email_list = ['user1@email.com', 'user2@email.com',
              'user1@email.com', 'user3@email.com']
unique_emails = list(set(email_list))  # set으로 중복 제거 후 다시 리스트로
print(f"중복 제거된 이메일: {unique_emails}")

# 2) 빠른 멤버십 테스트
print("\n2) 빠른 멤버십 테스트:")
valid_users = {'admin', 'user1', 'user2', 'user3'}  # set 사용
user_input = 'user1'
if user_input in valid_users:  # O(1) 시간복잡도
    print(f"{user_input}는 유효한 사용자입니다.")

# 3) 공통 관심사 찾기
print("\n3) 공통 관심사 찾기:")
alice_interests = {'영화', '음악', '독서', '요리'}
bob_interests = {'음악', '운동', '독서', '게임'}
common_interests = alice_interests & bob_interests
print(f"공통 관심사: {common_interests}")

# 4) 데이터 검증
print("\n4) 데이터 검증:")
required_fields = {'name', 'email', 'password'}
provided_fields = {'name', 'email', 'age'}
missing_fields = required_fields - provided_fields
print(f"누락된 필드: {missing_fields}")

# 5) 태그 시스템
print("\n5) 태그 시스템:")
post1_tags = {'python', 'programming', 'tutorial'}
post2_tags = {'python', 'data-science', 'tutorial'}
all_tags = post1_tags | post2_tags  # 모든 태그
shared_tags = post1_tags & post2_tags  # 공유 태그
print(f"모든 태그: {all_tags}")
print(f"공유 태그: {shared_tags}")

print("\n" + "=" * 60)
print("Set vs 다른 자료구조 비교")
print("=" * 60)

print("Set 사용이 좋은 경우:")
print("- 중복을 허용하지 않는 데이터 저장")
print("- 빠른 멤버십 테스트가 필요할 때")
print("- 집합 연산(교집합, 합집합 등)이 필요할 때")
print("- 데이터의 유일성이 중요할 때")

print("\nList 사용이 좋은 경우:")
print("- 순서가 중요할 때")
print("- 인덱스 접근이 필요할 때")
print("- 중복 데이터를 허용해야 할 때")

print("\nDict 사용이 좋은 경우:")
print("- 키-값 쌍의 데이터가 필요할 때")
print("- 키를 통한 빠른 값 검색이 필요할 때")

######################################################################################################
# 실습 1 set 종합 연습

'''
1. 중복 제거 및 개수 세기
    어떤 학급의 학생들이 제출한 팀 과제 파일 이름 목록이 아래와 같습니다. 중복 제출된 경우도 포함되어 있습니다.
    중복을 제거한 후, 총 몇 명이 제출했느지 출력하는 프로그램을 작성하세요.
    submissions = ['Kim', 'lee', 'Kim', 'park', 'choi', 'lee', 'lee']
'''

# 리스트 선언
submissions = ['Kim', 'lee', 'Kim', 'park', 'choi', 'lee', 'lee']
# 중복 원소 제거 및 오름차순 정렬
submissions = sorted(set(submissions))
# 결과 값 출력
print(f'제출한 학생 수 : {len(submissions)} \n제출자 명단 : {submissions}')

'''
2. 공통 관심사 찾기
    두 명의 사용자가 각자 좋아하는 영화 장르를 아래와 같이 입력했습니다.
    두 사용자의 공통 관심 장르, 서로 다른 장르, 모든 장르 목록을 출력하세요.
        user1 = {'SF', 'Action', 'Drama'}
        user2 = {'Drama', 'Romance', 'Action'}
'''
# 리스트 선언
user1 = {'SF', 'Action', 'Drama'}
user2 = {'Drama', 'Romance', 'Action'}
# 결과 값 출력
print(f'공통 관심 장르 : {sorted(user1.intersection(user2))}',
      f'서로 다른 장르 : {sorted(user1.symmetric_difference(user2))}', f'전체 장르 : {sorted(user1.union(user2))}',
      sep="\n")

'''
3. 부분 집합 관계 판단
    어떤 유저가 가지고 있는 자격증 목록과 특정 직무에 필요한 자격증 목록이 주어집니다.
    이 사용자가 지원 자격을 갖추었는지 확인하세요.
        my_certificates = {"SQL", "Python", "Linux"}
        job_required = {"SQL", "Python"}
'''

# 리스트 선언
my_certificates = {"SQL", "Python", "Linux"}
job_required = {"SQL", "Python"}

# my_certificates 가 job_required 의 상위원소인지 출력
print(f'지원 자격 충족 여부 : {my_certificates.issuperset(job_required)}')
