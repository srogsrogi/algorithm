import sys
sys.stdin = open('input.txt')

# 테스트 케이스 수 입력
T = int(input())

# 모든 테스트 케이스 순회
for tc in range(T):
    # 색칠할 직사각형 수 입력
    N = int(input())
    # 흰색 10*10 배열 생성
    # 흰색 : 0, 빨간색 : 1, 파란색 : 2, 보라색 : 3
    color_array = [[0] * 10 for _ in range(10)]
    # 색칠할 정사각형 수만큼 순회
    for i in range(N):
        # 좌표와 색상값을 가지고 있는 입력값 unpack
        x1, y1, x2, y2, color = (map(int, input().split()))

        # 보라색 셀 count 초기화
        count = 0
        # range의 end값은 포함하지 않으므로 좌표값에 + 1
        for r in range(x1, x2 + 1):
            for c in range(y1, y2 + 1):
                # 현재 색과 칠해질 색이 같은 경우 경우 아무 일도 일어나지 않음
                # 현재 색과 칠해질 색이 다른 경우 color값 합연산
                if color_array[r][c] != color and color_array[r][c] != 3:
                    color_array[r][c] += color
                # 보라색이면 count += 1
                # 보라색에 다른 색이 덧칠되는 경우 color값이 3을 초과하여 올라가기 때문에 더이상 count되지 않음
                if color_array[r][c] == 3:
                    count += 1

    print(f'#{tc + 1} {count}')