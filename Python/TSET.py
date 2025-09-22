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