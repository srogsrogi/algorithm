import sys
sys.stdin = open('input.txt')

def dfs(x,y, current_sum):
    global best
    if best <= current_sum:
        return
    for i in range(N):
        visited[x][i] = True


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[False]*N for _ in range(N)]

    best = 999999

    # print(f'#{tc} {result}')