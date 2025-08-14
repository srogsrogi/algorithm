import sys
sys.stdin = open('input.txt')

T = int(input())

# dict로 문자열과 숫자 매핑
dict_numbers = {'ZRO' : 0, 'ONE' : 1, 'TWO' : 2, 'THR' : 3, 'FOR' : 4, 'FIV' : 5, 'SIX' : 6, 'SVN' : 7, 'EGT' : 8, 'NIN' : 9}

for tc in range(T):
    # 테스트케이스 번호와 문자열 개수 입력
    tc_num, length = input().split()
    # 문자열 개수만 int 변환
    length = int(length)
    # 문자열로 된 숫자 리스트 생성
    numbers = input().split()

    # 버블정렬
    for i in range(length):
        for j in range(length - i - 1):
            # 문자열을 key로 하는 value(숫자값)을 기반으로 정렬
            if dict_numbers[numbers[j]] > dict_numbers[numbers[j+1]]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    print(f'{tc_num} {" ".join(numbers)}')

