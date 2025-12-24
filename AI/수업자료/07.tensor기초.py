# 02_tensor_basics_and_dtype.py
# -*- coding: utf-8 -*-
"""
02_tensor_basics_and_dtype.py
=============================
Tensor 기초 + dtype(데이터 타입) 감 잡기

슬라이드 기반 핵심
------------------
- Tensor는 다차원 배열(0D~nD)로 데이터를 담는 컨테이너입니다.
- NumPy ndarray와 유사하지만, GPU 가속 및 딥러닝에 최적화되어 있습니다.
- dtype은 텐서 내부 원소의 자료형(float32, int64 등)을 의미합니다.
- torch.empty      : 초기화되지 않은(쓰레기 값) 텐서 생성

- torch.zeros/ones : 0 또는 1로 채운 텐서 생성
- torch.rand       : [0,1) 균등분포 난수 텐서
- torch.randn      : 평균 0, 표준편차 1 정규분포 난수 텐서
- torch.tensor     : 직접 값 입력하여 생성

추가로 알아두면 좋은 개념(추가)
------------------------------
1) dtype 선택 기준
   - 모델 학습: 보통 float32 (torch.float32)
   - 분류 레이블: 보통 int64 (torch.int64, torch.long)
   - 메모리 절약/속도 최적화: float16/bfloat16 (혼합정밀도)
2) 텐서 생성 함수 차이
   - torch.tensor: 입력 데이터 복사(copy)하는 경우가 많음
   - torch.as_tensor: 가능하면 메모리 공유(복사 최소화)
3) 파이썬 스칼라 <-> 텐서 스칼라
   - tensor.item()으로 파이썬 숫자 꺼내기

1) torch.full / zeros_like / ones_like / rand_like
   - 기존 텐서와 같은 shape/dtype/device로 생성 가능 (실무에서 매우 자주 씀)
2) arange / linspace / eye
   - 인덱스/좌표 생성, 간격 벡터 생성, 단위행렬 생성
3) 재현성(reproducibility)
   - torch.manual_seed(seed)로 난수 고정


실행
----
python 02_tensor_basics_and_dtype.py
"""
from __future__ import annotations

import torch


def print_tensor_info(name: str, t: torch.Tensor) -> None:
    """텐서의 핵심 속성을 한 번에 확인하는 헬퍼."""
    print(f"[{name}]")
    print("  value :", t)
    print("  shape :", tuple(t.shape))
    print("  ndim  :", t.ndim)
    print("  dtype :", t.dtype)
    print("  device:", t.device)
    print("  numel :", t.numel())  # 전체 원소 개수
    print()


def tensor_rank_examples() -> None:
    """
    0D~3D 텐서 예시를 만들어보고 'rank/ndim' 감각 잡기.
    """
    # 0D (스칼라) : 하나의 숫자
    t0 = torch.tensor(3.14)
    print_tensor_info("t0 (0D scalar)", t0)

    # 1D (벡터) : 리스트와 유사
    t1 = torch.tensor([1, 2, 3])
    print_tensor_info("t1 (1D vector)", t1)

    # 2D (행렬) : 샘플 x 특성 구조로 많이 사용
    t2 = torch.tensor([[1, 2, 3],
                       [4, 5, 6]])
    print_tensor_info("t2 (2D matrix)", t2)

    # 3D : 시퀀스/시계열/배치 구조에서 자주 사용 (batch, timesteps, features 등)
    t3 = torch.randn(2, 4, 3)  # (batch=2, timesteps=4, features=3)
    print_tensor_info("t3 (3D: batch, time, feature)", t3)


def dtype_examples() -> None:
    """
    dtype(자료형) 감각 잡기
    - float32/float64/float16
    - int32/int64
    """
    x_float32 = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)
    x_float64 = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float64)
    x_int64 = torch.tensor([1, 2, 3], dtype=torch.int64)

    print_tensor_info("x_float32", x_float32)
    print_tensor_info("x_float64", x_float64)
    print_tensor_info("x_int64", x_int64)

    # dtype 변환(캐스팅)
    print("== Casting ==")
    print("x_int64.float():", x_int64.float())
    print("x_float32.long():", x_float32.long())
    print()

    # 정수 나눗셈 vs 실수 나눗셈
    a = torch.tensor([3, 4, 5], dtype=torch.int64)
    print("a / 2 (int tensor):", a / 2)  # / 는 float로 승격되는 경우가 많음
    print("a // 2 (floor div):", a // 2)
    print()

    # item() : 0D 텐서를 파이썬 숫자로 추출
    b = torch.tensor(10.0)
    print("b:", b, "type:", type(b))
    print("b.item():", b.item(), "type:", type(b.item()))
    print()


def tensor_vs_as_tensor() -> None:
    """
    torch.tensor vs torch.as_tensor 차이(개념)
    - tensor: 보통 복사(copy)
    - as_tensor: 가능하면 복사 없이 텐서 뷰 생성(공유 가능)
    """
    import numpy as np

    arr = np.array([1, 2, 3], dtype=np.int64)

    t_copy = torch.tensor(arr)      # 일반적으로 복사
    t_view = torch.as_tensor(arr)   # 가능하면 공유

    print("== tensor() vs as_tensor() ==")
    print("np arr:", arr, "id:", id(arr))
    print("t_copy:", t_copy, "storage ptr:", t_copy.storage().data_ptr())
    print("t_view:", t_view, "storage ptr:", t_view.storage().data_ptr())
    print("(주의) storage ptr이 같다고 '항상 공유'를 보장하는 것은 아니지만,",
          "as_tensor는 공유를 우선 시도합니다.")
    print()



def show(title: str, t: torch.Tensor) -> None:
    """간단 출력 헬퍼"""
    print(f"== {title} ==")
    print("tensor:", t)
    print("shape :", tuple(t.shape))
    print("dtype :", t.dtype)
    print("device:", t.device)
    print()


def seed_demo() -> None:
    """시드 고정이 왜 중요한지 간단히 확인"""
    torch.manual_seed(0)
    a1 = torch.rand(2, 3)
    torch.manual_seed(0)
    a2 = torch.rand(2, 3)
    show("seed_demo a1", a1)
    show("seed_demo a2 (same seed => same)", a2)
    print("Allclose:", torch.allclose(a1, a2))
    print()


def empty_zeros_ones() -> None:
    # 초기화되지 않은 텐서: 값이 '의미 없음' (메모리 쓰레기 값)
    x = torch.empty(2, 3)
    show("torch.empty(2,3) - uninitialized", x)

    # 상수로 초기화
    z = torch.zeros(2, 3)
    o = torch.ones(2, 3, dtype=torch.float32)
    show("torch.zeros(2,3)", z)
    show("torch.ones(2,3, dtype=float32)", o)


def random_tensors() -> None:
    # 균등분포 [0,1)
    r = torch.rand(2, 3)

    # 정규분포 N(0,1)
    n = torch.randn(2, 3)

    show("torch.rand(2,3)", r)
    show("torch.randn(2,3)", n)

    # 평균/표준편차를 조정하고 싶으면?
    # N(mu, sigma^2) = sigma * randn + mu
    mu, sigma = 10.0, 2.0
    n2 = sigma * torch.randn(2, 3) + mu
    show("sigma*randn + mu", n2)


def direct_tensor() -> None:
    t = torch.tensor([1, 2, 3], dtype=torch.int64)
    show("torch.tensor([1,2,3], dtype=int64)", t)


def convenience_creators() -> None:
    """
    실무에서 자주 쓰는 편의 함수들:
    - full: 특정 상수로 채우기
    - zeros_like / ones_like: 기존 텐서 shape/dtype/device 따라가기
    - arange/linspace: 인덱스나 구간 벡터 만들기
    - eye: 단위행렬
    """
    base = torch.randn(2, 3)

    f = torch.full((2, 3), fill_value=7.0)  # (2,3)에 7.0 채움
    zl = torch.zeros_like(base)
    ol = torch.ones_like(base)
    rl = torch.rand_like(base)

    show("base", base)
    show("torch.full((2,3), 7.0)", f)
    show("torch.zeros_like(base)", zl)
    show("torch.ones_like(base)", ol)
    show("torch.rand_like(base)", rl)

    idx = torch.arange(0, 10, step=2)   # [0,2,4,6,8]
    lin = torch.linspace(0, 1, steps=5) # [0,0.25,0.5,0.75,1]
    eye = torch.eye(3)                  # 3x3 단위행렬

    show("torch.arange(0,10,2)", idx)
    show("torch.linspace(0,1,steps=5)", lin)
    show("torch.eye(3)", eye)

def main() -> None:
    tensor_rank_examples()
    dtype_examples()
    tensor_vs_as_tensor()

    seed_demo()
    empty_zeros_ones()
    random_tensors()
    direct_tensor()
    convenience_creators()


if __name__ == "__main__":
    main()
