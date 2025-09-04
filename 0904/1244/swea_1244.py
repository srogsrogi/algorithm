'''
최대 6자리의 수 N이 주어진다
공백을 두고 최대 10회의 교환 횟수 M이 주어진다
교환 횟수를 모두 사용하여 자릿수간 숫자를 일대일로 교환했을 때의 결과값을 극대화하라.

N-1 = M이면 모든 숫자를 내가 원하는 자리수에 넣을 수 있다.
그리고 짝수번의 교환 횟수가 남았거나 중복된 숫자가 있는 경우 제자리로 돌아올 수 있다.
홀수번의 교환 횟수가 남았으면서 중복된 숫자가 없는 경우 N번 실행 후 최적해에서 마지막 두 자리만 바꾼 것이 최적해가 된다.

그러므로 N-1 > M인 케이스는 완전탐색을 하고
N-1 <= M인 케이스는 직접 순회를 하지 않고 그냥 내림차순 sort해버린 다음
M - (N-1)이 홀수면서 중복된 숫자가 없는 경우에만 마지막 두 자리 인덱스를 바꿔준다.
'''

def switch(lst, num):
    for i in range(len(lst - 1)):
        for j in range(1, len(lst)):



import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N은 숫자배열, M은 교환 횟수
    N, M = list(map(int, input().split()))
    print(N, M)
    # 자리바꾸기 쉽게 리스트로 변환
    arr = list(str(N))



    # print(f'#{tc} {result}')