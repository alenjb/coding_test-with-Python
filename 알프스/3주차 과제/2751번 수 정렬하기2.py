def mergeSort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) //2
    low_arr = mergeSort(arr[:mid])
    high_arr = mergeSort(arr[mid:])
    newArr = []

    l=0
    h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            newArr.append(low_arr[l])
            l += 1
        else:
            newArr.append(high_arr[h])
            h += 1
    newArr += low_arr[l:]
    newArr += high_arr[h:]
    return newArr


n = int(input())
arr = [int(input()) for _ in range(n)]
print(*mergeSort(arr), sep='\n')
