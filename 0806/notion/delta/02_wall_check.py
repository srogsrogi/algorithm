N = 3
M = 3

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 기준점
r = 1
c = 1
for i in range(N):
    nr = r + dr[i]
    nc = c + dc[i]

    if 0 <= nr < N and 0 <= nc < M:
        print(arr[nr][nc])