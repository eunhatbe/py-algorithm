def search(arr, N, x):
 
    for i in range(0, N):
        if (arr[i] == x):
            return i
    return -1
  
  
 def linear_search(arr, key, size):
   
  # If the array is empty we will return -1
    if (size == 0):
        return -1
 
    elif (arr[size - 1] == key):
        # Return the index of found key.
        return size - 1
    else:
        return linear_search(arr, key, size - 1)
 
 
# __main__

if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    N = len(arr)
 
    # Function call
    result = search(arr, N, x)
    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)
