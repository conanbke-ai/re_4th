###################################################################################################################
# Titanic 생존 예측 분류 모델 (EDA -> 전처리 -> 피처 엔지니어링 -> 3모델 비교 -> RF 튜닝 -> 평가/중요도/Strata 리포트)
###################################################################################################################

import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_validate, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score, f1_score, roc_auc_score,
    confusion_matrix, classification_report,
    RocCurveDisplay
)
from sklearn.inspection import permutation_importance


# =========================================================
# 0) 경로/설정 (VSCode 기준: 파일 위치 맞게 수정)
# =========================================================
CANDIDATE_TRAIN = [Path("Titanic1.csv"), Path("./AI/머신러닝/Titanic1.csv")]
CANDIDATE_TEST  = [Path("Titanic2.csv"), Path("./AI/머신러닝/Titanic2.csv")]

OUT_DIR = Path("./AI/머신러닝/output")
OUT_DIR.mkdir(parents=True, exist_ok=True)

RANDOM_STATE = 42
FAST_MODE = True  # True: 튜닝 그리드 축소(빠름) / False: 넓은 그리드(느림)

# 결정트리 시각화(겹침 방지)
TREE_FIGSIZE = (52, 16)
TREE_FONT_SIZE = 6
TREE_PLOT_DEPTH = 3

plt.rcParams["figure.dpi"] = 170


def pick_path(candidates):
    for p in candidates:
        if p.exists():
            return p
    raise FileNotFoundError(f"파일을 찾지 못했습니다. 후보 경로: {candidates}")


TRAIN_PATH = pick_path(CANDIDATE_TRAIN)
TEST_PATH  = pick_path(CANDIDATE_TEST)

print("사용 파일:")
print(" - TRAIN:", TRAIN_PATH)
print(" - TEST :", TEST_PATH)


# =========================================================
# 1) 컬럼 표준화 (대소문자/공백 대응)
# =========================================================
def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = [c.strip() for c in df.columns]
    standard = ["PassengerId", "Survived", "Pclass", "Name", "Sex", "Age", "SibSp", "Parch",
                "Ticket", "Fare", "Cabin", "Embarked"]
    lower_map = {c.lower(): c for c in df.columns}
    rename_map = {}
    for std in standard:
        if std not in df.columns and std.lower() in lower_map:
            rename_map[lower_map[std.lower()]] = std
    if rename_map:
        df = df.rename(columns=rename_map)
    return df


# =========================================================
# 2) 누수 체크: Survived == (Sex=='female') 일치율
# =========================================================
def leakage_rate_survived_equals_female(df: pd.DataFrame):
    if "Survived" not in df.columns or "Sex" not in df.columns:
        return None
    tmp = df[["Survived", "Sex"]].dropna().copy()
    female = tmp["Sex"].astype(str).str.lower().eq("female").astype(int)
    y = pd.to_numeric(tmp["Survived"], errors="coerce").dropna().astype(int)
    if len(y) == 0:
        return None
    tmp = tmp.loc[y.index]
    female = female.loc[y.index]
    return float((y.values == female.values).mean())


# =========================================================
# 3) 1단계: EDA
# =========================================================
def eda(df: pd.DataFrame, prefix="train"):
    print(f"\n==================== 1단계: EDA ({prefix}) ====================")
    print("shape:", df.shape)
    print(df.head(3))

    # 결측치
    missing = df.isna().sum().sort_values(ascending=False)
    print("\n[결측치 개수 Top 15]")
    print(missing.head(15))

    miss = missing[missing > 0]
    if len(miss) > 0:
        plt.figure(figsize=(10, 4))
        plt.bar(miss.index.astype(str), miss.values)
        plt.xticks(rotation=45, ha="right")
        plt.title("Missing values count by column")
        plt.tight_layout()
        plt.savefig(OUT_DIR / f"{prefix}_eda_missing.png", bbox_inches="tight")
        plt.show()

    # 생존/사망 비율
    if "Survived" in df.columns:
        counts = df["Survived"].value_counts().sort_index()
        plt.figure(figsize=(5, 4))
        plt.bar(["Dead(0)", "Survived(1)"], [counts.get(0, 0), counts.get(1, 0)])
        plt.title("Survival count")
        plt.tight_layout()
        plt.savefig(OUT_DIR / f"{prefix}_eda_survival_count.png", bbox_inches="tight")
        plt.show()

        ratio = (df["Survived"].value_counts(normalize=True).sort_index() * 100).round(2)
        print("\n[생존 비율(%)]")
        print(ratio)

    # 범주별 생존율
    def plot_rate(col, title):
        if "Survived" not in df.columns or col not in df.columns:
            return
        rates = df.groupby(col)["Survived"].mean().sort_values(ascending=False)
        plt.figure(figsize=(6, 4))
        plt.bar(rates.index.astype(str), rates.values)
        plt.ylim(0, 1)
        plt.title(title)
        plt.ylabel("Survival rate")
        plt.tight_layout()
        plt.savefig(OUT_DIR / f"{prefix}_eda_survival_rate_{col}.png", bbox_inches="tight")
        plt.show()
        print(f"\n[{col}] 생존율")
        print(rates)

    plot_rate("Sex", "Survival rate by Sex")
    plot_rate("Pclass", "Survival rate by Pclass")
    plot_rate("Embarked", "Survival rate by Embarked")

    # 상관관계(숫자형)
    numeric_cols = [c for c in ["Survived", "Pclass", "Age", "SibSp", "Parch", "Fare"] if c in df.columns]
    if len(numeric_cols) >= 2:
        tmp = df[numeric_cols].copy()
        for c in numeric_cols:
            tmp[c] = pd.to_numeric(tmp[c], errors="coerce")
        corr = tmp.corr()

        plt.figure(figsize=(6, 5))
        plt.imshow(corr.values, aspect="auto")
        plt.xticks(range(len(corr.columns)), corr.columns, rotation=45, ha="right")
        plt.yticks(range(len(corr.index)), corr.index)
        plt.colorbar()
        plt.title("Correlation heatmap (numeric)")
        plt.tight_layout()
        plt.savefig(OUT_DIR / f"{prefix}_eda_corr_heatmap.png", bbox_inches="tight")
        plt.show()


# =========================================================
# 4) 피처 엔지니어링 Transformer
#    - Title (from Name)
#    - FamilySize, IsAlone
#    - TicketGroupSize (from Ticket)
#    - Deck (from Cabin)
# =========================================================
class TitanicFeatureEngineer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        X = X.copy()

        # TicketGroupSize: TRAIN 기준으로 티켓별 카운트 학습
        if "Ticket" in X.columns:
            ticket = X["Ticket"].astype(str)
            self.ticket_count_ = ticket.value_counts().to_dict()
        else:
            self.ticket_count_ = {}

        return self

    @staticmethod
    def _extract_title(name: str) -> str:
        if pd.isna(name):
            return "Unknown"
        name = str(name)
        m = re.search(r",\s*([^\.]+)\.", name)
        if not m:
            return "Unknown"
        title = m.group(1).strip()
        if title in ["Mlle", "Ms"]:
            return "Miss"
        if title == "Mme":
            return "Mrs"
        return title

    @staticmethod
    def _extract_deck(cabin: str) -> str:
        if pd.isna(cabin):
            return "Unknown"
        cabin = str(cabin).strip()
        if cabin == "":
            return "Unknown"
        # Cabin이 "C85" / "C23 C25 C27" 같은 형태일 수 있으니 첫 글자만
        return cabin[0].upper()

    def transform(self, X):
        X = X.copy()

        # Title
        if "Name" in X.columns:
            X["Title"] = X["Name"].apply(self._extract_title)
            common = set(["Mr", "Mrs", "Miss", "Master"])
            X["Title"] = X["Title"].apply(lambda t: t if t in common else "Rare")
            X = X.drop(columns=["Name"])
        else:
            X["Title"] = "Unknown"

        # FamilySize, IsAlone
        for c in ["SibSp", "Parch"]:
            if c in X.columns:
                X[c] = pd.to_numeric(X[c], errors="coerce")
        sibsp = X["SibSp"] if "SibSp" in X.columns else 0
        parch = X["Parch"] if "Parch" in X.columns else 0
        X["FamilySize"] = (sibsp.fillna(0) + parch.fillna(0) + 1).astype(int)
        X["IsAlone"] = (X["FamilySize"] == 1).astype(int)

        # TicketGroupSize
        if "Ticket" in X.columns:
            ticket = X["Ticket"].astype(str)
            X["TicketGroupSize"] = ticket.map(self.ticket_count_).fillna(1).astype(int)
        else:
            X["TicketGroupSize"] = 1

        # Deck
        if "Cabin" in X.columns:
            X["Deck"] = X["Cabin"].apply(self._extract_deck)
            X = X.drop(columns=["Cabin"])
        else:
            X["Deck"] = "Unknown"

        return X


# =========================================================
# 5) 전처리 파이프라인
# =========================================================
RAW_FEATURES = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked", "Name", "Ticket", "Cabin"]

NUM_FEATURES = ["Pclass", "Age", "SibSp", "Parch", "Fare", "FamilySize", "IsAlone", "TicketGroupSize"]
CAT_FEATURES = ["Sex", "Embarked", "Title", "Deck"]


def build_preprocess():
    numeric_pipe = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])
    categorical_pipe = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ])

    preprocess = ColumnTransformer(
        transformers=[
            ("num", numeric_pipe, NUM_FEATURES),
            ("cat", categorical_pipe, CAT_FEATURES),
        ],
        remainder="drop"
    )
    return preprocess


def get_feature_names(prep: ColumnTransformer):
    ohe = prep.named_transformers_["cat"].named_steps["onehot"]
    cat_names = list(ohe.get_feature_names_out(CAT_FEATURES))
    return list(NUM_FEATURES) + cat_names


# =========================================================
# 6) 모델 비교(CV): Accuracy + F1 + ROC-AUC
# =========================================================
def compare_models_cv(X_train, y_train):
    print("\n==================== 3단계: 모델 학습 및 비교 (CV) ====================")
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)

    scoring = {"acc": "accuracy", "f1": "f1", "auc": "roc_auc"}

    candidates = {
        "LogisticRegression": LogisticRegression(max_iter=3000, random_state=RANDOM_STATE),
        "DecisionTree": DecisionTreeClassifier(random_state=RANDOM_STATE),
        "RandomForest": RandomForestClassifier(random_state=RANDOM_STATE),
    }

    for name, model in candidates.items():
        pipe = Pipeline(steps=[
            ("fe", TitanicFeatureEngineer()),
            ("prep", build_preprocess()),
            ("model", model),
        ])
        res = cross_validate(pipe, X_train, y_train, cv=cv, scoring=scoring, n_jobs=-1)
        print(f"\n[{name}]")
        print(f"  Accuracy: {res['test_acc'].mean():.4f} ± {res['test_acc'].std():.4f}")
        print(f"  F1      : {res['test_f1'].mean():.4f} ± {res['test_f1'].std():.4f}")
        print(f"  ROC-AUC : {res['test_auc'].mean():.4f} ± {res['test_auc'].std():.4f}")


# =========================================================
# 7) RF 튜닝(GridSearchCV): Accuracy refit + F1/AUC 확인
# =========================================================
def tune_random_forest(X_train, y_train):
    print("\n==================== 3단계: RandomForest 튜닝 (GridSearchCV) ====================")

    base_pipe = Pipeline(steps=[
        ("fe", TitanicFeatureEngineer()),
        ("prep", build_preprocess()),
        ("model", RandomForestClassifier(random_state=RANDOM_STATE)),
    ])

    if FAST_MODE:
        param_grid = {
            "model__n_estimators": [400],
            "model__max_depth": [None, 8, 12],
            "model__min_samples_split": [2, 5],
            "model__min_samples_leaf": [1, 2],
            "model__max_features": ["sqrt"],
        }
    else:
        param_grid = {
            "model__n_estimators": [200, 400, 600],
            "model__max_depth": [None, 6, 8, 10, 12],
            "model__min_samples_split": [2, 5, 10],
            "model__min_samples_leaf": [1, 2, 5],
            "model__max_features": ["sqrt", "log2"],
        }

    scoring = {"acc": "accuracy", "f1": "f1", "auc": "roc_auc"}

    gs = GridSearchCV(
        estimator=base_pipe,
        param_grid=param_grid,
        scoring=scoring,
        refit="acc",
        cv=5,
        n_jobs=-1
    )
    gs.fit(X_train, y_train)

    print("Best Params:", gs.best_params_)
    print("Best CV Accuracy:", gs.best_score_)

    best_idx = gs.best_index_
    print("Best CV F1     :", gs.cv_results_["mean_test_f1"][best_idx])
    print("Best CV ROC-AUC:", gs.cv_results_["mean_test_auc"][best_idx])

    return gs.best_estimator_


# =========================================================
# 8) 최종 평가(Accuracy/F1/ROC-AUC + ROC curve)
# =========================================================
def evaluate_final(model, X_test, y_test, title="BestRF"):
    print("\n==================== 4단계: 최종 평가 (Test) ====================")

    pred = model.predict(X_test)
    proba = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else None

    acc = accuracy_score(y_test, pred)
    f1 = f1_score(y_test, pred)

    print(f"[{title}]")
    print(f"  Accuracy: {acc:.4f}")
    print(f"  F1      : {f1:.4f}")

    if proba is not None and len(np.unique(y_test)) == 2:
        auc = roc_auc_score(y_test, proba)
        print(f"  ROC-AUC : {auc:.4f}")
    else:
        auc = np.nan
        print("  ROC-AUC : NaN (확률 미지원 또는 한 클래스만 존재)")

    cm = confusion_matrix(y_test, pred)
    print("\nConfusion Matrix:\n", cm)
    print("\nClassification Report:\n", classification_report(y_test, pred, digits=4))

    # 혼동행렬 저장
    plt.figure(figsize=(4, 4))
    plt.imshow(cm, aspect="auto")
    plt.title(f"Confusion Matrix - {title}")
    plt.xticks([0, 1], ["Pred 0", "Pred 1"])
    plt.yticks([0, 1], ["True 0", "True 1"])
    for i in range(2):
        for j in range(2):
            plt.text(j, i, cm[i, j], ha="center", va="center")
    plt.colorbar()
    plt.tight_layout()
    plt.savefig(OUT_DIR / f"eval_confusion_{title}.png", bbox_inches="tight")
    plt.show()

    # ROC curve 저장
    if proba is not None and len(np.unique(y_test)) == 2:
        RocCurveDisplay.from_predictions(y_test, proba)
        plt.title(f"ROC Curve - {title}")
        plt.tight_layout()
        plt.savefig(OUT_DIR / f"eval_roc_{title}.png", bbox_inches="tight")
        plt.show()


# =========================================================
# 9) 중요도 분석
# =========================================================
def importance_analysis(best_model, X_test, y_test):
    print("\n==================== 4단계: 중요도 분석 ====================")

    prep = best_model.named_steps["prep"]
    clf  = best_model.named_steps["model"]

    # (A) RF feature_importances_ (원핫 포함)
    feat_names = get_feature_names(prep)
    fi = pd.DataFrame({"feature": feat_names, "importance": clf.feature_importances_}).sort_values("importance", ascending=False)

    print("\n[RF feature_importances_ Top 20 (원핫 포함)]")
    print(fi.head(20).to_string(index=False))

    topk = 15
    plt.figure(figsize=(10, 5))
    plt.barh(fi.head(topk)["feature"][::-1], fi.head(topk)["importance"][::-1])
    plt.title("RandomForest Feature Importance (Top 15)")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "fi_rf_top15.png", bbox_inches="tight")
    plt.show()

    # (B) Permutation Importance (원본 컬럼 기준)
    perm = permutation_importance(
        best_model, X_test, y_test,
        n_repeats=20, random_state=RANDOM_STATE, scoring="accuracy"
    )
    perm_df = pd.DataFrame({
        "feature": list(X_test.columns),
        "perm_importance_mean": perm.importances_mean,
        "perm_importance_std": perm.importances_std
    }).sort_values("perm_importance_mean", ascending=False)

    print("\n[Permutation Importance (원본 컬럼 기준, Accuracy drop)]")
    print(perm_df.to_string(index=False))

    plt.figure(figsize=(8, 4))
    plt.barh(perm_df["feature"][::-1], perm_df["perm_importance_mean"][::-1])
    plt.title("Permutation Importance (Accuracy Drop)")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "fi_permutation.png", bbox_inches="tight")
    plt.show()


# =========================================================
# 10) Stratified 성능 리포트: Sex/Pclass + Sex×Pclass
# =========================================================
def stratified_performance_report(model, X_test: pd.DataFrame, y_test: pd.Series,
                                  group_cols=("Sex", "Pclass"),
                                  title="Stratified performance (Test)"):
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else None

    def safe_auc(y_true, proba):
        if proba is None:
            return np.nan
        if len(np.unique(y_true)) < 2:
            return np.nan
        return roc_auc_score(y_true, proba)

    def metrics(mask):
        yt = y_test[mask]
        yp = y_pred[mask]
        pr = y_proba[mask] if y_proba is not None else None
        return {
            "n": int(len(yt)),
            "pos_rate": float(np.mean(yt)) if len(yt) else np.nan,
            "accuracy": float(accuracy_score(yt, yp)) if len(yt) else np.nan,
            "f1": float(f1_score(yt, yp)) if len(yt) else np.nan,
            "roc_auc": float(safe_auc(yt, pr)),
        }

    print(f"\n==================== {title} ====================")

    # 단일 그룹별
    for col in group_cols:
        if col not in X_test.columns:
            print(f"[주의] X_test에 '{col}' 컬럼이 없어 그룹별 성능 계산 불가")
            continue

        rows = []
        for val in sorted(X_test[col].dropna().unique()):
            m = (X_test[col] == val).values
            row = metrics(m)
            row[col] = val
            rows.append(row)

        df_rep = pd.DataFrame(rows).sort_values("n", ascending=False)
        print(f"\n--- By {col} ---")
        print(df_rep[[col, "n", "pos_rate", "accuracy", "f1", "roc_auc"]].to_string(index=False))

    # 조합 그룹(Sex x Pclass)
    if len(group_cols) >= 2:
        a, b = group_cols[0], group_cols[1]
        if a in X_test.columns and b in X_test.columns:
            combos = X_test[[a, b]].dropna().drop_duplicates()
            try:
                combos = combos.sort_values([a, b])
            except Exception:
                pass

            rows = []
            for _, r in combos.iterrows():
                va, vb = r[a], r[b]
                m = ((X_test[a] == va) & (X_test[b] == vb)).values
                row = metrics(m)
                row[a] = va
                row[b] = vb
                rows.append(row)

            df_combo = pd.DataFrame(rows).sort_values("n", ascending=False)
            print(f"\n--- By {a} x {b} ---")
            print(df_combo[[a, b, "n", "pos_rate", "accuracy", "f1", "roc_auc"]].to_string(index=False))


# =========================================================
# 11) 결정트리 시각화 저장(겹침 방지)
# =========================================================
def save_decision_tree_visual(X_train, y_train):
    dt_pipe = Pipeline(steps=[
        ("fe", TitanicFeatureEngineer()),
        ("prep", build_preprocess()),
        ("model", DecisionTreeClassifier(max_depth=4, random_state=RANDOM_STATE)),
    ])
    dt_pipe.fit(X_train, y_train)

    prep = dt_pipe.named_steps["prep"]
    feature_names = get_feature_names(prep)

    plt.rcParams["figure.dpi"] = 220
    fig, ax = plt.subplots(figsize=TREE_FIGSIZE)
    plot_tree(
        dt_pipe.named_steps["model"],
        feature_names=feature_names,
        class_names=["Dead(0)", "Survived(1)"],
        filled=True,
        rounded=True,
        fontsize=TREE_FONT_SIZE,
        max_depth=TREE_PLOT_DEPTH,
        ax=ax
    )
    fig.tight_layout()
    out = OUT_DIR / "decision_tree_depth3.png"
    fig.savefig(out, dpi=300, bbox_inches="tight")
    plt.show()
    print(f"\n[저장] 결정트리 시각화: {out}")


# =========================================================
# 12) TEST 처리: Survived 없으면 submission 생성 / 누수면 평가 경고
# =========================================================
def handle_test(best_model, test_df: pd.DataFrame):
    print("\n==================== (옵션) TEST 처리 ====================")
    print("TEST shape:", test_df.shape)

    # 예측에 필요한 컬럼 체크
    missing = [c for c in RAW_FEATURES if c not in test_df.columns]
    if missing:
        print(f"[주의] TEST에 필요한 컬럼이 없습니다: {missing}")
        return

    # Survived가 있으면 누수 체크 후 외부평가(의미 있으면)
    if "Survived" in test_df.columns:
        leak = leakage_rate_survived_equals_female(test_df)
        if leak is not None and leak >= 0.98:
            print(f"[경고] TEST Survived가 Sex와 거의 동일(일치율={leak:.3f}) → 평가 의미가 매우 약함(gender_submission 가능성).")
            return

        df_eval = test_df.dropna(subset=RAW_FEATURES + ["Survived"]).copy()
        X_ext = df_eval[RAW_FEATURES]
        y_ext = df_eval["Survived"].astype(int)

        pred = best_model.predict(X_ext)
        proba = best_model.predict_proba(X_ext)[:, 1]

        print("\n[External Evaluation]")
        print("  Accuracy:", accuracy_score(y_ext, pred))
        print("  F1      :", f1_score(y_ext, pred))
        print("  ROC-AUC :", roc_auc_score(y_ext, proba))
        print("Confusion Matrix:\n", confusion_matrix(y_ext, pred))
        print("Classification Report:\n", classification_report(y_ext, pred, digits=4))
        return

    # Survived 없으면 submission 저장
    pid = test_df["PassengerId"] if "PassengerId" in test_df.columns else pd.Series(np.arange(len(test_df)), name="PassengerId")
    X_submit = test_df[RAW_FEATURES].copy()
    pred_submit = best_model.predict(X_submit)

    sub = pd.DataFrame({"PassengerId": pid, "Survived": pred_submit.astype(int)})
    out_csv = OUT_DIR / "submission.csv"
    sub.to_csv(out_csv, index=False, encoding="utf-8-sig")
    print(f"[저장] submission.csv: {out_csv}")


# =========================================================
# MAIN
# =========================================================
def main():
    train_df = normalize_columns(pd.read_csv(TRAIN_PATH))
    test_df  = normalize_columns(pd.read_csv(TEST_PATH))

    # 누수 참고 출력
    leak_train = leakage_rate_survived_equals_female(train_df)
    leak_test  = leakage_rate_survived_equals_female(test_df)
    print("\n[누수 체크] Survived == (Sex=='female') 일치율")
    print(" - TRAIN:", None if leak_train is None else round(leak_train, 3))
    print(" - TEST :", None if leak_test  is None else round(leak_test, 3))

    # EDA (TRAIN)
    eda(train_df, prefix="train")

    # 필요한 컬럼 확인
    need_cols = ["Survived"] + RAW_FEATURES
    missing = [c for c in need_cols if c not in train_df.columns]
    if missing:
        raise ValueError(f"TRAIN에 필요한 컬럼이 없습니다: {missing}\n현재 컬럼: {list(train_df.columns)}")

    # 2단계: 분할
    X = train_df[RAW_FEATURES].copy()
    y = train_df["Survived"].astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y
    )
    print("\n==================== 2단계: 분할 ====================")
    print("X_train:", X_train.shape, "X_test:", X_test.shape)

    # 3단계: 모델 비교(CV)
    compare_models_cv(X_train, y_train)

    # 3단계: RF 튜닝
    best_model = tune_random_forest(X_train, y_train)

    # 4단계: 최종 평가(Accuracy/F1/ROC-AUC)
    evaluate_final(best_model, X_test, y_test, title="BestRF_FE_All")

    # 4단계: 중요도 분석
    importance_analysis(best_model, X_test, y_test)

    # 4단계: 성별/등급별 strata 성능 리포트
    stratified_performance_report(best_model, X_test, y_test, group_cols=("Sex", "Pclass"))

    # (옵션) 결정트리 시각화 저장
    save_decision_tree_visual(X_train, y_train)

    # (옵션) TEST 처리
    handle_test(best_model, test_df)

    print("\n완료. 결과 저장 폴더:", OUT_DIR)


if __name__ == "__main__":
    main()
