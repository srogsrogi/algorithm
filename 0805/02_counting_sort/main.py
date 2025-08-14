import sys
sys.stdin = open('input.txt')
# 테스트 케이스 수
T = int(input())
# 테스트 케이스만큼 순회
for _ in range(T):
    # N(입력되는 정수 개수), M(합연산할 범위) 입력 -> 리스트화
    N, M = list(map(int, input().split()))
    # N개의 정수 입력 -> 리스트화
    numbers = list(map(int, input().split()))
    # 합연산 결과 리스트 초기화
    list_sum_numbers = []

    for i in range(N-M+1):
        # 합연산값 초기화
        sum_numbers = 0
        for j in range(M):
            # 슬라이딩 윈도우 : 바깥 반복문이 돌 때마다 시작 인덱스가 1씩 옮겨감
            sum_numbers += numbers[i+j]
        # 합연산값 리스트에 append
        list_sum_numbers.append(sum_numbers)
    # 합연산값 리스트에서 max - min 계산
    diff = max(list_sum_numbers) - min(list_sum_numbers)
    # max - min 출력
    print(f'#{_+1} {diff}')