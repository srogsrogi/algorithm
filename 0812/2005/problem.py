import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    previous_row = [1]
    result_list = [1]
    for i in range(N):
        next_row = [1] + previous_row + [1]
        previous_row
        result_list.append(previous_row)

    print(result_list)

    # print(f'#{tc} {result}')