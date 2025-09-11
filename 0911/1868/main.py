'''
n * n 행렬
최소번 클릭하려면..
1. 지뢰가 없는 곳을 눌러야 한다
2. 누른 곳에서 8방향 델타이동을 연쇄적으로 했을 때 가장 많은 칸이 열리는 곳을 선택해야 한다.
3. 매 회차에서 그 선택을 greedy하게 반복하면서 count를 세면 될텐데
근데 지뢰가 없는 칸을 완탐하는 건 연산량이 말이 안 됨 무조건 망할 듯
---
1. 지뢰위치에서 8방향으로 인덱스 1씩 움직인 위치들을 다 점찍고나면, 나머지 구역은 지뢰와 상관 없는 위치니까 분리된 구역별로 1번씩만 클릭하면 된다.
2. 숫자칸은 무조건 1개당 1클릭
3. 그러니까 숫자칸 수 + 지뢰와 지뢰에서 8방이동한 점들이 배열에서 만들어내는 구역 수가 답이 될 것 같음
'''

import sys
sys.stdin = open('input.txt')

dr = [0, 1, 1, -1, 1, -1, -1, 0]
dc = [1, 0, 1, -1, -1, 1, 0, -1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(input().strip()) for row in range(N)]

    # 클릭 수
    count = 0
    # * 주변은 그냥 다 x로 칠해버림
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == '*':
                # 8방향 델타이동
                for i in range(8):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    # 벽 조건 설정, 원래 *인 곳은 순회할 때 걸려야 하니까 덮으면 안 됨
                    if 0 <= nr < N and 0 <= nc < N and matrix[nr][nc] != '*':
                        matrix[nr][nc] = 'x'

    # 구역 수 구하기
    for j in range(1, N):
        for k in range(1, N):
            # .인 경우 count할건데
            if matrix[j][k] == '.':
                # 왼쪽 또는 위에 .이 있었으면 연결돼있는 구역이니까 제외
                if matrix[j-1][k] == '.' or matrix[j][k-1] == '.':
                    continue
                count += 1

    # x는 숫자니까 count += 1
    for m in range(N):
        for n in range(N):
            if matrix[m][n] == 'x':
                count += 1

    print(f'#{tc} {count}')

    ############## 아 왜안됨