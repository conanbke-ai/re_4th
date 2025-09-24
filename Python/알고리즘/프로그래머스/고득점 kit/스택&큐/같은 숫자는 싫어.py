'''
배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 
    이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 
    단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 예를 들면,

    arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
    arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
    배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.

* 제한사항
    - 배열 arr의 크기 : 1,000,000 이하의 자연수
    - 배열 arr의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수
'''

from itertools import groupby


def solution(arr):
    return [key for key, _ in groupby(arr)]


'- groupby(arr)는 연속된 동일 원소들을 묶어서 그룹으로 만듦'
'- 각 그룹의 대표값(key)만 가져오면 → 연속 중복이 제거됨.'
'- 중간에 다른 값이 있을 시, 키 값이 동일하여도 각각 다른 그룹으로 묶이게 됨'
'''
groupby(iterable, key=None)
  - iterable : 리스트, 문자열 같은 순회 가능한 객체
  - key : 그룹을 나눌 기준 함수 (없으면 값 자체를 기준으로 묶음)
반환값 : (key, group) 쌍의 이터레이터
  - key : 그룹을 대표하는 값
  - group : 해당 그룹에 속하는 요소들을 돌려주는 이터레이터


    * 활용
        - 연속 중복 제거
        - 데이터 분류 : 문자열/리스트를 특정 기준(key)으로 묶어 통계 내기
'''

'''
예시1)
def solution(arr):
    result = []
    for num in arr:
        if not result or result[-1] != num:  # result가 비었거나 마지막 값과 다를 때만 추가
            result.append(num)
    return result

- set()을 사용할 경우, 순서 보장이 되지 않으므로, 리스트 형식 혹은 groupy() 함수를 사용해야 함
- 배열은 전체 배열이 비어있으면 False, 요소가 있으면 True
    not 배열은 전체 배열이 비어있으면 True, 요소가 있으면 False

예시2)
def no_continuous(s):
    # 함수를 완성하세요
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

- 슬라이싱을 통해 끝 값과 arr요소를 비교한 뒤, 값이 같을 시에는 continue로 다음 배열 체크
- 리스트 생성 과정 시, 메모리 할당 과정이 생겨나 실제 코드 효율은 낮음

예시3)
def no_continuous(s):
    return [s[i] for i in range(len(s)) if [s[i]] != s[i+1:i+2]]
'''
