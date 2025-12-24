# 06_indexing_broadcasting.py
# -*- coding: utf-8 -*-
"""
06_indexing_broadcasting.py
===========================
Tensor 인덱싱/슬라이싱 + 브로드캐스팅(broadcasting) 기초

슬라이드에는 "각종 연산"으로 묶일 수 있는 영역이지만,
실무/과제에서 난이도가 올라가는 포인트가 바로 여기입니다(추가 개념).

추가 개념(핵심)
---------------
1) 기본 인덱싱: t[i], t[i, j], t[:, :, k]
2) 슬라이싱: t[start:stop:step]
3) boolean mask: 조건에 맞는 원소만 선택/수정
4) fancy indexing: 인덱스 텐서로 선택
5) broadcasting: shape이 다른 텐서끼리 연산할 때 자동 확장되는 규칙
   - trailing dimension부터 비교
   - 같거나(=), 한쪽이 1이면 확장 가능
   - 그 외는 에러

실행
----
python 06_indexing_broadcasting.py
"""
from __future__ import annotations

import torch


def basic_indexing() -> None:
    x = torch.arange(0, 12).reshape(3, 4)
    print("== basic_indexing ==")
    print("x:\n", x)

    # 단일 원소
    print("x[0, 0]:", x[0, 0])

    # 행/열 슬라이싱
    print("x[1]:", x[1])          # 두 번째 행
    print("x[:, 2]:", x[:, 2])    # 세 번째 열

    # 부분 행렬
    print("x[0:2, 1:3]:\n", x[0:2, 1:3])
    print()


def boolean_masking() -> None:
    x = torch.randn(3, 4)
    print("== boolean_masking ==")
    print("x:\n", x)

    mask = x > 0
    print("mask (x>0):\n", mask)

    # 조건에 맞는 원소만 1D로 뽑힘
    positives = x[mask]
    print("x[mask] (flattened positives):", positives)

    # 조건에 맞는 곳을 값으로 덮어쓰기
    x[mask] = 0
    print("x after x[mask]=0:\n", x)
    print()


def fancy_indexing() -> None:
    x = torch.arange(0, 20).reshape(5, 4)
    print("== fancy_indexing ==")
    print("x:\n", x)

    row_idx = torch.tensor([0, 2, 4])   # 0,2,4행
    col_idx = torch.tensor([1, 3, 0])   # 각각 1,3,0열

    # (row_idx[i], col_idx[i]) 쌍으로 뽑힘
    picked = x[row_idx, col_idx]
    print("picked = x[row_idx, col_idx]:", picked)

    # 특정 행들만 선택
    rows = x[row_idx]
    print("x[row_idx]:\n", rows)
    print()


def broadcasting_demo() -> None:
    print("== broadcasting_demo ==")
    a = torch.randn(3, 4)
    b = torch.randn(4)      # (4,) -> (1,4)로 확장 -> (3,4)로 확장 가능
    c = torch.randn(3, 1)   # (3,1) -> (3,4)로 확장 가능

    print("a.shape:", a.shape)
    print("b.shape:", b.shape)
    print("c.shape:", c.shape)

    y1 = a + b
    y2 = a + c
    print("y1 = a + b -> shape:", y1.shape)
    print("y2 = a + c -> shape:", y2.shape)

    # 확장(expand) vs repeat
    # - expand: 실제 메모리 복사 없이 "뷰"로 확장(가능할 때만)
    # - repeat: 실제로 데이터를 복제하여 메모리 사용 증가
    b2 = b.view(1, 4).expand(3, 4)  # (1,4) -> (3,4)
    print("b2.shape (expanded):", b2.shape, "contiguous:", b2.is_contiguous())

    b3 = b.view(1, 4).repeat(3, 1)  # (1,4) -> (3,4) 복사
    print("b3.shape (repeated):", b3.shape, "contiguous:", b3.is_contiguous())
    print()


def main() -> None:
    basic_indexing()
    boolean_masking()
    fancy_indexing()
    broadcasting_demo()


if __name__ == "__main__":
    main()
