import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    # N = 3, M = 5
    answers = input().split()

    # 학생들이 제출한 정답 배열
    submitted = []

    # 학생들의 점수를 담을 리스트
    scores_list = []

    # 정답 배열에 점수 담기
    for r in range(M):
        row = input().split()
        submitted.append(row)
    # answers = ['1', '2', '3', '4', '5']
    # submitted = [['1', '1', '2', '4', '4'], ['1', '1', '1', '1', '1'], ['1', '2', '3', '4', '5'], ...]

    # 정답을 제출한 학생 수만큼 순회
    for i in range(len(submitted)):
        # 각 문제의 정답여부를 담을 리스트 생성
        # 길이 = 문항 수인 리스트, 오답(False)을 기본값으로 하고 맞으면 True로 갱신할 것
        is_correct = [False] * M

        # 문항을 순회하며 정답이면 해당 문항의 index를 참조하여 is_correct의 요소를 True로 변경
        for j in range(len(answers)):
            if answers[j] == submitted[i][j]:
                is_correct[j] = True

        # is_correct = [True, False, False, False, False]

        # 문항별 득점을 담을 리스트 생성
        scores = [0] * M
        for k in range(len(is_correct)):
            # 정답일 때
            if is_correct[k]:
                # k가 0이면 k-1번째 요소가 없으니까 점수에 1 할당
                if k == 0:
                    scores[k] = 1
                # k가 0이 아닌 경우 이전 요소 + 1의 점수 할당
                else:
                    scores[k] = scores[k-1] + 1

        # 문항별 득점 리스트 합산
        total_score = sum(scores)

        # 합산한 점수를 각 학생의 점수 리스트에 append
        # scores_list = [2, 1, 15, 0, 6]
        scores_list.append(total_score)

    # 학생들의 점수 리스트에서 최대값 - 최소값 계산
    result = max(scores_list) - min(scores_list)

    print(f'#{tc} {result}')