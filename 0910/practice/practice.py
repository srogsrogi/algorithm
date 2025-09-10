import sys
sys.stdin = open('input.txt')


def partition(arr, start, end):
    # 맨 뒤에 pivot 놓기
    pivot = arr[end]
    # 맨 앞 - 1에 i 놓기
    i = start - 1

    for j in range(start, end):
        # j가 순회하면서, pivot보다 작은 값은 왼쪽, 큰 값은 오른쪽으로 몰아넣기
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # i, j 위치 바꾸기
    arr[i+1], arr[end] = arr[end], arr[i+1]

    # pivot이 들어갈 인덱스 반환
    return i + 1


def quick_sort(arr, start, end):
    if start < end:
        pivot_idx = partition(arr, start, end)

        # 양쪽으로 분할해나가며 재귀
        quick_sort(arr, start, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, end)


T = int(input())

for tc in range(1, T+1):
    lst = list(map(int, input().split()))

    quick_sort(lst, 0, len(lst) - 1)

    print(f'#{tc} {" ".join(map(str, lst))}')