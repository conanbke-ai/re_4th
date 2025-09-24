# 예외처리

'''
에러(ERROR)
    - 코드 문법을 잘못 작성한 경우
    - 프로그램이 실행 자체를 할 수 없게 만드는 치명적인 문제
    - 코드를 수정해야지만 해결될 수 있다
    - Python 인터프리터가 코드를 파싱할 때 발견
    - ex) 구문(syntax) 오류 : 문법에 맞지 않거나 오타가 많은 경우 발생하는 오류
                            IDE에서 실행 전에 뜰 수 있음
        예시:
        print('hello'  # 괄호가 안 닫힘 → SyntaxError
        if x = 5:      # == 대신 = 사용 → SyntaxError

예외(EXCEPTION)
    - 문법은 올바르지만 실행 중에 발생됨
    - 프로그램 실행 중(runtime)에 발생하며, 코드가 실행을 시작했으나, 특정 상황에서 중단되는 문제
    - 특정 조건에서 예외 발생
    - try-except 로 처리 가능
    - ex) 파일을 읽어 사용하려는데, 파일이 없는 경우,
            리스트 값을 출력하려는 데, 리스트 요소가 없는 경우,
            → 에러가 발생되면 프로그램의 동작이 중지 또는 종료됨
'''

# 예외 처리 없이 사용자 입력을 받는 위험한 코드
def dangerous_input_example():
    """
    이 함수는 사용자가 잘못된 입력을 하면 프로그램이 크래시되는 예시
    """
    try:
        print("=== 위험한 코드 시뮬레이션 ===")
        # 사용자가 'abc' 같은 문자를 입력하면 ValueError 발생으로 프로그램 종료
        # age = int(input('나이를 입력해주세요: '))
        # 위 코드는 실제로는 주석 처리 (크래시 방지)
        print("사용자가 'abc'를 입력했다고 가정...")
        age = int('abc')  # ValueError 발생
        print(f"나이: {age}")

    except ValueError:
        print("❌ 프로그램이 여기서 종료될 뻔했습니다!")

# dangerous_input_example()

# 올바른 예외 처리 시,
def safe_input_example():
    """
    예외 처리를 통해 안전하게 사용자 입력을 받는 방법
    잘못된 입력이 들어와도 프로그램이 계속 실행됨
    """
    while True:  # 올바른 입력을 받을 때까지 반복
        try:
            # 위험할 수 있는 코드를 try 블록 안에 배치
            age = int(input('나이를 입력해주세요 (숫자만): '))

            # 예외가 발생하지 않으면 여기서 반복문 종료
            print(f"입력된 나이: {age}세")
            break  # 정상 입력 시 루프 탈출

        except ValueError:  # int() 변환 실패 시 발생하는 예외
            print('❌ 숫자로만 입력해주세요!')
            print('다시 시도해보세요.\n')
            # continue가 없어도 while문이 다시 실행됨

# 실제 실행은 주석 처리 (사용자 입력 필요)
# safe_input_example()


'''
예외 처리
    에러가 발생할만한 부분을 예측하여, 미리 예외 상황에 대한 처리를 하는 것
    Try 블록에서 발생한 예외를 except 블록에서 처리한다.
    예외 발생 시, 프로그램이 즉시 종료되지만, 예외 처리 시, 프로그램을 계속 실행시킬 수 있음

* 기본 문법
    Try 블록에서 발생한 예외를 except 블록에서 처리

    try:
        # 예외가 발생할 수 있는 코드(최소한으로 작성)
    except:
        # 예외가 발생했을 때 실행할 코드
'''
# 예외 처리 사용의 나쁜 예
def bad_try_block_example():
    """
    try 블록이 너무 크면 어디서 예외가 발생했는지 파악하기 어려움
    """
    print("=== 나쁜 예시 ===")
    try:
        name = input('이름: ')           # 예외 발생 가능성 낮음
        age = int(input('나이: '))       # 예외 발생 가능성 높음
        print(f'안녕하세요 {name}님')    # 예외 발생 가능성 낮음
        calculation = 100 / age         # 예외 발생 가능성 있음
        print(f'계산 결과: {calculation}')
    except:  # 어떤 예외가 어디서 발생했는지 알기 어려움
        print('어딘가에서 오류 발생!')


print("\n[ 좋은 예시: try 블록 최소화 ]")

# 예외 처리 사용의 좋은 예
def good_try_block_example():
    """
    예외가 발생할 수 있는 부분만 try 블록으로 감싸기
    각각의 위험한 작업을 개별적으로 처리
    """
    print("=== 좋은 예시 ===")

    # 예외 발생 가능성이 낮은 코드는 try 밖에
    name = input('이름: ')

    # 첫 번째 위험한 작업: 문자열을 정수로 변환
    while True:
        try:
            age = int(input('나이: '))  # 여기서만 ValueError 가능성
            break
        except ValueError:
            print('나이는 숫자로 입력해주세요!')

    # 안전한 코드는 try 밖에
    print(f'안녕하세요 {name}님')

    # 두 번째 위험한 작업: 0으로 나누기 방지
    if age == 0:
        print('나이는 0보다 커야 합니다.')
    else:
        try:
            calculation = 100 / age  # 여기서만 ZeroDivisionError 가능성
            print(f'계산 결과: {calculation}')
        except ZeroDivisionError:
            print('나이는 0이 될 수 없습니다!')

# 실제 실행은 주석 처리 (사용자 입력 필요)
# good_try_block_example()

# 의도적으로 예외 발생시키기
def demonstrate_raise():
    """
    raise 키워드를 사용해 의도적으로 예외를 발생시키는 방법
    특정 조건에서 프로그램을 중단시키고 싶을 때 사용
    """
    print("=== raise를 이용한 예외 발생 ===")

    try:
        # 시뮬레이션: 사용자가 0을 입력했다고 가정
        num = 0  # int(input('숫자를 입력해주세요: '))
        print(f"입력된 숫자: {num}")

        # 특정 조건에서 의도적으로 예외 발생
        if num == 0:
            # raise 키워드로 직접 예외 발생
            raise ZeroDivisionError('❌ 0은 입력할 수 없습니다!')

        result = 10 / num
        print(f"10 ÷ {num} = {result}")

    except ZeroDivisionError as e:
        print(f"예외 처리됨: {e}")


demonstrate_raise()

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

# 사용 예제
def comprehensive_exception_handling():
    """
    다양한 예외 유형을 개별적으로 처리하는 방법
    각 예외마다 적절한 대응 방법을 제시
    """
    print("=== 다양한 예외 상황 시뮬레이션 ===")

    # 여러 예외 상황을 테스트하기 위한 시나리오들
    test_scenarios = [
        ("ValueError", lambda: int('abc')),
        ("IndexError", lambda: [1, 2, 3][5]),
        ("ZeroDivisionError", lambda: 10 / 0),
        ("KeyError", lambda: {'a': 1}['b']),
        ("FileNotFoundError", lambda: open('nonexistent.txt')),
    ]

    for scenario_name, scenario_func in test_scenarios:
        print(f"\n--- {scenario_name} 시뮬레이션 ---")

        try:
            # 각 시나리오별 위험한 코드 실행
            result = scenario_func()
            print(f"결과: {result}")

        except ValueError as e:
            # 값 변환 오류 (문자열 → 숫자 실패 등)
            print(f"✅ 값 오류 처리됨: 올바른 형식으로 입력해주세요")
            print(f"   세부사항: {e}")

        except IndexError as e:
            # 리스트/튜플의 범위를 벗어난 인덱스 접근
            print(f"✅ 인덱스 오류 처리됨: 배열 범위를 초과했습니다")
            print(f"   세부사항: {e}")

        except ZeroDivisionError as e:
            # 0으로 나누기 시도
            print(f"✅ 나누기 오류 처리됨: 0으로 나눌 수 없습니다")
            print(f"   세부사항: {e}")

        except KeyError as e:
            # 딕셔너리에 없는 키 접근
            print(f"✅ 키 오류 처리됨: 존재하지 않는 키입니다")
            print(f"   세부사항: {e}")

        except FileNotFoundError as e:
            # 존재하지 않는 파일 접근
            print(f"✅ 파일 오류 처리됨: 파일을 찾을 수 없습니다")
            print(f"   세부사항: {e}")

        except Exception as e:
            # 위에서 처리되지 않은 모든 예외를 catch
            # 예상치 못한 오류를 로깅하고 프로그램 계속 실행
            print(f"⚠️  예상치 못한 오류 발생: {type(e).__name__}")
            print(f"   세부사항: {e}")
            print("   개발팀에 문의해주세요.")

        else:
            # try 블록이 예외 없이 정상 완료된 경우만 실행
            print("✅ 모든 작업이 정상적으로 완료되었습니다!")

        finally:
            # 예외 발생 여부와 상관없이 항상 실행
            # 정리 작업(파일 닫기, 연결 해제 등)에 주로 사용
            print(f"   📝 {scenario_name} 시나리오 완료")


comprehensive_exception_handling()

# 사용 예제 - 완전한 예외 처리
def complete_exception_structure():
    """
    try-except-else-finally의 완전한 구조와 실행 순서 설명
    """
    print("=== 완전한 예외 처리 구조 테스트 ===")

    test_cases = [
        ("정상 케이스", lambda: 10 / 2),
        ("예외 케이스", lambda: 10 / 0),
    ]

    for case_name, test_func in test_cases:
        print(f"\n--- {case_name} ---")

        try:
            print("1️⃣ try 블록 시작")
            result = test_func()
            print(f"   결과: {result}")
            print("   try 블록 정상 완료")

        except ZeroDivisionError as e:
            print("2️⃣ except 블록 실행")
            print(f"   예외 처리: {e}")

        except Exception as e:
            print("2️⃣ except 블록 실행 (일반 예외)")
            print(f"   예상치 못한 예외: {e}")

        else:
            # try 블록에서 예외가 발생하지 않은 경우에만 실행
            print("3️⃣ else 블록 실행")
            print("   정상적으로 처리되었을 때의 후속 작업")

        finally:
            # 예외 발생 여부와 관계없이 항상 실행
            print("4️⃣ finally 블록 실행")
            print("   정리 작업 (파일 닫기, 리소스 해제 등)")


complete_exception_structure()

# 사용 예제 - 파일과 예외 처리
def file_handling_with_exceptions():
    """
    실제 개발에서 자주 사용되는 파일 처리 + 예외 처리 패턴
    """
    print("=== 파일 처리 예외 처리 예제 ===")

    filename = 'test_file.txt'

    # 1. 파일 쓰기 작업
    try:
        print("1️⃣ 파일 생성 및 쓰기 시도...")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("안녕하세요!\n파이썬 예외 처리 테스트입니다.\n")
        print("   ✅ 파일 생성 성공!")

    except PermissionError:
        print("   ❌ 권한 오류: 파일을 생성할 권한이 없습니다.")
    except OSError as e:
        print(f"   ❌ 시스템 오류: {e}")
    except Exception as e:
        print(f"   ❌ 예상치 못한 오류: {e}")

    # 2. 파일 읽기 작업
    try:
        print("\n2️⃣ 파일 읽기 시도...")
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            print("   ✅ 파일 읽기 성공!")
            print(f"   내용: {content.strip()}")

    except FileNotFoundError:
        print(f"   ❌ 파일을 찾을 수 없음: {filename}")
    except PermissionError:
        print("   ❌ 권한 오류: 파일을 읽을 권한이 없습니다.")
    except UnicodeDecodeError:
        print("   ❌ 인코딩 오류: 파일의 문자 인코딩이 올바르지 않습니다.")
    except Exception as e:
        print(f"   ❌ 예상치 못한 오류: {e}")
    finally:
        print("   📝 파일 처리 작업 완료")

    # 3. 파일 정리
    try:
        import os
        if os.path.exists(filename):
            os.remove(filename)
            print("   🗑️ 테스트 파일 삭제 완료")
    except:
        print("   ⚠️ 테스트 파일 삭제 실패 (무시해도 됩니다)")


file_handling_with_exceptions()

######################################################################################################
# 실습 1 나이 입력 프로그램

'''
사용자로부터 나이를 입력받아 연령대를 출력하는 프로그램을 작성하세요.
    - 숫자가 아니면 다시 입력 요청
    - 음수나 150 초과는 오류 메시지
    - 정상 입력 시 연령대 출력(미성년자/청년/중년/노년)
'''

def get_age_group():
    """나이를 입력받아 연령대 반환"""
    
    # 숫자가 아니면 다시 입력 요청
    # while True:
    #     try:
    #         usr_age = int(input("나이를 입력해주세요. \n : "))
    #         break
    #     except ValueError:
    #         print("숫자를 입력해주세요.")
    
    # # 입력된 나이가 음수 혹은 150 이상인 경우, 에러 발생
    # if usr_age < 0 or usr_age >= 150:
    #     raise ValueError("양수 혹은 150 미만의 숫자를 입력해주세요.")
    
    '- 입력된 나이에 따른 에러 처리가 따로 되어 불편'
    
    while True:
            
        try:
            usr_age = int(input("나이를 입력해주세요. \n : "))
            if not (0<= usr_age < 150):
                raise Exception
        except:
            print("양수 혹은 150 미만의 숫자를 입력해주세요.")
        else:
            if usr_age:
                break
                
        if 0 <= usr_age < 20:
            print(f'{usr_age}살은 미성년자입니다.')
        elif 20 <= usr_age < 40:
            print(f'{usr_age}살은 청년입니다.')
        elif 40 <= usr_age < 65:
            print(f'{usr_age}살은 중년입니다.')
        else:
            print(f'{usr_age}살은 노년입니다.')

# 테스트
get_age_group()

######################################################################################################
# 실습 2 리스트 안전 접근

'''
리스트의 특징 인덱스 값을 안전하게 가져오는 함수를 작성하세요.
'''
def safe_get(lst, index, default=None):
    """
    리스트에서 안전하게 값 가져오기
    - lst: 리스트
    - index: 인덱스
    - default: 기본값
    """
    # 여기에 코드 작성
    try:
        if not default:
            return lst[index]
        else:
            return default
    except:
        return None
    
# 테스트
numbers = [10, 20, 30]
print(safe_get(numbers, 1))      # 20
print(safe_get(numbers, 10))     # None
print(safe_get(numbers, 10, -1)) # -1

"""
🎯 예외 처리 베스트 프랙티스:

1. 구체적인 예외 처리
   ❌ except: (모든 예외를 무차별적으로 처리)
   ✅ except ValueError: (특정 예외만 처리)
   
2. 예외 정보 활용
   ✅ except FileNotFoundError as e:
      print(f"파일 오류: {e}")
   
3. try 블록 최소화
   ❌ 많은 코드를 try 안에 넣기
   ✅ 예외 가능성이 있는 코드만 try 안에
   
4. else와 finally 활용
   ✅ else: 정상 처리 후 작업
   ✅ finally: 정리 작업 (리소스 해제)
   
5. 로깅과 디버깅 정보
   ✅ 예외 발생 시 충분한 정보 제공
   ✅ 사용자 친화적인 오류 메시지

⚠️  주의사항:
- except: 문만 사용하면 모든 예외를 숨길 수 있어 위험
- 예외를 무시(pass)하는 것은 디버깅을 어렵게 만듦
- 너무 넓은 범위의 try 블록은 예외 원인 파악을 어렵게 함
- 예외 처리가 성능에 미치는 영향 고려 (예외는 비용이 큰 연산)

🔧 실전 팁:
- 사용자 입력 검증은 예외 처리보다 사전 검증이 더 효율적
- 로그 파일에 예외 정보를 기록하여 디버깅에 활용
- 단위 테스트에서 예외 상황도 함께 테스트
- 예외 메시지를 통해 사용자에게 해결 방법 제시
"""
"""
📚 파이썬 주요 예외 유형:

🔤 ValueError: 올바르지 않은 값
   - int('abc'), float('xyz')
   - 타입은 맞지만 값이 부적절한 경우

📍 IndexError: 인덱스 범위 초과  
   - list[100] (리스트에 100번째 요소가 없을 때)
   - string[50] (문자열 길이보다 큰 인덱스)

🔑 KeyError: 딕셔너리에 없는 키
   - dict['nonexistent_key']
   - 존재하지 않는 키에 접근할 때

➗ ZeroDivisionError: 0으로 나누기
   - 10 / 0, 5 // 0, 3 % 0

📁 FileNotFoundError: 파일을 찾을 수 없음
   - open('nonexistent.txt')
   - 존재하지 않는 파일 접근

🔓 PermissionError: 권한 부족
   - 읽기 전용 파일에 쓰기 시도
   - 관리자 권한이 필요한 작업

🔤 UnicodeDecodeError: 인코딩 문제
   - 잘못된 문자 인코딩으로 파일 읽기
   - 바이너리 파일을 텍스트로 읽기

🌐 AttributeError: 속성/메서드 없음
   - 'string'.append() (문자열에는 append 메서드 없음)
   - None.some_method()

🏷️ NameError: 정의되지 않은 변수/함수
   - 변수명 오타, 정의되지 않은 변수 사용

🔧 TypeError: 타입 오류
   - 'string' + 5 (문자열과 숫자 연산 불가)
   - len(5) (숫자에 len 함수 적용 불가)
"""
