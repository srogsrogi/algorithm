import sys
sys.stdin = open('input.txt')


# 단조증가여부 판별 함수
def is_monotone(num):
    # 인덱싱을 위해 str 변환
    str_num = str(num)
    # 단조증가여부 초기화
    monotone = True
    # 다음 인덱스의 숫자와 비교할 것이므로 len()-1 범위에서 반복
    for k in range(len(str_num) - 1):
        # 다음 인덱스의 숫자와 비교해서 단조증가하지 않는 경우가 있으면 False 바로 반환
        if str_num[k] > str_num[k+1]:
            monotone = False
            return monotone
    # 전부 단조증가했으면 True 반환
    return monotone


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    multiplied = []

    # 2중 for문으로 순회하며 모든 곱 연산하여 리스트에 담음
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            multiplied.append(arr[i] * arr[j])

            # 곱해진 수 중 단조증가하는 수만 다시 리스트에 담음
            monotones = [num for num in multiplied if is_monotone(num)]
            # 단조증가하는 수가 하나라도 있으면 그 중 최대값 검색
            if monotones:
                result = max(monotones)
            # 하나도 없으면 문제 조건에 따라 -1
            else:
                result = -1

    print(f'#{tc} {result}')