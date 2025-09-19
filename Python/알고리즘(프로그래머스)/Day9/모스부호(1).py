'''
머쓱이는 친구에게 모스부호를 이용한 편지를 받았습니다.
그냥은 읽을 수 없어 이를 해독하는 프로그램을 만들려고 합니다.
문자열 letter가 매개변수로 주어질 때, letter를 영어 소문자로 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.

모스부호는 다음과 같습니다.
morse = {
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}

* 제한사항
    - 1 ≤ letter의 길이 ≤ 1,000
    - return값은 소문자입니다.
    - letter의 모스부호는 공백으로 나누어져 있습니다.
    - letter에 공백은 연속으로 두 개 이상 존재하지 않습니다.
    - 해독할 수 없는 편지는 주어지지 않습니다.
    - 편지의 시작과 끝에는 공백이 없습니다.
'''
morse = {
    '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
    '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
    '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
    '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
    '-.--': 'y', '--..': 'z'
}


def solution(letter):

    for x, y in morse.items():
        for word in letter.split(" "):
            if word == x:
                result = "".join(letter.replace(word, y))
            else:
                continue
    return result


'''
* 문제점

    1. for x, y in morse.items() → 모든 모스부호를 반복하면서 letter 전체를 replace하려고 하는 구조는 불필요하게 반복이 많습니다.
    2. letter.replace(word, y) → replace는 문자열 전체를 바꾸므로, 한 글자씩 처리하려는 의도와 맞지 않습니다.
    3. result를 반복문 안에서 덮어쓰기 때문에 마지막 반복 값만 남습니다.

* 올바른 접근 방법
    1. letter.split(" ") → 모스부호를 글자 단위 리스트로 분리
    2. 각 글자를 morse 딕셔너리로 변환
    3. 변환한 글자들을 "".join()으로 합쳐서 반환
'''


def solution(letter):
    # 1. 모스부호를 공백 기준으로 나누고
    words = letter.split(" ")
    # 2. 각 모스부호를 문자로 변환
    decoded = [morse[w] for w in words]
    # 3. 문자열로 합쳐서 반환
    return "".join(decoded)


'''
예시1) 
# 람다
solution = lambda letter: "".join(map(lambda w: morse[w], letter.split(" ")))

예시2)
# 모스 부호 데이터가 정확하지 않을 경우
def solution(letter):
    # 모스부호를 공백으로 나누고, 없는 부호는 '?'로 처리
    return "".join(morse.get(w, '?') for w in letter.split(" "))

예시3)
# 모스 부호 데이터가 정확하지 않은 경우 - 람다
solution = lambda letter: "".join(map(lambda w: morse.get(w, '?'), letter.split(" ")))

'''
