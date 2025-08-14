import sys

sys.stdin = open('input.txt')


T = int(input())

# 델타이동 배열
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(T):
    N = int(input())
    # 2차원 배열 list comprehension으로 받아오기
    arr = [list(map(int, input().split())) for _ in range(N)]
    # abs(주변 값과의 차)의 누적합을 담을 변수
    result = 0
    for r in range(N):
        for c in range(N):
            # 상하좌우로이동
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                # 이동할 수 있는 경우만 절대값 구하여 result에 합산
                if 0 <= nr < N and 0 <= nc < N:
                    result += abs(arr[nr][nc] - arr[r][c])

    print(f'#{tc + 1} {result}')