students = [
    {'name': "홍길동", 'score': 80},
    {'name': "김철수", 'score': 92},
    {'name': "이영희", 'score': 72}
]

students.sort(key=lambda x: x['score'], reverse=True)

for student in students:
    print(f'{students['name']}: {students['score']}점')


students.sort(key=lambda x: x['name'])

for student in students:
    print(f'{students['name']}: {student['score']}점')
