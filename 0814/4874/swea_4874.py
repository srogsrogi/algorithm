import sys
sys.stdin = open('input.txt')

T = int(input())

precedence = {
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2
}

for tc in range(1, T+1):
    # . 없애고 연산하기 위해 슬라이싱
    expression = input().split()[:-1]

    stack = []

    for token in expression:
        # 피연산자(숫자) 확인
        if token.isdigit():
            stack.append(int(token))
        else:
            right = stack.pop()

            # 입력형식이 맞지 않아 두 개의 숫자가 스택에 쌓여 있지 않는 경우 error로 처리
            if stack:
                left = stack.pop()
            else:
                result = 'error'
                break

            if token == '+':
                val = left + right
            elif token == '-':
                val = left - right
            elif token == '*':
                val = left * right
            elif token == '/':
                val = left / right

            stack.append(val)

    # 입력형식이 맞지 않아 stack이 비어 있는 경우 error로 처리
    if len(stack) == 1:
        result = stack.pop()
    else:
        result = 'error'

    print(f'#{tc} {result}')