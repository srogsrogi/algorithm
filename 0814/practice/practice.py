import sys
sys.stdin = open('input.txt')

# precedence = {
#     '+' : 1,
#     '-' : 1,
#     '*' : 2,
#     '/' : 2
# }

T = int(input())

for tc in range(1, T+1):
    expression = input()

    stack = []
    result = []

    for token in expression:
        if token.isalnum():
            result.append(token)
        else:
            stack.append(token)

    while stack:
        result.append(stack.pop())


    # for token in expression:
    #     if token.isalnum():
    #         result.append(token)
    #
    #     elif token == '(':
    #         stack.append(token)
    #
    #     elif token == ')':
    #         while stack and stack[-1] != '(':
    #             result.append(stack.pop())
    #         stack.pop()
    #
    #     else:
    #         while(
    #                 stack
    #                 and stack[-1] != '('
    #                 and precedence.get(stack[-1]) >= precedence.get(token)
    #         ):
    #
    #             result.append(stack.pop())
    #
    #         stack.append(token)
    #
    # while stack:
    #     result.append(stack.pop())

    print(f'#{tc} {"".join(result)}')