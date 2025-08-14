import sys

sys.stdin = open('input.txt')

# 테스트 케이스 수 입력
T = int(input())

# 케이스 수만큼 순회
for i in range(T):
    # 개별 테스트 케이스에서 정수의 개수
    N = int(input())

    numbers = list(map(int, input().split()))

    for j in range(N-1):
        for k in range(N-1-j):
            # 왼쪽 수가 더 큰 경우 자리바꾸기 -> 오름차순
            if numbers[k] > numbers[k+1]:
                numbers[k], numbers[k+1] = numbers[k+1], numbers[k]
    # 각 테스트케이스별 순회가 끝난 후 min, max 할당
    min_val = numbers[0]
    max_val = numbers[N-1]
    # 두 수의 차 계산
    result = max_val - min_val

    print(f'#T{i+1} {result}')