'''
델타이동 + 백트래킹인가 싶었는데 경우의 수가 너무 많음 망할듯
bfs인 거 같기도 하고..
일단 시간초과 나더라도 쌩 완탐 시도
'''

import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for row in range(N)]

    sum_cost = 0
    for r in range(N):
        for c in range(N):
            # 방향이 정해져있지 않아서 for문으로 못가겠는데?;;;;;;;;



    # print(f'#{tc} {result}')