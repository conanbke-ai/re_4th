# Scikit-learn
# Python 머신러닝 라이브러리의 표준

# 특징
# 쉬운 API(fit, predict, transform)
# 다양한 알고리즘 제공
# 전처리, 평가 도구 포함
# 풍부한 문서와 예제
# 무료, 오픈소스


# 제공 기능
# 분류 (Classification)
# LogisticRegression, SVC, 등등

# 회귀 (Regression)
# LinearRegression, Ridge, 등등

# 군집화

# 차원 축소

# 전처리

# 모델 선택

# from sklearn.어디서든 import 모델

# # 1 모델 생성
# model = 모델(하이퍼파라미터)

# # 2. 학습
# model.fit(x_train, y_train)

# # 3. 예측
# predictions = model.predict(x_test)

# # 4. 평가
# score = model.score(x_test, y_test)

from sklearn.datasets import load_iris

iris = load_iris()
print(f"특성:", iris.feature_names)

print(f'타겟:', iris.target_names)

x = iris.data
y = iris.target

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

print(f'훈련: {x_train.shape} 테스트: {x_test.shape}')

from sklearn.neighbors import KNeighborsClassifier

# 1. 모델 생성 (k)
model = KNeighborsClassifier(n_neighbors=3)

# 2. 학습
model.fit(x_train, y_train)

# 3. 예측
y_pred = model.predict(x_test)
print('예측 결과: ',y_pred[:10])
print('실제 결과: ',y_test[:10])

# 모델 평가
from sklearn.metrics import accuracy_score, classification_report

# 정확도
accuracy = accuracy_score(y_test, y_pred)
print(f'정확도: {accuracy:.2%}')

# 간단히
print(f'정확도: {model.score(x_test, y_test):.2%}')

# 상세 리포트
print(classification_report(
    y_test, y_pred, 
    target_names=iris.target_names
    ))

from sklearn.linear_model import LogisticRegression

# model = LogisticRegression(max_iter=200)
# model.fit(x_train, y_train)
# print(f'로지스틱 회귀 정확도: {model.score(x_test, y_test):.2%}')


from sklearn.tree import DecisionTreeClassifier

# model = DecisionTreeClassifier()
# model.fit(x_train, y_train)
# print(f'결정 트리 정확도: {model.score(x_test, y_test):.2%}')


from sklearn.ensemble import RandomForestClassifier

# model = RandomForestClassifier()
# model.fit(x_train, y_train)
# print(f'랜덤 포레스트 정확도: {model.score(x_test, y_test):.2%}') 

models = {
    'Logistic':LogisticRegression(max_iter=200),
    'Dec':DecisionTreeClassifier(),
    "Random":RandomForestClassifier(),
}

for name, model in models.items():
    model.fit(x_train, y_train)
    print(f'{name} 정확도: {model.score(x_test, y_test):.2%}') 

# 데이터 전처리
# 스케일링의 중요성
# 특성별 스케일이 다르면 문제!!
print('원본 데이터 범위:')
print(f'특성1: {x[:,0].min():.1f} ~ {x[:,0].max():.1f}')
print(f'특성2: {x[:,1].min():.1f} ~ {x[:,1].max():.1f}')
# 범위가 다르면 일부 특성이 과도한 영향

from sklearn.preprocessing import StandardScaler

# 스케일러 생성 및 학습
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test) # fit은 하지 않음!

print('스케일링 후')
print(f'평균: {x_train_scaled.mean(axis=0)}')
print(f'표준편차: {x_train_scaled.std(axis=0)}')


from sklearn.svm import SVC
# 스케일링 없이

model = SVC()
model.fit(x_train, y_train)
print(f'스케일링 전: {model.score(x_test, y_test):.2%}') 


# 스케일링 후
model = SVC()
model.fit(x_train_scaled, y_train)
print(f'스케일링 후: {model.score(x_test_scaled, y_test):.2%}')

# 핵심 정리
# 1. Scikit-learn 기본 워크플로우:
#    - 모델 생성: model = Model(hyperparameters)
#    - 학습: model.fit(X_train, y_train)
#    - 예측: predictions = model.predict(X_test)
#    - 평가: score = model.score(X_test, y_test)
#
# 2. 제공되는 주요 기능:
#    - 분류: LogisticRegression, KNN, SVC, DecisionTree, RandomForest 등
#    - 회귀: LinearRegression, Ridge, Lasso 등
#    - 군집화: KMeans, DBSCAN 등
#    - 전처리: StandardScaler, MinMaxScaler 등
#    - 모델 선택: train_test_split, cross_validation 등
#
# 3. 데이터 전처리의 중요성:
#    - 특성 간 스케일이 다르면 모델 성능 저하
#    - StandardScaler: 평균 0, 표준편차 1로 정규화
#    - fit_transform(): 훈련 데이터에 적용
#    - transform(): 테스트 데이터에 적용 (fit 제외!)
#
# 4. 모델 비교:
#    - 여러 모델을 학습시켜 성능 비교
#    - 데이터 특성에 따라 최적 모델이 다름
#    - 항상 테스트 데이터로 평가
#
# 5. 평가 지표:
#    - accuracy_score: 전체 정확도
#    - classification_report: 클래스별 상세 성능
#    - precision, recall, f1-score 등 확인 가능


# ============================================================
# 와인 데이터셋으로 분류 모델 만들기 (실습 과제 1~4)
# ============================================================

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix
from sklearn.base import clone

# 비교할 모델들(3개 이상)
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier


# ----------------------------
# 0) 데이터 로드
# ----------------------------
wine = load_wine()
x, y = wine.data, wine.target


# ----------------------------
# 1) 훈련/테스트 분할 (70:30)
#    - stratify=y : 클래스 비율을 최대한 유지
# ----------------------------
x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.30,
    stratify=y,
    random_state=42
)

print("전체:", len(y), "훈련:", len(y_train), "테스트:", len(y_test))


# ----------------------------
# 2) 3가지 이상 모델 준비
# ----------------------------
models = [
    ("LogReg", LogisticRegression(max_iter=10000, random_state=42)),
    ("KNN", KNeighborsClassifier(n_neighbors=5)),
    ("SVM(RBF)", SVC(kernel="rbf", C=1.0, gamma="scale", random_state=42)),
    ("RandomForest", RandomForestClassifier(n_estimators=300, random_state=42)),
]


# ----------------------------
# 3) 스케일링 전/후 성능 비교 함수
#    - 스케일링 '후'는 Pipeline으로 처리하여
#      scaler가 train에만 fit 되도록(데이터 누수 방지)
# ----------------------------
def evaluate(estimator, x_tr, y_tr, x_te, y_te):
    """모델 학습/예측 후 accuracy, f1_macro 반환"""
    estimator.fit(x_tr, y_tr)
    pred = estimator.predict(x_te)
    acc = accuracy_score(y_te, pred)
    f1  = f1_score(y_te, pred, average="macro")
    return acc, f1

results = []

for name, model in models:
    # (A) 스케일링 전(원본 데이터)
    raw_model = clone(model)
    acc_raw, f1_raw = evaluate(raw_model, x_train, y_train, x_test, y_test)

    # (B) 스케일링 후(StandardScaler + 모델)
    scaled_model = Pipeline([
        ("scaler", StandardScaler()),
        ("model", clone(model))
    ])
    acc_scaled, f1_scaled = evaluate(scaled_model, X_train, y_train, X_test, y_test)

    results.append({
        "model": name,
        "acc_raw": acc_raw,
        "f1_raw": f1_raw,
        "acc_scaled": acc_scaled,
        "f1_scaled": f1_scaled
    })

# 결과 출력(정렬: 스케일링 후 정확도 -> f1_macro)
results_sorted = sorted(results, key=lambda d: (d["acc_scaled"], d["f1_scaled"]), reverse=True)

print("\n=== 모델 성능 비교 (스케일링 전/후) ===")
for r in results_sorted:
    print(f"- {r['model']:12s} | "
          f"RAW acc={r['acc_raw']:.4f}, f1={r['f1_raw']:.4f} || "
          f"SCALED acc={r['acc_scaled']:.4f}, f1={r['f1_scaled']:.4f}")


# ----------------------------
# 4) 가장 좋은 모델 선택 (스케일링 후 기준)
#    - 보통 KNN/SVM/LogReg는 스케일링 후가 유리
# ----------------------------
best_name = results_sorted[0]["model"]
print(f"\n>>> 선택된 Best Model(스케일링 후 기준): {best_name}")

# best 모델 재구성 및 상세 평가 출력
best_base_model = dict(models)[best_name]  # 이름으로 원본 모델 가져오기
best_model = Pipeline([
    ("scaler", StandardScaler()),
    ("model", clone(best_base_model))
])

best_model.fit(x_train, y_train)
best_pred = best_model.predict(x_test)

print("\n=== Best Model 상세 리포트 ===")
print("Accuracy:", accuracy_score(y_test, best_pred))
print("F1(macro):", f1_score(y_test, best_pred, average="macro"))
print("\n[Classification Report]")
print(classification_report(y_test, best_pred, target_names=wine.target_names))

print("[Confusion Matrix]")
print(confusion_matrix(y_test, best_pred))

# 전체: 178 훈련: 124 테스트: 54

# === 모델 성능 비교 (스케일링 전/후) ===
# - RandomForest | RAW acc=1.0000, f1=1.0000 || SCALED acc=1.0000, f1=1.0000
# - LogReg       | RAW acc=0.9630, f1=0.9610 || SCALED acc=0.9815, f1=0.9829
# - SVM(RBF)     | RAW acc=0.6667, f1=0.5271 || SCALED acc=0.9815, f1=0.9808
# - KNN          | RAW acc=0.7222, f1=0.7174 || SCALED acc=0.9444, f1=0.9441

# >>> 선택된 Best Model(스케일링 후 기준): RandomForest

# === Best Model 상세 리포트 ===
# Accuracy: 1.0
# F1(macro): 1.0

# [Classification Report]
#               precision    recall  f1-score   support

#      class_0       1.00      1.00      1.00        18
#      class_1       1.00      1.00      1.00        21
#      class_2       1.00      1.00      1.00        15

#     accuracy                           1.00        54
#    macro avg       1.00      1.00      1.00        54
# weighted avg       1.00      1.00      1.00        54

# [Confusion Matrix]
# [[18  0  0]
#  [ 0 21  0]
#  [ 0  0 15]]