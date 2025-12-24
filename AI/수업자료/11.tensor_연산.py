# 07_tensor_ops_device_inplace.py
# -*- coding: utf-8 -*-
"""
07_tensor_ops_device_inplace.py
===============================
Tensor 연산(산술/행렬/감소연산) + device 이동 + in-place 연산(_)

슬라이드 기반 핵심
------------------
- 기본적으로 텐서는 CPU에 생성되며,
  GPU로 텐서를 명시적으로 이동할 수 있습니다.
- in-place(바꿔치기) 연산은 연산명 뒤에 '_'를 붙입니다.
  예) add_(), mul_(), zero_() 등

추가 개념(실무에서 중요)
------------------------
1) in-place 연산 주의:
   - autograd가 필요한 텐서(requires_grad=True)에 in-place를 남발하면
     그래프가 깨지거나 RuntimeError가 날 수 있음.
2) matmul/@ 와 elementwise * 차이:
   - A * B : 원소별 곱(elementwise)
   - A @ B : 행렬곱(matrix multiplication)
3) reduction(감소) 연산:
   - sum/mean/max/min은 dim 인자를 통해 축 방향 계산 가능
4) .to(device) 패턴:
   - 모델/텐서를 같은 device에 올려야 함

실행
----
python 07_tensor_ops_device_inplace.py
"""
from __future__ import annotations

import torch


def device_demo() -> torch.device:
    print("== device_demo ==")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Using device:", device)

    x = torch.randn(2, 3)  # 기본은 CPU
    print("x.device:", x.device)

    x2 = x.to(device)      # 원하는 디바이스로 이동
    print("x2.device:", x2.device)
    print()
    return device


def arithmetic_demo(device: torch.device) -> None:
    print("== arithmetic_demo ==")
    a = torch.rand(2, 3, device=device)
    b = torch.rand(2, 3, device=device)

    print("a:\n", a)
    print("b:\n", b)

    # 원소별 연산(elementwise)
    print("a + b:\n", a + b)
    print("a - b:\n", a - b)
    print("a * b:\n", a * b)
    print("a / b:\n", a / b)

    # 스칼라 연산
    print("a * 2:\n", a * 2)
    print()


def matmul_demo(device: torch.device) -> None:
    print("== matmul_demo ==")
    A = torch.randn(2, 3, device=device)
    B = torch.randn(3, 4, device=device)

    # 행렬곱
    C = A @ B
    print("A.shape:", A.shape)
    print("B.shape:", B.shape)
    print("C = A @ B -> shape:", C.shape)
    print("C:\n", C)
    print()


def reduction_demo(device: torch.device) -> None:
    print("== reduction_demo ==")
    x = torch.arange(0, 12, device=device).reshape(3, 4)
    print("x:\n", x)

    print("sum:", x.sum())
    print("mean:", x.float().mean())
    print("max:", x.max())

    # dim=0: 행 방향(열별)으로 감소 => (4,)
    print("sum(dim=0):", x.sum(dim=0))

    # dim=1: 열 방향(행별)으로 감소 => (3,)
    print("sum(dim=1):", x.sum(dim=1))

    # keepdim=True: 축을 유지(브로드캐스팅 편의)
    print("mean(dim=1, keepdim=True):\n", x.float().mean(dim=1, keepdim=True))
    print()


def inplace_demo(device: torch.device) -> None:
    print("== inplace_demo ==")
    x = torch.ones(2, 3, device=device)
    print("x (before):\n", x)

    # in-place 연산: 원본을 덮어씀
    x.add_(2)
    print("x after add_(2):\n", x)

    x.mul_(3)
    print("x after mul_(3):\n", x)
    print()

    # autograd + in-place 주의 예시
    print("== inplace + autograd caution ==")
    y = torch.tensor([1.0, 2.0, 3.0], device=device, requires_grad=True)
    z = (y * 2).sum()

    # 아래처럼 y를 in-place로 바꾸면, 그래프/미분 계산이 꼬일 수 있습니다.
    # 상황에 따라 에러가 나거나, 의도치 않은 결과가 나옵니다.
    # y.add_(1.0)  # <- 주석 해제하면 RuntimeError가 날 수 있음

    z.backward()
    print("y:", y)
    print("y.grad:", y.grad)
    print()


def main() -> None:
    device = device_demo()
    arithmetic_demo(device)
    matmul_demo(device)
    reduction_demo(device)
    inplace_demo(device)


if __name__ == "__main__":
    main()
