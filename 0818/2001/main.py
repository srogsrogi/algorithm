import sys
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0

    count_lst = []

    for r in range(N-M+1):
        for c in range(N-M+1):
            count = 0
            for i in range(M):
                for j in range(M):
                    count += arr[r+i][c+j]
                    count_lst.append(count)

    result = max(count_lst)


    print(f'#{tc} {result}')