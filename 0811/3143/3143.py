import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    # 문자열 입력
    # str_1이 긴 문자열, str_2가 패턴
    str_1, str_2 = input().split()
    # 각 문자열 길이 계산
    M = len(str_1)
    N = len(str_2)

    # i는 index를 의미하면서 while문의 종료조건
    # count는 패턴 등장 횟수
    i = 0
    count = 0

    # (i + N - 1) <= (M - 1)이어야 하므로 i <= M - N
    while i <= M - N:
        # 슬라이딩 윈도우 방식으로 탐색
        if str_1[i : i + N] == str_2:
            # 패턴 등장횟수 += 1
            count += 1
            # 패턴의 길이만큼 인덱스 이동
            i += N
        # 패턴을 못 찾은 경우 인덱스 1만 이동
        else:
            i += 1

    # 패턴 1개당 줄어드는 입력 수 : {패턴의 길이 - 1}
    # 문자열 길이에서 {패턴 발견 횟수 * 패턴 1개당 줄어드는 입력 수}를 빼면 총 입력 횟수 산출
    result = M - count * (N - 1)

    print(f'#{tc + 1} {result}')