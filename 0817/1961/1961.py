import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N = int(input())

    arr = []
    for r in range(N):
        row = input().split()
        arr.append(row)

    # 90도 회전 패턴 반복 적용
    for i in range(N):
        rotated_90 = list(zip(*arr[::-1]))

        rotated_180 = list(zip(*rotated_90[::-1]))

        rotated_270 = list(zip(*rotated_180[::-1]))

    for j in range(N):
        print(''.join(rotated_90[j]), ''.join(rotated_180[j]), ''.join(rotated_270[j]))



