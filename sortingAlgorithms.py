def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                   temp = arr[j]
                   arr[j] = arr[j+1]
                   arr[j+1] = temp
    return arr

arr = [1, 13, 5, 2, 4, -1, 2, 2, 4]
# print(bubbleSort(arr))

def mergeSort(arr):
    if len(arr) == 1: return arr #deals with 1 item long arrays, already sorted)
    m = len(arr)//2 #length of the array, middle
    firstHalf = arr[:m]
    secondHalf = arr[m:]
    print(arr, firstHalf, secondHalf)
    firstHalf = mergeSort(firstHalf)
    secondHalf = mergeSort(secondHalf)
    return merge(firstHalf, secondHalf)

def merge(firstHalf, secondHalf):
    out = []
    fhIndex = 0
    shIndex = 0
    outIndex = fhIndex
    while (fhIndex < len(firstHalf) and shIndex < len(secondHalf)):
        if firstHalf
    return out
print(mergeSort(arr))