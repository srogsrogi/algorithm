'''
N*N 벌통 배열에서
일꾼 둘이 가로 방향으로 길이 M만큼 벌통 선택
서로 겹치는 벌통이 있으면 안 됨
각자 선택한 벌통 묶음에서 누적합이 C 이하인 선에서 원하는 만큼의 벌통을 선택하여 수익(각 벌통의 값^2의 누적합)을 극대화하라.

일꾼 1이 선택할 수 있는 길이 M의 벌통 조합(2중 for문)
일꾼 2가 선택할 수 있는 길이 M의 벌통 조합(2중 for문). 일꾼 1이 이미 탐색한 조합들은 제외
각 일꾼이 고를 수 있는 부분집합(<C 조건 검사)에 대하여 완전탐색. 적당히 가지치기는 필요해 보이는데... 어떡하지?
최대값 둘이 더해서 전체 최대값 갱신


'''


import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for r1 in range(N-M+1):
        for c1 in range(N):
            for r2 in range(r1, )





    # print(f'#{tc} {result}')