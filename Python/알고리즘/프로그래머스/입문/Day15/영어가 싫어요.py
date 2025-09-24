'''
영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다. 
문자열 numbers가 매개변수로 주어질 때, numbers를 정수로 바꿔 return 하도록 solution 함수를 완성해 주세요.

* 제한 사항
    - numbers는 소문자로만 구성되어 있습니다.
    - numbers는 "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" 들이 공백 없이 조합되어 있습니다.
    - 1 ≤ numbers의 길이 ≤ 50
    - "zero"는 numbers의 맨 앞에 올 수 없습니다.
'''

def solution(numbers):
    
    nums_dict = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    
    for e, n in nums_dict.items():
        numbers = numbers.replace(e, n)
    
    return int(numbers)

# print(solution("onetwothreefourfivesixseveneightninezero"))

'- translate() 는 한 글자씩 매핑 처리만 가능하기 때문에 부정확할 수 있음'
# # 정규표현식 패턴 생성 (모든 숫자 단어)'
# pattern = re.compile("|".join(num_map.keys()))  # "zero|one|two|three|..."
# # lambda와 group() 사용하여 치환
# result = pattern.sub(lambda x: num_map[x.group()], numbers)
'- | 는 정규표현식에서 “또는(or)” 의미'
'- re.compil() : 객체화'
'- sub() : 치환'
'''
re.compile()	정규식을 객체로 만들어 여러 번 재사용 가능, 성능 향상
꼭 필요한가?	단순 1회 사용이면 re.sub("패턴", ...)만 써도 됨
                파이프라인(|)과 compile은 효율성과 깔끔함을 위해 일반적으로 쓰는 것일 뿐, 기술적으로는 없어도 됨
'''

'''
예시1)
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)
    
예시2)
def solution(numbers):
    r = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',\
         'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for k in r.keys():
        numbers = numbers.replace(k, r[k])

    return int(numbers)
    
예시3)
def solution(numbers):
    map = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    i=0
    for word in map:
        numbers = numbers.replace(word, str(i))
        i+=1
    return int(numbers)
'''