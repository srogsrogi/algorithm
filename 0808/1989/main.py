import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    word = input()
    reversed_word = ''.join(reversed(word))
    # 이걸 더 많이 씀
    # reversed_word = word[::-1]
    if word == reversed_word:
        result = 1
    else:
        result = 0

    print(f'#{tc + 1} {result}')