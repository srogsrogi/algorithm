import sys
sys.stdin = open('input.txt')

T = int(input())

arr = []

for tc in range(1, T+1):
    N, M = map(int, input().split())

    for r in range(N):
        row = list(map(int, input().split()))
        arr.append(row)






    # print(f'#{tc} {result}')