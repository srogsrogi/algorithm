'''
남학생(sex==1)은 num의 배수에 해당하는 모든 스위치의 상태를 바꾼다.
여학생(sex==2)은 num의 좌우로 한 칸씩 탐색해나가며 좌우 스위치의 상태가 같은 동안 스위치 상태를 모두 바꾼다.
한 칸만 탐색해도 좌우 스위치 상태가 다르면, num번째 스위치 상태만 바꾼다. 즉, num번쨰 스위치는 항상 바뀐다.
모든 학생이 순서대로 규칙을 수행했을 때 최종 상태를 출력하라.
한 줄에 최대 20개까지 스위치 상태를 출력하고 구분자는 공백문자로 한다.
'''

import sys
sys.stdin = open('input.txt')

N = int(input()) # 스위치 개수
arr = list(map(int, input().split())) # 각 스위치 상태
M = int(input()) # 학생 수

# print(N,M)
students = []
for i in range(M):
    sex, num = map(int, input().split())
    students.append([sex, num])

    # 남학생
    if students[i][0] == 1:
        # 스위치 수/가진 수의 몫까지 순회
        # index와 '번째'를 맞추기 위해 이하 모든 인덱스에 -1
        for j in range(1, N//num + 1):
            # num의 배수가 0이면 1로, 1이면 0으로 토글
            if arr[j * num - 1] == 0:
                arr[j * num - 1] = 1
            else:
                arr[j * num - 1] = 0
    # 여학생
    else:
        # num 자리는 무조건 바꿈
        if arr[num - 1] == 0:
            arr[num - 1] = 1
        else:
            arr[num - 1] = 0

        k = 1
        # num 기준 좌/우 범위 벗어나지 않도록 범위설정
        while num - k - 1 >= 0 and num + k - 1 < N:
            # 양쪽 다르면 바로 break
            if arr[num - k - 1] != arr[num + k - 1]:
                break
            # 양쪽 같으면 토글
            else:
                if arr[num - k - 1] == 0:
                    arr[num - k - 1], arr[num + k - 1] = 1, 1
                else:
                    arr[num - k - 1], arr[num + k - 1] = 0, 0
            # 토글 후 탐색 인덱스 증가
            k += 1

# 출력형식 맞추기
for l in range(N):
    print(arr[l], end = ' ')
    if (l+1) % 20 == 0:
        print()