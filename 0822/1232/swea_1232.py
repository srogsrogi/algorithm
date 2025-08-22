import sys
sys.stdin = open('input.txt')


def calc(node_index):
    # len == 2면 leaf node
    if len(tree_info[node_index]) == 2:

        return float(tree_info[node_index][1])

    # len != 2면 leaf node가 아니므로 추가 연산 필요
    else:
        # 뒤쪽 두 개 값은 각각 왼쪽/오른쪽 노드의 index
        left_idx = int(tree_info[node_index][2])
        right_idx = int(tree_info[node_index][3])

        # index값으로 재귀
        left = calc(left_idx)
        right = calc(right_idx)

        # index 1번 자리는 연산자가 있음
        operator = tree_info[node_index][1]
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            return left / right


T = 10

for tc in range(1, T+1):
    N = int(input())
    # N+1 길이로 리스트 생성하고 맨 왼쪽 비워서 인덱스 맞추기
    tree_info = [[] for _ in range(N + 1)]

    for _ in range(N):
        node_input = input().split()
        # 0번 인덱스가 노드 인덱스이므로 tree_info의 그 자리에 값 저장
        tree_info[int(node_input[0])] = node_input

    result = int(calc(1))

    print(f'#{tc} {result}')

