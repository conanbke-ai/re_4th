# ============================================================
# 12월 24일 학습 자료 - 2 (완성본)
# 주제: PyTorch 텐서 기초 실습 문제
# - TODO 채우기 + 개념/포인트를 주석으로 상세히 보강
# ============================================================

import torch


# ============================================================
# [개념 메모] PyTorch Tensor 핵심 요약
# ============================================================
# 1) Tensor 생성
#   - torch.zeros, torch.ones: 0/1로 채운 텐서 생성
#   - torch.arange: 연속 정수 범위 텐서 생성 (Python range와 유사)
#   - torch.randn: 표준정규분포 N(0,1) 샘플링
#   - torch.eye: 단위행렬 생성
#
# 2) shape(형태) 변경
#   - reshape: 원하는 shape로 재배치 (원소 수가 동일해야 함)
#   - view: reshape와 유사하지만 contiguous(메모리 연속성) 요구가 있을 수 있음
#   - flatten: (N,) 1차원으로 펼치기
#
# 3) 연산
#   - element-wise(원소별) 연산: +, -, *, /, ** 등
#   - reduction(축소) 연산: sum/mean/min/max (dim으로 축 지정)
#   - boolean indexing: 조건에 맞는 원소 추출 (A[A>3])
#
# 4) Broadcasting(브로드캐스팅)
#   - 서로 다른 shape라도 규칙이 맞으면 자동으로 확장하여 연산
#   - (10,5) + (5,) => (5,)가 (10,5)로 “행 방향” 복제되어 더해짐
#   - (10,5) - (1,5) 또는 (5,) 모두 가능
#
# 5) dtype / device
#   - dtype=torch.float32, torch.int64 등
#   - device='cpu' or 'cuda' (GPU 사용 시)
# ============================================================


# ============================================================
# 실습 1: 텐서 생성
# ============================================================
print("=" * 50)
print("실습 1: 텐서 생성")
print("=" * 50)

# 1. 3x3 크기의 0으로 채워진 텐서
zeros = torch.zeros((3, 3), dtype=torch.float32)
# TIP: dtype을 지정하지 않으면 기본 dtype(대개 float32)이 사용될 수 있으나
#      명시하면 실습에서 혼동이 줄어듭니다.

# 2. 2x4 크기의 1로 채워진 텐서
ones = torch.ones((2, 4), dtype=torch.float32)

# 3. 0부터 9까지의 숫자가 들어있는 1차원 텐서
# torch.arange(10) => [0,1,2,3,4,5,6,7,8,9]
numbers = torch.arange(10)

# 4. 평균 0, 표준편차 1인 정규분포에서 샘플링한 5x5 텐서
# randn은 표준정규분포 N(0,1) 샘플을 생성합니다.
random_normal = torch.randn((5, 5))

# 5. 3x3 단위행렬 (대각선이 1인 행렬)
identity = torch.eye(3, dtype=torch.float32)

print("zeros:\n", zeros)
print("ones:\n", ones)
print("numbers:\n", numbers)
print("random_normal:\n", random_normal)
print("identity:\n", identity)


# ============================================================
# 실습 2: 텐서 형태 변환
# ============================================================
print("\n" + "=" * 50)
print("실습 2: 텐서 형태 변환")
print("=" * 50)

# 주어진 텐서
x = torch.arange(24)
print(f"원본: {x}\n")
print("원본 shape:", x.shape)  # torch.Size([24])

# 1. 2x12 형태로 변환
# 원소 수: 24개 = 2*12 가능
shape_2_12 = x.reshape(2, 12)

# 2. 3x8 형태로 변환
shape_3_8 = x.reshape(3, 8)

# 3. 2x3x4 형태로 변환
shape_2_3_4 = x.reshape(2, 3, 4)

# 4. 4x2x3 형태로 변환 (힌트: reshape 사용)
shape_4_2_3 = x.reshape(4, 2, 3)

# 5. 다시 1차원으로 펴기 (24,)
flattened = x.flatten()  # 또는 x.reshape(-1)

print("shape_2_12:\n", shape_2_12, "\nshape:", shape_2_12.shape)
print("shape_3_8:\n", shape_3_8, "\nshape:", shape_3_8.shape)
print("shape_2_3_4:\n", shape_2_3_4, "\nshape:", shape_2_3_4.shape)
print("shape_4_2_3:\n", shape_4_2_3, "\nshape:", shape_4_2_3.shape)
print("flattened:\n", flattened, "\nshape:", flattened.shape)

# (검증) reshape 전후 원소는 동일해야 합니다.
assert x.numel() == shape_2_12.numel() == shape_3_8.numel() == shape_2_3_4.numel() == shape_4_2_3.numel() == flattened.numel()


# ============================================================
# 실습 3: 텐서 연산
# ============================================================
print("\n" + "=" * 50)
print("실습 3: 텐서 연산")
print("=" * 50)

# 두 행렬 정의
A = torch.tensor([[1, 2, 3],
                  [4, 5, 6]], dtype=torch.float32)

B = torch.tensor([[2, 0, 1],
                  [1, 3, 2]], dtype=torch.float32)

print(f"A:\n{A}\n")
print(f"B:\n{B}\n")

# 1. A와 B의 원소별 합
element_sum = A + B  # element-wise add

# 2. A와 B의 원소별 곱
element_mul = A * B  # element-wise multiply

# 3. A의 모든 원소를 제곱
squared = A ** 2

# 4. A의 각 행의 합 (결과: [6, 15])
# dim=1 => 열 방향으로 더해 행마다 1개 값
row_sum = A.sum(dim=1)

# 5. A의 각 열의 평균 (결과: [2.5, 3.5, 4.5])
# dim=0 => 행 방향으로 평균내 열마다 1개 값
col_mean = A.mean(dim=0)

# 6. A에서 3보다 큰 원소들만 추출
# boolean indexing: 조건을 만족하는 원소만 1차원으로 뽑힘
greater_than_3 = A[A > 3]

print("element_sum:\n", element_sum)
print("element_mul:\n", element_mul)
print("squared:\n", squared)
print("row_sum:", row_sum)
print("col_mean:", col_mean)
print("greater_than_3:", greater_than_3)

# (검증) 기대값 체크
assert torch.allclose(row_sum, torch.tensor([6., 15.]))
assert torch.allclose(col_mean, torch.tensor([2.5, 3.5, 4.5]))


# ============================================================
# 실습 4: 브로드캐스팅 활용
# ============================================================
print("\n" + "=" * 50)
print("실습 4: 브로드캐스팅 활용")
print("=" * 50)

torch.set_printoptions(precision=3)  # 소수점 3자리까지만 표시

# 배치 데이터 (10개 샘플, 각 5개 특성)
batch = torch.randn(10, 5)
print(f"배치 데이터 크기: {batch.shape}\n")

# 1. 모든 샘플에 벡터 [1, 2, 3, 4, 5]를 더하기
vector = torch.tensor([1, 2, 3, 4, 5], dtype=torch.float32)

# (10,5) + (5,) => (5,)가 (10,5)로 브로드캐스팅되어 더해짐
result1 = batch + vector

# 2. 각 특성(열)의 평균을 구하고, 각 샘플에서 해당 평균을 빼기 (중심화)
# dim=0 => 각 열별 평균, shape=(5,)
# keepdim=True를 주면 shape=(1,5)가 되어 브로드캐스팅이 더 “명확”해짐
col_mean = batch.mean(dim=0, keepdim=True)  # (1,5)
centered = batch - col_mean                  # (10,5) - (1,5)

# 3. 각 특성의 최솟값과 최댓값을 구하고, 0~1 범위로 정규화
# 공식: (x - min) / (max - min)
# dim=0으로 열별 min/max를 구하면 shape=(5,) 또는 keepdim=True면 (1,5)
min_vals = batch.min(dim=0, keepdim=True).values
max_vals = batch.max(dim=0, keepdim=True).values

# (안전장치) max-min이 0이면 나눗셈이 불가능하므로 작은 epsilon을 더해줄 수 있음
eps = 1e-8
normalized = (batch - min_vals) / (max_vals - min_vals + eps)

print("vector:", vector)
print("result1 (batch + vector) shape:", result1.shape)

print("\ncol_mean shape:", col_mean.shape)
print("centered shape:", centered.shape)
print("centered (일부):\n", centered[:3])  # 앞 3개 샘플만 보기

print("\nmin_vals shape:", min_vals.shape)
print("max_vals shape:", max_vals.shape)
print("normalized shape:", normalized.shape)
print("normalized (일부):\n", normalized[:3])

# (검증) 정규화 결과는 열별로 대체로 0~1 범위(수치오차로 아주 약간 벗어날 수 있음)
assert normalized.shape == batch.shape


# ============================================================
# [추가 학습] 자주 쓰는 텐서 기능 예제 (보강)
# ============================================================
print("\n" + "=" * 50)
print("추가 학습: 인덱싱 / dtype 변환 / 차원 유지")
print("=" * 50)

T = torch.tensor([[10, 20, 30],
                  [40, 50, 60]])

# 1) 슬라이싱
print("T[0]:", T[0])          # 첫 행
print("T[:, 1]:", T[:, 1])    # 두 번째 열
print("T[0, 2]:", T[0, 2])    # (0행,2열) 원소 하나

# 2) dtype 변환
Tf = T.to(torch.float32)
print("Tf dtype:", Tf.dtype)

# 3) keepdim 차이
print("sum dim=0 keepdim=False:", T.sum(dim=0), T.sum(dim=0).shape)              # (3,)
print("sum dim=0 keepdim=True :", T.sum(dim=0, keepdim=True), T.sum(dim=0, keepdim=True).shape)  # (1,3)
