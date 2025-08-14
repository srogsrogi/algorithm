import sys
sys.stdin = open('input.txt')

def find_palindrome_in_row(matrix_size, length, matrix):
    '''가로방향의 회문을 찾는 함수입니다. 찾은 회문 전부를 리스트에 담아 반환합니다.
    입력값 1 : 전체 배열 크기
    입력값 2 : 회문 여부를 탐색할 문자열의 길이
    입력값 3 : 탐색할 배열
    '''
    # 찾은 회문들을 담을 리스트
    lst = []

    # 행렬 가로(=세로)길이만큼 반복
    for j in range(N):
        # 벽에 안 부딛히려면 배열길이 - 문자열 길이 + 1까지만 반복해야 함
        for k in range(N-M+1):
            # 문자열과 뒤집은 문자열 정의
            chars = matrix[j][k:k+M]
            reversed_chars = chars[::-1]
            # 둘이 같으면 회문이니까 리스트에 append
            if chars == reversed_chars:
                lst.append(chars)
    # 찾은 회문들이 있는 리스트 반환
    return lst

T = int(input())

for tc in range(T):
    char_matrix = []
    N, M = map(int, (input().split()))
    for i in range(N):
        temp = input()
        char_matrix.append(temp)
    # print(N, M, matrix)

    # 전치행렬 만들기
    # 함수는 가로방향 회문만 검사하므로 전치한 후 같은 함수를 사용해서 세로방향 회문도 탐색
    transposed = [''.join(col) for col in zip(*char_matrix)]

    # 가로방향 회문과 세로방향 회문 각각 정의
    palindrome_in_row = find_palindrome_in_row(N, M, char_matrix)
    palindrom_in_col = find_palindrome_in_row(N, M, transposed)

    # 배열 전체에 회문이 하나 밖에 없다고 가정하고(문제 조건)
    # result에 정답 할당
    if palindrome_in_row:
        result = palindrome_in_row[0]
    else:
        result = palindrom_in_col[0]

    print(f'T{tc + 1} {result}')