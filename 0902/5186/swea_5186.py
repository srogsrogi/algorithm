import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 입력값 실수로 받기
    n = float(input())
    # 이진수 변환해서 담을 리스트
    binary = []

    # 14부터는 overflow로 처리할 거니까 14번 루프
    for i in range(14):ㅊ
        # 매 루프 남아있는 부분(소수부)에 2를 곱해서 1보다 크면 그 때 비트는 1, 아니면 0
        n *= 2
        bit = int(n)
        binary.append(bit)
        # 비트가 1이 됐을 때 1을 빼서 소수부만 남겨주고 반복
        n -= bit
        # n이 0이 되면 계산 끝, 아니면 14자리까지 쭉 진행
        if n == 0:
            break

    # 14자리 이하면 그대로 출력, 14자리까지 있으면 overflow
    if len(binary) < 14:
        result = ''.join(str(x) for x in binary)
    else:
        result = 'overflow'

    print(f'#{tc} {result}')