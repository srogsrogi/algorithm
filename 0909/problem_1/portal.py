import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # print(arr)
    now = 1
    visited = [1] + [0] * (N-1)
    # print(visited)
    count = 0
    while now < N:
        if visited[now - 1] == 0:
            visited[now - 1] = 1
            now = arr[now - 1]
            count += 1
        else:
            now += 1
            count += 1

    print(count)





    # print(f'#{tc} {result}')