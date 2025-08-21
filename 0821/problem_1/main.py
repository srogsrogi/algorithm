import sys
import itertools

sys.stdin = open('input.txt')

T = int(input())


# 3개의 숫자가 든 리스트를 입력받아 triplet 여부 반환
def is_triplet(numbers):
    if numbers[0] == numbers[1] == numbers[2]:
        return True


# 3개의 숫자가 든 리스트를 입력받아 run 여부 반환
def is_run(numbers):
    if numbers[0] + 1 == numbers[1] and numbers[1] + 1 == numbers[2]:
        return True


for tc in range(1, T+1):
    arr = list(map(int, input().strip()))

    # 순서 섞어서도 조건 확인할 수 있으므로 길이 6인 순열 생성
    perm = list(itertools.permutations(arr, 6))

    # babygin 여부 기본값 0
    is_baby_gin = 0

    # 만든 순열 순회
    for p in perm:

        # 앞쪽 3개가 triplet이면
        if is_triplet(p[:3]):
            # 뒤쪽 3개가 triplet인지 확인하고, 맞으면 baby-gin
            if is_triplet(p[3:]):
                is_baby_gin = 1
            # 뒤쪽 3개가 run인지 확인하고, 맞으면 baby-gin
            elif is_run(p[3:]):
                is_baby_gin = 1

        # 앞쪽 3개가 run이면
        elif is_run(p[:3]):
            # 뒤쪽 3개가 triplet인지 확인하고, 맞으면 baby-gin
            if is_triplet(p[3:]):
                is_baby_gin = 1
            # 뒤쪽 3개가 run인지 확인하고, 맞으면 baby-gin
            elif is_run(p[3:]):
                is_baby_gin = 1

    print(f'#{tc} {is_baby_gin}')