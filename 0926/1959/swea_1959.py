import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ai = list(map(int, input().split()))
    bj = list(map(int, input().split()))

    if N > M:
        ai, bj = bj, ai
        N, M = M, N

    best = 0

    for i in range(M-N+1):
        prefix_sum = 0
        for j in range(N):
            prefix_sum += ai[j] * bj[i+j]

        if best < prefix_sum:
            best = prefix_sum

    print(f'#{tc} {best}')




import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    best = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            prefix_sum = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    prefix_sum += arr[k][l]

            if prefix_sum > best:
                best = prefix_sum


    print(f'#{tc} {best}')


    # print(f'#{tc} {result}')