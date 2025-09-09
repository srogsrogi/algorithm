import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    now = 0
    count = 0
    while now + K < N:
        next_pos = now
        for station in arr:
            if now < station <= now + K:
                next_pos = station

        if next_pos == now:
            count = 0
            break

        now = next_pos
        count += 1

    print(count)






    # print(f'#{tc} {result}')