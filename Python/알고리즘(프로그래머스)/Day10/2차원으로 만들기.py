'''
정수 배열 num_list와 정수 n이 매개변수로 주어집니다. num_list를 다음 설명과 같이 2차원 배열로 바꿔 return하도록 solution 함수를 완성해주세요.

num_list가 [1, 2, 3, 4, 5, 6, 7, 8] 로 길이가 8이고 n이 2이므로 num_list를 2 * 4 배열로 다음과 같이 변경합니다. 2차원으로 바꿀 때에는 num_list의 원소들을 앞에서부터 n개씩 나눠 2차원 배열로 변경합니다.

num_list	                n	result
[1, 2, 3, 4, 5, 6, 7, 8]	2	[[1, 2], [3, 4], [5, 6], [7, 8]]

* 제한 사항
    - num_list의 길이는 n의 배 수개입니다.
    - 0 ≤ num_list의 길이 ≤ 150
    - 2 ≤ n < num_list의 길이
'''

# def solution(num_list, n):
#     answer = [[]]
    
#     for i, num in enumerate(num_list):
#         if i % n != 1:
#             answer.extend(num_list[i:i+n-1])
        
#     return answer

def solution(num_list, n):
    result = []
    for i in range(0, len(num_list), n):  # n개씩 건너뛰면서 슬라이싱
        result.append(num_list[i:i+n])
    return result

'''
예시1)
def solution(num_list, n):
    return [num_list[ix-n:ix] for ix in range(n, len(num_list)+1, n)]

예시2)
import numpy as np
def solution(num_list, n):
    li = np.array(num_list).reshape(-1,n)
    return li.tolist()


🧾 NumPy란?

Numerical Python의 줄임말.
파이썬에서 **과학 계산(수치 연산)**을 하기 위해 만들어진 핵심 라이브러리.
특히 배열(Array)과 행렬(Matrix) 연산에 강력합니다.

파이썬의 기본 list는 범용적이지만, 속도가 느리고 메모리 사용이 비효율적일 수 있어요.
NumPy는 C 언어 기반으로 구현되어 있어서, 훨씬 빠르고 효율적으로 대규모 수치 데이터를 처리할 수 있습니다.

✨ NumPy의 특징

- ndarray (다차원 배열) 지원
    NumPy의 핵심 객체는 ndarray (N-dimensional array).
    파이썬 리스트보다 메모리를 덜 쓰고, 연산 속도가 빠름.
    벡터 및 행렬 연산을 손쉽게 지원.
- 브로드캐스팅(Broadcasting)
    서로 다른 크기의 배열끼리도 자동으로 연산 가능.
    예: [1,2,3] + 10 → [11,12,13]

- 다양한 수학 함수 제공
    선형대수, 푸리에 변환, 통계 계산 등 과학/수학 연산 지원.
- 빠른 속도
    내부적으로 C로 구현 → 반복문을 돌지 않고 벡터화 연산 지원.
- 다른 라이브러리의 기반
    Pandas, Scikit-learn, TensorFlow, PyTorch 등 데이터/AI 라이브러리들이 NumPy 기반으로 동작.


예시3)
def solution(num_list, n):
    answer = []
    cnt = 0
    temp = []
    for num in num_list:
        temp.append(num)
        cnt += 1
        if cnt == n:
            answer.append(temp)
            temp = []
            cnt = 0

    return answer
'''