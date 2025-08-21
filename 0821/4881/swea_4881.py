import itertools
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = []
    for r in range(N):
        row = list(map(int, input().split()))
        arr.append(row)

    # min 초기값 충분히 크게 설정
    min_prefix = 10 ** 10

    # 순서대로 인덱스값을 선택하여 누적합하면 되므로 순열 생성
    for perm in itertools.permutations(range(N), N):
        # 누적합 초기값 설정
        prefix = 0
        # 생성한 순열(인덱스값) 기반으로 순회하며 누적합
        for i in range(N):
            prefix += arr[i][perm[i]]

        # 누적합이 min값보다 작을 경우 갱신
        if prefix < min_prefix:
            min_prefix = prefix

    print(min_prefix)






    # print(f'#{tc} {result}')


