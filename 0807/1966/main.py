import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

#     # 선택 정렬
#     for i in range(N-1):
#         # 안쪽 반복문이 돌 때마다 기준값을 해당 회차의 첫 인덱스로 설정
#         min_idx = i
#         for j in range(i+1, N):
#             # 비교한 값이 더 작으면 최소값 index 갱신
#             if arr[min_idx] > arr[j]:
#                 min_idx = j
#         # 끝까지 순회한 후 원본 arr의 i번째 자리에 최소값 넣기
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]

    # 버블 정렬
    for i in range(N):
        for j in range(N-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    # 출력형식 맞추기
    result = ' '.join(map(str, arr))

    print(f'#{tc + 1} {result}')