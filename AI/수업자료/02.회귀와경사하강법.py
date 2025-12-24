# -*- coding: utf-8 -*-
"""
04_회귀와경사하강법.py
======================
(원본 PDF: 04_회귀와경사하강법.pdf 기반 정리 + 실습 예제 확장)

핵심 개념(수업 슬라이드 요지)
---------------------------
- 회귀(Regression): 연속값(숫자)을 예측하는 문제
- 선형/다중/비선형/다항 회귀
- 정규화(규제): Ridge(L2), Lasso(L1)로 과적합 완화
- 손실함수(loss) vs 평가 지표(metric)
- 경사하강법(Gradient Descent): 손실함수를 줄이는 방향으로 파라미터 업데이트
- 볼록함수(convex)에서는 전역 최솟값에 수렴하기 쉬움(이론적 배경)

이 파일에 추가로 덧붙인 실무 보강
--------------------------------
- (중요) 학습률(lr)의 선택과 스케줄링(감쇠, warmup 등)
- BGD/SGD/미니배치의 장단점 비교(속도/안정성/노이즈)
- 수치 미분 vs 해석적 미분(gradient) 차이
- 큰 데이터에서 MemoryError를 피하는 미니배치/청크 패턴

실행:
    python 04_회귀와경사하강법.py
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple

import numpy as np


# ---------------------------------------------------------------------
# 1) 회귀 문제 정의와 대표 손실/지표
# ---------------------------------------------------------------------
def mse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Mean Squared Error (MSE) - 회귀에서 대표적인 손실/지표"""
    return float(np.mean((y_true - y_pred) ** 2))


def mae(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Mean Absolute Error (MAE) - 이상치에 MSE보다 덜 민감"""
    return float(np.mean(np.abs(y_true - y_pred)))


def r2_score(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    결정계수 R^2
    - 1에 가까울수록 설명력이 높음
    - 0이면 '평균으로 예측'한 것과 동일
    - 음수도 가능(평균보다 못한 예측)
    """
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return float(1 - ss_res / (ss_tot + 1e-12))


# ---------------------------------------------------------------------
# 2) 선형회귀: y = Xw + b
# ---------------------------------------------------------------------
def add_bias(X: np.ndarray) -> np.ndarray:
    """편향항(bias)을 위해 X에 1 컬럼을 추가합니다."""
    return np.concatenate([np.ones((X.shape[0], 1)), X], axis=1)


def closed_form_linear_regression(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    """
    선형회귀 해석해(정규방정식 기반):
        w = (X^T X)^(-1) X^T y

    주의
    - (X^T X)가 역행렬을 가지지 않을 수 있음(특히 feature가 중복/상관이 강할 때)
    - 수치 불안정성 문제
    그래서 실무에서는:
    - np.linalg.lstsq / QR / SVD 기반 풀이
    - 또는 Ridge로 안정화
    """
    Xb = add_bias(X)
    # solve(A, b)는 A^-1을 직접 계산하지 않고 더 안정적으로 풉니다.
    return np.linalg.solve(Xb.T @ Xb, Xb.T @ y)


def ridge_closed_form(X: np.ndarray, y: np.ndarray, l2: float = 1e-2) -> np.ndarray:
    """
    Ridge(L2 규제) 회귀 해석해:
        w = (X^T X + λI)^(-1) X^T y
    """
    Xb = add_bias(X)
    I = np.eye(Xb.shape[1])
    # bias까지 규제하고 싶지 않으면 I[0,0]=0으로 만들기도 합니다.
    I[0, 0] = 0.0
    return np.linalg.solve(Xb.T @ Xb + l2 * I, Xb.T @ y)


# ---------------------------------------------------------------------
# 3) 경사하강법(Gradient Descent) 구현
# ---------------------------------------------------------------------
"""
경사하강법의 핵심 아이디어
- 손실함수 J(w)의 기울기(gradient) ∂J/∂w는 "증가 방향"을 가리킴
- 따라서 손실을 줄이려면 반대 방향으로 이동:
    w <- w - lr * gradient

학습률(lr, learning rate)
- 너무 크면: overshooting(진동/발산)
- 너무 작으면: 수렴이 너무 느림
- 실무에서는 스케줄링(exponential decay, cosine, step decay 등)이나
  적응형 최적화(Adam)도 많이 사용
"""


def grad_mse(Xb: np.ndarray, y: np.ndarray, w: np.ndarray) -> np.ndarray:
    """
    MSE = (1/n) * Σ(y - Xw)^2 에 대한 gradient
      ∂/∂w MSE = -(2/n) X^T (y - Xw)

    해석적 미분(analytic gradient)을 쓰는 이유
    - 수치미분은 느리고 오차가 생기기 쉬움
    - 딥러닝에서는 수백만~수억 파라미터를 수치미분으로 계산할 수 없음
    """
    n = Xb.shape[0]
    y_pred = Xb @ w
    return -(2.0 / n) * (Xb.T @ (y - y_pred))


@dataclass
class GDConfig:
    lr: float = 0.03
    steps: int = 2_000
    batch_size: int = 64  # n이면 Batch GD, 1이면 SGD
    seed: int = 42
    lr_decay: float = 1.0  # 1.0이면 감쇠 없음, <1이면 시간이 갈수록 lr 감소(단순 감쇠)


def fit_linear_regression_gd(X: np.ndarray, y: np.ndarray, cfg: GDConfig) -> Tuple[np.ndarray, Dict[str, list]]:
    """
    선형회귀를 경사하강법으로 학습합니다.
    - batch_size로 BGD/SGD/미니배치 선택

    반환값
    - w: (d+1,) (bias 포함)
    - history: 손실 로그(간단 기록)
    """
    rng = np.random.default_rng(cfg.seed)

    Xb = add_bias(X)
    n, d = Xb.shape
    w = np.zeros(d)
    history = {"loss": []}

    lr = cfg.lr
    log_every = max(1, cfg.steps // 20)

    for step in range(cfg.steps):
        # --- 미니배치 샘플링 ---
        if cfg.batch_size >= n:
            idx = np.arange(n)  # Batch GD
        else:
            idx = rng.choice(n, size=cfg.batch_size, replace=False)

        g = grad_mse(Xb[idx], y[idx], w)
        w -= lr * g

        # 단순 lr decay(지수 감쇠 느낌으로)
        lr *= cfg.lr_decay

        if step % log_every == 0:
            history["loss"].append(mse(y, Xb @ w))

    return w, history


# ---------------------------------------------------------------------
# 4) 데모 데이터 + 비교 실험
# ---------------------------------------------------------------------
def make_regression_data(n: int = 2000, seed: int = 0) -> Tuple[np.ndarray, np.ndarray, np.ndarray, float]:
    """
    y = X @ true_w + bias + noise
    """
    rng = np.random.default_rng(seed)
    X = rng.normal(0, 1, size=(n, 2))
    true_w = np.array([2.0, -3.0])
    bias = 0.5
    y = X @ true_w + bias + rng.normal(0, 0.5, size=n)
    return X, y, true_w, bias


def demo_gd_variants() -> None:
    X, y, true_w, true_b = make_regression_data()

    print("== 회귀 + 경사하강법 데모 ==")
    print(f"true: w={true_w}, bias={true_b}")

    # Batch GD (안정적, 하지만 매 step마다 전체 데이터 사용)
    w_bgd, h_bgd = fit_linear_regression_gd(X, y, GDConfig(lr=0.05, steps=1200, batch_size=len(y)))
    # SGD (노이즈 큼, step 수 늘려야 할 수 있음)
    w_sgd, h_sgd = fit_linear_regression_gd(X, y, GDConfig(lr=0.01, steps=6000, batch_size=1, lr_decay=1.0))
    # Mini-batch GD (현업에서 많이 쓰는 타협점)
    w_mbgd, h_mbgd = fit_linear_regression_gd(X, y, GDConfig(lr=0.03, steps=2500, batch_size=64, lr_decay=1.0))

    print(f"BGD : w={w_bgd[1:]}, bias={w_bgd[0]:.3f}, MSE={mse(y, add_bias(X)@w_bgd):.4f}")
    print(f"SGD : w={w_sgd[1:]}, bias={w_sgd[0]:.3f}, MSE={mse(y, add_bias(X)@w_sgd):.4f}")
    print(f"MBGD: w={w_mbgd[1:]}, bias={w_mbgd[0]:.3f}, MSE={mse(y, add_bias(X)@w_mbgd):.4f}")

    # 학습률이 너무 크면?
    w_bad, _ = fit_linear_regression_gd(X, y, GDConfig(lr=1.0, steps=200, batch_size=64))
    print(f"(참고) lr=1.0: w={w_bad} (발산하거나 불안정할 수 있음)")


def demo_regularization() -> None:
    """
    Ridge(L2) 규제의 효과를 "다항 특징"에서 확인해봅니다.
    - feature 차수가 커질수록 과적합 위험 증가
    - Ridge는 가중치 크기를 제한하여 일반화를 돕는 경향
    """
    rng = np.random.default_rng(1)
    n = 260
    x = rng.uniform(-3, 3, size=n)
    y = 0.5 * x**3 - x**2 + 0.3 * x + rng.normal(0, 3.0, size=n)

    def poly(x1: np.ndarray, degree: int) -> np.ndarray:
        x1 = x1.reshape(-1, 1)
        return np.concatenate([x1 ** d for d in range(1, degree + 1)], axis=1)

    # split
    from 01_utils_memory_and_data import train_val_test_split
    split = train_val_test_split(x.reshape(-1, 1), y, seed=1)

    deg = 12
    Xtr = poly(split.X_train[:, 0], deg)
    Xva = poly(split.X_val[:, 0], deg)

    # no reg
    w0 = ridge_closed_form(Xtr, split.y_train, l2=0.0)  # 사실상 OLS
    # with reg
    w1 = ridge_closed_form(Xtr, split.y_train, l2=1e-2)

    pred0 = add_bias(Xva) @ w0
    pred1 = add_bias(Xva) @ w1

    print("\n== Ridge 규제 데모 ==")
    print("degree=12에서 val MSE 비교")
    print("no reg  val MSE:", mse(split.y_val, pred0))
    print("ridge   val MSE:", mse(split.y_val, pred1))


def main() -> None:
    demo_gd_variants()
    demo_regularization()

    print("\n[연습문제]")
    print("1) GDConfig의 lr, batch_size, steps를 바꿔서 수렴/발산을 비교하세요.")
    print("2) lr_decay를 0.999, 0.9995 등으로 설정해 학습률 감쇠가 성능에 미치는 영향을 보세요.")
    print("3) Ridge의 l2 값을 0, 1e-4, 1e-2, 1e-1로 바꾸어 과적합 완화 효과를 기록하세요.")


if __name__ == "__main__":
    main()
