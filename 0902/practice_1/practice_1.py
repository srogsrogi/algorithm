import sys
sys.stdin = open('input.txt')

T = input()

for i in range(0, len(T), 7):
    bin_num = (T[i:i+7])
    print(int(bin_num, 2), end=' ')







    # print(f'#{tc} {result}')