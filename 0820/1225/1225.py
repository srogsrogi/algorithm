from collections import deque
import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    # 배열(리스트)로 입력
    arr = list(map(int, input().split()))

    # deque객체 만들기
    queue = deque()

    # 배열 순회하며 deque에 append
    for elem in arr:
        queue.append(elem)

    # 뺄 값(1~5) 초기값 지정
    val = 1

    # append한 후 마지막 숫자가 0 이하가 될 때까지 반복
    while queue[-1] > 0:
        # val이 1씩 증가하다가 6이 되면 다시 1로 초기화
        if val > 5:
            val = 1

        # 왼쪽에서 dequeue
        popped = queue.popleft()
        # val만큼 뺀 후
        popped -= val
        # 오른쪽에 enqueue
        queue.append(popped)

        # 뺄 값 올려주기
        val += 1

    # 마지막 숫자가 음수일 수도 있으므로 0으로 보정
    queue[-1] = 0

    # join 메서드 사용을 위해 각 요소 str로 변환
    for i in range(len(queue)):
        queue[i] = str(queue[i])

    # 입력형식에 맞게 변환
    result = ' '.join(queue)

    print(f'#{tc} {result}')