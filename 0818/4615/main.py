import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())

    arr = []
    matrix = [[0] * N] * N

    for r in range(M):
        row = list(map(int, input().split()))
        arr.append(row)

    for i in range(M):
        matrix[arr[0]][arr[1]] = arr[2]
        

    # print(f'#{tc} {result}')