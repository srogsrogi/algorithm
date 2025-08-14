def counting_sort(input_arr, k):
    # k는 정수의 최대값이고, 숫자는 0도 있으니까 배열은 k+1칸
    counts = [0] * (k + 1)
    # 반환할 배열
    temp = [0] * len(input_arr)

    # count 배열
    for i in input_arr:
        counts[i] += 1
    # count 누적합 배열
    for j in range(len(counts)):
        counts[j] += counts[j - 1]
    # stable sort를 위해 역순 순회
    for k in range(len(input_arr) - 1, -1, -1):
        # 처음 + 같은 값이 등장할 때마다 index 한 칸씩 땡겨주기
        counts[input_arr[k]] -= 1
        # 정렬된 배열(temp)에 값 하나씩 업데이트
        temp[counts[input_arr[k]]] = input_arr[k]

    return temp


arr = [0, 4, 1, 3, 1, 2, 4, 1]
print('정렬 결과:', counting_sort(arr, 5))  # [0, 1, 1, 1, 2, 3, 4, 4]