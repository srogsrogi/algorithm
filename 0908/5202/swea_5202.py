import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = []
    for i in range(N):
        plan = list(map(int, input().split()))
        arr.append(plan)
    # 끝나는 시간순 정렬
    arr.sort(key= lambda x: x[1])

    # 작업 추가할 리스트 초기화
    works = []

    # 추가된 작업이 하나도 없는 경우 조건 없이 추가
    # 끝나는 시간이 가장 빠른 작업이 리스트 맨 앞에 있음
    for work in arr:
        if not works:
            works.append(work)
        else:
            # 이전 작업의 종료시보다 다음 작업의 시작시가 늦는 경우 추가
            if work[0] >= works[-1][1]:
                works.append(work)

    # 리스트 길이 == 배정된 작업 수
    count = len(works)

    print(f'#{tc} {count}')