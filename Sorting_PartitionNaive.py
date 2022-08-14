def partition(arr: list[int], p: int) -> None:
    n = len(arr)
    arr[p], arr[n-1] = arr[n-1], arr[p]
    temp = []
    for x in arr:
        if x <= arr[n-1]:
            temp.append(x)
    for x in arr:
        if x > arr[n-1]:
            temp.append(x)
    for i in range(len(arr)):
        arr[i] = temp[i]
