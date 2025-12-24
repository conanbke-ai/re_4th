# -*- coding: utf-8 -*-
"""
03_머신러닝기초.py
==================
(원본 PDF: 03_머신러닝기초.pdf 기반 정리 + 실습 예제 확장)

이 파일의 목표
--------------
수업 슬라이드의 흐름을 '코드로 체감'하는 것입니다.

머신러닝의 기본 과정(슬라이드 요지)
----------------------------------
1) 데이터(Data)
2) 모델(Model)
3) 학습 알고리즘(Training Algorithm)
4) 평가/예측(Evaluation & Inference)

또한 수업에서는 아래를 강조합니다.
- 데이터 전처리(결측/이상치/형식 통일/스케일링/차원축소 등)는 전체 작업 시간의 상당 부분을 차지함
- 하이퍼파라미터(학습률, 에폭, 레이어 수 등)는 학습 전에 사람이 정하는 값
- train/validation/test 분할을 통해 과적합을 점검해야 함
- 지도/비지도/강화학습 등 문제 유형별 대표 알고리즘이 다름

이 파일에 추가로 덧붙인 실무 관점(수업 보강)
--------------------------------------------
- 데이터 누수(Data Leakage)란 무엇이며, 왜 파이프라인이 중요한가
- 스케일링(표준화/정규화)의 차이와 언제 쓰는지
- 간단한 베이스라인(Baseline) 설정 방법
- 과적합/과소적합을 "정량 지표"로 확인하는 패턴

필요 패키지
-----------
- 필수: numpy
- 선택: matplotlib, scikit-learn
  (scikit-learn이 없으면 from scratch 예제만 수행)

실행
----
    python 03_머신러닝기초.py
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Optional, Tuple

import numpy as np

from 01_utils_memory_and_data import MinMaxScaler, StandardScaler, train_val_test_split


# ---------------------------------------------------------------------
# 1) 머신러닝에서 자주 쓰는 용어 정리
# ---------------------------------------------------------------------
"""
[용어 1] feature(특징), label(정답)
- feature: 모델이 보는 입력 변수 (예: 공부시간, 수면시간, 기온, 습도 ...)
- label: 모델이 맞춰야 하는 목표값/정답 (예: 시험점수, 내일 발전량, 스팸 여부 ...)

[용어 2] parameter vs hyperparameter
- parameter(파라미터): 모델이 학습으로 '찾아내는 값' (예: 선형회귀의 가중치 w, bias b)
- hyperparameter(하이퍼파라미터): 학습 전에 사람이 정하는 값
  예: 학습률(lr), 에폭(epochs), 규제 강도(lambda), 레이어 수/유닛 수 등

[용어 3] loss vs metric
- loss(손실함수): 학습 과정에서 최적화 대상으로 사용하는 함수 (미분 가능성이 중요)
- metric(평가지표): 사람이 성능을 판단하기 위한 수치 (정확도, F1, R2 등)
  * loss와 metric은 같을 수도, 다를 수도 있습니다.
"""


# ---------------------------------------------------------------------
# 2) 데이터 전처리(Preprocessing) 핵심: "데이터 품질"과 "일관성"
# ---------------------------------------------------------------------
def impute_missing_with_mean(X: np.ndarray) -> np.ndarray:
    """
    결측치 처리(아주 단순 버전): 컬럼 평균으로 대체

    실무에서는?
    - 수치형: 평균/중앙값/모델 기반 imputation(KNN, IterativeImputer 등)
    - 범주형: 최빈값/새 카테고리(Unknown) 부여
    - 결측 자체가 의미가 있는 경우(예: 센서 미수집)는 '결측 여부'를 feature로 추가하기도 함
    """
    X = X.copy()
    for j in range(X.shape[1]):
        col = X[:, j]
        mask = np.isnan(col)
        if mask.any():
            mean = np.nanmean(col)
            col[mask] = mean
            X[:, j] = col
    return X


def clip_outliers_iqr(X: np.ndarray, k: float = 1.5) -> np.ndarray:
    """
    이상치 처리(단순 버전): IQR 기반 클리핑
    - Q1, Q3로 IQR = Q3 - Q1
    - [Q1 - k*IQR, Q3 + k*IQR] 범위를 벗어나면 경계값으로 잘라냄(clip)

    왜 '제거'가 아니라 '클리핑'?
    - 데이터가 적을 때는 삭제가 학습 신호를 약화시킬 수 있음
    - 단, 명백한 오류(센서 고장 값)라면 삭제/수정이 더 타당할 수 있음
    """
    X = X.copy()
    for j in range(X.shape[1]):
        col = X[:, j]
        q1 = np.percentile(col, 25)
        q3 = np.percentile(col, 75)
        iqr = q3 - q1
        lo = q1 - k * iqr
        hi = q3 + k * iqr
        X[:, j] = np.clip(col, lo, hi)
    return X


# ---------------------------------------------------------------------
# 3) 모델 복잡도와 과적합(Overfitting): 작은 예제로 체감
# ---------------------------------------------------------------------
def polynomial_features(x: np.ndarray, degree: int) -> np.ndarray:
    """
    1차원 입력 x를 다항 특징으로 확장:
        degree=3 -> [x, x^2, x^3]

    포인트
    - 차수를 올리면(복잡도 증가) train 성능은 좋아지기 쉽지만
    - val/test 성능은 나빠질 수 있음(과적합)
    """
    x = x.reshape(-1, 1)
    return np.concatenate([x ** d for d in range(1, degree + 1)], axis=1)


def ridge_closed_form(X: np.ndarray, y: np.ndarray, l2: float = 1e-2) -> np.ndarray:
    """
    Ridge 회귀(=L2 규제) 해석해:
        w = (X^T X + λI)^(-1) X^T y

    왜 Ridge를 쓰나?
    - 다항 차수가 커지면 X^T X가 수치적으로 불안정해질 수 있음(조건수 증가)
    - 규제는 가중치가 과하게 커지는 것을 막아 과적합을 완화
    """
    I = np.eye(X.shape[1])
    return np.linalg.solve(X.T @ X + l2 * I, X.T @ y)


def mse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.mean((y_true - y_pred) ** 2))


def demo_overfitting() -> None:
    rng = np.random.default_rng(0)
    n = 220

    # 비선형 관계 + 노이즈 데이터 생성
    x = rng.uniform(-3, 3, size=n)
    y = 0.5 * x**3 - x**2 + 0.3 * x + rng.normal(0, 3.0, size=n)

    split = train_val_test_split(x.reshape(-1, 1), y, seed=0)

    degrees = [1, 2, 3, 5, 8, 12]
    print("\n[데모] 모델 복잡도(다항 차수) vs 과적합")
    print("degree | train_MSE | val_MSE | test_MSE")
    for deg in degrees:
        Xtr = polynomial_features(split.X_train[:, 0], deg)
        Xva = polynomial_features(split.X_val[:, 0], deg)
        Xte = polynomial_features(split.X_test[:, 0], deg)

        w = ridge_closed_form(Xtr, split.y_train, l2=1e-3)
        tr = Xtr @ w
        va = Xva @ w
        te = Xte @ w

        print(f"{deg:>6} | {mse(split.y_train, tr):>9.2f} | {mse(split.y_val, va):>7.2f} | {mse(split.y_test, te):>8.2f}")


# ---------------------------------------------------------------------
# 4) 데이터 누수(Data Leakage)와 파이프라인 사고방식
# ---------------------------------------------------------------------
"""
[데이터 누수]란?
- 모델이 "실제로는 알 수 없는 정보"를 학습에 사용해버리는 현상
- 결과: 검증/테스트 성능이 비정상적으로 높게 나오고, 실전 배포에서 성능이 급락

대표적인 누수 예시
1) 스케일러/인코더를 전체 데이터에 fit 해버림
   - train/val/test 모두의 통계(평균/표준편차)를 사용하게 되어 미래 정보가 섞임
2) 타깃(y) 정보를 feature 생성에 사용
   - 예: y를 포함해 상관관계 높은 지표를 먼저 계산하고 그걸 feature로 넣는 경우
3) 시계열에서 미래 시점 데이터가 과거 feature에 섞임

예방 원칙
- "fit은 train으로만"
- 변환(transform)은 train/val/test 모두 동일한 파라미터로
- (가능하면) Pipeline으로 묶어 실수 가능성을 줄이기
"""


def demo_preprocessing_and_split() -> None:
    """
    전처리 + split + scaling을 전체 흐름으로 보여주는 예제입니다.
    """
    rng = np.random.default_rng(1)
    n = 500

    # 예시: 3개 feature로 회귀 타깃 y 생성
    X = rng.normal(0, 1, size=(n, 3))
    y = 2.0 * X[:, 0] - 1.5 * X[:, 1] + 0.3 * X[:, 2] + rng.normal(0, 0.5, size=n)

    # 1) 일부 결측치 만들기(데모)
    X_missing = X.copy()
    miss_idx = rng.choice(n, size=30, replace=False)
    X_missing[miss_idx, 1] = np.nan

    # 2) 결측치 처리
    X_imputed = impute_missing_with_mean(X_missing)

    # 3) 이상치 만들기(데모) 후 클리핑
    X_out = X_imputed.copy()
    out_idx = rng.choice(n, size=10, replace=False)
    X_out[out_idx, 0] *= 8
    X_clipped = clip_outliers_iqr(X_out)

    # 4) split
    split = train_val_test_split(X_clipped, y, seed=1)

    # 5) scaling - 반드시 train으로만 fit!
    scaler = StandardScaler().fit(split.X_train)
    Xtr = scaler.transform(split.X_train)
    Xva = scaler.transform(split.X_val)
    Xte = scaler.transform(split.X_test)

    print("\n[데모] 전처리 + split + scaling")
    print("train mean(스케일 후, 대략 0 근처여야 함):", Xtr.mean(axis=0))
    print("train std (스케일 후, 대략 1 근처여야 함):", Xtr.std(axis=0))
    print("val  mean(스케일 후):", Xva.mean(axis=0), "(val을 0으로 맞추는 것이 목적이 아님)")

    # 선택: sklearn로 baseline 모델 확인
    try:
        from sklearn.linear_model import LinearRegression
        from sklearn.metrics import mean_squared_error, r2_score

        model = LinearRegression()
        model.fit(Xtr, split.y_train)

        pred_val = model.predict(Xva)
        pred_test = model.predict(Xte)

        print("\n[baseline] sklearn LinearRegression")
        print("val  MSE:", mean_squared_error(split.y_val, pred_val))
        print("val  R2 :", r2_score(split.y_val, pred_val))
        print("test MSE:", mean_squared_error(split.y_test, pred_test))
        print("test R2 :", r2_score(split.y_test, pred_test))
    except Exception:
        print("\n[info] scikit-learn이 없어 baseline 예제를 건너뜁니다. (pip install scikit-learn)")


# ---------------------------------------------------------------------
# 5) main
# ---------------------------------------------------------------------
def main() -> None:
    demo_overfitting()
    demo_preprocessing_and_split()

    print("\n[연습문제]")
    print("1) StandardScaler 대신 MinMaxScaler를 적용해보고, 성능/안정성 차이를 관찰하세요.")
    print("2) 다항 차수(degree)와 Ridge 규제(l2)를 바꿔가며 과적합/일반화의 변화를 기록해보세요.")
    print("3) 전처리 단계에서 '결측 여부'를 추가 feature로 만들어 성능이 개선되는지 실험해보세요.")


if __name__ == "__main__":
    main()
