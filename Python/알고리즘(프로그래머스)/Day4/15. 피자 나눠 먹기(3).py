'''
머쓱이네 피자가게는 피자를 2 ~ 10 조각까지 원하는 조각 수로 잘라 줍니다.
    피자를 나눠먹을 사람의 수 n이 매개변수로 주어질 때, 
    한 사람당 최소 1조각 이상 먹을 수 있는 피자의 판 수를 return 하도록 solution 함수를 완성해주세요.

* 제한사항
    2 <= slice <= 100
    1 <= n <= 100
'''

import math

def solution(slice, n):
    """
    slice : 한 판의 피자를 자른 조각 수 (2 ~ 10)
    n     : 피자를 먹는 사람 수

    각 사람이 최소 한 조각 이상 먹어야 할 때,
    최소 피자 판 수를 반환
    """
    # 각 사람 최소 1 조각씩 → 필요한 조각 수 total_slices
    total_slices = n  # 한 사람당 한 조각이니까

    # 한 판당 slice 조각이 있으므로,
    # 필요한 판 수 = total_slices / slice 를 올림
    pizzas = math.ceil(total_slices / slice)
    return pizzas

'''
예시1)
def solution(slice, n):
    return ((n - 1) // slice) + 1
    
예시2)
def solution(slice, n):
    d, m = divmod(n, slice)
    return d + int(m != 0)

예시3)
from math import ceil
def solution(slice, n):
    return ceil(n/slice)
    
예시4)
def solution(slice, n):
    return (n + slice - 1) // slice
'''