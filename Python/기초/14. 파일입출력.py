# 파일입출력

'''
프로그램이 저장장치(예: 하드디스크)에 저장된 파일을 읽어오거나, 반대로 데이터를 파일에 저장하는 작업
    - 입력(input) : 파일로부터 데이터를 읽어오는 것
    - 출력(output) : 데이터를 파일로 저장(기록)하는 것
'''

'''
입, 출력 스트림

    - 스트림(Stream) : 자료 흐름이 물의 흐름과 같다는 뜻
        - 입력 스트림 : 동영상을 재생하기 위해 동영상 파일에서 자료를 읽을 때 사용함
        - 출력 스트림 : 사용자가 쓴 글을 파일에 저장할 때는 출력 스트림 사용함

    - 파일 입출력의 필요성
        - 프로그램 실행 중에 메모리에 저장된 데이터는 프로그램이 종료되면 사라짐
        - 데이터를 프로그램이 종료된 후에도 계속해서 사용하려면 파일에 저장하고
        - 필요할 때 파일을 읽어서 데이터를 사용할 수 있음

    - 파일 입출력 프로세스
        파일 열기       →   파일 읽기/쓰기      →   파일 닫기
        f=open(파일경로)    f.read()/f.write()      f.close()
'''

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
import pickle
import random
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
read()      전체 텍스트를 문자열로 반환
readline()  한 줄씩 반환
readlines() 줄 목록을 리스트로 반환
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

# 사용 예제 - readline() : 한 줄씩 순차적으로 읽기
f = open("example.txt", "r", encoding="utf-8")
line1 = f.readline()
line2 = f.readline()
print("첫 번째 줄", line1.strip())
print("두 번째 줄", line2.strip())
f.close()

'- 호출할 때마다 한 줄씩 반환'
'- 텍스트 파일을 줄 단위로 처리할 때 유용'

# 사용 예제 - readlines() : 모든 줄을 리스트로 읽기
f.open("example.txt", "r", encoding="utf-8")
lines = f.readlines()
print("줄 목록:", lines)
f.close()

'- 줄 단위 문자열을 리스트 형태로 반환'
'- ["첫 줄\n", "둘째 줄\n", "셋째 줄\n"] 형태'

# 사용 예제 - 반복문을 활용한 파일 기능
f.open("example.txt", "r", encoding="utf-8")
for line in f:
    print(line.strip())
f.close()

'- 파일 객체는 반복 가능한 이터러블 → for문에 직접 사용 가능'
'- strip() 함수 : 문자열 양쪽에 있는 공백 문자(스페이스, 탭, 줄바꿈\n 등)을 제거'

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
        f.write(f"{name}", f"{password}", sep=sepchar, end=endchar)

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
        pass

    # 새 전화번호 추가 또는 기존 번호 수정
    member_tel[login_name] = phone_number

    # member_tel.txt에 저장
    with open(filename_member_tel, "w", encoding="utf-8") as f:
        for n, tel in member_tel.items():
            f.write(f"{n}", f"{tel}", sep=sepchar, end=endchar)

else:
    print("로그인 실패")

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
    f2.write(img)

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
