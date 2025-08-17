import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(T):
        N, M = map(int, input().split())
        arr = [list(map(int, input().split())) for _ in range(N)]

        # 위력 최대값 초기화
        max_total = 0

        for r in range(N):
                for c in range(M):
                     # 폭발 범위
                     power = arr[r][c]
                     # 총 위력(델타 이동하며 상하좌우방향의 값들만 더할 것이므로 초기값에 중심값 입력)
                     total = arr[r][c]

                     for i in range(4):
                             for step in range(1, power + 1):
                                     nr = r + dr[i] * step
                                     nc = c + dc[i] * step
                                     # 벽 제한
                                     if 0 <= nr < N and 0 <= nc < M:
                                             total += arr[nr][nc]
                     # 위력 최대값 갱신
                     if max_total < total:
                             max_total = total

        print(f'#{tc} {max_total}')