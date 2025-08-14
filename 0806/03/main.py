import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(T):
    N = int(input())
    arr = []
    for r in range(100):
        row = list(map(int, input().split()))
        arr.append(row)

    sum_list = []
    num = 0
    for num in row:
        num += num
        sum_list.append(num)

