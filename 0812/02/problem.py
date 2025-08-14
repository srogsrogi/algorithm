import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    brackets = input().strip()

    # 스택 생성
    stack = []
    # result 기본값은 1, 짝이 안 맞으면 -1로 갱신할 것
    result = 1

    # 입력받은 문자열 순회
    for e in brackets:
        # 여는 괄호면 append
        if e == '(':
            stack.append('c(')
        # 닫는 괄호면..
        elif e == ')':
            # stack이 비어있으면 앞에 여는 괄호 짝이 없는 거니까 -1
            if not stack:
                result = -1
                break
            # top이 여는 괄호면 pop
            if stack[-1] == '(':
                stack.pop()

    # 반복이 끝나고 stack이 비어있지 않으면 (가 남아있으니까 -1
    if stack:
        result = -1

    print(f'#{tc} {result}')