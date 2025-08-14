import sys

sys.stdin = open('02_input.txt')

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

print(arr)