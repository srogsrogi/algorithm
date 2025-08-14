import sys

sys.stdin = open("input.txt")


# def binary_search_iterative(end_page, target_page):
#     """반복문을 이용한 이진 탐색. 탐색 횟수를 반환."""
#     start = 1
#     end = end_page
#     count = 0
#
#     # 시작점이 끝점보다 작거나 같은 동안 계속 탐색
#     while start <= end:
#         # 1. 탐색 횟수 1 증가
#         count += 1
#         # 2. 중간값 계산
#         middle = (start + end) // 2
#
#         # 3. 중간값과 목표값 비교
#         if middle == target_page:
#             return count  # 목표를 찾았으므로 종료
#         # 목표가 중간보다 작으면, 끝 범위를 중간값으로 축소
#         elif middle > target_page:
#             end = middle
#         # 목표가 중간보다 크면, 시작 범위를 중간값으로 축소
#         else:
#             start = middle
#
#     return count
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     P, Pa, Pb = map(int, input().split())
#
#     # A와 B의 탐색 횟수 계산
#     count_a = binary_search_iterative(P, Pa)
#     count_b = binary_search_iterative(P, Pb)
#
#     # 결과 판정
#     winner = ""
#     if count_a < count_b:
#         winner = "A"
#     elif count_b < count_a:
#         winner = "B"
#     else:
#         winner = "0"
#
#     print(f"#{tc} {winner}")
#


def binary(pages, answer):
    start = 1
    end = pages
    count = 0

    while start <= end:
        count += 1
        middle = (start + end) // 2

        if middle == answer:
            return count

        elif middle > answer:
            end = middle - 1

        else:
            start = middle + 1

T = int(input())
for tc in range(T):
    P, Pa, Pb = list(map(int, input().split()))

    a_count = binary(P, Pa)
    b_count = binary(P, Pb)

    # print(a_count, b_count)

    if a_count == b_count:
        result = 0

    elif a_count > b_count:
        result = 'B'

    else:
        result = 'A'

    print(result)


arr = [3,2,5,1]

def selection_sort(arr):
    N = len(arr)
    for i in range(N):
        min_idx = i
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]

    return arr

def bubble_sort(arr):
    N = len(arr)
    for i in range(N):
        for j in range(N - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

r, c = 0

for d in range(4):
    nr = r + dr
    nc = c + dc

    if N > nr >= 0 and M > nc >= 0:
