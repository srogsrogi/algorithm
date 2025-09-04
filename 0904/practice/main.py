# 중복 순열(3P2)

visited = []

# 시작점 : 0개의 카드를 고른 상태
# 기저조건 : r개의 카드를 모두 뽑았으면 종료
# 다음 재귀호출 : [0, 1, 2] 카드 중 하나를 고른다.

def recur(count):
    # 기저조건
    if count == 2:
        print(*visited)
        return

    # 0, 1, 2 중 하나 선택. count와 range만 바꿔주면 n, r값 변경 가능
    for num in range(3):
        visited.append(num)
        recur(count + 1)
        visited.pop()

recur(0)
print('-----------------------------------------------------------')

# 주사위 굴리기
# 3번 굴려서 10 이하인 경우의 수 세기
result = 0
path = []

def dice(count):
    global result

    # 이미 조건 안 맞으면 조기종료
    if sum(path) > 10:
        return

    if count == 3:
        if sum(path) <= 10:
            print(*path)
            result += 1
        return
    
    for num in range(1,7):
        path.append(num)
        dice(count + 1)
        path.pop()
    
dice(0)
print(result)
print('----------------------------------------')

# A,J,Q,K 카드가 충분히 많을 때 5장 뽑아서 나열하고 같은 카드가 3장 연속으로 나오는 경우의 수 구하기

def count_three():
    for i in range(3):
        if path[i] == path[i+1] == path[i+2]:
            return True
    return False

result_card = 0
cards = ['A', 'J', 'Q', 'K']
path = []
def card(count):
    global result_card

    if count == 5:
        if count_three():
            print(*path)
            result_card += 1
        return
    
    for idx in range(len(cards)):
        path.append(cards[idx])
        card(count + 1)
        path.pop()

card(0)
print(result_card)