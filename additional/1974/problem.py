import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 빈 배열 생성
    arr = []

    # result 기본값 1, 조건에 부합하지 않는 경우 0으로 갱신
    result = 1

    # 9 * 9 행렬 만들기
    for i in range(9):
        row = list(map(int, input().split()))
        arr.append(row)

    # 원본 배열의 행을 순회하며 set 길이가 9인지 검사
    # 9번 add했으므로 중복이 없었다면 길이가 9여야 함
    for r in arr:
        if len(set(r)) != 9:
            result = 0

    # 전치행렬 만들기
    transposed = list(map(list, zip(*arr)))

    # 전치된 배열의 행을 순회하며 set 길이가 9인지 검사
    # 전치된 배열의 행 == 원래 배열의 열
    for r in transposed:
        if len(set(r)) != 9:
            result = 0

    # 3 * 3 구역 만들기
    indices = [0, 3, 6]
    for r_idx in indices:
        for c_idx in indices:
            # 중복 여부 확인을 위한 set
            unique_numbers = set()
            # 인덱스 3씩 이동하며 3 * 3 범위 지정
            for k in range(r_idx, r_idx+3):
                for l in range(c_idx, c_idx+3):
                    # set에 add(중복인 경우 추가되지 않음)
                    unique_numbers.add(arr[k][l])

    # 3 * 3 구역별 원소도 set에 담아 길이가 9인지 검사
            if len(unique_numbers) != 9:
                result = 0

    print(f'#{tc} {result}')