from collections import deque
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 배열로 입력받기
    arr = list(map(int, input().split()))

    # queue 객체 생성
    queue = deque()

    # 배열의 요소를 순회하며 queue에 append
    # 배열의 요소와 queue의 요소가 같아짐
    for elem in arr:
        queue.append(elem)

    # 왼쪽에서 dequeue, 오른쪽에 enqueue M번 반복
    for i in range(M):
        popped = queue.popleft()
        queue.append(popped)

    # 맨 왼쪽 요소 반환
    result = queue[0]

    # 출력
    print(f'#{tc} {result}')