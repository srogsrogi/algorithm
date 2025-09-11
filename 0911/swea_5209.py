import sys
sys.stdin = open('input.txt')


def dfs(r, sum_cost):
    global best
    # 현재 비용 + 남은 최소 가능 비용 >= 현재 best 이면 skip
    if sum_cost + remained_min_sum[r] >= best:
        return
    # 행 순회
    if r == N:
        if sum_cost < best:
            best = sum_cost
        return
    # 열 순회
    for c in range(N):
        # 아직 배정 안 된 자리면 True로 갱신하면서 재귀호출
        # 배정된 자리는 skip
        if not visited[c]:
            visited[c] = True
            dfs(r + 1, sum_cost + matrix[r][c])
            # 백트래킹하고 돌아오면 원상복구
            visited[c] = False


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 각 행의 최소값
    row_min = []
    for i in range(N):
        row = matrix[i]
        # 각 행 최소값 첫 번째 원소로 초기화
        min_value = row[0]
        for j in range(1, N):
            # 더 작은 값 만나면 최소값 갱신
            if row[j] < min_value:
                min_value = row[j]
        row_min.append(min_value)

    # 남은 구간의 최소값을 담을 리스트
    remained_min_sum = [0] * (N + 1)
    # 뒤에서부터 순회하면서 더해주기
    for i in range(N - 1, -1, -1):
        remained_min_sum[i] = remained_min_sum[i + 1] + row_min[i]

    # 제품 배정됐는지 여부를 담을 리스트
    visited = [False] * N
    best = 999999

    dfs(0, 0)

    print(f'#{tc} {best}')
