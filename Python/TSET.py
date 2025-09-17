'''
2. 유효한 나이만 평균 내기
    사용자에게 총 5명의 나이를 입력받아, 유효한 나이들만 평균을 내어 출력하세요.
    - 변수 times는 유효한 입력의 개수를 셈.
    - 변수 sum_age 는 나이의 합계를 저장함.
    - 나이는 정수로 입력받음.
    - 나이가 0이하이거나 120보다 크면 무시하고, 반복을 건너뜀
    - 5개의 유효한 나이를 입력받으면 루프를 종료하고, 총합과 평균을 출력함.
'''

# 5명의 사용자 입력 나이 리스트
ageList = input("5명의 나이를 입력해주십시오.(구분자 : \" \") \n : ").split()

# 변수 초기화
times, sum_age = 0, 0

# 무한 반복문
while True:
    # ageList 길이만큼 반복
    for x in range(0, len(ageList)):
        # 0 이하이거나 120보다 큰 나이 무시
        if int(ageList[x]) <= 0 or int(ageList[x]) > 120:
            continue
        else:
            # 유효한 나이 개수 카운트
            times += 1
            # 유효한 나이 합계 계산
            sum_age += int(ageList[x])
    # while 반복 멈춤
    break
print(f'times = {times}, sum_age = {sum_age}')
