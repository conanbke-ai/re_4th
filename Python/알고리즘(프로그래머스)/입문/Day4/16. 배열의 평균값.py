'''
정수 배열 numbers가 매개변수로 주어집니다.
    numbers안의 원소의 평균값을 return 하도록 solution 함수를 완성해주세요.

* 제한사항
    0 <= numbers의 원소 <= 1000
    1 <= numbers의 길이 <= 100
    정답의 소수 부분이 .0 또는 .5인 경우만 입력으로 주어집니다.
'''

def solution(numbers):
    answer = int(sum(numbers))
    if (answer % 1) == (0.5 or 0.0) :
        return answer