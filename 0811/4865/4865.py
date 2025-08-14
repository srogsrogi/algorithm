import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    str_1 = input()
    str_2 = input()

    # set() 없이 str_1의 unique한 요소 리스트로 추출
    str_1_unique = []
    for i in range(len(str_1)):
        if str_1[i] not in str_1_unique:
            str_1_unique.append(str_1[i])
    # dict comprehension으로 unique한 요소별 count를 담은 딕셔너리 생성
    count_dict = {elem : 0 for elem in str_1_unique}

    # str_2에서 str_1에 있는 문자를 발견할 때마다 count_dict의 각 value값 += 1
    for char in str_2:
        if char in str_1_unique:
            count_dict[char] += 1

    # count_dict의 value의 최대값 구하기
    max_count = 0
    # dict.values()로 value 받은 후
    for c in count_dict.values():
        # max_count 갱신 반복
        if c > max_count:
            max_count = c

    print(f'#{tc + 1} {max_count}')

