# 실습 6 피보나치 수열(Fibonacci Numbers)

'''
1. 먼저 반복문을 활용해서 피보나치 수열을 구현합니다.
2. 1번을 바탕으로 작동 원리를 파악하고, 재귀함수를 이용해서 피보나치 수열을 구현합니다.

    0 이하의 수가 입력될 시 0 리턴
'''

n = 7

# i     0 1 2
# lst   1 1 2

lst=[]

for i in range(n):
    if i == 0 or i == 1:
        lst.append(1)
    else : 
        lst.append(lst[i-1] + lst[i-2])

print(lst)

def fibonachi(n):
    if n < 0 :
        return 0
    elif n == 0 or n == 1:
        return 1
    return fibonachi(n-1) + fibonachi(n-2)

print(fibonachi(5))