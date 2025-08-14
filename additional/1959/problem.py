import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr_1 = list(map(int, input().split()))
    arr_2 = list(map(int, input().split()))

    # arr_2가 더 길게 조정
    if len(arr_1) > len(arr_2):
        arr_1, arr_2 = arr_2, arr_1

    # 길이 변수 할당(N > M)
    M = len(arr_1)
    N = len(arr_2)

    # shift별 누적합 넣을 리스트
    list_prefix_sum = []

    for i in range(N-M+1):
        # shift별 누적합 초기화
        prefix_sum = 0
        for j in range(M):
            # 슬라이딩 윈도우로 기준인덱스 옮겨가며 누적합 연산
            prefix_sum += arr_2[i+j] * arr_1[j]
        # 누적합 구한거 list에 append
        list_prefix_sum.append(prefix_sum)
    # shift별 누적합 리스트에서 max값 추출
    result = max(list_prefix_sum)

    print(f'#{tc} {result}')