# -*- coding: utf-8 -*-
"""
05_분류.py
==========
(원본 PDF: 05_분류.pdf 기반 정리 + 실습 예제 확장)

수업 슬라이드 핵심
------------------
- 분류의 주요 개념
  * 이진 분류(Binary): 클래스 2개 (0/1)
  * 다항 분류(Multi-class): 여러 클래스 중 1개 선택
  * 다중 라벨(Multi-label): 샘플이 여러 클래스에 동시에 속할 수 있음
- 이항 분류: Sigmoid + Binary Cross Entropy(BCE)
- 다항 분류: Softmax + (Categorical Cross Entropy / Sparse Categorical Cross Entropy)
- 로지스틱 회귀(Logistic Regression): 선형 모델 + sigmoid로 확률 예측
- 역전파(Backpropagation): 오차를 이용해 각 가중치의 기여도를 계산하여 업데이트(체인룰)

이 파일에 추가한 보강(실무 관점)
-------------------------------
- 임계값(threshold) 조정이 왜 중요한가(특히 불균형 데이터)
- 정확도(Accuracy)만 보면 위험한 이유
- confusion matrix, precision/recall/F1의 해석
- (간단) ROC-AUC와 PR-AUC의 직관

실행:
    python 05_분류.py
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

import numpy as np


# ---------------------------------------------------------------------
# 1) 활성화 함수 / 확률 변환
# ---------------------------------------------------------------------
def sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Sigmoid
    - 이진 분류에서 확률(0~1)로 변환할 때 사용
    - z가 크면 1에 가까워지고, 작으면 0에 가까워짐
    - 단점: 큰 |z|에서 기울기(미분값)가 거의 0 -> 깊은 네트워크에서는 기울기 소실 원인이 됨
    """
    return 1.0 / (1.0 + np.exp(-z))


def softmax(z: np.ndarray, axis: int = 1) -> np.ndarray:
    """
    Softmax
    - 다항 분류에서 클래스별 점수(logit)를 확률로 변환
    - 각 샘플에 대해 확률 합이 1이 되도록 정규화
    - 수치 안정화를 위해 max를 빼는 트릭을 사용(overflow 방지)
    """
    z = z - np.max(z, axis=axis, keepdims=True)
    exp_z = np.exp(z)
    return exp_z / np.sum(exp_z, axis=axis, keepdims=True)


# ---------------------------------------------------------------------
# 2) 손실 함수: BCE / CCE / Sparse CCE
# ---------------------------------------------------------------------
def binary_cross_entropy(y_true: np.ndarray, y_prob: np.ndarray, eps: float = 1e-12) -> float:
    """
    Binary Cross Entropy (이항 분류)
    - y_true: 0/1
    - y_prob: sigmoid 출력 확률
    """
    y_prob = np.clip(y_prob, eps, 1 - eps)
    return float(-np.mean(y_true * np.log(y_prob) + (1 - y_true) * np.log(1 - y_prob)))


def categorical_cross_entropy_onehot(y_true_onehot: np.ndarray, y_prob: np.ndarray, eps: float = 1e-12) -> float:
    """
    Categorical Cross Entropy (One-hot)
    - y_true_onehot: (n, C) 형태의 원-핫 벡터
      예: 클래스 4개, 정답이 2번이면 [0,1,0,0]
    """
    y_prob = np.clip(y_prob, eps, 1 - eps)
    return float(-np.mean(np.sum(y_true_onehot * np.log(y_prob), axis=1)))


def categorical_cross_entropy_sparse(y_true_int: np.ndarray, y_prob: np.ndarray, eps: float = 1e-12) -> float:
    """
    Sparse Categorical Cross Entropy
    - y_true_int: (n,) 형태의 정수 라벨
      예: 클래스 4개, 정답이 2번이면 2
    - 장점: 클래스 수가 크면(one-hot이 거대하면) 메모리와 연산이 유리
    """
    y_prob = np.clip(y_prob, eps, 1 - eps)
    n = y_prob.shape[0]
    return float(-np.mean(np.log(y_prob[np.arange(n), y_true_int])))


# ---------------------------------------------------------------------
# 3) 로지스틱 회귀 (from scratch)
# ---------------------------------------------------------------------
def add_bias(X: np.ndarray) -> np.ndarray:
    return np.concatenate([np.ones((X.shape[0], 1)), X], axis=1)


@dataclass
class LogisticConfig:
    lr: float = 0.2
    steps: int = 2_000


def fit_logistic_regression(X: np.ndarray, y: np.ndarray, cfg: LogisticConfig) -> np.ndarray:
    """
    로지스틱 회귀 학습(경사하강법)
    - 모델: p = sigmoid(Xw)
    - 손실: BCE
    - gradient: (1/n) X^T (p - y)

    포인트
    - 선형 회귀와 달리 출력이 확률(0~1)
    - 임계값(threshold)을 0.5로 두는 것이 기본이지만,
      클래스 불균형/비용 구조에 따라 조정해야 실무적으로 유의미해지는 경우가 많음
    """
    Xb = add_bias(X)
    n, d = Xb.shape
    w = np.zeros(d)

    for _ in range(cfg.steps):
        p = sigmoid(Xb @ w)
        grad = (Xb.T @ (p - y)) / n
        w -= cfg.lr * grad

    return w


def predict_proba_logistic(X: np.ndarray, w: np.ndarray) -> np.ndarray:
    return sigmoid(add_bias(X) @ w)


def predict_logistic(X: np.ndarray, w: np.ndarray, threshold: float = 0.5) -> np.ndarray:
    return (predict_proba_logistic(X, w) >= threshold).astype(int)


# ---------------------------------------------------------------------
# 4) 평가: confusion matrix, precision/recall/f1, accuracy
# ---------------------------------------------------------------------
def confusion_matrix_binary(y_true: np.ndarray, y_pred: np.ndarray) -> Tuple[int, int, int, int]:
    """
    이진 분류 혼동행렬
    - TN: true negative (정상 -> 정상)
    - FP: false positive(정상 -> 양성으로 오탐)
    - FN: false negative(양성 -> 정상으로 미탐)
    - TP: true positive (양성 -> 양성)
    """
    tn = int(np.sum((y_true == 0) & (y_pred == 0)))
    fp = int(np.sum((y_true == 0) & (y_pred == 1)))
    fn = int(np.sum((y_true == 1) & (y_pred == 0)))
    tp = int(np.sum((y_true == 1) & (y_pred == 1)))
    return tn, fp, fn, tp


def precision_recall_f1(tn: int, fp: int, fn: int, tp: int) -> Tuple[float, float, float]:
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0.0
    return precision, recall, f1


# ---------------------------------------------------------------------
# 5) 역전파(Backpropagation) - "개념"을 코드/주석으로 설명
# ---------------------------------------------------------------------
"""
역전파는 "미분(기울기)을 효율적으로 계산"하기 위한 알고리즘입니다.
핵심은 체인룰(chain rule)입니다.

예를 들어 아래와 같은 계산 그래프가 있다고 합시다.

    z = w*x
    a = sigmoid(z)
    L = BCE(y, a)

역전파는 L을 w에 대해 미분하기 위해 다음을 연쇄적으로 계산합니다.
    dL/dw = dL/da * da/dz * dz/dw

딥러닝 프레임워크(PyTorch/TensorFlow)는
이 과정을 자동으로 수행(자동미분, autograd)하여 복잡한 네트워크에서도 학습이 가능해집니다.
"""


# ---------------------------------------------------------------------
# 6) 데모
# ---------------------------------------------------------------------
def demo_losses() -> None:
    print("== 손실함수(BCE / CCE / Sparse CCE) 예시 ==")

    # 이항 분류 손실 예
    y_true = np.array([1, 0, 1, 1])
    y_prob = np.array([0.9, 0.4, 0.2, 0.8])
    print("BCE:", binary_cross_entropy(y_true, y_prob))

    # 다항 분류 손실 예
    y_prob_mc = np.array([
        [0.1, 0.7, 0.1, 0.1],
        [0.8, 0.1, 0.05, 0.05],
    ])
    y_true_sparse = np.array([1, 0])
    y_true_onehot = np.array([
        [0, 1, 0, 0],
        [1, 0, 0, 0],
    ])

    print("CCE(one-hot):", categorical_cross_entropy_onehot(y_true_onehot, y_prob_mc))
    print("SCCE(sparse):", categorical_cross_entropy_sparse(y_true_sparse, y_prob_mc))


def demo_logistic_regression(threshold: float = 0.5) -> None:
    rng = np.random.default_rng(0)
    n = 800

    # 2개 클러스터 생성(이진 분류)
    X0 = rng.normal(loc=[-1.0, -1.0], scale=1.0, size=(n // 2, 2))
    X1 = rng.normal(loc=[2.0, 2.0], scale=1.0, size=(n // 2, 2))
    X = np.vstack([X0, X1])
    y = np.array([0] * (n // 2) + [1] * (n // 2), dtype=float)

    # 학습
    w = fit_logistic_regression(X, y, LogisticConfig(lr=0.2, steps=2500))

    # 예측
    prob = predict_proba_logistic(X, w)
    y_pred = (prob >= threshold).astype(int)
    y_true = y.astype(int)

    # 평가
    loss = binary_cross_entropy(y_true, prob)
    tn, fp, fn, tp = confusion_matrix_binary(y_true, y_pred)
    acc = float(np.mean(y_pred == y_true))
    precision, recall, f1 = precision_recall_f1(tn, fp, fn, tp)

    print("\n== Logistic Regression (from scratch) ==")
    print(f"threshold={threshold}")
    print(f"BCE Loss: {loss:.4f}")
    print(f"Accuracy: {acc:.4f}")
    print(f"Confusion (TN,FP,FN,TP): {(tn, fp, fn, tp)}")
    print(f"Precision/Recall/F1: {precision:.4f} / {recall:.4f} / {f1:.4f}")

    # 임계값을 바꾸면 precision/recall이 어떻게 달라지는지 간단히 확인
    for t in [0.3, 0.5, 0.7]:
        yp = (prob >= t).astype(int)
        tn, fp, fn, tp = confusion_matrix_binary(y_true, yp)
        pr, rc, f1 = precision_recall_f1(tn, fp, fn, tp)
        print(f"  t={t:.1f} -> precision={pr:.3f}, recall={rc:.3f}, f1={f1:.3f}")


def main() -> None:
    demo_losses()
    demo_logistic_regression(threshold=0.5)

    print("\n[연습문제]")
    print("1) 데이터가 불균형(positive 10%, negative 90%)인 상황을 만들어 threshold 최적화를 해보세요.")
    print("2) 다항 분류용 softmax regression을 직접 구현해보세요(softmax + sparse CCE).")
    print("3) sklearn LogisticRegression과 성능/계수를 비교해보세요.")


if __name__ == "__main__":
    main()
