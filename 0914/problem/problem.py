import sys
sys.stdin = open('input.txt')

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x,y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                dfs(nx, ny)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for row in range(N)]
    visited = [[False]*N for _ in range(N)]

    count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1 and not visited[i][j]:
                count += 1
                dfs(i, j)

    print(f'#{tc} {count}')