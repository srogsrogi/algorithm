import sys
sys.stdin = open('input.txt')


dx = [0, 1]
dy = [1, 0]

def dfs(x, y, current_sum):
    global best

    if current_sum >= best:
        return

    if x == N-1 and y == N-1:
        if current_sum < best:
            best = current_sum
            return

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            dfs(nx, ny, current_sum + arr[nx][ny])


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for r in range(N)]
    best = 99999
    dfs(0, 0, arr[0][0])

    print(f'#{tc} {best}')