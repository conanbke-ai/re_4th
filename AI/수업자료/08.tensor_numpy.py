# 04_tensor_numpy_interop.py
# -*- coding: utf-8 -*-
"""
04_tensor_numpy_interop.py
==========================
PyTorch Tensor ↔ NumPy ndarray 변환 + "메모리 공유" 주의사항

슬라이드 기반 핵심
------------------
- torch.from_numpy(ndarray): NumPy 배열로부터 Tensor 생성
- tensor.numpy(): Tensor를 NumPy 배열로 변환
- Tensor와 NumPy 배열은 메모리를 공유할 수 있음(복사 없이 같은 메모리 참조)

메모리 공유가 의미하는 것
------------------------
- 공유 상태에서는 한쪽을 수정하면 다른 쪽도 같이 바뀔 수 있음
- "성능"에는 이점이 있지만, 의도치 않은 side-effect가 생길 수 있음

추가로 알아두면 좋은 개념(추가)
------------------------------
1) gradient를 갖는 텐서 -> numpy 변환
   - requires_grad=True인 텐서는 바로 numpy()가 안 될 수 있음
   - 보통 detach().cpu().numpy() 순서로 변환
2) GPU 텐서 -> numpy 변환
   - GPU 텐서는 numpy() 불가(NumPy는 CPU 메모리 기반)
   - cpu()로 옮긴 뒤 numpy()를 호출해야 함

실행
----
python 04_tensor_numpy_interop.py
"""
from __future__ import annotations

import numpy as np
import torch


def show(title: str, x) -> None:
    print(f"== {title} ==")
    print(x)
    print("type:", type(x))
    print()


def sharing_demo() -> None:
    """
    torch.from_numpy / tensor.numpy()로 공유되는 메모리 확인
    """
    np_arr = np.array([1, 2, 3], dtype=np.float32)
    t = torch.from_numpy(np_arr)  # (대부분) 메모리 공유
    show("np_arr (before)", np_arr)
    show("t (before)", t)

    # NumPy 배열 수정 -> Tensor도 같이 바뀜
    np_arr[0] = 999
    show("np_arr (after change)", np_arr)
    show("t (after numpy change)", t)

    # Tensor 수정 -> NumPy도 같이 바뀜
    t[1] = -5
    show("t (after tensor change)", t)
    show("np_arr (after tensor change)", np_arr)


def safe_copy_demo() -> None:
    """
    공유가 싫다면 copy를 만들어서 안전하게 분리합니다.
    """
    np_arr = np.array([1, 2, 3], dtype=np.float32)
    t_shared = torch.from_numpy(np_arr)           # 공유
    t_copied = torch.tensor(np_arr, copy=True)    # 복사(파이토치 2.x에서 copy 인자 지원)

    # t_shared 변경 => np_arr 변경
    t_shared[0] = 111

    # t_copied 변경 => np_arr 영향 없음
    t_copied[1] = 222

    show("np_arr", np_arr)
    show("t_shared", t_shared)
    show("t_copied", t_copied)


def grad_and_numpy_demo() -> None:
    """
    requires_grad 텐서를 numpy로 바꿀 때의 안전한 패턴.
    """
    x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
    y = (x * x).sum()
    y.backward()

    # x.numpy()는 autograd와 충돌 가능성이 있어 에러가 날 수 있음.
    # 정석: detach()로 그래프에서 분리 후 numpy 변환
    x_np = x.detach().numpy()

    show("x (tensor)", x)
    show("x.grad", x.grad)
    show("x.detach().numpy()", x_np)


def gpu_to_numpy_demo() -> None:
    """
    GPU 텐서를 numpy로 바꾸는 정석.
    - GPU 텐서는 바로 numpy로 불가
    - cpu()로 옮긴 뒤 numpy()
    """
    if not torch.cuda.is_available():
        print("CUDA not available -> skip gpu_to_numpy_demo()")
        print()
        return

    x = torch.randn(2, 3, device="cuda")
    # x.numpy()는 불가 -> cpu로 이동
    x_np = x.detach().cpu().numpy()
    show("x (cuda tensor)", x)
    show("x.detach().cpu().numpy()", x_np)


def main() -> None:
    sharing_demo()
    safe_copy_demo()
    grad_and_numpy_demo()
    gpu_to_numpy_demo()


if __name__ == "__main__":
    main()
