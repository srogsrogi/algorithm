import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    code = input().strip()

    # 스택 생성
    stack = []

    # 여는 괄호, 닫는 괄호 확인용 리스트
    openers = ['{', '(']
    closers = ['}', ')']

    # 결과 기본값 1. 조건에 맞지 않으면 0으로 갱신할 것
    result = 1

    # 입력받은 문자열 순회
    for e in code:
        # 여는 괄호면 append
        if e in openers:
            stack.append(e)
        # 닫는 괄호면..
        elif e in closers:
            # stack이 비어있으면 앞에 여는 괄호 짝이 없는 거니까 0
            if not stack:
                result = 0
                break
            # top이 종류가 같은 여는 괄호면 pop
            # closers에서 e의 index로 openers에서 조회
            if stack[-1] == openers[closers.index(e)]:
                stack.pop()
            # 괄호 종류가 안 맞으면 0
            else:
                result = 0
                break

    # stack이 없어야 괄호의 짝이 다 맞은 거니까
    # stack에 요소가 있으면 0, 없으면 1
    if stack:
        result = 0

    print(f'#{tc} {result}')