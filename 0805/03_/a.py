import sys
sys.stdin = open('input.txt')

# 테스트 케이스 수


T = int(input())

for _ in range(T):
    # 한 번에 이동할 수 있는 최대 정류장 수, 종점, 충전가능 정류장 수
    K, N, M = map(int, input().split())
    # 충전 가능한 정류장 리스트
    can_charge = list(map(int, input().split()))

    # print(K, N, M, can_charge)

