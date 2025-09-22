'''
2. Student 클래스 : 성적 검증(@property 사용)
    - Student 클래스를 정의하세요.
    - 인스턴스 변수 __score는 private로 선언합니다.
    - score에 대한 getter/setter를 @property를 사용하여 정의하세요.
        - 점수는 0이상 100이하만 허용되며, 범위를 벗어나면 ValueError를 발생시킵니다.(raise ValueError 사용)
'''


class Student:

    def __init__(self, score):
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if 0 <= score <= 100:
            self.__score = score
            return f'점수는 {score}입니다.'
        else:
            raise ValueError("0이상 100이하의 점수만 허용됩니다.")


s1 = Student(100)
print(s1.score)     # 100
s1.score = 50
print(s1.score)     # 50
# s1.score = 150    # ValueError: 0이상 100이하의 점수만 허용됩니다.
# print(s1.score)
