import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                guard_x, guard_y = i, j

    for k in range(4):
        nr = arr[guard_x][guard_y] + dr[k]
        nc = arr[guard_x][guard_y] + dc[k]

        c



    # print(f'#{tc} {result}')