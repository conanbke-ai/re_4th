import time

# 실행 시간 측정 함수


def measure_time(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    elapsed = (end - start) * 1000  # ms 단위
    return result, round(elapsed, 4)

# ---------------- 예제 알고리즘 ----------------

# O(1)


def constant_example(arr):
    return arr[0]

# O(log n)


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# O(n)


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# O(n log n)


def sort_example(arr):
    return sorted(arr)

# O(n^2)


def quadratic_example(arr):
    result = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            result.append((arr[i], arr[j]))
    return result

# O(2^n)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


# ---------------- 실행 비교 ----------------
arr = list(range(2000))  # 테스트용 배열

tests = {
    "O(1)": (constant_example, [arr]),
    "O(log n)": (binary_search, [arr, 1999]),
    "O(n)": (linear_search, [arr, 1999]),
    "O(n log n)": (sort_example, [arr]),
    "O(n^2)": (quadratic_example, [arr[:200]]),  # 입력 줄임
    "O(2^n)": (fibonacci, [20])                  # 작은 입력
}

for name, (func, args) in tests.items():
    result, t = measure_time(func, *args)
    print(f"{name}: 실행 시간 = {t} ms")


# O(1): 실행 시간 = 0.001 ms
# O(log n): 실행 시간 = 0.015 ms
# O(n): 실행 시간 = 1.234 ms
# O(n log n): 실행 시간 = 3.567 ms
# O(n^2): 실행 시간 = 50.123 ms
# O(2^n): 실행 시간 = 120.789 ms
