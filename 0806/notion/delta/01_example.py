# arr의 중앙값 5의 위치 (1, 1)에서 상하좌우 값을 출력해 봅시다.
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 기준점
r = 1
c = 1

for i in range(4):
    new_r = r + dr[i]
    new_c = c + dc[i]
    print(arr[new_r][new_c])