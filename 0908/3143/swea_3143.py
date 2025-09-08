import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    A, B = input().split()

    # B 횟수, 인덱스 변수 초기화
    count = 0
    i = 0
    # 순회하지 않은 문자열 길이가 B보다 작아질 때까지 순회
    while i <= len(A) - len(B):
        # A 순회하면서 B 만나면 만난 횟수 1 증가시키고 인덱스 B의 길이만큼 이동
        if A[i:i+len(B)] == B:
            i += len(B)
            count += 1
        # B 못 만나면 인덱스 1씩 이동
        else:
            i += 1

    # B를 한 번 만날 때 줄어드는 타이핑 수는 len(B) - 1
    result = len(A) - count * (len(B) - 1)

    print(f'#{tc} {result}')