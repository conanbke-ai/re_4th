import numpy as np

'''
1. 아래의 1차원 배열을 오름차순과 내림차순으로 각각 정렬하는 코드를 작성하세요.
    arr = np.array([7, 2, 9, 4, 5])
'''
arr = np.array([7, 2, 9, 4, 5])
print(np.sort(arr))     # [2 4 5 7 9]
print(np.sort(arr)[::-1])   # [9 7 5 4 2]

'''
2. 아래의 2차원 배열에서 각 행(row) 별로 오름차순 정렬된 배열을 구하세요.
    arr = np.array([[9, 2, 5],
                    [3, 8, 1]])
'''
arr = np.array([[9, 2, 5],
                    [3, 8, 1]])
print(np.sort(arr, axis=0))
# [[3 2 1]
#  [9 8 5]]

'''
3. 아래의 1차원 배열에서 정렬 결과(오름차순)가 되는 인덱스 배열을 구하고, 
    그 인덱스를 이용해 원본 배열을 직접 재정렬하는 코드를 작성하세요.
    arr = np.array([10, 3, 7, 1, 9]) 
'''
arr = np.array([10, 3, 7, 1, 9])
idx = np.argsort(arr)
print(arr[idx]) # [ 1  3  7  9 10]

'''
4. 아래 2차원 배열을 열(column) 기준(axis=0)으로 오름차순 정렬된 배열을 구하세요.
    arr = np.array([[4, 7, 2],
                    [9, 1, 5],
                    [6, 8, 3]])
'''
arr = np.array([[4, 7, 2],
                    [9, 1, 5],
                    [6, 8, 3]])

print(np.sort(arr, axis=0))