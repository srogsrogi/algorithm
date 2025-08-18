import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = []

    for r in range(N):
        row = list(map(int, input().split()))
        arr.append(row)
    max_count = 0
    for i in range(N):
        for j in range(M):
            count = arr[i][j]

            for k in range(4):
                for step in range(1, arr[i][j]+1):
                    nr = i + dr[k] * step
                    nc = j + dc[k] * step

                    if 0 <= nr < N and 0 <= nc < M:
                        count += arr[nr][nc]

            max_count = max(count, max_count)



    print(f'#{tc} {max_count}')