import sys

sys.stdin = open("input.txt")


# 입력 처리
N, M = map(int, input().split())
grid = [list(map(int, input())) for _ in range(N)]

# 방문 여부
visited = [[False] * M for _ in range(N)]

# 상, 하, 좌, 우, 대각선 4방향을 포함한 8방향 델타


# DFS 함수 정의 (재귀 방식)
def dfs(r, c):
    pass


# --- 메인 로직 ---
island_count = 0

# 최종 섬의 개수를 출력합니다.
print(island_count)
