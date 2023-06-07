arr = [6,5,1,4,7,2,3]


# pivot : 4


def quick_sort(arr):
    # 만약 원소의 개수가 한개라면
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]                           # pivot 값을 배열 중간 인덱스 값으로 설정
    lesser_arr, equal_arr, greater_arr = [], [], []     # 분할을 위한 빈 배열 생성

    for num in arr:
        if num < pivot:         # 만약 요소가 pivot 값보다 작다면 pivot보다 작은 그룹으로 이동
            lesser_arr.append(num)
        elif num > pivot:       # 만약 요소가 pivot 값보다 크다면 pivot보다 큰 그룹으로 이동
            greater_arr.append(num)
        else:
            equal_arr.append(num)

    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)     # 정렬한 그룹 병합


arr = quick_sort(arr)

print(arr)

# 재귀호출할 떄마다 매번 새로운 리스트를 생성하기 떄문에 메모리에 매우 비효율적
