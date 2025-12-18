###################################################################################################################
# 실습 1 (누수 대응 + 중요도/Permutation Importance + VSCode 시각화 개선)

import pandas as pd
import numpy as np
from pathlib import Path

from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.inspection import permutation_importance

import matplotlib.pyplot as plt


# =========================================================
# 0. 설정
# =========================================================
CSV_PATH = Path("./AI/머신러닝/Titanic.csv")
OUT_DIR  = Path("./AI/머신러닝")
OUT_DIR.mkdir(parents=True, exist_ok=True)

STOP_IF_LEAKAGE = False   # True면 누수 감지 시 바로 중단
AUTO_SWITCH_TO_TRAIN = True  # True면 train.csv가 있으면 자동 전환
RUN_DROP_SEX_ANALYSIS = True # train.csv가 없을 때 "Sex 제외 분석"을 추가 수행


TARGET_COL = "Survived"
BASE_FEATURES = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]


# =========================================================
# 유틸: 누수 체크 (Survived == (Sex=='female') 일치율)
# =========================================================
def leakage_check(df, target_col="Survived", sex_col="Sex"):
    if sex_col not in df.columns or target_col not in df.columns:
        return None

    tmp = df[[target_col, sex_col]].copy().dropna()

    # Sex가 문자열이면 female 마스크
    if tmp[sex_col].dtype == "object":
        female_mask = tmp[sex_col].astype(str).str.lower().eq("female").astype(int)
    else:
        female_mask = pd.to_numeric(tmp[sex_col], errors="coerce").round().fillna(0).astype(int)

    y = pd.to_numeric(tmp[target_col], errors="coerce")
    if y.isna().all():
        return None
    y = y.fillna(0).astype(int)

    same_rate = (y.values == female_mask.values).mean()
    return float(same_rate)


# =========================================================
# 유틸: 데이터 준비(결측치 채움 + 인코딩)
# =========================================================
def prepare_dataframe(df_raw, target_col, feature_cols):
    df_raw = df_raw.copy()
    df_raw.columns = [c.strip() for c in df_raw.columns]

    # 컬럼명 대소문자 보정
    lower_map = {c.lower(): c for c in df_raw.columns}
    if target_col not in df_raw.columns and target_col.lower() in lower_map:
        target_col = lower_map[target_col.lower()]

    fixed_features = []
    for col in feature_cols:
        if col in df_raw.columns:
            fixed_features.append(col)
        elif col.lower() in lower_map:
            fixed_features.append(lower_map[col.lower()])
    feature_cols = fixed_features

    need_cols = [target_col] + feature_cols
    missing = [c for c in need_cols if c not in df_raw.columns]
    if missing:
        raise ValueError(f"CSV에 필요한 컬럼이 없습니다: {missing}\n현재 컬럼: {list(df_raw.columns)}")

    df = df_raw[need_cols].copy()

    # 숫자형 강제 변환 (있으면)
    for c in ["Pclass", "Age", "SibSp", "Parch", "Fare"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    # 결측치 채우기: 숫자=중앙값, 범주=최빈값
    for c in ["Pclass", "Age", "SibSp", "Parch", "Fare"]:
        if c in df.columns:
            df[c] = df[c].fillna(df[c].median())

    if "Embarked" in df.columns:
        if df["Embarked"].isna().any():
            mode_val = df["Embarked"].mode(dropna=True)
            fill_val = mode_val.iloc[0] if len(mode_val) > 0 else "S"
            df["Embarked"] = df["Embarked"].fillna(fill_val)

    # Sex 인코딩: male=0, female=1 (이미 숫자면 유지)
    if "Sex" in df.columns:
        if df["Sex"].dtype == "object":
            df["Sex"] = df["Sex"].astype(str).str.lower().map({"male": 0, "female": 1})
        else:
            df["Sex"] = pd.to_numeric(df["Sex"], errors="coerce")

        # 변환 실패 대비(최빈값)
        if df["Sex"].isna().any():
            df["Sex"] = df["Sex"].fillna(df["Sex"].mode().iloc[0])

    # Embarked 원-핫
    if "Embarked" in df.columns:
        df = pd.get_dummies(df, columns=["Embarked"], drop_first=False)

    # 타깃 정리
    y = pd.to_numeric(df[target_col], errors="coerce").fillna(0).astype(int)
    X = df.drop(columns=[target_col])

    return X, y, target_col


# =========================================================
# 유틸: 모델 학습/튜닝/평가/중요도/시각화
# =========================================================
def train_and_report(X, y, title, out_png):
    print(f"\n==================== {title} ====================")
    print("데이터 크기:", (len(y), X.shape[1]))
    print("타깃 분포:\n", y.value_counts())

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    def evaluate(model, X_te, y_te, name):
        pred = model.predict(X_te)
        acc = accuracy_score(y_te, pred)
        print(f"\n[{name}] Accuracy: {acc:.4f}")
        print("Confusion Matrix:\n", confusion_matrix(y_te, pred))
        print("Classification Report:\n", classification_report(y_te, pred, digits=4))
        return acc

    # Baseline
    baseline = DecisionTreeClassifier(max_depth=4, random_state=42)
    baseline.fit(X_train, y_train)
    _ = evaluate(baseline, X_test, y_test, "Baseline (max_depth=4)")

    # GridSearchCV
    param_grid = {
        "max_depth": [2, 3, 4, 5, 6, 8, 10, None],
        "min_samples_leaf": [1, 2, 5, 10],
        "min_samples_split": [2, 5, 10],
    }

    gs = GridSearchCV(
        estimator=DecisionTreeClassifier(random_state=42),
        param_grid=param_grid,
        scoring="accuracy",
        cv=5,
        n_jobs=-1,
    )
    gs.fit(X_train, y_train)
    best_model = gs.best_estimator_

    print("\n=== GridSearchCV Best Params ===")
    print(gs.best_params_)
    print("CV Best Score:", gs.best_score_)

    _ = evaluate(best_model, X_test, y_test, f"Best Tree {gs.best_params_}")

    # (A) 트리 기본 중요도
    fi = pd.DataFrame({
        "feature": X.columns,
        "importance": best_model.feature_importances_
    }).sort_values("importance", ascending=False)

    print("\n=== Feature Importances (Tree) Top 15 ===")
    print(fi.head(15).to_string(index=False))

    # (B) Permutation Importance (테스트 기준)
    perm = permutation_importance(
        best_model, X_test, y_test,
        n_repeats=20, random_state=42, scoring="accuracy"
    )
    perm_df = pd.DataFrame({
        "feature": X.columns,
        "perm_importance_mean": perm.importances_mean,
        "perm_importance_std": perm.importances_std
    }).sort_values("perm_importance_mean", ascending=False)

    print("\n=== Permutation Importance (Accuracy Drop) Top 15 ===")
    print(perm_df.head(15).to_string(index=False))

    # 트리 시각화(너무 크면 max_depth=3으로 그림만 제한 가능)
    plt.rcParams["figure.dpi"] = 170
    fig, ax = plt.subplots(figsize=(42, 14), dpi=220)
    plot_tree(
        best_model,
        feature_names=X.columns,
        class_names=["Dead(0)", "Survived(1)"],
        filled=True,
        rounded=True,
        fontsize=5,
        max_depth=4,
        impurity=False,    # gini 표시 제거(텍스트 줄어듦)
        proportion=True,   # value를 비율로 표시(길이 감소)
        ax=ax
    )

    fig.tight_layout()
    fig.savefig(OUT_DIR / "titanic_tree_clean.png", dpi=300, bbox_inches="tight")
    plt.show()
    print(f"\n트리 이미지 저장: {out_png}")

    return best_model


# =========================================================
# 1) Titanic.csv 로드
# =========================================================
df_raw = pd.read_csv(CSV_PATH)
df_raw.columns = [c.strip() for c in df_raw.columns]

same_rate = leakage_check(df_raw, TARGET_COL, "Sex")

if same_rate is not None and same_rate >= 0.98:
    print(
        "\n[경고] Survived가 Sex(여성=1/남성=0)과 거의 동일합니다.\n"
        f"Survived == (Sex=='female') 일치율: {same_rate:.3f}\n"
        "=> 이 데이터로는 '성별 외 생존 영향'을 정상적으로 분석할 수 없습니다.\n"
    )

    if STOP_IF_LEAKAGE:
        raise SystemExit("STOP_IF_LEAKAGE=True 이므로 중단합니다.")

    # 1) 가능하면 train.csv로 자동 전환
    train_path = CSV_PATH.with_name("train.csv")
    if AUTO_SWITCH_TO_TRAIN and train_path.exists():
        print(f"[자동 전환] 진짜 라벨이 있는 파일로 추정되는 {train_path} 를 사용합니다.")
        df_train = pd.read_csv(train_path)
        X, y, _ = prepare_dataframe(df_train, TARGET_COL, BASE_FEATURES)
        train_and_report(X, y, "Train.csv 기반 분석(정상 라벨)", OUT_DIR / "titanic_tree_train.png")

    else:
        # 2) train.csv가 없다면: Sex 제외 분석(대리변수 중요도)
        if RUN_DROP_SEX_ANALYSIS:
            print(
                "[대안] train.csv가 없어 Sex를 제외한 모델을 추가 학습합니다.\n"
                "     (주의: 이는 생존 영향이 아니라 '성별로 만든 라벨(Survived)'을 다른 변수로 근사하는 분석입니다.)\n"
            )
            X_all, y_all, _ = prepare_dataframe(df_raw, TARGET_COL, BASE_FEATURES)

            # Sex 컬럼 제거(원본이 numeric Sex=0/1 형태이므로 그냥 drop)
            if "Sex" in X_all.columns:
                X_nosex = X_all.drop(columns=["Sex"])
            else:
                X_nosex = X_all.copy()

            train_and_report(X_nosex, y_all, "Titanic.csv (Sex 제외 분석)", OUT_DIR / "titanic_tree_no_sex.png")

        else:
            # 그냥 원본으로 진행(원하면)
            X, y, _ = prepare_dataframe(df_raw, TARGET_COL, BASE_FEATURES)
            train_and_report(X, y, "Titanic.csv (누수 라벨 그대로)", OUT_DIR / "titanic_tree.png")

else:
    # 누수 없으면 정상 진행
    X, y, _ = prepare_dataframe(df_raw, TARGET_COL, BASE_FEATURES)
    train_and_report(X, y, "Titanic.csv 기반 분석(정상으로 판단)", OUT_DIR / "titanic_tree.png")


# 결정 트리
# 스무고개 게임!

# 이 과일 뭔지 맞추기
# Q1. 빨간색인가요?
# Yes -> Q2 작은가요?
            # -> Yes => 체리
            # -> No =>  사과

# No -> Q2 노란색인가요?

# 컴퓨터가 하는 일은 어떤 질문을 어떤 순서로 할지 데이터에서 자동으로 찾는것 

# 트리구조 용어
#            [루트 노드]        ← 맨 위, 첫 번째 질문
#           연소득 > 5000?
#            /         \
#          Yes          No
#          /             \
#     [내부 노드]      [내부 노드]   ← 중간 질문들
#     신용등급 > 3?    보증인 있음?
#       /    \          /    \
#     Yes    No       Yes    No
#      |      |        |      |
#   [리프]  [리프]   [리프]  [리프]  ← 최종 결정 (잎사귀)
#    승인    검토     승인    거절

#   깊이(Depth) 루트에서 리프까지 거치는 질문 수

# 좋은 질문 vs 나쁜 질문
# 핵심은 잘 나누는 질문을 찾는 것

# 데이터: 사과 10개, 오렌지 10개를 구분하고 싶음
# 나쁜 질문 : "무게가 100g" 이상인가?

# 좋은 질문 : :"빨간색이가?"

# 각 그룹이 순수 해지도록 나누기

# 순수도 

# 지니 불순도(Gini Impurity)
# Gini = 1 - (각 클래스 비율의 제곱의 합)
#      = 1 - Σ(pᵢ²)

# 직관적 의미:  랜덤을 뽑아서 랜덤으로 라벨 붙이면 틀릴 확률

# 예시 1 : 상자에 [사과 10개]만 있음
# - 사과 비율 = 10/10 = 1.0
# - Gini = 1 - (1.0²) = 1 - 1 = 0
# - 완전히 순수! ( 틀릴 일이 없음)

# 예시 2 : 상자에 [사과 5개 오렌지 5개]
# 사과 비율 = 0.5, 오렌지 비율 0.5
# - Gini = 1 - (0.5² + 0.5²) = 1 - 0.5 = 0.5
# 최대로 불순! (반반이라 가장 헷갈림)

# 예시 3 : 상자에 [사과 9개 오렌지 1개]
# 사과 비율 = 0.9, 오렌지 비율 0.1
# - Gini = 1 - (0.9² + 0.1²) = 1 - 0.82 = 0.18
# 꽤 순수함

# 이진 분류에서는 0.5
# 0 ~ 0.5 

# 다중 클래스 에서는
# 3개 0.66666
# 4개 0.75

# 엔트로피(Entropy)
# Entropy = -Σ(pᵢ × log₂(pᵢ))
# 직관적 의미: "얼마나 혼란스러운가?" (정보이론 개념)

# 예시 1: [사과 10개]
# Entropy = -(1.0 x log₂(1.0)) = 0
# 전혀 혼란스럽지 않음

# 예시 1: [사과 5개 오렌지 5개]
# Entropy = -(0.5 x log₂(0.5) = -0.5) X 2 = 1
# 최대로 혼란스러움

# 예시 1: [사과 9개 오렌지 1개]
# Entropy = 0.47
# 약간 혼란스러움

# 0 ~ 1까지 

from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 데이터 로드
iris = load_iris()
X, y = iris.data, iris.target

# 분할
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 모델 학습
model = DecisionTreeClassifier(
    criterion='gini', # 분할 기준 : 'gini' 또는 'entropy'                        
    max_depth=5, # 최대 깊이                     
    min_samples_split=10, # 분할을 위한 최소 샘플 수
    min_samples_leaf=5, # 리프 노드 최소 샘플 수
    max_features=None, # 분할에 사용할 특성 수
    random_state=42  
)
model.fit(X_train, y_train)

# 예측
y_pred = model.predict(X_test)
print(f'정확도: {accuracy_score(y_test, y_pred):.2%}')

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt


# 한글 폰트 설정 추가
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows
# plt.rcParams['font.family'] = 'AppleGothic'  # Mac
plt.rcParams['axes.unicode_minus'] = False


plt.figure(figsize=(20, 10))
plot_tree(model,
          feature_names=iris.feature_names,
          class_names=iris.target_names,
          filled=True,
          rounded=True,
          fontsize=10)
plt.title('붓꽃 분류 결정 트리')
plt.show()

# 텍스트로 출력
from sklearn.tree import export_text

tree_rules = export_text(model,
                         feature_names=list(iris.feature_names))
print(tree_rules)


import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# 1. 데이터 로드 (CSV 파일 경로)
# Titanic 데이터셋: 타이타닉호 승객 정보와 생존 여부
df = pd.read_csv('Titanic.csv')
print(df.head())  # 처음 5개 행만 출력
print(f'\n전체 데이터 크기: {df.shape}')

# 2. 필요한 특성만 선택 (dropna())
# 결측치(NaN)가 있는 행 제거
df = df[['Survived','Pclass','Sex','Age','SibSp','Parch','Fare']].dropna()
print(f'\n결측치 제거 후 데이터 크기: {df.shape}')

# Survived      생존 여부

# Pclass    객실 등급                   부유층일수록 생존율 높음
# Sex       성별                        여성 우선 구조
# Age       나이                        어린이 우선 구조
# SibSp     함께 탑승한 형제/배우자 수    가족 유무가 생존에 영향
# Parch     함께 탑승한 부모/자녀 수      가족 유무가 생존에 영향
# Fare      운임 요금                   부유층일수록 생존율 높음     

# Name      이름
# Ticket    티켓 번호
# Cabin     객실 번호           
# Embarked  탑승 항구

# 3. 성별을 숫자로 변환 (범주형 -> 숫자형)
# male: 0, female: 1로 인코딩
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# 4. 특성과 타겟 분리
# X: 예측에 사용할 특성들 (독립 변수)
X = df.drop(['Survived'], axis=1)
# y: 예측할 대상 (종속 변수 - 생존 여부)
y = df['Survived']

# 5. 훈련/테스트 데이터 분할 (80% 훈련, 20% 테스트)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6. 모델 학습
# 기본 하이퍼파라미터로 결정 트리 생성
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# 7. 평가
y_pred = model.predict(X_test)
print(f"\n정확도: {accuracy_score(y_test, y_pred):.2%}")
print(f"올바르게 예측한 개수: {accuracy_score(y_test, y_pred, normalize=False)}/{len(y_test)}")

# 8. 시각화
plt.figure(figsize=(20, 12))
plot_tree(model,
          feature_names=X.columns,
          class_names=['사망','생존'],
          filled=True,
          rounded=True,
          fontsize=10)
plt.title('타이타닉 생존 예측 결정 트리')
plt.show()

# 트리 해석 방법:
# - 각 노드: 분할 조건 (예: Sex <= 0.5)
# - gini: 불순도 (0에 가까울수록 순수)
# - samples: 해당 노드의 샘플 수
# - value: [사망 수, 생존 수]
# - class: 다수 클래스 (사망 또는 생존)