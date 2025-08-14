import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    string = input().strip()

    # 스택 생성
    stack = []

    # 입력받은 문자열 순회
    for char in string:
        # 스택이 비어 있으면 append(elif문의 indexing error 방지)
        if not stack:
            stack.append(char)
        # 스택의 마지막 요소와 같으면 pop
        elif char == stack[-1]:
            stack.pop()
        # 다르면 append
        else:
            stack.append(char)

    # 스택 길이 계산
    result = len(stack)

    print(f'#{tc} {result}')