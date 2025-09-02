import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 16진수 문자열 입력
    hex_num = input()

    # 10진수 변환
    decimal_num = int(hex_num, 16)
    # 2진수 변환. 변환시 생략되는 앞자리수 0을 다시 패딩
    bin_num = bin(decimal_num)[2:].zfill(len(hex_num) * 4)

    # 인덱스를 7씩 이동시키며 7비트 2진수를 10진수로 변환
    start_idx = 0
    result = []
    while start_idx < len(bin_num):
        chunk = bin_num[start_idx:start_idx+7]
        # 문제 조건대로, 0000000일 때만 append하지 않고 자리수 4만큼 이동
        if chunk == '0000000':
            start_idx += 4

        else:
            result.append(int(chunk, 2))
            start_idx += 7

    print(f'#{tc}', *result)
