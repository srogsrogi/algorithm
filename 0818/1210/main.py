import sys
sys.stdin = open('input.txt')

dr = [-1, 0, 0, 0]
dc = [0, 0, -1, 1]


T = 10

for tc in range(1, T+1):
    number = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    for idx in range(100):
        if arr[99][idx] == 2:
            c = idx

    r = 99

    while r > 0:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < 100 and 0 <= nc < 100:
                if arr[nr][nc] == 1:

                    arr[r][c] = 0
                    r, c = nr, nc

    print(f'#{tc} {c}')