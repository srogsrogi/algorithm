# 중위표기식 -> 후위표기식 변환
def infix_to_postfix(expression):
    op_dict = {
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1,
        '(': 0
        }
    
    postfix = []
    stack = []

    for char in expression:
        if char.isnumeric:
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            popped = stack.pop()

            while popped != '(':
                postfix.append(popped)
                pop_token = stack.pop()
        
        else:
            while stack and op_dict[char] <= op_dict[stack[-1]]:
                postfix.append(stack.pop())
            stack.append(char)

    while stack:
        postfix.append(stack.pop())

    return ' '.join(postfix)

postfix_expression = infix_to_postfix('12+')
print(postfix_expression)

# 후위표기식 계산
def calculate(expression):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isnumeric():
            stack.append(int(token))
        else:
            op_2 = stack.pop()
            op_1 = stack.pop()

            if token == '*':
                result = op_1 * op_2
            elif token == '/':
                result = op_1 / op_2
            elif token == '+':
                result = op_1 + op_2
            elif token == '-':
                result = op_1 - op_2

            stack.append(result)
    return stack.pop()

print(calculate(postfix_expression))
