import sys

sys.stdin = open('input.txt')

# 테스트 케이스 개수
T = int(input())

# 테스트 케이스 순회
for i in range(T):
    N = int(input())
    # 각 테스트 케이스 리스트화(구분자가 쓰이지 않아서 split() 사용 불가)
    ai = list(map(int, list(input())))

    # 카드 숫자를 key, 등장횟수를 value로 하는 딕셔너리
    my_dict = {}

    # 카드 리스트를 순회
    for _ in range(len(ai)):
        # 해당 key가 이미 있으면 value(등장횟수) 1 증가
        if ai[_] in my_dict:
            my_dict[ai[_]] += 1
        # 해당 key가 없으면 key-value쌍 생성, value(등장횟수) = 1 할당
        else:
            my_dict[ai[_]] = 1

    # print(my_dict)

    # key만 추출해서 숫자 리스트 만들기
    number_list = list(my_dict.keys())
    # value만 추출해서 등장횟수 리스트 만들기. 두 리스트의 크기는 같음
    count_list = list(my_dict.values())

    # bubble sort로 count_list 오름차순 정렬
    for m in range(len(count_list)-1):
        for n in range(len(count_list)-1-m):
            # 등장 횟수가 같으면 카드 숫자를 기준으로 정렬해야 함
            if count_list[n] == count_list[n+1]:
                if number_list[n] > number_list[n+1]:
                    # count_list를 오름차순 정렬할 때, number_list도 똑같이 움직여서 페어링
                    count_list[n], count_list[n+1] = count_list[n+1], count_list[n]
                    number_list[n], number_list[n+1] = number_list[n+1], number_list[n]
            # 왼쪽 숫자의 등장횟수가 더 크면 순서 뒤집기, number_list도 같이 뒤집기
            elif count_list[n] > count_list[n+1]:
                count_list[n], count_list[n + 1] = count_list[n + 1], count_list[n]
                number_list[n], number_list[n + 1] = number_list[n + 1], number_list[n]

    # print(number_list)
    # print(count_list)
    # 오름차순 정렬했으므로 각 리스트의 마지막 인덱스만 출력
    print(f'#{i+1} {number_list[-1]} {count_list[-1]}')



