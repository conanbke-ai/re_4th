# 행렬
# 행렬(matrix) : 숫자들을 행과 열로 배열한 것
#
#
#
#
#
#
#

# 텐서 : 3차원 이상의 배열

# 일상에서의 행렬
# 성적표
#
#
#
#
#

# 이미지
# 28x28 픽셀 이미지 : 28행x28열 행렬
# 각 셀의 값 = 픽셀 밝기 (0~255)
import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix)

zeros = np.zeros((3, 4))
print(zeros)

###################################################################################################################
# 실습 1
# 다음 벡터 연산을 수행하세요.
A = np.array([[1, 2], [3, 4], [5, 6]])
B = np.array([[1, 2, 3], [4, 5, 6]])

# 1. A의 shape 확인
print("A 의 shape : ", A.shape, sep="\n", end="\n\n")

# 2. A의 전치 행렬 구하기
print("A 의 전치 행렬 : ", A.T, sep="\n", end="\n\n")

# 3. A @ B 계산하기
if (A @ B).any():
    print("A @ B : ", A @ B, sep="\n", end="\n\n")
else:
    print("A @ B를 계산할 수 없습니다.")

# 4. B @ A 계산하기
if (B @ A).any():
    print("B @ A : ", B @ A, sep="\n", end="\n\n")
else:
    print("B @ A를 계산할 수 없습니다.")

# 5. np.arange(12)를 3x4 행렬로 reshape
print("np.arange(12) 의 reshape : ", np.arange(12).reshape(3, 4), sep="\n", end="\n\n")