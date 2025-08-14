def evaluate_postfix(expression):
    """
    후위 표기법으로 표현된 수식을 계산하여 결과를 반환하는 함수.

    Args:
        expression (str): 후위 표기법으로 작성된 문자열 (예: "53+2*")

    Returns:
        int or float: 수식의 최종 계산 결과
    """
    stack = []

    # 후위표기된 수식 순회
    for token in expression:
        # token이 숫자인 경우
        if token.isdigit():
            stack.append(int(token))
        # token이 연산자인 경우
        # 먼저 pop한게 꼭 오른쪽으로 가야 함!
        else:
            right = stack.pop()
            left = stack.pop()
            
            if token == '+':
                result = left + right
            elif token == '-':
                result = left + right
            elif token == '*':
                result = left * right
            elif token == '/':
                result = left / right

            # 연산된 값을 stack에 push
            stack.append(result)

    # 반복문이 다 돌고 나면 stack에 값이 1개만 남고, 이게 연산 결과
    return stack.pop()



# --- 실행 코드 ---
# (5 + 3) * 2 를 후위 표기법으로 표현
postfix_expr = "53+2*"
result = evaluate_postfix(postfix_expr)
print(f"'{postfix_expr}'의 계산 결과: {result}")  # '53+2*'의 계산 결과: 16
