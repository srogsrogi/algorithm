'''
뒤엣놈이 큰놈..
일단 첫 조합을 배열에 넣고 조합을 하나씩 대볼건데
- 작은놈(0번인덱스)이 배열의 제일 큰놈과 같으면: 오른쪽에 다른 원소가 없으면 해당 조합의 1번인덱스를 append
- 작은놈(0번인덱스)이 배열의 제일 큰놈보다 크면: 해당 조합의 0번 1번 인덱스를 차례로 append
- 큰놈(1번인덱스)이 배열의 제일 작은놈과 같으면: 왼쪽에 다른 원소가 없으면 해당 조합의 0번인덱스를 appendleft
- 큰놈(1번인덱스)이 배열의 제일 작은놈보다도 작으면: 해당 조합의 1번 0번 인덱스를 차례로 appendleft
다 하고 나면 배열에 들어간 애들은 확실하게 정렬된 거고, 여기다 남은 애들만 어떻게 낑겨넣으면 안되나..
'''

from collections import deque
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    M = int(input())
    arr = [list(map(int, input().split())) for row in range(M)]

    # 오름차순 키순 정렬할 리스트
    tall_deque = deque(arr[0])
    # 0번조합은 이미 넣었으니까 제외
    for i in range(1, len(arr)):
        # 새 조합의 작은놈이 정렬배열에서 제일 큰 놈인 경우
        if arr[i][0] == tall_deque[-1]:
            tall_deque.append(arr[i][1])
        # 새 조합의 작은 놈이 정렬배열에서 제일 큰 놈보다도 더 큰 경우
        if arr[i][0] > tall_deque[-1]:
            tall_deque.append(arr[i][0])
            tall_deque.append(arr[i][1])
        # 새 조합의 큰 놈이 정렬배열에서 제일 작은 놈보다도 작은 경우
        if arr[i][1] < tall_deque[0]:
            tall_deque.appendleft(arr[i][1])
            tall_deque.appendleft(arr[i][0])
        # 새 조합의 큰 놈이 정렬배열에서 제일 작은 놈인 경우
        if arr[i][1] == tall_deque[0]:
            tall_deque.appendleft(arr[i][0])

    print(tall_deque)

# 아 망한거같음