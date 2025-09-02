import sys

sys.stdin = open('input.txt')


# --- 그래프 구성 (인접 행렬) ---
# 정점과 간선의 개수
V, E = map(int, input().split())
edge_data = list(map(int, input().split()))

# 행렬의 첫 인덱스 비우고 만들기
adj_matrix = [[0]*(V+1) for _ in range(V+1)]
print(adj_matrix)
ㅊ
# 간선정보를 바탕으로 2개씩 짝지어서 인접행렬 표기
# 총 표기 횟수는 간선 개수(E)
for i in range(E):
    # 정점의 번호 -> 인접행렬의 index 값
    n1, n2 = edge_data[i*2], edge_data[i*2+1]
    # 무향 그래프이므로 양방향 모두 연결
    adj_matrix[n1][n2], adj_matrix[n2][n1] = 1, 1


for row in adj_matrix:
    print(row)
# --- 결과 확인 ---
