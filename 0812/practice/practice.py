import sys
sys.stdin = open('input.txt')


def check_brackets_no_dict(string):
    brackets_open = ['{', '[', '(']
    brackets_close = ['}', ']', ')']
    list_brackets = []
    # 문자열 순회하면서 괄호만 append나 pop할 것
    for elem in string:
        # 여는 괄호면 append
        if elem in brackets_open:
            list_brackets.append(elem)
        # 닫는 괄호면 스택이 비어있는지부터 확인. 비어있으면 -1
        elif elem in brackets_close:
            if not list_brackets:
                return -1
            # 닫는 괄호고 스택도 비어있지 않으면, 가장 뒤 인덱스가 닫는 괄호와 짝이 맞는 여는 괄호인지 확인
            elif list_brackets[-1] == brackets_open[brackets_close.index(elem)]:
                list_brackets.pop(-1)
            # 짝이 안 맞으면 -1
            else:
                return -1

    # 다 돌고 나서 list가 비어있어야 짝이 맞는 거니까 요소가 있으면 -1, 없으면 1 return
    if list_brackets:
        return -1
    else:
        return 1



T = int(input().strip())
for tc in range(1, T + 1):
    line = input().strip()
    result = check_brackets_no_dict(line)
    print(f'#{tc} {result}')