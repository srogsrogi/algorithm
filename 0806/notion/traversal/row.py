# 예시: 1부터 9까지 숫자를 3x3 형태로 담은 리스트

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# 행의 수
N = len(arr)

# 열의 수
M = len(arr[0])


# 행 우선 순회
for r in range(N):
    for c in range(M):
        print(arr[r][c], end = ' ')