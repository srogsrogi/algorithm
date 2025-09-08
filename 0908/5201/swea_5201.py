import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N : 컨테이너 수, M : 적재용량
    weights = list(map(int, input().split()))
    capacities = list(map(int, input().split()))

    # 무게와 적재용량 내림차순 정렬
    weights.sort(reverse=True)
    capacities.sort(reverse=True)

    # 총 적재용량 초기화
    sum_weight = 0

    # 이미 실은 컨테이너 제외하기 위한 set
    container_selected = set()
    # 트럭 수 만큼 순회
    for i in range(len(capacities)):
        # 컨테이너 수 만큼 순회
        for j in range(N):
            # 적재용량이 무게보다 크면서, 이미 싣지 않은 컨테이너 찾기
            if capacities[i] >= weights[j] and j not in container_selected:
                # 총 적재용량 재연산
                sum_weight += weights[j]
                # 실은 컨테이너 set 업데이트
                container_selected.add(j)
                # 실었으면 해당 반복회차 스킵
                break

    print(f'#{tc} {sum_weight}')