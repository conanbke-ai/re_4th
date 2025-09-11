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
unique_numbers = {3, 1, 4, 1, 5}
for num in unique_numbers:
    print(num)
