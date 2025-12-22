# -*- coding: utf-8 -*-
"""
07_딥러닝모델개요.py
====================
(원본 PDF: 07_딥러닝모델개요.pdf 기반 정리 + 예제 보강)

딥러닝 모델의 주요 특징(수업 슬라이드 요지)
-------------------------------------------
1) 계층적 구조: 여러 은닉층을 통해 복잡한 패턴/추상 특징을 학습
2) 역전파 알고리즘: 오차를 역으로 전파하여 가중치/편향 업데이트
3) 대량의 데이터와 연산: 학습에 많은 데이터/연산 자원이 필요
4) 종단간(end-to-end) 학습: 입력-출력만으로 학습 가능(특징 추출을 모델이 함께 수행)

대표 모델 패밀리
----------------
- FNN(MLP): 가장 기본적인 feedforward 네트워크(회귀/분류 모두 가능)
- CNN: 합성곱/풀링으로 특징 추출(이미지/시계열에서 강함)
- RNN/LSTM/GRU: 순차 데이터 처리(언어/시계열), 장기 의존성 문제로 LSTM/GRU 등장
- Transformer: Self-Attention 기반, 병렬 처리 효율, 2017 "Attention is All You Need"로 대중화

이 파일의 목표
--------------
각 모델의 '핵심 연산'을 아주 작은 NumPy 예제로 직접 구현해보며 직관을 잡는 것입니다.
(실무에서는 PyTorch/TensorFlow 같은 프레임워크를 사용합니다.)

실행:
    python 07_딥러닝모델개요.py
"""

from __future__ import annotations

import numpy as np


# ---------------------------------------------------------------------
# 1) FNN(MLP): Dense + Activation
# ---------------------------------------------------------------------
def dense(x: np.ndarray, W: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    [Dense / Fully-Connected Layer]
    --------------------------------
    가장 기본적인 신경망 층입니다.
    입력 feature들을 선형변환(가중합)한 뒤 bias를 더합니다.

    수식:
        y = xW + b

    shape 규약:
        x: (n, in_dim)
        W: (in_dim, out_dim)
        b: (out_dim,)

    반환:
        y: (n, out_dim)
    """
    return x @ W + b


def relu(x: np.ndarray) -> np.ndarray:
    """
    [ReLU 활성화 함수]
    -------------------
    ReLU(x) = max(0, x)

    - 음수는 0으로, 양수는 그대로 통과
    - 비선형성 부여
    - 계산이 단순하고, sigmoid/tanh보다 기울기 소실 문제가 덜함
    """
    return np.maximum(0.0, x)


def mlp_forward(x: np.ndarray, W1: np.ndarray, b1: np.ndarray, W2: np.ndarray, b2: np.ndarray) -> np.ndarray:
    """
    [2-layer MLP 순전파 예시]
    - hidden = relu(xW1 + b1)
    - out    = hiddenW2 + b2
    """
    h = relu(dense(x, W1, b1))
    out = dense(h, W2, b2)
    return out


# ---------------------------------------------------------------------
# 2) CNN: Convolution + Pooling (1D로 단순화)
# ---------------------------------------------------------------------
def conv1d_valid(x: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """
    [1D Convolution (valid)]
    - padding 없이 계산
    - 입력 길이 n, 커널 길이 k -> 출력 길이 n-k+1

    주의:
    - 딥러닝 프레임워크의 Conv1d는 보통 커널을 뒤집지 않는 cross-correlation 방식입니다.
    - 이 구현도 커널을 뒤집지 않으므로 PyTorch Conv1d와 방향이 같습니다.
    """
    n = len(x)
    k = len(kernel)
    out = []
    for i in range(n - k + 1):
        out.append(np.sum(x[i : i + k] * kernel))
    return np.array(out, dtype=float)


def conv1d_same(x: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """
    [연습문제 1 해설/정답: conv1d padding='same' 흉내]
    ---------------------------------------------------
    목표:
    - 출력 길이를 입력 길이와 같게 만드는(same) 1D convolution을 구현합니다.

    핵심 아이디어:
    - valid convolution은 길이가 줄어듭니다. (n-k+1)
    - 따라서 입력 x 양쪽에 padding을 추가해서, valid를 하더라도 출력이 n이 되도록 맞춥니다.

    padding 규칙(일반적):
    - total pad = k - 1
    - left pad  = floor((k-1)/2)
    - right pad = (k-1) - left pad
      (커널 길이가 짝수일 때 좌/우 패딩이 비대칭이 될 수 있습니다.)

    이 구현은 딥러닝 프레임워크의 'SAME' 방식과 유사한 패딩을 사용합니다.

    반환:
        y: (len(x),)
    """
    n = len(x)
    k = len(kernel)
    pad_total = k - 1
    pad_left = pad_total // 2
    pad_right = pad_total - pad_left

    # np.pad로 양쪽 0-padding
    x_pad = np.pad(x, (pad_left, pad_right), mode="constant", constant_values=0.0)

    # 이제 valid를 수행하면 길이가 n이 됩니다:
    # len(x_pad) - k + 1 = (n + pad_left + pad_right) - k + 1 = n
    out = []
    for i in range(n):
        out.append(np.sum(x_pad[i : i + k] * kernel))
    return np.array(out, dtype=float)


def maxpool1d(x: np.ndarray, pool: int = 2) -> np.ndarray:
    """
    [1D Max Pooling]
    - 구간(pool)마다 최대값만 취해 다운샘플링
    - 계산량 감소, 노이즈에 어느 정도 강해짐
    """
    out = []
    for i in range(0, len(x), pool):
        out.append(np.max(x[i : i + pool]))
    return np.array(out, dtype=float)


# ---------------------------------------------------------------------
# 3) RNN: 순차 데이터 처리(단일 step)
# ---------------------------------------------------------------------
def rnn_step(x_t: np.ndarray, h_prev: np.ndarray, Wx: np.ndarray, Wh: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    단일 time-step RNN (tanh)
    수식:
        h_t = tanh(x_t @ Wx + h_prev @ Wh + b)
    """
    return np.tanh(x_t @ Wx + h_prev @ Wh + b)


# ---------------------------------------------------------------------
# 4) Transformer: Self-Attention (Scaled Dot-Product)
# ---------------------------------------------------------------------
def softmax(z: np.ndarray, axis: int = 1) -> np.ndarray:
    """
    softmax 안정화:
    - exp overflow 방지 위해 최대값을 빼고 exp 계산
    """
    z = z - np.max(z, axis=axis, keepdims=True)
    exp_z = np.exp(z)
    return exp_z / np.sum(exp_z, axis=axis, keepdims=True)


def scaled_dot_product_attention(Q: np.ndarray, K: np.ndarray, V: np.ndarray) -> np.ndarray:
    """
    Attention(Q, K, V) = softmax(QK^T / sqrt(d)) V
    """
    d = Q.shape[1]
    scores = (Q @ K.T) / np.sqrt(d)
    weights = softmax(scores, axis=1)
    return weights @ V


# =====================================================================
# 5) PyTorch 방식(실무형) 추가
# =====================================================================
"""
PyTorch 파트는 "실무에서 실제 구현되는 형태"를 보여주기 위한 블록입니다.

중요한 shape 규약:
- MLP: (batch, features)
- Conv1d: (batch, channels, length)
- RNN: 기본 (seq_len, batch, features)  (batch_first=True면 (batch, seq_len, features))
- MultiheadAttention: 기본 (seq_len, batch, embed_dim)

또한,
- PyTorch nn.Conv1d는 보통 convolution(커널 뒤집기)이 아니라 cross-correlation(커널 그대로)입니다.
"""

try:
    import torch
    import torch.nn as nn
    import torch.nn.functional as F
    TORCH_AVAILABLE = True
except Exception:
    TORCH_AVAILABLE = False


class TorchMLP(nn.Module):
    """
    [2-layer MLP: Linear -> ReLU -> Linear]
    NumPy의 mlp_forward 구조와 동일합니다.
    """
    def __init__(self, in_dim: int, hidden_dim: int, out_dim: int):
        super().__init__()
        self.fc1 = nn.Linear(in_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, out_dim)

    def forward(self, x: "torch.Tensor") -> "torch.Tensor":
        x = self.fc1(x)        # (batch, hidden_dim)
        x = F.relu(x)          # (batch, hidden_dim)
        x = self.fc2(x)        # (batch, out_dim)
        return x


def torch_conv1d_valid(signal_1d: "torch.Tensor", kernel_1d: "torch.Tensor") -> "torch.Tensor":
    """
    [PyTorch Conv1d로 valid convolution 재현]

    입력:
        signal_1d: (L,)
        kernel_1d: (K,)

    Conv1d 요구 shape:
        input : (batch, channels, length)
        weight: (out_channels, in_channels, kernel_size)

    여기서는 단일 채널/단일 필터:
        batch=1, channels=1, out_channels=1
    """
    assert signal_1d.dim() == 1
    assert kernel_1d.dim() == 1

    x = signal_1d.view(1, 1, -1)  # (1,1,L)
    k = kernel_1d.view(1, 1, -1)  # (1,1,K)

    conv = nn.Conv1d(in_channels=1, out_channels=1, kernel_size=k.shape[-1], bias=False)

    # 학습이 아니라 "동일 연산 재현" 목적이므로 weight를 고정으로 넣습니다.
    with torch.no_grad():
        conv.weight.copy_(k)

    y = conv(x)      # (1,1,L-K+1)
    return y.view(-1)


def torch_conv1d_same(signal_1d: "torch.Tensor", kernel_1d: "torch.Tensor") -> "torch.Tensor":
    """
    [연습문제 1 대응: PyTorch로 padding='same' 흉내]

    Conv1d의 padding 파라미터는 대칭 패딩만 간편하게 처리합니다.
    커널 길이가 짝수일 때 "SAME"처럼 비대칭이 될 수 있어,
    여기서는 F.pad로 직접 좌/우 패딩을 넣는 방식을 사용합니다.

    규칙:
        pad_total = K - 1
        pad_left  = floor((K-1)/2)
        pad_right = (K-1) - pad_left

    반환:
        y: (L,)
    """
    assert signal_1d.dim() == 1
    assert kernel_1d.dim() == 1

    L = signal_1d.shape[0]
    K = kernel_1d.shape[0]

    pad_total = K - 1
    pad_left = pad_total // 2
    pad_right = pad_total - pad_left

    x = signal_1d.view(1, 1, -1)  # (1,1,L)
    x = F.pad(x, (pad_left, pad_right))  # 마지막 차원(length)에 좌/우 패딩

    # weight shape 맞추기
    k = kernel_1d.view(1, 1, -1)  # (1,1,K)
    conv = nn.Conv1d(in_channels=1, out_channels=1, kernel_size=K, bias=False)

    with torch.no_grad():
        conv.weight.copy_(k)

    y = conv(x)  # (1,1,L)
    return y.view(-1)


def torch_maxpool1d(x_1d: "torch.Tensor", pool: int = 2) -> "torch.Tensor":
    """
    [PyTorch max_pool1d]
    NumPy maxpool1d와 동일 개념.
    """
    x = x_1d.view(1, 1, -1)
    y = F.max_pool1d(x, kernel_size=pool, stride=pool)
    return y.view(-1)


def torch_rnn_demo(seq_len: int = 5, batch: int = 1, in_dim: int = 4, hidden_dim: int = 6):
    """
    [PyTorch nn.RNN 사용 예제]

    입력 shape(기본):
        (seq_len, batch, in_dim)

    출력:
        output: (seq_len, batch, hidden_dim)  # 각 시점의 hidden state
        h_n   : (num_layers, batch, hidden_dim)  # 마지막 hidden state
    """
    rnn = nn.RNN(input_size=in_dim, hidden_size=hidden_dim, nonlinearity="tanh", batch_first=False)
    X = torch.randn(seq_len, batch, in_dim)
    output, h_n = rnn(X)
    return output, h_n


def torch_scaled_dot_product_attention_manual(Q: "torch.Tensor", K: "torch.Tensor", V: "torch.Tensor"):
    """
    [Scaled Dot-Product Attention: manual 구현 + weights 반환]

    Q,K,V: (seq_len, d)
    scores: (seq_len, seq_len)
    weights: (seq_len, seq_len)  # 각 query별 확률분포(행 합 = 1)
    out: (seq_len, d)
    """
    d = Q.shape[-1]
    scores = (Q @ K.T) / (d ** 0.5)
    weights = torch.softmax(scores, dim=-1)
    out = weights @ V
    return out, weights


def _set_mha_identity_projections(mha: "nn.MultiheadAttention") -> None:
    """
    [MultiheadAttention을 'manual attention'과 동일하게 맞추기 위한 설정]
    --------------------------------------------------------------------
    nn.MultiheadAttention은 원래 다음을 수행합니다:
        Q = XWq, K = XWk, V = XWv   (학습되는 선형 투영)
        attention(Q,K,V)

    그런데 "개념 데모"에서는 Q=K=V=X 자체로 attention을 보고 싶습니다.
    따라서 아래처럼 투영을 항등행렬(identity)로 세팅하면,
        Wq=Wk=Wv=I, out_proj=I
    가 되어 manual 구현과 거의 동일한 동작을 합니다.

    주의:
    - 이 설정은 "학습"이 아니라 "개념 비교"를 위한 것입니다.
    """
    E = mha.embed_dim

    with torch.no_grad():
        # 많은 버전에서 in_proj_weight, in_proj_bias를 사용합니다.
        if hasattr(mha, "in_proj_weight") and mha.in_proj_weight is not None:
            # in_proj_weight: (3E, E)  = [Wq; Wk; Wv]
            W = torch.zeros((3 * E, E), dtype=mha.in_proj_weight.dtype, device=mha.in_proj_weight.device)
            I = torch.eye(E, dtype=mha.in_proj_weight.dtype, device=mha.in_proj_weight.device)
            W[0:E, :] = I         # Wq = I
            W[E:2*E, :] = I       # Wk = I
            W[2*E:3*E, :] = I     # Wv = I
            mha.in_proj_weight.copy_(W)

            if mha.in_proj_bias is not None:
                mha.in_proj_bias.zero_()

        # out projection도 identity로
        mha.out_proj.weight.copy_(torch.eye(E, dtype=mha.out_proj.weight.dtype, device=mha.out_proj.weight.device))
        if mha.out_proj.bias is not None:
            mha.out_proj.bias.zero_()


def torch_multihead_attention_demo(seq_len: int = 4, embed_dim: int = 8):
    """
    [nn.MultiheadAttention(1 head) 데모 + weights 출력]
    ---------------------------------------------------
    - num_heads=1로 두면 scaled dot-product attention의 기본 형태와 거의 같아집니다.
    - 추가로, 투영을 identity로 세팅하면 manual attention(Q=K=V=X)과 비교가 쉬워집니다.

    입력 규약:
        X: (seq_len, batch, embed_dim)
    """
    mha = nn.MultiheadAttention(embed_dim=embed_dim, num_heads=1, batch_first=False, dropout=0.0)
    _set_mha_identity_projections(mha)

    X = torch.randn(seq_len, 1, embed_dim)  # batch=1

    # need_weights=True로 가중치(attn weights)도 받습니다.
    # PyTorch 버전에 따라 average_attn_weights 인자가 있을 수 있어 try로 안전 처리합니다.
    try:
        out, weights = mha(X, X, X, need_weights=True, average_attn_weights=False)
        # average_attn_weights=False인 경우:
        # weights: (batch, num_heads, tgt_len, src_len)
        weights_2d = weights[0, 0]  # (tgt_len, src_len)
    except TypeError:
        out, weights = mha(X, X, X, need_weights=True)
        # 기본(average=True)인 경우:
        # weights: (batch, tgt_len, src_len)
        weights_2d = weights[0]  # (tgt_len, src_len)

    return X, out, weights_2d


def torch_tiny_training_loop_demo() -> None:
    """
    [아주 짧은 학습 루프 데모]
    -------------------------
    목표:
    - "forward만"이 아니라, 실제로 loss를 정의하고 backward로 gradient를 구해
      optimizer.step()으로 파라미터가 업데이트되는 과정을 최소 코드로 보여줍니다.

    문제 설정(간단한 회귀):
    - 입력 X (N, 3)
    - 정답 y = X @ trueW + trueb + noise  (N, 2)
    - MLP가 y를 맞추도록 MSELoss로 학습

    학습 루프의 정석:
    1) model.train()
    2) pred = model(X)
    3) loss = criterion(pred, y)
    4) optimizer.zero_grad()
    5) loss.backward()
    6) optimizer.step()
    """
    # CPU로도 충분히 동작하는 작은 데모입니다.
    device = torch.device("cpu")

    torch.manual_seed(0)

    N = 256
    in_dim = 3
    out_dim = 2

    # (1) synthetic data 생성
    X = torch.randn(N, in_dim, device=device)

    trueW = torch.tensor([[2.0, -1.0],
                          [0.5,  1.5],
                          [-1.0, 0.3]], device=device)   # (3,2)
    trueb = torch.tensor([0.2, -0.1], device=device)     # (2,)

    y = X @ trueW + trueb + 0.05 * torch.randn(N, out_dim, device=device)

    # (2) 모델/손실/옵티마이저
    model = TorchMLP(in_dim=in_dim, hidden_dim=8, out_dim=out_dim).to(device)
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.05)

    # (3) 학습
    model.train()
    for step in range(1, 201):
        pred = model(X)
        loss = criterion(pred, y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if step % 50 == 0 or step == 1:
            print(f"[train] step={step:03d} | loss={loss.item():.6f}")

    # (4) 평가(여기서는 동일 데이터로 간단히 확인)
    model.eval()
    with torch.no_grad():
        pred = model(X)
        loss_eval = criterion(pred, y).item()
    print(f"[eval] loss={loss_eval:.6f}")


def main_torch_optional() -> None:
    """
    PyTorch가 설치된 환경에서만 실행되는 데모 모음.
    - 설치가 안 되어 있으면 안내만 출력.
    """
    if not TORCH_AVAILABLE:
        print("\n== PyTorch demo ==")
        print("PyTorch가 설치되어 있지 않아 PyTorch 파트를 생략합니다.")
        print("설치(예): pip install torch")
        print("※ CUDA/OS/버전에 따라 설치 방법이 다를 수 있으니 공식 설치 가이드를 권장합니다.")
        return

    print("\n== PyTorch demo: MLP ==")
    x = torch.randn(5, 3)
    mlp = TorchMLP(in_dim=3, hidden_dim=8, out_dim=2)
    out = mlp(x)
    print("입력 shape:", tuple(x.shape))
    print("출력 shape:", tuple(out.shape))

    print("\n== PyTorch demo: Conv1d(valid) + Conv1d(same) + MaxPool1d ==")
    signal = torch.tensor([1, 2, 3, 2, 0, 1, 2], dtype=torch.float32)
    kernel = torch.tensor([1, 0, -1], dtype=torch.float32)

    conv_valid = torch_conv1d_valid(signal, kernel)
    conv_same = torch_conv1d_same(signal, kernel)
    pool_out = torch_maxpool1d(conv_valid, pool=2)

    print("signal:", signal)
    print("kernel:", kernel)
    print("conv(valid):", conv_valid, " | shape:", tuple(conv_valid.shape))
    print("conv(same) :", conv_same,  " | shape:", tuple(conv_same.shape))
    print("pool(valid):", pool_out,   " | shape:", tuple(pool_out.shape))

    print("\n== PyTorch demo: RNN multi-step ==")
    output, h_n = torch_rnn_demo(seq_len=5, batch=1, in_dim=4, hidden_dim=6)
    print("output shape (all steps):", tuple(output.shape))
    print("h_n shape (last hidden):", tuple(h_n.shape))

    print("\n== PyTorch demo: Self-Attention (manual, weights 포함) ==")
    seq_len, d = 4, 8
    X = torch.randn(seq_len, d)
    out_manual, weights_manual = torch_scaled_dot_product_attention_manual(X, X, X)
    print("manual attention output shape:", tuple(out_manual.shape))
    print("manual weights shape:", tuple(weights_manual.shape))
    print("manual weights row-sum:", weights_manual.sum(dim=-1))

    print("\n== PyTorch demo: nn.MultiheadAttention (1 head, weights 포함) ==")
    X_mha, out_mha, weights_mha = torch_multihead_attention_demo(seq_len=4, embed_dim=8)
    print("MHA input shape:", tuple(X_mha.shape))      # (L,1,E)
    print("MHA output shape:", tuple(out_mha.shape))   # (L,1,E)
    print("MHA weights shape:", tuple(weights_mha.shape))  # (L,S)
    print("MHA weights row-sum:", weights_mha.sum(dim=-1))

    print("\n[참고] 위 MHA 데모는 투영을 identity로 세팅했기 때문에 manual attention과 형태가 유사해집니다.")
    print("       실제 학습에서는 Wq/Wk/Wv/out_proj가 학습되며, 그게 Transformer의 표현력을 키웁니다.")

    print("\n== PyTorch demo: Tiny Training Loop (loss 감소 확인) ==")
    torch_tiny_training_loop_demo()


def main() -> None:
    rng = np.random.default_rng(0)

    print("== FNN(MLP) forward demo ==")
    x = rng.normal(0, 1, size=(5, 3))
    W1 = rng.normal(0, 0.5, size=(3, 8))
    b1 = np.zeros(8)
    W2 = rng.normal(0, 0.5, size=(8, 2))
    b2 = np.zeros(2)
    out = mlp_forward(x, W1, b1, W2, b2)
    print("MLP output shape:", out.shape)

    print("\n== CNN(1D conv + pool) demo ==")
    signal = np.array([1, 2, 3, 2, 0, 1, 2], dtype=float)
    kernel = np.array([1, 0, -1], dtype=float)

    conv_out = conv1d_valid(signal, kernel)
    conv_same_out = conv1d_same(signal, kernel)  # (추가) same padding 버전
    pool_out = maxpool1d(conv_out, pool=2)

    print("conv(valid) output:", conv_out, " | len:", len(conv_out))
    print("conv(same)  output:", conv_same_out, " | len:", len(conv_same_out))
    print("pool output:", pool_out)

    print("\n== RNN step demo ==")
    x_t = rng.normal(0, 1, size=(1, 4))
    h_prev = np.zeros((1, 6))
    Wx = rng.normal(0, 0.2, size=(4, 6))
    Wh = rng.normal(0, 0.2, size=(6, 6))
    b = np.zeros((1, 6))
    h_t = rnn_step(x_t, h_prev, Wx, Wh, b)
    print("h_t shape:", h_t.shape)

    print("\n== Transformer Attention demo ==")
    seq_len, d = 4, 8
    Q = rng.normal(0, 1, size=(seq_len, d))
    K = rng.normal(0, 1, size=(seq_len, d))
    V = rng.normal(0, 1, size=(seq_len, d))
    attn = scaled_dot_product_attention(Q, K, V)
    print("attention output shape:", attn.shape)

    print("\n[연습문제]")
    print("1) conv1d에 padding='same'을 흉내내는 버전을 구현해보세요.  -> (정답: conv1d_same)")
    print("2) RNN을 여러 step 반복해 간단한 시퀀스 입력을 처리해보세요. -> (PyTorch demo에 multi-step 예시 포함)")
    print("3) attention에서 Q,K,V를 동일하게 두는 self-attention을 구성하고, weights를 출력해 해석해보세요.")
    print("   -> (PyTorch demo에 manual weights + MultiheadAttention weights 출력 포함)")

    # (추가) PyTorch 데모 실행
    main_torch_optional()


if __name__ == "__main__":
    main()
