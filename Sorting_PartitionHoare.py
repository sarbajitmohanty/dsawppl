def hoarePartition(arr: list[int], l: int, h: int) -> int:
    pivot = arr[l]
    i = l - 1
    j = h + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]
