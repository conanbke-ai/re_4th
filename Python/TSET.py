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
            f.write(n + sepchar + tel + endchar)

else:
    print("로그인 실패")
