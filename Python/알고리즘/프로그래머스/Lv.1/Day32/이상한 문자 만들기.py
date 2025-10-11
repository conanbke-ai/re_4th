'''
문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 
각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 
각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

* 제한 사항
    - 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
    - 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.
'''

def solution(s):
    result = ""
                                # split() 와 다름
    for word in s.split(" "):  # 공백 기준으로 단어 분리 # 공백 개수 유지를 위함
        for i, c in enumerate(word):
            if i % 2 == 0:
                result += c.upper()
            else:
                result += c.lower()
        result += " "  # 단어 끝에 공백 추가
    
    return result[:-1]  # 마지막 공백 제거

'''
예시1)
def solution(s):
    return " ".join(
        "".join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(word))
        for word in s.split(" ")
    )

예시2)
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

'''