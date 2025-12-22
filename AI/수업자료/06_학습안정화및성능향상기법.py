# -*- coding: utf-8 -*-
"""
06_학습안정화및성능향상기법.py
=============================
(원본 PDF: 06_학습안정화및성능향상기법.pdf 기반 정리 + 예제 보강)

수업 슬라이드 핵심(요약)
----------------------
- 기울기 소실(Vanishing Gradient): sigmoid의 미분 최대값은 1/4, 큰 입력에서 기울기 ~ 0
- ReLU: 기울기 소실을 완화하는 활성화 함수(단, dying ReLU 주의)
- BN(Batch Normalization): 학습 안정/빠른 수렴, 학습률에 덜 민감
  * 추론(inference) 단계에서는 moving average로 추정한 mean/var 사용
  * 미니배치 크기에 의존(작은 배치에서 불안정)
  * RNN에는 적용이 어려워 LN(LayerNorm) 등 대안 사용
- 과적합 완화: Dropout, L1/L2(=weight decay), 데이터 증강, Early Stopping 등
- L1/L2 Norm의 의미와 직관

이 파일의 구성
--------------
1) 왜 기울기 소실이 생기는지(수치 시뮬레이션)
2) 활성화 함수(ReLU/LeakyReLU)와 장단점
3) 정규화(BN/LN) 개념과 forward 계산 예제
4) 정규화/규제: L1/L2, weight decay, dropout
5) 옵티마이저: Momentum / RMSProp / Adam (단순 함수에서 동작 원리 체감)
6) 추가: gradient clipping, early stopping 체크리스트

실행:
    python 06_학습안정화및성능향상기법.py
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple

import numpy as np


# ---------------------------------------------------------------------
# 1) 기울기 소실(Vanishing Gradient) 체감
# ---------------------------------------------------------------------
def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-x))


def dsigmoid(x: np.ndarray) -> np.ndarray:
    """
    sigmoid'(x) = sigmoid(x) * (1 - sigmoid(x))
    - 최대값: x=0일 때 1/4
    - |x|가 커질수록 0에 수렴(포화 영역) -> 기울기 소실
    """
    s = sigmoid(x)
    return s * (1 - s)


def relu(x: np.ndarray) -> np.ndarray:
    return np.maximum(0.0, x)


def drelu(x: np.ndarray) -> np.ndarray:
    # x<=0에서 gradient 0 -> dying ReLU 가능성
    return (x > 0).astype(x.dtype)


def leaky_relu(x: np.ndarray, alpha: float = 0.01) -> np.ndarray:
    return np.where(x > 0, x, alpha * x)


def dleaky_relu(x: np.ndarray, alpha: float = 0.01) -> np.ndarray:
    return np.where(x > 0, 1.0, alpha).astype(x.dtype)


def simulate_gradient_product(depth: int = 30, seed: int = 0) -> None:
    """
    매우 단순화한 시뮬레이션:
    - 깊이가 깊어질수록 활성화함수 미분값이 연쇄적으로 곱해짐
    - sigmoid는 미분값이 (0, 0.25] 범위인 경우가 많아 depth가 커지면 급격히 0으로 수렴
    - relu/leaky_relu는 상대적으로 gradient 흐름이 유지될 수 있음(조건에 따라 다름)

    주의: 실제 딥러닝은 가중치 행렬이 포함되어 "기울기 폭발"도 같이 고려해야 합니다.
    """
    rng = np.random.default_rng(seed)
    x = rng.normal(0, 3, size=1)  # 큰 값일수록 sigmoid 포화 가능
    gs, gr, gl = 1.0, 1.0, 1.0

    for _ in range(depth):
        gs *= float(dsigmoid(x))
        gr *= float(drelu(x))
        gl *= float(dleaky_relu(x))
        x = x + rng.normal(0, 0.5, size=1)

    print("== Vanishing Gradient toy simulation ==")
    print(f"depth={depth}")
    print(f"sigmoid grad product: {gs:.6e}")
    print(f"relu    grad product: {gr:.6e}")
    print(f"lrelu   grad product: {gl:.6e}")


# ---------------------------------------------------------------------
# 2) BN / LN (forward) - 직관 잡기
# ---------------------------------------------------------------------
def batch_norm(x: np.ndarray, eps: float = 1e-5, gamma: float = 1.0, beta: float = 0.0) -> np.ndarray:
    """
    Batch Normalization (아주 단순한 forward 구현)
    x: (batch, features)

    학습 시(train-time) 개념
    - 배치 단위 mean/var로 정규화
    - gamma, beta로 다시 스케일/시프트(학습 가능 파라미터)

    추론 시(inference) 개념
    - 배치가 1개일 수도 있어 train-time 통계를 그대로 쓰기 어렵다.
    - 그래서 train 동안 moving average로 누적한 mean/var를 사용
      (수업 슬라이드에서 exponential decay, momentum 값(0.9/0.99/0.999) 언급)
    """
    mean = x.mean(axis=0, keepdims=True)
    var = x.var(axis=0, keepdims=True)
    x_hat = (x - mean) / np.sqrt(var + eps)
    return gamma * x_hat + beta


def layer_norm(x: np.ndarray, eps: float = 1e-5, gamma: float = 1.0, beta: float = 0.0) -> np.ndarray:
    """
    Layer Normalization
    x: (batch, features)

    - 샘플(행) 단위로 평균/분산을 계산
    - 배치 크기에 덜 민감(작은 배치에서도 안정적)
    - RNN/Transformer에서 LN이 자주 사용되는 이유 중 하나
    """
    mean = x.mean(axis=1, keepdims=True)
    var = x.var(axis=1, keepdims=True)
    x_hat = (x - mean) / np.sqrt(var + eps)
    return gamma * x_hat + beta


def demo_bn_ln() -> None:
    rng = np.random.default_rng(1)
    x = rng.normal(10, 5, size=(4, 6))

    bn = batch_norm(x)
    ln = layer_norm(x)

    print("\n== BN vs LN demo ==")
    print("input mean over batch axis:", x.mean(axis=0))
    print("BN   mean over batch axis:", bn.mean(axis=0), "(배치 평균이 0 근처로 맞춰짐)")
    print("LN   mean over batch axis:", ln.mean(axis=0), "(LN은 '배치 평균=0'이 목적이 아님)")


# ---------------------------------------------------------------------
# 3) Dropout / L1-L2 / Weight Decay
# ---------------------------------------------------------------------
def dropout(x: np.ndarray, p: float = 0.5, seed: int = 0) -> np.ndarray:
    """
    Dropout (train-time)
    - p 확률로 뉴런을 끔
    - inverted dropout: (1-p)로 나눠 기대값을 맞춤(추론 때 스케일 필요 없게)

    직관
    - 특정 뉴런/특정 경로에 과도하게 의존하는 "동조화(co-adaptation)"를 줄여 일반화 개선
    """
    rng = np.random.default_rng(seed)
    mask = (rng.random(size=x.shape) >= p).astype(x.dtype)
    return x * mask / (1 - p)


def l1_l2_penalty(w: np.ndarray, l1: float = 0.0, l2: float = 0.0) -> float:
    """
    규제 항(패널티) 값
    - L1: |w| 합 -> sparsity(일부 가중치를 0으로 유도)
    - L2: w^2 합 -> 가중치 크기 억제(부드럽게)
    """
    return float(l1 * np.sum(np.abs(w)) + l2 * np.sum(w**2))


# ---------------------------------------------------------------------
# 4) 옵티마이저: Momentum / RMSProp / Adam (원리 체감)
# ---------------------------------------------------------------------
"""
실무에서 SGD만 쓰는 경우는 점점 줄고,
Momentum, RMSProp, Adam 같은 변형을 자주 씁니다.

여기서는 아주 단순한 2차 함수 f(w) = (w-3)^2 + 1 을 최소화하며
각 옵티마이저의 업데이트 차이를 체감합니다.
"""


def grad_quadratic(w: float) -> float:
    # f(w) = (w-3)^2 + 1
    return 2 * (w - 3)


@dataclass
class OptConfig:
    lr: float = 0.1
    steps: int = 50


def optimize_sgd(cfg: OptConfig) -> float:
    w = 0.0
    for _ in range(cfg.steps):
        g = grad_quadratic(w)
        w -= cfg.lr * g
    return w


def optimize_momentum(cfg: OptConfig, beta: float = 0.9) -> float:
    w = 0.0
    v = 0.0
    for _ in range(cfg.steps):
        g = grad_quadratic(w)
        v = beta * v + (1 - beta) * g
        w -= cfg.lr * v
    return w


def optimize_rmsprop(cfg: OptConfig, beta: float = 0.9, eps: float = 1e-8) -> float:
    w = 0.0
    s = 0.0
    for _ in range(cfg.steps):
        g = grad_quadratic(w)
        s = beta * s + (1 - beta) * (g * g)
        w -= cfg.lr * g / (np.sqrt(s) + eps)
    return w


def optimize_adam(cfg: OptConfig, beta1: float = 0.9, beta2: float = 0.999, eps: float = 1e-8) -> float:
    w = 0.0
    m = 0.0
    v = 0.0
    for t in range(1, cfg.steps + 1):
        g = grad_quadratic(w)
        m = beta1 * m + (1 - beta1) * g
        v = beta2 * v + (1 - beta2) * (g * g)

        # bias correction
        m_hat = m / (1 - beta1**t)
        v_hat = v / (1 - beta2**t)

        w -= cfg.lr * m_hat / (np.sqrt(v_hat) + eps)
    return w


# ---------------------------------------------------------------------
# 5) 추가: gradient clipping / early stopping 체크리스트(주석 중심)
# ---------------------------------------------------------------------
"""
[Gradient Clipping]
- 기울기 폭발(exploding gradient)을 막기 위해
  gradient의 norm이 임계값을 넘으면 스케일링하는 기법
- 특히 RNN 계열에서 많이 사용

예) L2 norm clip
    g <- g * (clip_norm / (||g|| + eps))   if ||g|| > clip_norm

[Early Stopping]
- val loss가 더 이상 좋아지지 않으면 학습 중단
- 실무적으로 매우 강력한 일반화 기법(특히 데이터가 적을 때)

체크리스트
1) patience(몇 번 연속으로 개선이 없으면 멈출지)
2) best model weight 저장/복원
3) val metric 기준 명확히(Accuracy? F1? Loss?)
"""


def main() -> None:
    simulate_gradient_product(depth=30)
    demo_bn_ln()

    print("\n== Dropout / Regularization demo ==")
    rng = np.random.default_rng(0)
    x = rng.normal(0, 1, size=(3, 6))
    print("before dropout:", x[0])
    print("after  dropout:", dropout(x, p=0.5, seed=1)[0])

    w = rng.normal(0, 1, size=10)
    print("L1 penalty (0.1):", l1_l2_penalty(w, l1=0.1, l2=0.0))
    print("L2 penalty (0.1):", l1_l2_penalty(w, l1=0.0, l2=0.1))

    print("\n== Optimizer demo on simple quadratic ==")
    cfg = OptConfig(lr=0.2, steps=30)
    print("SGD     ->", optimize_sgd(cfg))
    print("Momentum->", optimize_momentum(cfg))
    print("RMSProp ->", optimize_rmsprop(cfg))
    print("Adam    ->", optimize_adam(cfg))

    print("\n[연습문제]")
    print("1) sigmoid 대신 tanh의 미분을 구현하고, gradient product가 어떻게 달라지는지 비교해보세요.")
    print("2) dying ReLU를 유발하는 입력 분포를 만들어보고, LeakyReLU가 어떻게 완화하는지 확인하세요.")
    print("3) 배치 크기를 2, 4, 32로 바꿔 BN 통계가 얼마나 흔들리는지 실험해보세요(가능하면 PyTorch로).")


if __name__ == "__main__":
    main()
