
def runningTime(arr):
    # Write your code here
    shifts_count = 0
    for i in range(1, len(arr)):
        j = i - 1
        val = arr[i]
        while j >= 0 and arr[j] > val:
            arr[j + 1] = arr[j]
            shifts_count += 1
            j -= 1
        arr[j + 1] = val

    return shifts_count
