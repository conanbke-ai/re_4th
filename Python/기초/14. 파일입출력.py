# 파일입출력(I/O)

'''
프로그램이 저장장치(예: 하드디스크)에 저장된 파일을 읽어오거나, 반대로 데이터를 파일에 저장하는 작업
    - 입력(input) : 파일로부터 데이터를 읽어오는 것
    - 출력(output) : 데이터를 파일로 저장(기록)하는 것

* 필요한 상황
    1. 설정 파일 저장 : 게임 설정, 프로그램 옵션
    2. 데이터 백업 : 중요한 정보 보관
    3. 로그 기록 : 프로그램 실행 기록, 에러 추적
    4. 데이터 교화 : 엑셀, csv 파일로 다른 프로그램과 데이터 공유
    5. 대용량 처리 : 메모리에 다 못 담는 빅데이터 처리
'''

'''
입, 출력 스트림

    - 스트림(Stream) : 자료 흐름이 물의 흐름과 같다는 뜻
        - 입력 스트림 : 동영상을 재생하기 위해 동영상 파일에서 자료를 읽을 때 사용함
        - 출력 스트림 : 사용자가 쓴 글을 파일에 저장할 때는 출력 스트림 사용함

    - 파일 입출력의 필요성
        - 프로그램 실행 중에 메모리에 저장된 데이터는 프로그램이 종료되면 사라짐
        - 데이터를 프로그램이 종료된 후에도 계속해서 사용하려면 파일에 저장하고
        - 필요할 때 파일을 읽어서 데이터를 사용할 수 있음(하드 디스크 사용)

    - 파일 입출력 프로세스
        파일 열기       →   파일 읽기/쓰기      →   파일 닫기
        f=open(파일경로)    f.read()/f.write()      f.close()
'''
# 위험한 방법 - 파일 열기/닫기 수동 작업
# 1단계 : 파일 열기(open) - 파일과 연결 통로 생성
import random
import pickle

try:
    file = open("Python/TEST/member.txt", "r", encoding="utf-8")

# 2단계 - 파일 작업(Read/Write) - 데이터 읽기/쓰기
    content = file.read()
    print(content)

# 3단계 - 파일 닫기(close) - 연결 종료 (반드시 해야 함!)
    file.close()
except FileNotFoundError:
    print("member.txt 파일이 존재하지 않습니다.")

except Exception as e:
    print(f'파일 처리 중 오류 발생 : {e}')

# 안전한 방법 - with문(권장!) / 파일 자동 닫기
with open("Python/TEST/member.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
    # 자동으로 f.close()

# 새 파일 생성 또는 덮어쓰기
with open("Python/TEST/test.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")
    f.write("파이썬 파일 입출력\n")

with open("Python/TEST/test.txt", "a", encoding="utf-8") as f:
    f.write("추가된 내용\n")

######################################################################################################
# 파일 열기 open()

'''
- open() 함수 : 파일을 열어 파일 객체(file,object)를 반환하는 내장 함수
- 파일 객체 : open()으로 반환되는 객체로, 이 객체를 통해 파일의 내용을 읽거나 쓰는 메서드
        (read, write 등)을 사용할 수 있음

- 주요 파일 객체 메서드
    read() : 전체 내용을 문자열로 읽음
    .readline() : 한 줄씩 읽음
    .readlines() : 모든 줄을 리스트로 읽음
    .wite() : 문자열을 파일에 씀
    .close() : 파일을 닫음

* 기본 문법
open(file, mode='r', encoding= None)

    - file : 읽고자 하는 파일의 경로
    - mode : 열기 모드 (기본값은 'r' 읽기 모드)
    - encoding : 텍스트 파일의 인코딩 방식 (ex) 'utf-8', 'cp949')
'''

'''
파일 인코딩

    사람이 읽는 문자(예: '가', 'A')를 컴퓨터가 저장하고 처리할 수 있는 이진수로 바꾸는 방식
        - 서로 다른 인코딩으로 저장/읽기 시, 글자가 깨질 수 있음(대표적으로 한글 깨짐 현상 발생)
        - Python의 open()에서 기본 인코딩은 UTF-8 (Python 3 기준)

        * 대표 인코딩 방식

        인코딩      설명                        주요 특징
        UTF-8   국제 표준 인코딩               전 세계 언어 지원, 웹 표준
        CP949   마이크로소프트의 한글 인코딩    옛 Window에서 한글 처리 사용됨
        ASCII   영어 및 숫자 중심               한글 미지원

* 인코딩 지정 방법

# UTF-8 인코딩으로 파일 열기
with open("data.txt", "r", encoding= "utf-8") as f:
    print(f.read())

# CP949 (Windows 한글 파일) 인코딩으로 읽기
with open("old_data.txt", "r", encoding= "cp949") as f:
    print(f.read())  

* 파일 열기 모드 종류

모드    설명
'r'     읽기 전용(파일이 존재하지 않으면 오류 발생)
'w'     쓰기 전용(파일이 존재하면 내용 삭제 후 새로 작성)
'a'     추가 모드(기존 내용 뒤에 이어쓰기)
'b'     바이너리 모드(이미지, 영상 등)
        단독이 아니라 rb, wb, ab 처럼 다른 모드와 함께 사용됨
'x'     배타적 생성 모드(파일이 존재하면 오류)
'r+'    읽기/쓰기 겸용
'w+'    읽기 쓰기 겸용(기존 내용 삭제)
'a+'    읽기/쓰기 겸용(추가 모드)
'''

######################################################################################################
# 파일 닫기 close()

'''
close() 함수 : 열린 파일을 닫아 시스템 자원을 해제하는 내장 함수

* 반드시 해야 하는 이유
    - 파일을 닫지 않으면 시스템 자원(메모리, 파일 핸들 등)이 해제되지 않아 누수(leak)가 발생할 수 있음
    - 파일이 잠긴 채로 남아 다른 프로그램이 접근하지 못할 수 있음
    - 데이터가 디스크에 제대로 쓰이지 않을 수 있음(버퍼 미처리)
    - 프로그램이 사용하는 자원이 계속 증가할 수 있음
'''

# 사용 예제
# 파일을 쓰기 모드('w')로 열고 파일 객체를 f에 저장합니다.
f = open("example.txt", "w", encoding="utf-8")

# 파일에 문자열을 씁니다.
f.write("파이썬 파일 입출력 예제입니다.\n")
f.write("이 파일을 write()로 작성되었습니다.\n")

# 파일을 닫아 자원을 해제하고, 내용이 안전하게 저장되도록 합니다.
f.close()

######################################################################################################
# 파일 읽기 read()

'''
* 파일 읽기 주요 메서드

메서드      설명
read()      전체 텍스트를 문자열로 반환     메모리 비효율(메모리에 전체 텍스트 크기만큼 사용됨)     간단하지만 대용량 파일 처리 시, 메모리 부족 위험
readline()  한 줄씩 반환                    메모리 효율적(메모리에 한 줄 텍스트 크기만큼 사용됨)    메모리 효율적, 대용량 파일 처리 가능
readlines() 줄 목록을 리스트로 반환         메모리 비효율(전체 파일 메모리에 로드)                  대용량 파일 처리에 부적함
tell()      현재 파일 포인터 위치 확인
seek(n)     n 위치로 파일 포인터 이동
'''

# 사용 예제 - read() : 전체 내용을 문자열로 한 번에 읽기
f = open("example.txt", "r", encoding="utf-8")
content = f.read()
print(content)
f.close()

'- 모든 텍스트를 한꺼번에 읽어 하나의 문자열로 반환'
'- 줄바꿈 문자(\n) 포함됨'
'- r 모드 : 파일을 읽기 위해서 연다.(기본값)'

# 문자열 전체 읽기
with open("Python/TEST/test.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 지정한 크기 만큼만 읽기
with open("Python/TEST/test.txt", "r", encoding="utf-8") as f:
    content = f.read(3)  # 3byte 만큼 읽기
    print(content)

# 사용 예제 - readline() : 한 줄씩 순차적으로 읽기
f = open("example.txt", "r", encoding="utf-8")
line1 = f.readline()
line2 = f.readline()
print("첫 번째 줄", line1.strip())
print("두 번째 줄", line2.strip())
f.close()

'- 호출할 때마다 한 줄씩 반환'
'- 텍스트 파일을 줄 단위로 처리할 때 유용'

with open("Python/TEST/test.txt", "r", encoding="utf-8") as f:
    line1 = f.readline()
    line2 = f.readline()
    print("첫 번째 줄", line1)
    print("두 번째 줄", line2)

with open("Python/TEST/test.txt", "r", encoding="utf-8") as f:
    line1 = f.readline()
    line2 = f.readline()
    print("첫 번째 줄 strip() 처리", line1.strip())
    print("두 번째 줄 strip() 처리", line2.strip())

# 사용 예제 - 반복문을 활용한 파일 기능 - readline() for 문
f.open("example.txt", "r", encoding="utf-8")
for line in f:
    print(line.strip())
f.close()

'- 파일 객체는 반복 가능한 이터러블 → for문에 직접 사용 가능'
'- strip() 함수 : 문자열 양쪽에 있는 공백 문자(스페이스, 탭\t, 줄바꿈\n 등)을 제거'

with open('example.txt', 'r', encoding='utf-8') as f:
    line_number = 1
    for line in f:  # 파일의 각 줄을 순차적으로 처리 (메모리 절약!)
        print(f"{line_number}번째 줄: {line.strip()}")
        line_number += 1

        # 대용량 파일 처리 예시: 조건에 따라 중단 가능
        # if line_number > 1000:  # 1000줄까지만 처리
        #     break

# 사용 예제 - readlines() : 모든 줄을 리스트로 읽기
f.open("example.txt", "r", encoding="utf-8")
lines = f.readlines()
print("줄 목록:", lines)
f.close()

'- 줄 단위 문자열을 리스트 형태로 반환'
'- ["첫 줄\n", "둘째 줄\n", "셋째 줄\n"] 형태'

with open("Python/TEST/test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
        
with open('Python/TEST/test.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()  # 모든 줄을 리스트로 반환
    print(f"읽은 줄 수: {len(lines)}")
    print("각 줄의 원본 데이터:")
    for i, line in enumerate(lines):
        print(f"  {i+1}: {repr(line)}")  # repr(): 특수문자도 보여줌

    print("\n정리된 내용:")
    for i, line in enumerate(lines):
        print(f"  {i+1}: {line.strip()}")

# 사용 예제 - tell() : 현재 읽고 있는 위치(바이트)를 반환
# 사용 예제 - readlines() : 모든 줄을 리스트로 읽기
f.open("example.txt", "r", encoding="utf-8")
print("처음 위치:", f.tell())   # 일반적으로 0
f.read(5)
print("5바이트 읽은 후 위치:", f.tell())
f.close()

'- 반환 값은 바이트 기준 위치'
'- 한글은 UTF-8 인코딩 시, 1글자당 3바이트일 수 있음'

# 사용 예제 - seek(offset) : 파일 포인터 위치를 이동
f.open("example.txt", "r", encoding="utf-8")
print(f.read(10))   # 처음에 10번째 글자부터 읽음
f.seek(0)   # 포인터를 다시 맨 처음으로 이동
print("다시 처음부터", f.readline().strip())
f.close()

'- seek(0)은 파일의 맨 처음으로 이동'
'- 텍스트를 반복해서 읽거나, 중간 위치로 이동할 때 사용'

with open("Python/TEST/test.txt", "r", encoding="utf-8") as f:
    print("처음 위치:", f.tell())   # 일반적으로 0
    line1 = f.readline()
    print("첫 번째 줄 strip() 처리", line1.strip())
    print("첫 번째 줄 읽고 난 다음 위치", f.tell())
    line2 = f.readline()
    print("두 번째 줄 strip() 처리", line2.strip())
    print("두 번째 줄 읽고 난 다음 위치", f.tell())
    f.seek(0)   # 포인터 처음으로
    line3 = f.readline()
    print("세 번째 줄 strip() 처리", line3.strip())
    print("세 번째 줄 읽고 난 다음 위치", f.tell())
    f.seek(18)   # 포인터 18바이트 자리에 위치
    line4 = f.readline()
    print("네 번째 줄 strip() 처리", line4.strip())
    print("네 번째 줄 읽고 난 다음 위치", f.tell())

# 처음 위치: 0
# 첫 번째 줄 strip() 처리 Hello, World!
# 첫 번째 줄 읽고 난 다음 위치 15
# 두 번째 줄 strip() 처리 파이썬 파일 입출력
# 두 번째 줄 읽고 난 다음 위치 43
# 세 번째 줄 strip() 처리 Hello, World!
# 세 번째 줄 읽고 난 다음 위치 15
# 네 번째 줄 strip() 처리 이썬 파일 입출력
# 네 번째 줄 읽고 난 다음 위치 43

######################################################################################################
# 파일 쓰기 write()

'''
write() 함수
    - 파일에 문자열을 작성하는 기능을 제공
    - 문자열을 인자로 받아 파일에 기록하며, 호출할 때마다 포인터가 이동함

* 기본 문법
file_object.write(string)
    - string : 작성할 문자열
    - 반환값 : 기록한 문자열의 길이(문자 개수)
'''

# 사용 예제
f = open("write_example.txt", "w", encoding="utf-8")
chars_written = f.write("파이썬으로 파일 쓰기 예제입니다.")
print("작성한 문자 수 : ", chars_written)
f.close()

# 사용 예제 - 줄바꿈 처리(\n)
f = open("write_example.txt", "w", encoding="utf-8")
f.write("첫 번째 줄입니다.\n")
f.write("두 번째 줄입니다.\n")
f.write("세 번째 줄입니다.\n")
f.close()

'- 파일에 여러 줄을 작성할 때에는 줄바꿈 문자를 직접 추가해야 함'

'''
파일 덮어쓰기 vs 추가쓰기 모드

    - 'w'모드 : 덮어쓰기
        - 파일이 존재하면 기존 내용을 모두 삭제하고 새로 작성
        - 파일이 없으면 새로 생성
    
    - 'a'모드 : 추가쓰기
        - 기존 파일 끝에 새로운 내용을 추가
        - 파일이 없으면 새로 생성
'''

# 사용 예제 - w 모드
f = open("write_example.txt", "w", encoding="utf-8")
f.write("이전 내용은 삭제되고 새로 작성됩니다.")
f.close()

# 사용 예제 - a 모드
f = open("write_example.txt", "a", encoding="utf-8")
f.write("\n이 내용은 기존 내용 뒤에 추가됩니다.")
f.close()

# 사용 예제
# w 모드
f = open("test_mode.txt", "w", encoding="utf-8")
f.write("Hello")
f.close()

# w 모드 덮어쓰기
f = open("test_mode.txt", "w", encoding="utf-8")
f.write("World")
f.close()

# a 모드 추가쓰기
f = open("test_mode.txt", "a", encoding="utf-8")
f.write("\nPython")
f.close()

######################################################################################################
# with

'''
with 문 : 파일 작업 시, 컨텍스트 관리자를 사용해 블록이 끝나면 자동으로 close()를 호출해 주는 안전한 파일 처리 구문

* 기본 문법

    with open("파일경로", "모드", encoding="utf-8") as 파일객체:
        # 파일 작업 수행

    - 파일 객체 : open()으로 반환된 파일 객체를 받는 변수
    - with 블록이 끝나면 자동으로 close()가 호출됨
'''

# 사용 예제 - 파일 쓰기
with open("with_example.txt", "w", encoding="utf-8") as f1:
    f1.write("이 파일은 with문을 사용하여 작성되었습니다.")

# 사용 예제 - 파일 읽기
with open("with_example.txt", "r", encoding="utf-8") as f2:
    data = f2.read()
    print(data)

# 사용 예제 - with 문을 활용한 파일 처리
#           word.txt 파일 만들고, 랜덤 추출하기

# 단어를 파일에 작성
with open("word.txt", "w", encoding="utf-8") as f:
    word = [
        'sky', 'earth', 'moon', 'flower', 'tree', 'strawberry',
        'grape', 'garlic', 'onion', 'potato'
    ]
    for i in word:
        f.write(i + " ")


# 단어를 랜덤 추출
with open("word.txt", "r", encoding="utf-8") as f:
    data = f.read().split()
    word = random.choice(data)
    print(word)

# 사용 예제 - with 문을 활용한 파일 처리
#           입력 받아 파일 쓰기
with open("./output/input.txt", "a", encoding="utf-8") as f:
    while True:
        text = input("저장할 내용을 입력해 주세요(종료 - z) : ")
        if text == 'z' or text == 'Z':
            break
        f.write(text)
        f.write("\n")

######################################################################################################
# 실습 1 회원 명부 작성하기

'''
1. 사용자에게 3명의 회원에 대한 이름, 비밀번호 입력 받기
2. 사용자로부터 입력된 정보를 member.txt에 기록(파일 쓰기모드)
3. member.txt에 저장된 회원명부 출력(파일 읽기모드)
'''
filename_member = "Python/TEST/member.txt"
filename_member_tel = "Python/TEST/member_tel.txt"
sepchar = ","
endchar = "\n"

# 회원 이름, 비밀번호 입력받아 쓰기
with open(filename_member, "w", encoding="utf-8") as f:
    for i in range(3):
        name = input(f"{i+1}번째 회원 이름을 입력하세요: ")
        password = input(f"{i+1}번째 회원 비밀번호를 입력하세요: ")
        f.write(name + sepchar + password + endchar)

print("\n=== 현재 회원 명부 ===")
with open(filename_member, "r", encoding="utf-8") as f:
    print(f.read())

######################################################################################################
# 실습 2 회원 명부를 이용한 로그인 기능

'''
앞에서 만든 member.txt 회원 명부를 활용해서

1. 사용자에게 "이름을 입력하세요."라는 메세지를 출력한 뒤 이름 입력 받기
2. 사용자에게 "비밀번호를 입력하세요."라는 메세지를 출력한 뒤 비번 입력 받기
3. member.txt 에서 한 줄씩 "이름"과 "비번"을 검사하여 로그인 성공 시 "로그인 성공" 실패 시 "로그인 실패" 출력
'''

# with open("Python/TEST/member.txt", "r", encoding="utf-8") as f:
#     name = input("이름을 입력하세요. : ")
#     password = input("비밀번호를 입력하세요 : ")

#     for r in f.readlines():
#         n, p = r.split()
#         if name == n and password == p:
#             print("로그인 성공")
#         else:
#             print("로그인 실패")


######################################################################################################
# 실습 3 로그인 성공 시 전화번호 저장하기

'''
1. 로그인 성공 시, 사용자에게 "전화번호를 입력하세요." 라는 메시지를 출력한 뒤 전화번호 입력 받기
2. 사용자로부터 입력 받은 전화번호를 이름과 함께 member_tel.txt에 기록하기
3. 새로운 사람이 로그인 성공 시, member_tel.txt에 전화번호 추가하기
4. member_tel.txt에 이미 존재하는 사람이 로그인 성공 시 전화번호 수정하기
'''

# with open("Python/TEST/member.txt", "r", encoding="utf-8") as f1:
#     name = input("이름을 입력하세요. : ")
#     password = input("비밀번호를 입력하세요 : ")
#     b = False

#     for r in f1.readlines():
#         n, p = r.split()
#         if name == n and password == p:
#             print("로그인 성공")
#             b = True
#             break

#         else:
#             print("로그인 실패")

#     if b:
#         with open("Python/TEST/member.txt", "a", encoding="utf-8") as f2:
#             tel = input("전화번호를 입력하세요. : ")
#             f2.write(" ", tel)

login_name = input("이름을 입력하세요: ")
login_password = input("비밀번호를 입력하세요: ")

login_success = False

with open(filename_member, "r", encoding="utf-8") as f:
    for line in f:
        name, password = line.strip().split(sepchar)
        if name == login_name and password == login_password:
            login_success = True

if login_success:
    print("로그인 성공")

# 전화번호 입력 및 저장/수정
    phone_number = input("전화번호를 입력하세요: ")

    # 기존 member_tel.txt 읽기
    member_tel = {}
    try:
        with open(filename_member_tel, "r", encoding="utf-8") as f:
            for line in f:
                n, tel = line.strip().split(sepchar)
                member_tel[n] = tel
    except FileNotFoundError:
        # 파일이 없는 경우 새로 생성
        with open(filename_member_tel, "w", encoding="utf-8") as f:
            f.write("")

    # 새 전화번호 추가 또는 기존 번호 수정
    member_tel[login_name] = phone_number

    # member_tel.txt에 저장
    with open(filename_member_tel, "w", encoding="utf-8") as f:
        for n, tel in member_tel.items():
            f.write(n + sepchar + tel + endchar)

else:
    print("로그인 실패")

######################################################################################################
# 실습 1~3 에단 리더님 답변

"""
이 프로그램은 파일 입출력과 예외 처리를 활용하여
회원 정보 관리와 전화번호 저장 기능을 제공합니다.

주요 기능:
1. 회원 가입 (이름, 비밀번호를 파일에 저장)
2. 로그인 검증 (파일에서 회원 정보 확인)
3. 전화번호 저장/수정 (로그인 성공 시)
"""

def saved_phone(input_id):
    """
    로그인한 회원의 전화번호를 저장하거나 수정하는 함수

    매개변수:
        input_id (str): 로그인한 회원의 이름

    동작 과정:
        1. 사용자로부터 전화번호 입력받기
        2. 기존 전화번호 파일 읽기 (없으면 새로 생성)
        3. 딕셔너리에 모든 회원의 전화번호 저장
        4. 현재 사용자의 전화번호 추가/수정
        5. 업데이트된 정보를 파일에 다시 저장
    """
    print(f"\n=== {input_id}님의 전화번호 등록 ===")

    # 사용자로부터 전화번호 입력받기
    input_phone = input('전화번호를 입력하세요 (예: 010-1234-5678): ')

    # 전화번호를 저장할 딕셔너리 초기화
    members = {}  # {이름: 전화번호} 형태로 저장할 딕셔너리

    # 기존 전화번호 파일이 있는지 확인하고 읽어오기
    try:
        print("📁 기존 전화번호 파일을 확인하는 중...")

        # 'member_tel.txt' 파일을 읽기 모드로 열기
        with open('member_tel.txt', 'r', encoding='utf-8') as f2:
            # 파일의 각 줄을 순서대로 처리
            for line in f2:
                # line.strip(): 앞뒤 공백과 개행문자 제거
                # split(): 공백을 기준으로 문자열을 나누어 리스트로 변환
                # 예: "철수 010-1234-5678\n" → ["철수", "010-1234-5678"]
                saved_name, saved_phone = line.strip().split()

                # 딕셔너리에 기존 회원들의 전화번호 저장
                members[saved_name] = saved_phone

        print(f"✅ 기존 회원 {len(members)}명의 전화번호를 불러왔습니다.")

        # 현재 상태 출력 (디버깅 및 확인용)
        print("현재 저장된 전화번호:")
        for name, phone in members.items():
            print(f"  - {name}: {phone}")

    except FileNotFoundError:
        # 파일이 존재하지 않는 경우 (첫 번째 실행)
        print("📝 전화번호 파일이 없습니다. 새로 생성합니다.")

    except Exception as e:
        # 파일 읽기 중 다른 오류 발생 시
        print(f"⚠️ 파일 읽기 중 오류 발생: {e}")
        print("빈 상태로 시작합니다.")

    # 현재 로그인한 사용자의 전화번호 추가 또는 업데이트
    old_phone = members.get(input_id, None)  # 기존 전화번호 확인

    if old_phone:
        print(f"📞 기존 전화번호: {old_phone}")
        print(f"🔄 새 전화번호로 업데이트: {input_phone}")
    else:
        print(f"📞 새 전화번호 등록: {input_phone}")

    # 딕셔너리에 전화번호 추가/수정
    # 키가 이미 있으면 값이 수정되고, 없으면 새로 추가됨

    members[input_id] = input_phone

    # 업데이트된 전화번호 딕셔너리를 파일에 저장
    try:
        print("💾 전화번호 파일을 업데이트하는 중...")

        # 'member_tel.txt' 파일을 쓰기 모드로 열기 (기존 내용은 덮어씀)
        with open('member_tel.txt', 'w', encoding='utf-8') as f2:
            # 딕셔너리의 모든 항목을 파일에 저장
            for name, phone in members.items():
                # 각 줄에 "이름 전화번호" 형태로 저장
                f2.write(f'{name} {phone}\n')

        print("✅ 전화번호가 성공적으로 저장되었습니다!")

        # 최종 저장 상태 확인
        print("\n📋 최종 저장된 전화번호 목록:")
        for name, phone in members.items():
            status = "🆕" if name == input_id and not old_phone else "🔄" if name == input_id else "📞"
            print(f"  {status} {name}: {phone}")

    except Exception as e:
        print(f"❌ 파일 저장 중 오류 발생: {e}")
        print("전화번호 저장에 실패했습니다.")


def register_members():
    """
    실습 1: 회원 가입 기능
    3명의 회원 정보(이름, 비밀번호)를 입력받아 파일에 저장
    """
    print("=" * 50)
    print("📝 회원 가입")
    print("=" * 50)

    try:
        # 'member.txt' 파일을 쓰기 모드로 열어서 회원 정보 저장
        with open('member.txt', 'w', encoding='utf-8') as f:
            print("3명의 회원 정보를 입력해주세요.\n")

            # 3명의 회원 정보 입력받기
            for i in range(3):
                print(f"--- {i+1}번째 회원 ---")

                # 사용자 입력받기
                user_id = input('이름을 입력해주세요: ').strip()
                user_pw = input('비밀번호를 입력해주세요: ').strip()

                # 입력값 검증
                if not user_id or not user_pw:
                    print("⚠️ 이름과 비밀번호는 필수입니다!")
                    i -= 1  # 다시 입력받기
                    continue

                # 파일에 "이름 비밀번호" 형태로 저장
                f.write(f'{user_id} {user_pw}\n')
                print(f"✅ {user_id}님 가입 완료!\n")

        print("🎉 모든 회원 가입이 완료되었습니다!")

        # 저장된 회원 목록 확인
        print("\n📋 가입된 회원 목록:")
        with open('member.txt', 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, 1):
                user_id = line.split()[0]  # 이름만 추출 (비밀번호는 보안상 숨김)
                print(f"  {i}. {user_id}")

    except Exception as e:
        print(f"❌ 회원 가입 중 오류 발생: {e}")


def login_and_save_phone():
    """
    실습 2: 로그인 검증 및 전화번호 저장 기능
    저장된 회원 정보로 로그인하고, 성공 시 전화번호 저장 기능 실행
    """
    print("\n" + "=" * 50)
    print("🔐 로그인")
    print("=" * 50)

    try:
        # 회원 파일이 존재하는지 확인
        with open('member.txt', 'r', encoding='utf-8') as f:
            # 사용자로부터 로그인 정보 입력받기
            print("로그인 정보를 입력해주세요.")
            input_id = input('이름을 입력해주세요: ').strip()
            input_pw = input('비밀번호를 입력해주세요: ').strip()

            print("\n🔍 회원 정보를 확인하는 중...")

            # 파일의 각 줄을 확인하여 로그인 정보 검증
            login_success = False

            for line_num, line in enumerate(f, 1):
                try:
                    # 각 줄에서 이름과 비밀번호 분리
                    # strip(): 개행문자 제거, split(): 공백으로 분리
                    user_id, user_pw = line.strip().split()

                    print(f"  📄 {line_num}번째 회원 정보 확인 중...")

                    # 입력받은 정보와 파일의 정보 비교
                    if user_id == input_id and user_pw == input_pw:
                        print(f"✅ 로그인 성공! {input_id}님 환영합니다!")
                        login_success = True

                        # 로그인 성공 시 전화번호 저장 함수 호출
                        saved_phone(input_id)
                        break  # 로그인 성공했으므로 반복문 종료

                except ValueError:
                    # 파일 형식이 올바르지 않은 경우 (이름 비밀번호가 아닌 다른 형태)
                    print(f"⚠️ {line_num}번째 줄 형식 오류: '{line.strip()}'")
                    continue

            # for-else: for문이 break 없이 정상 완료된 경우 실행
            else:
                if not login_success:
                    print("❌ 로그인 실패!")
                    print("이름 또는 비밀번호를 확인해주세요.")

                    # 등록된 회원 목록 힌트 제공
                    print("\n💡 등록된 회원 목록:")
                    f.seek(0)  # 파일 포인터를 처음으로 이동
                    for i, line in enumerate(f, 1):
                        try:
                            user_id = line.split()[0]
                            print(f"  {i}. {user_id}")
                        except:
                            continue

    except FileNotFoundError:
        print("❌ 회원 파일을 찾을 수 없습니다!")
        print("먼저 회원 가입을 진행해주세요.")

    except Exception as e:
        print(f"❌ 로그인 중 오류 발생: {e}")


def display_all_members():
    """
    저장된 모든 회원 정보를 표시하는 함수 (디버깅/확인용)
    """
    print("\n" + "=" * 50)
    print("👥 전체 회원 정보")
    print("=" * 50)

    try:
        # 회원 기본 정보 표시
        print("📋 회원 목록 (member.txt):")
        with open('member.txt', 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, 1):
                try:
                    user_id, user_pw = line.strip().split()
                    # 보안을 위해 비밀번호는 * 로 마스킹
                    masked_pw = '*' * len(user_pw)
                    print(f"  {i}. {user_id} ({masked_pw})")
                except:
                    print(f"  {i}. 형식 오류: {line.strip()}")

    except FileNotFoundError:
        print("📂 member.txt 파일이 없습니다.")

    try:
        # 전화번호 정보 표시
        print("\n📞 전화번호 목록 (member_tel.txt):")
        with open('member_tel.txt', 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, 1):
                try:
                    name, phone = line.strip().split()
                    print(f"  {i}. {name}: {phone}")
                except:
                    print(f"  {i}. 형식 오류: {line.strip()}")

    except FileNotFoundError:
        print("📂 member_tel.txt 파일이 없습니다.")


def main_menu():
    """
    메인 메뉴를 표시하고 사용자 선택을 처리하는 함수
    """
    while True:
        print("\n" + "=" * 60)
        print("🏠 파일 기반 회원 관리 시스템")
        print("=" * 60)
        print("1️⃣ 회원 가입 (3명 등록)")
        print("2️⃣ 로그인 및 전화번호 저장")
        print("3️⃣ 전체 회원 정보 보기")
        print("4️⃣ 프로그램 종료")
        print("=" * 60)

        try:
            choice = input("선택하세요 (1-4): ").strip()

            if choice == '1':
                register_members()

            elif choice == '2':
                login_and_save_phone()

            elif choice == '3':
                display_all_members()

            elif choice == '4':
                print("👋 프로그램을 종료합니다. 안녕히 가세요!")
                break

            else:
                print("❌ 잘못된 선택입니다. 1-4 중에서 선택해주세요.")

        except KeyboardInterrupt:
            print("\n\n⏹️ 사용자에 의해 프로그램이 중단되었습니다.")
            break

        except Exception as e:
            print(f"❌ 예상치 못한 오류 발생: {e}")


if __name__ == "__main__":
    """
    프로그램의 진입점
    직접 실행될 때만 메인 메뉴 실행
    """
    print("🚀 파일 기반 회원 관리 시스템을 시작합니다!")

    # 실제 실행 시에는 main_menu()를 호출하세요
    main_menu()

    # 코드 설명을 위한 시뮬레이션 실행
    print("\n" + "=" * 60)
    print("📚 코드 동작 시뮬레이션")
    print("=" * 60)

    # 실제 사용 예시 설명
    simulation_text = """
    
실제 프로그램 실행 순서:

1️⃣ 회원 가입 단계:
   - register_members() 함수 실행
   - 3명의 이름과 비밀번호 입력
   - member.txt 파일에 저장
   
2️⃣ 로그인 단계:
   - login_and_save_phone() 함수 실행  
   - 저장된 회원 정보로 로그인 시도
   - 성공 시 saved_phone() 함수 자동 호출
   
3️⃣ 전화번호 저장 단계:
   - 기존 member_tel.txt 파일 읽기 (없으면 생성)
   - 딕셔너리에 모든 전화번호 로드
   - 현재 사용자 전화번호 추가/수정
   - 업데이트된 정보를 파일에 저장

💡 핵심 개념:
   - 파일 입출력: 데이터 영구 저장
   - 예외 처리: 파일 없음, 형식 오류 등 처리  
   - 딕셔너리: 메모리에서 빠른 검색/수정
   - 문자열 처리: split(), strip() 활용
"""

    print(simulation_text)

    # 파일 형식 예시
    print("\n📁 파일 형식 예시:")
    print("member.txt:")
    print("철수 1234")
    print("영희 abcd")
    print("민수 5678")
    print()
    print("member_tel.txt:")
    print("철수 010-1111-2222")
    print("영희 010-3333-4444")

    print("\n✅ 코드 분석이 완료되었습니다!")
    print("실제 실행하려면 main_menu() 함수의 주석을 해제하세요.")


######################################################################################################
# 바이너리 파일 읽고 쓰기

'''
바이너리 파일 : 0과 1로 이루어진 이진 데이터를 포함한 파일
이미지(.jpg), 오디오(.mp3), 영상(.mp4), 실행 파일(.exe) 등이 대표적인 바이너리 파일

* 파일 모드

모드        설명
'rb'    바이너리 파일 읽기(Read Binary)
'wb'    바이너리 파일 쓰기(Write Binary), 기존 내용 삭제 후 작성
'ab'    바이너리 파일 추가(Append Binary), 기존 내용 뒤에 이어쓰기
'rb+'   읽기와 쓰기를 동시에
'wb+'   쓰기와 읽기를 동시에(덮어쓰기)
'''

# 사용 예제 - 바이너리 파일 쓰기
with open("./output/data.bin", 'wb') as f1:
    txt = "드론이 비행한다."
    # f.write(txt)  #TypeError : 문자열을 직접 쓰면 오류 발생
    f1.write(txt.encode())   # 문자열을 바이트로 인코딩 후 작성

# 사용 예제 - 바이너리 파일 읽기
with open("./output/data.bin", 'rb') as f2:
    data = f2.read()
    print(data)             # 바이트 형태로 출력
    print(data.decode())    # 디코딩하여 문자열로 출력
    print(f"바이너리 데이터 크기: {len(data)} 바이트")
    print(f"바이너리 데이터 일부: {data[:50]}")  # 처음 50바이트만 출력

'- "wb"모드 : 바이너리 쓰기 모드 → 문자열은 endcode()로 변환 후 작성'
'- "rb"모드 : 바이너리 읽기 모드 → 바이트 데이터를 decode()로 다시 문자열 반환'

'''
이미지 복사하기 : 이미지 파일을 읽어와서 다른 이름으로 쓰기
'''

# 원본 이미지 읽기
with open("paragliber.jpg", "rb") as f1:
    img = f1.read()

# 복사된 이미지를 새로운 파일로 저장
with open("./output/paraglider.jpg", "wb") as f2:
    f2.write(img)   # 바이너리 데이터 그대로 복사

######################################################################################################
# pickle 모듈

'''
pickle 모듈
    - 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있는 모듈이다.
    - 이때 객체란, 리스트나 딕셔너리 등의 자료구조도 포함한다.

* 모드
    - pickle.dump   : 쓰기
    - pickle.load   : 읽기
'''

# 사용 예제


# 리스트와 딕셔너리를 파일에 저장
with open("./output/data.txt", "wb") as f:
    li = ["강아지", "고양이", "닭"]
    dic = {1: "강아지", 2: "고양이", 3: "닭"}
    pickle.dump(li, f)  # 리스트 쓰기
    pickle.dump(dic, f)  # 딕셔너리 쓰기

# 저장한 데이터를 다시 읽어오기
with open("./output/data.txt", "rb") as f:
    li = pickle.load(f)
    dic = pickle.load(f)
    print(li)   # ['강아지', '고양이', '닭']
    print(dic)  # {1: '강아지', 2: '고양이', 3: '닭'}
    
    
# 정리용 파일들 삭제 (선택적)
import os

try:
    os.remove('test_data.txt')
    os.remove('test_data_copy.txt')
    os.remove('output.txt')
    print("\n테스트 파일들이 정리되었습니다.")
except:
    pass

"""
텍스트 모드:
  'r'  : 읽기 전용 (기본값)
  'w'  : 쓰기 전용 (파일이 있으면 덮어씀, 없으면 생성)
  'a'  : 추가 모드 (파일 끝에 내용 추가)
  'x'  : 배타적 생성 (파일이 이미 있으면 에러)
  'r+' : 읽기/쓰기 (파일이 반드시 존재해야 함)
  'w+' : 읽기/쓰기 (파일이 있으면 덮어씀, 없으면 생성)

바이너리 모드 (위 모드에 'b' 추가):
  'rb' : 바이너리 읽기
  'wb' : 바이너리 쓰기
  'ab' : 바이너리 추가
  
인코딩:
  encoding='utf-8'  : 한글 등 유니코드 문자 처리 (권장)
  encoding='cp949'  : 한국어 윈도우 기본 인코딩
  encoding='ascii'  : 영어만 지원
"""
"""
💡 실전 팁:

1. 항상 with문 사용하기
   - 파일이 자동으로 닫혀서 안전
   - 예외 발생 시에도 파일이 제대로 닫힘

2. 인코딩 명시하기
   - encoding='utf-8' 사용 권장
   - 한글 깨짐 현상 방지

3. 대용량 파일 처리
   - read() 대신 readline()이나 for문 사용
   - 메모리 효율성 고려

4. 예외 처리하기
   - FileNotFoundError: 파일이 없을 때
   - PermissionError: 권한이 없을 때
   - UnicodeDecodeError: 인코딩 문제

5. 파일 경로 주의
   - 절대경로 vs 상대경로
   - 운영체제별 경로 구분자 차이 (/, \\)

⚠️  주의사항:
- 'w' 모드는 기존 파일을 완전히 삭제함
- 바이너리 파일은 반드시 'b' 모드 사용
- 대용량 파일에서 read()는 메모리 부족 위험
- 파일 경로에 한글이 있으면 인코딩 문제 발생 가능
"""