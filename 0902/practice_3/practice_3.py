import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):


    # print(f'#{tc} {result}')

patterns_dict = {
    0: '001101',
    1: '010011',
    2: '111011',
    3: '110001',
    4: '100011',
    5: '110111',
    6: '001011',
    7: '111101',
    8: '011001',
    9: '101111'
}

