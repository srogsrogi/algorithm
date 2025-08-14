import sys
sys.stdin = open('input.txt')


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(T):
    N, M = list(map(int, input().split()))
    arr = []
    for r in range(N):
        row = list(map(int, input().split()))
        arr.append(row)

    best = 0
    