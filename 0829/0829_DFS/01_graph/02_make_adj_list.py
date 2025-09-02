import sys

sys.stdin = open('input.txt')


# --- 그래프 구성 (인접 리스트) ---
V, E = map(int, input().split())
edge_data = list(map(int, input().split()))

adj_list = [[0] for _ in range(V+1)]

for i in range(E):
    # 인접한 두 정점 저장
    n1, n2 = edge_data[i*2], edge_data[i*2+1]

    # 정점 n1번 리스트에 n2정점 추가, 반대로도 추가
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

print(adj_list)


# --- 결과 확인 ---
