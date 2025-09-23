# 예외처리

'''
에러(ERROR)
    - 프로그램이 실행 자체를 할 수 없게 만드는 치명적인 문제
    - ex) 구문(syntax) 오류 : 문법에 맞지 않거나 오타가 많은 경우 발생하는 오류
                            IDE에서 실행 전에 뜰 수 있음

예외(EXCEPTION)
    - 실행 중(runtime)에 발생하며, 코드가 실행을 시작했으나, 특정 상황에서 중단되는 문제
    - ex) 파일을 읽어 사용하려는데, 파일이 없는 경우,
            리스트 값을 출력하려는 데, 리스트 요소가 없는 경우,
            → 에러가 발생되면 프로그램의 동작이 중지 또는 종료됨
'''

'''
예외 처리
    에러가 발생할만한 부분을 예측하여, 미리 예외 상황에 대한 처리를 하는 것
    Try 블록에서 발생한 예외를 except 블록에서 처리한다.

* 기본 문법
    Try 블록에서 발생한 예외를 except 블록에서 처리

    try:
        # 예외가 발생할 수 있는 코드
    except:
        # 예외가 발생했을 때 실행할 코드
'''

'''
발생 가능한 에외 종류

- IndexError : 리스트 인덱스 상위 오류
        ex) IndexError : Index out of range
            리스트 길이를 넘는 인덱스로 요소에 접근하려 할 때

- ValueError : 부적절한 값을 가진 인자를 받았을 때 발생
        ex) ValueError : invalid literal for int() with base 10: 'hello'
            int() 정수 값이 인자로 와야 하는데, 문자열이 옴

- ZeroDivisionError : 0으로 나눌 때 발생하는 오류

- NameError : 존재하지 않는 변수를 호출할 때

- FileNotFoundError : 존재하지 않는 파일을 호출할 때
'''
# 사용 예제 - 단일 except
try:
    num = int(input("숫자를 입력하세요:"))
    print(10/num)
except:
    print("오류가 발생했습니다.")

'- 하나의 except 블록으로 모든 예외 처리'

# 사용 예제 - 특정 예외 지정
try:
    value = int("abc")
except ValueError:
    print("잘못된 숫자 형식입니다.")

'- 특정 예외 유형만 처리'

# 사용 예제 - 모든 예외 처리(except Exception as e)
try:
    value = int("abc")
except Exception as e:
    print("예외 발생:", e)

'- 모든 예외 처리는 디버깅을 어렵게 만들 수 있으므로 필요한 경우에만 사용'

# 사용 예제 - 예외 객체 활용
try:
    num = int("abc")
except Exception as e:
    # 예외 메시지 출력
    print("예외 메시지:", e)
    # 예외 클래스 타입 출력
    print("예외 타입:", type(e))

'- 예외 정보를 출력하거나 타입 확인 가능'

# 사용 예제 - 다중 except
try:
    num = int(input("숫자를 입력하세요: "))
    print(10 / num)
except ValueError:
    print("숫자가 아닙니다.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

'- 여러 예외를 다중 처리'

# 사용 에제 - else 절
try:
    num = int(input("숫자를 입력하세요: "))
except ValueError:
    print("유효하지 않은 숫자입니다.")
else:
    print(f'{num}을 입력했습니다.')

'- else 절은 try 블록에서 예외가 발생하지 않을 때 실행'

# 사용 예제 - finally절
try:
    num = int(input("숫자를 입력하세요: "))
    print(10 / num)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
finally:
    print("프로그램을 종료합니다.")

'- finally 절은 예외 발생 여부와 관계없이 항상 실행됨'

# 사용 예제 - raise ~ Exception


def divide(a, b):
    if b == 0:
        # 강제로 예외 발생
        raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    return a / b


try:
    print(divide(10, 0))
except ZeroDivisionError as e:
    print("예외 처리 : ", e)

'- 일반적으로 함수나 로직에서 잘못된 조건을 감지했을 때 의도적으로 예외를 발생시킴'
