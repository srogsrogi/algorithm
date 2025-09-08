import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    now = 0
    count = 0

    # 도착지까지 갈 수 있을 때까지 반복
    while now + K < N:
        # 다음 이동위치 일단 현재위치로 초기화
        next_position = now
        # 충전 가능한 정류소 순회
        for station in arr:
            # 정류소가 현재 위치보다는 뒤에 있고, 현재 위치에서 갈 수 있는 최대 거리보다는 작거나 같아야 함
            if now < station <= now + K:
                # 이동
                # 앞에서 뒤로 여러 번 순회하므로, 더 멀리 있는 정류소에 갈 수 있는 경우 한 번에 이동함
                next_position = station

        # 이동이 불가해서 가만히 있는 경우 문제 조건에 따라 0 출력
        if next_position == now:
            count = 0
            break

        # 이동했으니 현위치 바꾸고 count 증가 후 다시 반복
        now = next_position
        count += 1

    print(f'#{tc} {count}')