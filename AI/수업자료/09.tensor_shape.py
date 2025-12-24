# 05_tensor_properties_and_shape_ops.py
# -*- coding: utf-8 -*-
"""
05_tensor_properties_and_shape_ops.py
=====================================
Tensor 속성(size/shape/dtype/device) + shape 변형(view/reshape/unsqueeze/permute)

슬라이드 기반 핵심
------------------
- tensor.size() / tensor.shape : 모양(shape)
- tensor.dtype : 자료형
- tensor.device: 장치(CPU/GPU)

추가로 넣으면 좋은 실무 개념(추가)
---------------------------------
1) view vs reshape
   - view: "메모리 연속(contiguous)"일 때만 가능
   - reshape: 필요한 경우 내부적으로 복사하여 모양 변경 가능
2) squeeze/unsqueeze
   - 차원(축)을 추가/제거. 배치 차원 맞출 때 자주 사용
3) transpose / permute
   - 축 순서 변경 (예: 이미지 N,H,W,C ↔ N,C,H,W)
4) contiguous()
   - permute/transponse 이후에는 연속 메모리가 아닐 수 있어 view가 실패할 수 있음
   - contiguous()로 메모리 연속으로 만든 뒤 view 가능

실행
----
python 05_tensor_properties_and_shape_ops.py
"""
from __future__ import annotations

import torch


def info(name: str, t: torch.Tensor) -> None:
    print(f"[{name}] shape={tuple(t.shape)}, ndim={t.ndim}, dtype={t.dtype}, device={t.device}, contiguous={t.is_contiguous()}")


def view_vs_reshape_demo() -> None:
    x = torch.arange(0, 12)  # (12,)
    info("x", x)
    print("x:", x)

    # (3,4)로 모양 변경
    x_view = x.view(3, 4)
    x_reshape = x.reshape(3, 4)

    info("x_view", x_view)
    info("x_reshape", x_reshape)
    print("x_view:\n", x_view)
    print("x_reshape:\n", x_reshape)
    print()


def squeeze_unsqueeze_demo() -> None:
    # 배치차원 1개짜리 예시 (1, 3, 224, 224)
    x = torch.randn(1, 3, 4, 4)
    info("x", x)

    # squeeze: 크기가 1인 축 제거
    x_sq = x.squeeze(0)
    info("x_sq = x.squeeze(0)", x_sq)

    # unsqueeze: 특정 위치에 축 추가
    x_us = x_sq.unsqueeze(0)
    info("x_us = x_sq.unsqueeze(0)", x_us)
    print()


def permute_transpose_contiguous_demo() -> None:
    # (N, H, W, C) 형태의 이미지 배치를 가정
    x = torch.randn(2, 4, 5, 3)  # (batch=2, height=4, width=5, channel=3)
    info("x (NHWC)", x)

    # 딥러닝 모델은 보통 (N, C, H, W)를 선호
    x_nchw = x.permute(0, 3, 1, 2)
    info("x_nchw = x.permute(0,3,1,2)", x_nchw)

    # permute 후에는 메모리가 연속이 아닐 수 있음.
    # view를 쓰려면 contiguous()로 메모리 정렬 필요
    try:
        flat = x_nchw.view(2, -1)
        info("flat", flat)
    except RuntimeError as e:
        print("view failed after permute (expected):", e)

    x_nchw_contig = x_nchw.contiguous()
    info("x_nchw_contig", x_nchw_contig)

    flat2 = x_nchw_contig.view(2, -1)
    info("flat2 = x_nchw_contig.view(2,-1)", flat2)
    print()


def main() -> None:
    view_vs_reshape_demo()
    squeeze_unsqueeze_demo()
    permute_transpose_contiguous_demo()


if __name__ == "__main__":
    main()
