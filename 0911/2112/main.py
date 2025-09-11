'''
D*W 배열에 0 또는 1 값이 있음
모든 W에 대해 D방향으로 연속된 K개의 0 또는 1이 있어야 함
약품을 투입하면 한 행(D)의 모든 값을 0 또는 1로 바꿀 수 있음
조건을 만족시키는 최소 약품투입횟수 출력


'''

import sys
sys.stdin = open('input.txt')


# 검사 함수
def test(arr, D, W, K):
    # 열 단위로 검사
    for j in range(W):
        # 연속된 0과 1을 각각 count해서 하나라도 K가 되면 True 찍고 반환
        # 끝까지 K가 안 되면 False 반환
        count_0 = 0
        count_1 = 0
        passed = False

        # 행 순회
        for i in range(D):
            # 0이나 1이 나오면 해당 숫자 count는 올리고 다른 놈은 불연속이니까 0으로 초기화
            if arr[i][j] == 0:
                count_0 += 1
                count_1 = 0
            # count가 K에 도달했으면 해당 열은 일단 pass
            if count_0 == K:
                passed = True
                break

            if arr[i][j] == 1:
                count_1 += 1
                count_0 = 0
            if count_1 == K:
                passed = True
                break

        # 한 열이라도 pass 못 하면 바로 False 반환,
        if not passed:
            return False

    # 다 돌고도 False로 간 적 없으면 True 반환
    return True


T = int(input())

for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for row in range(D)]

    # 하..


    # print(f'#{tc} {result}')