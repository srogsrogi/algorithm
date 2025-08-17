import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N, K = map(int, input().split())

    arr = []
    for r in range(N):
        row = input().split()
        arr.append(row)

    rotated = list(zip(*arr))
    count = 0
    for i in range(N):
        if arr[i] == 1:
            count += 1

