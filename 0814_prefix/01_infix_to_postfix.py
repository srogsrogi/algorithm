def infix_to_postfix(expression):
    stack = []
    result = []
    
    precedence = {
        '+' : 1,
        '-' : 1,
        '*' : 2,
        '/' : 2
    }

    for token in expression:
        # token이 피연산자
        if token.isalnum():
            result.append(token)
        # 왼쪽 괄호
        elif token == '(':
            stack.append(token)
        # 오른쪽 괄호
        elif token == ')':
            # stack의 top이 (가 될 때까지 모든 연산자를 pop
            # stack이 비어있으면 pop할 수 없음
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            # 반복이 끝난 후 (를 버림
            stack.pop()
        # 연산자
        else:
            # stack top의 연산자 우선순위(isp)와 현재 연산자 우선순위(icp) 비교
            # stack이 비어있지 않고, top이 여는 괄호가 아니고, isp가 icp보다 크거나 같으면 pop
            while (
                stack
                and stack[-1] != '('
                and precedence.get(stack[-1]) >= precedence.get(token)
            ):
                result.append(stack.pop())

            # token이 자기보다 우선순위가 낮은 연산자를 만나면
            # 현재 연산자(token)를 스택에 push
            stack.append(token)
    
    # 모든 token 처리가 끝난 후 stack에 남아 있는 연산자 처리
    while stack:
        result.append(stack.pop())

    return ''.join(result)

# 테스트
expr1 = '(A+B)*C'
expr2 = '(A+B)*(C-D)'
print(infix_to_postfix(expr1))  # "AB+C*"
print(infix_to_postfix(expr2))  # "AB+CD-*"
