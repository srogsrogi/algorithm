import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    chars = input()
    is_pal = 0

    if chars == chars[::-1]:

        is_pal = 1

    print(f'#{tc} {is_pal}')