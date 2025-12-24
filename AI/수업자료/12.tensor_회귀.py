# 08_autograd_mini_training.py
# -*- coding: utf-8 -*-
"""
08_autograd_mini_training.py
============================
(추가 확장) Autograd + 아주 작은 "학습" 예제 (선형회귀)

이 파일은 슬라이드의 범위를 살짝 확장합니다.
왜 확장하나?
-------------
PyTorch를 "딥러닝 프레임워크"로 쓰려면 결국
- Tensor 연산
- device 이동
- autograd(미분)
- optimizer(step)
흐름을 한 번은 경험해야 합니다.

여기서는 가장 단순한 회귀 문제 y = 3x + 2 + noise를 만들고,
Linear 모델(W,b)을 gradient descent로 학습합니다.

핵심 개념
---------
1) requires_grad=True: 학습할 파라미터에 미분 추적
2) loss.backward(): gradient 계산
3) torch.no_grad(): 파라미터 업데이트 시 그래프 추적 방지
4) grad 누적: backward는 grad를 누적하므로 zero_() 필요

실행
----
python 08_autograd_mini_training.py
"""
from __future__ import annotations

import torch


def make_toy_data(n: int = 200, device: torch.device | str = "cpu") -> tuple[torch.Tensor, torch.Tensor]:
    """
    y = 3x + 2 + noise 형태의 데이터 생성
    """
    device = torch.device(device)
    torch.manual_seed(0)

    x = torch.linspace(-1, 1, steps=n, device=device).unsqueeze(1)  # (n,1)
    noise = 0.1 * torch.randn(n, 1, device=device)
    y = 3.0 * x + 2.0 + noise
    return x, y


def train_linear_regression(steps: int = 300, lr: float = 0.1) -> None:
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    x, y = make_toy_data(device=device)

    # 학습 파라미터(가중치 W, 편향 b)
    # requires_grad=True => autograd가 미분을 추적
    W = torch.randn(1, 1, device=device, requires_grad=True)
    b = torch.zeros(1, device=device, requires_grad=True)

    for step in range(1, steps + 1):
        # forward
        y_pred = x @ W + b  # (n,1)
        loss = ((y_pred - y) ** 2).mean()

        # backward: grad 누적되므로, 먼저 grad를 0으로 초기화
        if W.grad is not None:
            W.grad.zero_()
        if b.grad is not None:
            b.grad.zero_()

        loss.backward()

        # gradient descent update (그래프 추적 방지)
        with torch.no_grad():
            W -= lr * W.grad
            b -= lr * b.grad

        if step % 50 == 0 or step == 1:
            print(f"step={step:4d}  loss={loss.item():.6f}  W={W.item():.4f}  b={b.item():.4f}")

    print("\n== Final ==")
    print("W:", W.item(), "(target 3.0)")
    print("b:", b.item(), "(target 2.0)")
    print("device:", device)


def main() -> None:
    train_linear_regression()


if __name__ == "__main__":
    main()
