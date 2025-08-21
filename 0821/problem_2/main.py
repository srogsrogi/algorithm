import itertools

# input.txt 미사용
arr = list(range(1, 11))

result = []

for i in range(11):
    # 길이가 i(턴마다 증가)인 조합을 반복 생성
    # j가 arr의 모든 부분집합이 됨
    for j in itertools.combinations(arr, i):
        # 요소의 합이 10인 경우에만 result 리스트에 append
        if sum(j) == 10:
            result.append(j)

print(result)