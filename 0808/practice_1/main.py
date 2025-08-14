import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):

    # 방법 1 : reverse 내장함수 사용
    word = input()
    # reverse함수는 이터레이터를 반환하므로 join함수를 사용하여 str로 변환
    reversed_word = ''.join(reversed(word))
    print(reversed_word)

    # 방법 2 : list 변환하여 in-place 연산
    # 입력값을 각 문자를 요소로 하는 list로 받아옴
    # lst = list(input())
    #
    # 리스트 절반까지 순회하며 자리 바꾸기
    # for i in range(len(lst) // 2):
    #     lst[i], lst[-(i+1)] = lst[-(i+1)], lst[i]
    #
    # 다시 문자열로 변환
    # result = ''.join(lst)
    # print(f'#{tc + 1} {result}')