import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    number = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_val = 0

    for i in range(100):
        prefix_row = 0
        prefix_col = 0
        prefix_diagonal = 0
        for j in range(100):
            prefix_row += arr[i][j]
            prefix_col += arr[j][i]
            prefix_diagonal += arr[j][j]

            if prefix_row > max_val:
                max_val = prefix_row
            if prefix_col > max_val:
                max_val = prefix_col
            if prefix_diagonal > max_val:
                max_val = prefix_diagonal


    result = max_val

    print(f'#{tc} {result}')