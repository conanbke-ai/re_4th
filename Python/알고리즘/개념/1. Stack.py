# 스택(Stack)
'''

'''
'''

'''
'''
* 대표 함수
push(data)          스택의 맨 위에 요소 추가            O(1)
pop()               스택의 맨 위 요소 제거 및 반환      O(1)
peek() / top()      맨 위의 요소 확인(제거 X)           O(1)
is_empty()          스택이 비어있는지 확인              O(1)
size()              스택의 요소 개수 반환               O(1)
'''


class Stack:
    def __init__(self):
        "스택 초기화"
        self.items = []

    def push(self, item):
        "요소 추가"
        self.items.append(item)

    def pop(self):
        "요소 제거 및 반환"
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        "맨 위 요소 확인"
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        "스택 출력"
        return str(self.items)


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(f'스택 : {stack}')
