def bubble_sort(arr):
    # 리스트 요소 수만큼 순회
    for i in range(len(numbers)-1):
        # -i를 해주면 이미 정렬된 요소는 순회하지 않음
        for j in range(len(numbers)-1-i):
            # 앞 요소보다 뒤 요소가 작으면 위치 바꾸기
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    # 정렬된 배열 반환
    return numbers

numbers = [64, 13, 9, 62, 3]
sorted_numbers = bubble_sort(numbers)
print("정렬 후:", sorted_numbers)