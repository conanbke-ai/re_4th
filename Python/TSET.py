import numpy as np

# 사용 예제 - np,concatenate()
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

# 행방향 결합
result = np.concatenate((a, b), axis=0)
print(result)
# [[1 2]
#  [3 4]
#  [5 6]]

# 열방향 결합
c = np.array([[7], [8], [9]])
result2 = np.concatenate((result, c), axis=1)
print(result2)
# [[1 2 7]
#  [3 4 8]
#  [5 6 9]]