def bubble_sort(arr):
    length = len(arr)
    swapped = False

    # 첫번째 요소부터 반복
    for i in range(length):
        
        # for문을 순회하고나면 우측부터 이미 정렬이 완료되었기 떄문에
        #  length - i - 1 로 요소를 줄인다 
        for j in range(0, length - i - 1):
            
            # 오름차순으로 스왑해준다. 이 떄 한번이라도 스왑이 일어나지 않는다면 
            # 그 인덱스의 정렬을 멈추고 다음 인덱스로 넘어간다.
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

            if(swapped == False):
                break


if __name__ == "__main__":
    x = [5,4,8,11,3,2,1]
    bubble_sort(x)
    print(x)
