import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # 두 수를 곱한 모든 경우의 수를 담을 리스트
    multiplied = []
    for i in range(N):
        for j in range(i+1, N):
            multiplied.append(numbers[i] * numbers[j])
    # multiplied = [8, 14, 20, 28, 40, 70]

    # multiplied의 각 요소가 단조증가하는지 여부를 담을 리스트
    list_is_increasing = []

    # multiplied의 요소 순회
    for elem in multiplied:
        # 각 자리수를 순회하기 위해 시퀀스인 문자열로 변환
        chars = str(elem)

        # 기본값 True 설정
        is_increasing = True

        # len(chars)까지 비교하면 마지막에 비교할 요소 하나가 없으므로 -1
        for k in range(len(chars) - 1):

            # int로 변환하지 않은 문자열 상태로도 크기 비교 가능
            # 앞 숫자가 더 크면 단조증가하지 않으므로 False로 갱신하고 break
            if chars[k] > chars[k+1]:
                is_increasing = False
                break

        # 단조증가하는지 여부 append
        list_is_increasing.append(is_increasing)

    # list_is_increasing = [True, True, False, True, False, False]

    # multiplied의 요소 중 단조증가하는 수만 담을 리스트
    list_increasing_numbers = []

    # multiplied랑 list_is_increasing이랑 배열 구조와 index가 같으니까..
    # list_is_increasing이 True인 multiplied의 요소들만 리스트에 추가
    for m in range(len(multiplied)):
        if list_is_increasing[m]:
            list_increasing_numbers.append(multiplied[m])

    # 최대값만 출력
    result = max(list_increasing_numbers)


    print(f'#{tc} {result}')