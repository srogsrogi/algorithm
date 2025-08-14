T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    # 기준값 설정
    min_val = arr[0]

    # 버블정렬
    for i in range(N):
        # 큰 순서대로 뒤에서부터 쌓여나감
        for j in range(0, N - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # 정렬 결과 담을 리스트
    result_list = []

    # 정수 개수가 10 미만이어서 result_list가 10이 되기 전에 arr이 비게 되는 경우 처리
    # result_list에 10개가 차기 전까지 반복
    while arr and len(result_list) < 10:
        # arr의 마지막 요소를 result에 추가하고 pop
        result_list.append(arr[-1])
        arr.pop(-1)
        '''
        큰 수, 작은 수 합쳐서 두 번의 append와 pop을 하나의 while문에서 하면
        len(arr)이 홀수인 경우 이미 비어있는 arr의 요소를 검색하는 오류가 발생
        그래서 while문 안에서 한 번 더 arr이 빈 배열인지 아닌지를 검사한 후
        두 번째 append와 pop을 진행합니다.
        '''
        if arr:
            result_list.append(arr[0])
            arr.pop(0)

    # 출력을 위해 str로 변환
    result = ' '.join(map(str, result_list))

    print(f'#{tc + 1} {result}')