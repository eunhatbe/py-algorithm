def gen_combinations(arr, n):
    result = []
    combination = []

    def backtrack(start, remain):
        if remain == 0:
            result.append(combination[:])
        else:
            for i in range(start, len(arr)):
                combination.append(arr[i])
                backtrack(i + 1, remain - 1)
                combination.pop()

    backtrack(0, n)
    return result

print(gen_combinations([1,2,3,4,5], 3))
