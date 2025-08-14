import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    str_1 = input()
    str_2 = input()
#     if str_1 in str_2:
#         result = 1
#     else:
#         result = 0
#
#     print(f'{tc + 1} {result}')

    M = len(str_1)
    N = len(str_2)
    result = 0
    for i in range(N-M+1):
        if str_2[i:i+M] == str_1:
            result = 1
            break

    print(f'#{tc + 1} {result}')

