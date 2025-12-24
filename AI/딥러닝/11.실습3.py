# -*- coding: utf-8 -*-
"""
pytorch_autograd_step_by_step.py
================================
주제: PyTorch Autograd(자동미분) - y = (2x + 1)^3 단계별 분해 & gradient 확인

이 파일은 다음 예제들을 "한 파일"에 통합한 실습용 스크립트입니다.

[기본]
1) backward() + retain_grad()로 중간 텐서의 grad까지 확인
2) torch.autograd.grad()로 원하는 gradient를 "리턴값"으로 직접 받기
3) 2차 미분(Second derivative): create_graph=True 활용

[추가]
4) gradient 누적(accumulation)과 초기화(zeroing)
5) detach() / torch.no_grad()로 그래프 끊기 및 추론 모드
6) in-place 연산(예: +=, relu_ 등) 주의사항과 대표 에러 사례

실습 포인트
-----------
- leaf tensor(x처럼 사용자가 직접 만든 텐서 + requires_grad=True)만 기본적으로 .grad에 누적됩니다.
- 연산으로 만들어진 텐서(a, b)는 non-leaf tensor:
    - 기본적으로 a.grad, b.grad는 저장되지 않습니다.
    - 중간 노드 grad를 보고 싶으면 a.retain_grad(), b.retain_grad()를 호출해야 합니다.
- autograd.grad()는 .grad에 누적시키지 않고, 원하는 미분값을 "리턴"으로 받습니다.
- 2차 미분(또는 더 높은 차수 미분)을 하려면 create_graph=True로 그래프를 유지/생성해야 합니다.
- backward()를 여러 번 호출하면 grad는 "누적"됩니다. 학습 루프에서는 보통 optimizer.zero_grad()를 호출합니다.
- detach() 또는 torch.no_grad()는 그래프를 끊어, 불필요한 gradient 추적을 방지합니다.
- in-place 연산은 Autograd가 필요한 중간값을 덮어써서 오류를 유발할 수 있습니다.

수학적 기대값 (x=3)
-------------------
b = 2x + 1 = 7
y = b^3 = 343

dy/db = 3b^2 = 147
dy/da = dy/db * db/da = 147 * 1 = 147
dy/dx = dy/da * da/dx = 147 * 2 = 294

2차 미분:
dy/dx = 6(2x+1)^2
d2y/dx2 = 24(2x+1) -> x=3이면 24*7=168
"""

import torch


# ----------------------------------------------------------------------
# 예제 1) backward() + retain_grad()
# ----------------------------------------------------------------------
def example_backward_with_retain_grad(x_value: float = 3.0) -> None:
    """
    [예제 1] backward()로 grad를 구하고, retain_grad()로 중간 텐서 grad도 확인.

    주의:
    - a, b는 leaf tensor가 아니라서 기본적으로 a.grad, b.grad가 None입니다.
    - retain_grad()를 호출해야 backward 이후 a.grad, b.grad를 확인할 수 있습니다.
    """
    print("=" * 70)
    print("[예제 1] backward() + retain_grad()")
    print("=" * 70)

    # leaf tensor 생성
    x = torch.tensor(x_value, requires_grad=True)

    # y = (2x + 1)^3 단계별 분해
    a = 2 * x        # a = 2x
    b = a + 1        # b = 2x + 1
    y = b ** 3       # y = (2x + 1)^3

    # 중간 텐서 grad 추적을 원하면 retain_grad() 필요
    a.retain_grad()
    b.retain_grad()

    # dy/dx 계산
    y.backward()

    # 결과 출력
    print(f"x = {x.item()}")
    print(f"a = 2x = {a.item()}")
    print(f"b = 2x+1 = {b.item()}")
    print(f"y = (2x+1)^3 = {y.item()}")
    print(f"dy/dx (x.grad) = {x.grad.item()}")
    print(f"dy/da (a.grad) = {a.grad.item()}")
    print(f"dy/db (b.grad) = {b.grad.item()}")

    # 기대값 검증(부동소수 오차 고려)
    expected_dy_db = 3 * (b.detach() ** 2)         # 3b^2
    expected_dy_da = expected_dy_db * 1            # db/da = 1
    expected_dy_dx = expected_dy_da * 2            # da/dx = 2

    assert torch.allclose(b.grad, expected_dy_db), "dy/db 검증 실패"
    assert torch.allclose(a.grad, expected_dy_da), "dy/da 검증 실패"
    assert torch.allclose(x.grad, expected_dy_dx), "dy/dx 검증 실패"
    print("검증: OK\n")


# ----------------------------------------------------------------------
# 예제 2) torch.autograd.grad()
# ----------------------------------------------------------------------
def example_autograd_grad(x_value: float = 3.0) -> None:
    """
    [예제 2] torch.autograd.grad()로 gradient를 리턴값으로 받기.

    장점:
    - backward()처럼 .grad에 누적되는 방식이 아니라 "원하는 gradient"를 곧바로 얻습니다.
    - 중간 노드 grad도 retain_grad() 없이 뽑아낼 수 있습니다.

    주의:
    - 동일한 그래프에서 grad()를 여러 번 호출하면 기본적으로 그래프가 소모(free)됩니다.
      -> 여러 번 계산하려면 retain_graph=True를 사용합니다.
    """
    print("=" * 70)
    print("[예제 2] torch.autograd.grad()로 단계별 미분값 얻기")
    print("=" * 70)

    x = torch.tensor(x_value, requires_grad=True)

    a = 2 * x
    b = a + 1
    y = b ** 3

    # dy/db
    (dy_db,) = torch.autograd.grad(y, b, retain_graph=True)
    # dy/da
    (dy_da,) = torch.autograd.grad(y, a, retain_graph=True)
    # dy/dx
    (dy_dx,) = torch.autograd.grad(y, x)

    print(f"x = {x.item()}")
    print(f"a = {a.item()}")
    print(f"b = {b.item()}")
    print(f"y = {y.item()}")
    print(f"dy/db = {dy_db.item()}")
    print(f"dy/da = {dy_da.item()}")
    print(f"dy/dx = {dy_dx.item()}")

    # 기대값 검증
    expected_dy_db = 3 * (b.detach() ** 2)   # 3b^2
    expected_dy_da = expected_dy_db          # db/da = 1
    expected_dy_dx = expected_dy_da * 2      # da/dx = 2

    assert torch.allclose(dy_db, expected_dy_db), "dy/db 검증 실패"
    assert torch.allclose(dy_da, expected_dy_da), "dy/da 검증 실패"
    assert torch.allclose(dy_dx, expected_dy_dx), "dy/dx 검증 실패"
    print("검증: OK\n")


# ----------------------------------------------------------------------
# 예제 3) 2차 미분
# ----------------------------------------------------------------------
def example_second_derivative(x_value: float = 3.0) -> None:
    """
    [예제 3] 2차 미분 계산 (d2y/dx2)

    핵심:
    - 1차 미분 dy/dx를 구할 때 create_graph=True로 "미분 결과"가 다시 미분 가능하도록 그래프를 생성해야 합니다.
    - 그 다음 torch.autograd.grad(dy_dx, x)로 2차 미분을 구합니다.
    """
    print("=" * 70)
    print("[예제 3] 2차 미분(Second derivative) - create_graph=True")
    print("=" * 70)

    x = torch.tensor(x_value, requires_grad=True)

    # y = (2x + 1)^3
    y = (2 * x + 1) ** 3

    # 1차 미분: dy/dx
    (dy_dx,) = torch.autograd.grad(y, x, create_graph=True)

    # 2차 미분: d2y/dx2
    (d2y_dx2,) = torch.autograd.grad(dy_dx, x)

    print(f"x = {x.item()}")
    print(f"y = {y.item()}")
    print(f"dy/dx = {dy_dx.item()}")
    print(f"d2y/dx2 = {d2y_dx2.item()}")

    # 기대값 검증
    expected_dy_dx = 6 * (2 * x.detach() + 1) ** 2
    expected_d2y_dx2 = 24 * (2 * x.detach() + 1)

    assert torch.allclose(dy_dx.detach(), expected_dy_dx), "dy/dx 검증 실패"
    assert torch.allclose(d2y_dx2.detach(), expected_d2y_dx2), "d2y/dx2 검증 실패"
    print("검증: OK\n")


# ----------------------------------------------------------------------
# 예제 4) gradient 누적과 초기화 (zeroing)
# ----------------------------------------------------------------------
def example_grad_accumulation_and_zeroing(x_value: float = 3.0) -> None:
    """
    [예제 4] backward()는 기본적으로 gradient를 누적(accumulate)합니다.

    왜 중요한가?
    - 학습(Training)에서는 보통 배치마다 backward()를 호출하고,
      이전 배치에서 누적된 grad를 지워야 하므로 optimizer.zero_grad()를 호출합니다.

    여기서는 optimizer 없이 x.grad를 수동으로 초기화하는 방법을 보여줍니다.
    """
    print("=" * 70)
    print("[예제 4] gradient 누적(accumulation)과 초기화(zeroing)")
    print("=" * 70)

    x = torch.tensor(x_value, requires_grad=True)

    # 첫 번째 backward
    y1 = (2 * x + 1) ** 3
    y1.backward()
    print(f"1회차 backward 후 x.grad = {x.grad.item()}")

    # 두 번째 backward (같은 x에 대해 또 backward 하면 grad가 누적됨)
    # 주의: 동일 그래프를 두 번 backward하려면 retain_graph=True가 필요할 수 있지만,
    #       여기서는 y2를 새로 만들어 "새 그래프"로 backward하기 때문에 괜찮습니다.
    y2 = (2 * x + 1) ** 3
    y2.backward()
    print(f"2회차 backward 후 x.grad(누적) = {x.grad.item()}  (1회차의 2배가 되는 것이 정상)")

    # grad 초기화(방법 1): x.grad를 0으로
    x.grad.zero_()
    print(f"zero_()로 초기화 후 x.grad = {x.grad.item()}")

    # 다시 backward 해보면 처음 값으로 돌아옴
    y3 = (2 * x + 1) ** 3
    y3.backward()
    print(f"초기화 후 다시 backward -> x.grad = {x.grad.item()}")

    # 검증: 1회차와 동일해야 함
    expected = 6 * (2 * x.detach() + 1) ** 2  # dy/dx
    assert torch.allclose(x.grad, expected), "초기화 후 dy/dx 값 검증 실패"
    print("검증: OK\n")


# ----------------------------------------------------------------------
# 예제 5) detach() / torch.no_grad()
# ----------------------------------------------------------------------
def example_detach_and_no_grad(x_value: float = 3.0) -> None:
    """
    [예제 5] detach()와 torch.no_grad()의 차이를 이해합니다.

    - detach(): 특정 텐서를 그래프에서 "분리"한 새로운 텐서를 반환.
        -> detached 텐서는 requires_grad=False로 간주되고, 이후 연산은 grad 추적 안 함.
    - torch.no_grad(): 해당 컨텍스트(블록) 안에서 수행되는 연산 전체를 grad 추적하지 않음.
        -> 추론(inference)이나 파라미터 업데이트(일부 경우)에서 사용

    실무 팁:
    - 추론/평가 단계에서는 보통 torch.no_grad() + model.eval()을 함께 사용합니다.
    """
    print("=" * 70)
    print("[예제 5] detach() / torch.no_grad()로 그래프 끊기")
    print("=" * 70)

    x = torch.tensor(x_value, requires_grad=True)

    # (A) 일반 계산: grad 추적 O
    y = (2 * x + 1) ** 3
    y.backward()
    print(f"(A) 일반 계산 후 x.grad = {x.grad.item()}")

    # grad 초기화
    x.grad.zero_()

    # (B) detach(): 그래프 분리
    z = (2 * x + 1)          # z는 grad 추적됨
    z_detached = z.detach()  # 그래프에서 분리된 텐서 (requires_grad=False 취급)

    # z_detached로부터 만든 값은 x로 gradient가 전파되지 않음
    y_detached = z_detached ** 3
    # y_detached는 requires_grad=False이므로 backward 자체가 불가능 (에러)
    print(f"(B) z_detached.requires_grad = {z_detached.requires_grad}")
    try:
        y_detached.backward()
    except RuntimeError as e:
        print("(B) detach된 텐서로 만든 y_detached는 backward 불가(정상):")
        print("    ", str(e).splitlines()[0])

    # (C) torch.no_grad(): 블록 전체 grad 추적 OFF
    with torch.no_grad():
        y_ng = (2 * x + 1) ** 3
    print(f"(C) no_grad 블록 결과 y_ng.requires_grad = {y_ng.requires_grad}")

    # no_grad 결과 역시 backward 불가
    try:
        y_ng.backward()
    except RuntimeError as e:
        print("(C) no_grad 결과는 backward 불가(정상):")
        print("    ", str(e).splitlines()[0])

    print("정리: detach/no_grad는 '추론'이나 '그래프 끊기'에 사용하며, 그 결과로는 역전파가 되지 않습니다.\n")


# ----------------------------------------------------------------------
# 예제 6) in-place 연산 주의사항
# ----------------------------------------------------------------------
def example_inplace_pitfall(x_value: float = 3.0) -> None:
    """
    [예제 6] in-place 연산이 autograd를 망가뜨릴 수 있는 대표 사례

    in-place 연산 예:
    - 텐서에 직접 덮어쓰기: b += 1, b.mul_(2), relu_(), add_(), 등
    - 결과 메모리를 재사용하여 효율을 얻는 대신, autograd가 필요로 하는 중간값을 덮어쓸 수 있습니다.

    아래 코드는 일부 환경에서 다음과 같은 런타임 에러를 유발하는 전형적인 패턴입니다.
    - "one of the variables needed for gradient computation has been modified by an inplace operation"

    주의:
    - 에러가 항상 100% 동일하게 발생하지는 않지만, 원리는 동일합니다.
    - 실무에서는 in-place 연산을 피하거나, autograd 요구사항을 만족하도록 설계를 바꿉니다.
    """
    print("=" * 70)
    print("[예제 6] in-place 연산 주의사항")
    print("=" * 70)

    x = torch.tensor(x_value, requires_grad=True)

    # 문제를 유발하기 쉬운 예:
    # b를 이용해 y를 계산해두고, 그 이후 b를 in-place로 바꾸면
    # backward 때 b의 원래 값이 필요할 수 있어 오류가 날 수 있습니다.
    b = 2 * x + 1
    y = b ** 3

    # in-place 수정 (의도적으로 위험한 코드)
    # b = b + 1  (out-of-place) 는 안전한 편
    # b += 1     (in-place) 는 위험할 수 있음
    try:
        b += 1  # in-place
        y.backward()
        print("이 환경에서는 에러가 발생하지 않았습니다(하지만 일반적으로 위험한 패턴입니다).")
        print(f"x.grad = {x.grad.item()}")
    except RuntimeError as e:
        print("in-place 연산으로 인해 backward에서 에러 발생(정상적인 학습 코드에서는 피해야 함):")
        print("   ", str(e).splitlines()[0])

    # 안전한 대안 예시(권장):
    # out-of-place로 새 텐서 만들기
    x2 = torch.tensor(x_value, requires_grad=True)
    b2 = 2 * x2 + 1
    y2 = b2 ** 3
    b2_safe = b2 + 1  # out-of-place: b2는 그대로, b2_safe는 새로운 텐서
    # y2는 b2에 대한 그래프가 유지되어 안전하게 backward 가능
    y2.backward()
    print("안전한(out-of-place) 방식으로 backward 성공.")
    print(f"x2.grad = {x2.grad.item()}\n")


def main() -> None:
    """
    실행 엔트리포인트.
    - 예제 1~6을 순서대로 실행합니다.
    """
    torch.set_printoptions(precision=6)

    x_value = 3.0

    example_backward_with_retain_grad(x_value)
    example_autograd_grad(x_value)
    example_second_derivative(x_value)

    # 추가 예제
    example_grad_accumulation_and_zeroing(x_value)
    example_detach_and_no_grad(x_value)
    example_inplace_pitfall(x_value)

    print("모든 예제 실행 완료.")


if __name__ == "__main__":
    main()
