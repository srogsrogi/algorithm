import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 문제 조건에 따라 증가하는 경우가 없어도 1이므로 1로 초기화
    count = 1
    best = 1
    # 이전 수와 비교하기 위해 1부터 시작
    # 0번 인덱스에는 뭐가 있어도 이미 count = 1로 처리돼있음
    for i in range(1, len(arr)):
        # 이전 인덱스의 값과 비교하여 새 값이 더 큰 경우에만 count 증가
        if arr[i] > arr[i-1]:
            count += 1
            # count가 초기화된 경우 갱신당하지 않기 위해 best와 count 중 최대값으로 갱신
            best = max(best, count)
        else:
            # 단조증가하지 않았으면 count 초기화
            count = 1

    print(f'#{tc} {best}')