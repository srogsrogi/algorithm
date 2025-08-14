import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = []
    for r in range(N):
        row = list(map(int, (input())))
        arr.append(row)
    # arr = [[1, 4, 0, 5, 4], [4, 4, 2, 5, 0], [0, 2, 0, 3, 2], [5, 1, 2, 0, 4], [5, 2, 2, 1, 2]]

    # 중앙 행 index 구하기
    middle = N // 2

    # 수확량 누적합할 변수 설정
    harvest = 0

    # 중앙 포함, 위쪽 행에 대한 수확량 계산
    # 행인덱스는 중앙부터 위쪽으로 -1씩 올라감
    for i in range(middle, -1, -1):
        # 중앙과 계산할 행 사이의 거리
        d = middle - i
        # d부터 len - d까지의 범위를 열 index로 설정
        # len = N + 1이고 range는 끝 인덱스를 포함하지 않으므로
        # range(d, N-d)로 쓸 수 있음
        for j in range(d, N-d):
            # 칸별 수확량 순회하며 누적합
            harvest += arr[i][j]

    # 이번엔 k가 중앙부터 위쪽으로 1씩 올라감
    for k in range(middle + 1, N):
        # k가 middle보다 클테니 d도 k - middle로 계산
        d = k - middle
        # 범위 설정은 위쪽 계산할 때와 똑같이..
        for l in range(d, N-d):
            # 칸별 수확량 순회하며 누적합
            harvest += arr[k][l]

    print(f'#{tc} {harvest}')