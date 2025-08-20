from collections import deque

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    queue = deque()

    for elem in arr:
        queue.append(elem)

    while len(queue) > 1:
        

    # print(f'#{tc} {result}')