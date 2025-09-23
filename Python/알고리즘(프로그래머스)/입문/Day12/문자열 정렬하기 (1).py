'''
문자열 my_string이 매개변수로 주어질 때, my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를 return 하도록 solution 함수를 작성해보세요.

* 제한 사항
    - 1 ≤ my_string의 길이 ≤ 100
    - my_string에는 숫자가 한 개 이상 포함되어 있습니다.
    - my_string은 영어 소문자 또는 0부터 9까지의 숫자로 이루어져 있습니다.
'''

import re
def solution(my_string):
    
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    result = []
    
    for s in my_string:
        if s in nums:
            result.append(int(s))
        else:
            continue
    return sorted(result)

'''
예시1)
def solution(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])

'- str.isdigit() : 문자열이 숫자로만 구성되어 있는지 확인하는 메서드
    반환값: True / False
    - 문자열이 빈 문자열이면 False
    - 공백, 부호, 소수점, 문자 포함하면 False
    - 유니코드 숫자도 True'

'isdigit() vs isnumeric() vs isdecimal()
메서드	        예시	    True 여부 설명
isdigit()	    "²"	        True (제곱, 분수 등도 포함)
isnumeric()	    "²", "½"	True (숫자와 관련된 유니코드 포함)
isdecimal()	    "123"	    True (순수 0~9 숫자만)'

예시2)
def solution(my_string):
    return sorted(map(int, filter(lambda s: s.isdigit(), my_string)))

예시3)
import re
def solution(my_string):
    return sorted(map(int, (list(re.sub('[^0-9]', '', my_string)))))
'''