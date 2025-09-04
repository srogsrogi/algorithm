# stack 저수준 구현
class Stack:
    def __init__(self,capacity = 10):
        self.capacity = capacity
        self.items = [None] * capacity
        self.top = -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, item):
        if self.isfull():
            raise IndexError('Stack is full')
        self.top += 1
        self.items[self.top] = item

    def is_empty(self):
        return self.top == -1

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        item = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return item
    
    def peek(self):
        if self.is_empty(self):
            raise IndexError('Stack is empty')
        return self.items[self.top]


# 괄호검사
def check_match(expression):
    stack = []
    matching_dict = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in expression:
        if char in matching_dict.values():
            stack.append(char)
        elif char in matching_dict.keys():
            if not stack:
                return False
            else:
                if matching_dict[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        else:
            continue

    if stack:
        return False
    else:
        return True

problem_1 = '{das{{([]]])}zz}}'
print(check_match(problem_1))