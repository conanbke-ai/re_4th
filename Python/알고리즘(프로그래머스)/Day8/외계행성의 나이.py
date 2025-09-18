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
    
'''