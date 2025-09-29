'''
우주여행을 하던 머쓱이는 엔진 고장으로 PROGRAMMERS-962 행성에 불시착하게 됐습니다. 
입국심사에서 나이를 말해야 하는데, PROGRAMMERS-962 행성에서는 나이를 알파벳으로 말하고 있습니다. 
a는 0, b는 1, c는 2, ..., j는 9입니다. 
예를 들어 23살은 cd, 51살은 fb로 표현합니다. 
나이 age가 매개변수로 주어질 때 PROGRAMMER-962식 나이를 return하도록 solution 함수를 완성해주세요.

* 제한사항
    - age는 자연수입니다.
    - age ≤ 1,000
    - PROGRAMMERS-962 행성은 알파벳 소문자만 사용합니다.
'''


def solution(age):

    lst = str(age)

    for i in range(len(lst)):
        if "0" in lst:
            lst = lst.replace("0", "a")
        elif "1" in lst:
            lst = lst.replace("1", "b")
        elif "2" in lst:
            lst = lst.replace("2", "c")
        elif "3" in lst:
            lst = lst.replace("3", "d")
        elif "4" in lst:
            lst = lst.replace("4", "e")
        elif "5" in lst:
            lst = lst.replace("5", "f")
        elif "6" in lst:
            lst = lst.replace("6", "g")
        elif "7" in lst:
            lst = lst.replace("7", "h")
        elif "8" in lst:
            lst = lst.replace("8", "i")
        elif "9" in lst:
            lst = lst.replace("9", "j")

    return lst


print(solution(23))


'''
예시1)
def solution(age):
    # 숫자 0~9를 a~j로 매핑
    mapping = "abcdefghij"  
    
    # age를 문자열로 바꾸고 각 자리수마다 mapping 적용
    result = ''.join(mapping[int(digit)] for digit in str(age))
    
    return result

예시2)
def alien_shift(s: str, k: int) -> str:
    res = []
    k = k % 26
    for ch in s:
        if 'a' <= ch <= 'z':
            # 'a'를 0으로 맞추고 더한 뒤 다시 문자로
            res.append(chr((ord(ch) - ord('a') + k) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            res.append(chr((ord(ch) - ord('A') + k) % 26 + ord('A')))
        else:
            res.append(ch)
    return ''.join(res)

예시3)
def alien_to_indices(s: str) -> str:
    # 알파벳이면 1~26, 아니면 문자 그대로 (혹은 다른 규칙)
    parts = []
    for ch in s:
        if 'a' <= ch <= 'z':
            parts.append(str(ord(ch) - ord('a') + 1))  # a->1
        elif 'A' <= ch <= 'Z':
            parts.append(str(ord(ch) - ord('A') + 1))  # A->1
        else:
            parts.append(ch)
    return ' '.join(parts)

예시4)
def alien_reverse_alphabet(s: str) -> str:
    res = []
    for ch in s:
        if 'a' <= ch <= 'z':
            res.append(chr(ord('z') - (ord(ch) - ord('a'))))
        elif 'A' <= ch <= 'Z':
            res.append(chr(ord('Z') - (ord(ch) - ord('A'))))
        else:
            res.append(ch)
    return ''.join(res)
'''

'''
아스키코드 참조

* ord()
    - 문자(char) → 숫자(int, 유니코드 코드포인트) 로 바꿔줌
    - 파이썬은 문자를 유니코드(Unicode) 로 처리하기 때문에 영어, 알파벳, 한글, 이모지 등 숫자로 변환 가능

* chr()
    - 숫자(int) → 문자(char) 로 바꿔줌
    - ord() 의 반대 역할
'''
