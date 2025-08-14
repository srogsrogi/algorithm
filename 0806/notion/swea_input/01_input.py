import sys

sys.stdin = open('01_input.txt')

N, M = map(int, input().split())

# 방법 1 : 반복문
# arr = []
# for _ in range(N):
#     row = list(map(int, input().split()))
#     arr.append(row)

# print(arr)

# 방법 2 : list comprehension
arr = [list(map(int, input().split())) for _ in range(N)]

print(arr)