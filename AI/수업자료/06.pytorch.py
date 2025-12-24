# 01_pytorch_intro_setup.py
# -*- coding: utf-8 -*-
"""
01_pytorch_intro_setup.py
========================
PyTorch "입문 세팅" + 빠른 확인용 파일

이 파일의 목표
-------------
1) PyTorch가 어떤 프레임워크인지 1분 안에 감 잡기
2) CPU/GPU(CUDA) 사용 가능 여부 확인하기
3) "동적 계산 그래프" 감각을 간단히 확인하기

슬라이드 기반 핵심 요약
-----------------------
- PyTorch는 동적 계산 그래프 기반의 오픈소스 딥러닝 프레임워크이며,
  파이썬다운 문법/유연성과 고속 텐서 계산(특히 GPU)을 지원합니다.
- GPU 사용을 위해서는 CUDA 설치가 필요하며, 강의에서는 CUDA 11.8을 사용합니다.
  (Colab 사용 시 설치 없이도 실습 가능)

추가로 알아두면 좋은 팁(추가 개념)
---------------------------------
- device 선택: "cuda"가 있으면 GPU로, 없으면 CPU로.
- torch.manual_seed: 랜덤 텐서 재현성 확보.
- torch.set_printoptions: 텐서 출력 형식 제어.

실행
----
python 01_pytorch_intro_setup.py
"""
from __future__ import annotations

import platform
import sys
import torch


def get_default_device() -> torch.device:
    """
    사용 가능한 장치를 우선순위로 선택합니다.

    - CUDA가 가능하면 GPU 사용
    - 그렇지 않으면 CPU 사용
    """
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def show_environment() -> None:
    """파이썬/OS/PyTorch 환경을 출력합니다."""
    print("== Environment ==")
    print(f"Python    : {sys.version.split()[0]}")
    print(f"OS        : {platform.platform()}")
    print(f"PyTorch   : {torch.__version__}")
    print(f"CUDA avail: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"CUDA ver  : {torch.version.cuda}")
        print(f"GPU name  : {torch.cuda.get_device_name(0)}")
    print()


def dynamic_graph_demo(device: torch.device) -> None:
    """
    동적 계산 그래프(dynamc computation graph) "감각"을 간단히 확인합니다.

    핵심 아이디어
    -------------
    - PyTorch는 "실행되는 대로" 그래프가 만들어집니다.
    - 즉, if 문/for 문에 따라 다른 경로의 계산이 즉시 구성됩니다.
    - 디버깅이 직관적이고, 파이썬 코드처럼 모델을 작성할 수 있습니다.
    """
    torch.manual_seed(42)

    # requires_grad=True를 설정하면, 이후 연산의 그래프가 구성되고
    # backward() 호출 시 미분값(gradient)이 계산됩니다.
    x = torch.randn(5, device=device, requires_grad=True)

    # if 조건에 따라 다른 계산 경로가 선택됩니다. (동적 그래프)
    if x.mean().item() > 0:
        y = (x * 2).sum()
        branch = "positive-mean branch: y=(x*2).sum()"
    else:
        y = (x ** 2).sum()
        branch = "negative-mean branch: y=(x**2).sum()"

    print("== Dynamic Graph Demo ==")
    print("branch:", branch)
    print("x:", x)
    print("y:", y)

    # 역전파: dy/dx를 계산합니다.
    y.backward()

    # x.grad에는 y를 x로 미분한 결과가 들어갑니다.
    print("x.grad:", x.grad)
    print()


def main() -> None:
    device = get_default_device()

    show_environment()
    print("Using device:", device)
    print()

    dynamic_graph_demo(device=device)


if __name__ == "__main__":
    main()
