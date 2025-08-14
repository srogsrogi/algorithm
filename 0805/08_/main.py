import sys
sys.stdin = open('input.txt')

# 테스트 케이스 수
T = int(input())
# 테스트 케이스만큼 순회
for _ in range(T):
    # 입력될 정수 개수
    N = int(input())
    # 공백 없는 문자열로 정수 N개 입력 -> 리스트화
    numbers = list(map(int, input().strip()))

    # count는 연속된 1의 개수. 0이 나오면 그 때까지의 count를 count_list에 담고 count = 0으로 초기화
    count_list = []
    count = 0
    # 정수 리스트 순회
    for i in range(len(numbers)):
        # 끝 인덱스를 순회하는 경우
        if i == len(numbers) - 1:
            # 1이면 count += 1, 0이면 아무 것도 안 함
            if numbers[i] == 1:
                count += 1
            # list에 append
            count_list.append(count)
        # 끝 인덱스가 아니면서 정수값이 0인 경우
        elif numbers[i] == 0:
            # 그 전까지 쌓인 count를 list에 append하고 count 초기화
            count_list.append(count)
            count = 0
        # 끝 인덱스가 아니면서 정수값이 1인 경우
        elif numbers[i] == 1:
            # count += 1 하고 다음 반복
            count += 1
    # 쌓인 count_list에서 가장 큰 값 출력
    print(f'#{_+1} {max(count_list)}')