def lomutoPartition(arr: list[int], l: int, h: int) -> int:
    pivot = arr[h]
    i = l - 1
    for j in range(l, h):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return i+1
