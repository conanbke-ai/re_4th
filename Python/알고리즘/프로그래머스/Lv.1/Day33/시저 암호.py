'''
어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. 
"z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

* 제한 조건
    - 공백은 아무리 밀어도 공백입니다.
    - s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
    - s의 길이는 8000이하입니다.
    - n은 1 이상, 25이하인 자연수입니다.
'''

# def solution(s, n):
    
#     result = ""

#     for i in s:
#         if i == "z":
#             result += chr(96 + n)
#         elif i == "Z":
#             result += chr(64 + n)
#         elif i == " ":
#             result += " "
#         else:
#             result += chr(ord(i) + n)

#     return result
'- 특수문자 처리 안됨'

def solution(s, n):
    result = ""

    for i in s:
        if i.islower():  # 소문자
            result += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
        elif i.isupper():  # 대문자
            result += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
        else:  # 공백, 특수문자 등
            result += i

    return result