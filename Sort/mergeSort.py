def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr)//2

        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

if __name__ == '__main__':
    arr = [4, 8, 9, 11, 5, 3, 2, 1]
    print("정렬전 arr ↓", end="\n")
    print_list(arr)
    merge_sort(arr)

    print("정렬후 arr ↓ ", end="\n")
    print_list(arr)
