import sys
sys.stdin = open('input.txt')


def calculate_change(money, unit):
    # 몫 : 해당 화폐단위 수, 나머지 : 그 돈 빼고 남은 돈
    return money // unit, money % unit


T = int(input())

for tc in range(1, T+1):
    change = int(input())

    # 화폐 리스트 생성
    unit_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    # 화폐단위별 count 셀 리스트 생성
    count_list = [0] * len(unit_list)

    # 화폐단위별 count 구해서 배열에 담고, change는 나머지로 update하기를 반복
    for i in range(len(unit_list)):
        count, change = calculate_change(change, unit_list[i])
        count_list[i] = count

    # 출력형식 맞추기. join 사용을 위해 str 변환
    result = ' '.join(map(str, count_list))

    print(f'#{tc}\n{result}')