name = ['a', 'b', 'c']
path = []
arr = ['O', 'X']


def recur(count):
    # 종료조건(3명을 모두 고려)
    if count == 3:
        print(*path)
        return

    # 부분집합에 포함되는 경우
    path.append(arr[0])
    recur(count + 1)
    path.pop()

    # 부분집합에 포함되지 않는 경우
    path.append(arr[1])
    recur(count + 1)
    path.pop()


recur(0)
print('---------------------------------------------')

name = ['a', 'b', 'c']
path = []
arr = ['O', 'X']


def recur(count, subset):
    # 종료조건(3명을 모두 고려)
    if count == 3:
        print(*subset)
        return

    # 부분집합에 포함되는 경우
    recur(count + 1, subset + [name[count]])

    # 부분집합에 포함되지 않는 경우
    recur(count + 1, subset)


recur(0, [])