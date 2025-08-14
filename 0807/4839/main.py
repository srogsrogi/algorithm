import sys

sys.stdin = open('input.txt')


def binary_search(pages, number):
    '''책 페이지수와 찾을 페이지를 입력받아
    해당 페이지를 찾는데 필요한 이진탐색 시행횟수를
    반환하는 함수입니다.
    '''
    # 이진탐색의 시작과 끝값 설정
    start = 1
    end = pages

    # 시행횟수 초기화
    count = 0

    # 이진탐색 base 코드. 책 페이지는 정수범위 내에서 연속적이기 때문에 입력값에 오류가 없으면 else구문은 필요하지 않음
    while start <= end:
        middle = (start + end) // 2
        if middle == number:
            count += 1
            # 답을 맞혔을 때만 빠져나가기
            break

        # 찾으려는 책 페이지가 탐색한 값보다 큰 경우
        elif middle > number:
            end = middle - 1
            count += 1

        # 찾으려는 책 페이지가 탐색한 값보다 작은 경우
        else:
            start = middle + 1
            count += 1

    return count


T = int(input())

for tc in range(T):
    p, a, b = map(int, input().split())

    # 함수 반복 호출하여 count_a와 count_b 할당
    count_a = binary_search(p, a)
    count_b = binary_search(p, b)

    # count가 적은 쪽이 승리, 같으면 0
    if count_a > count_b:
        winner = 'B'
    elif count_a == count_b:
        winner = 0
    else:
        winner = 'A'

    print(f'#{tc + 1} {winner}')