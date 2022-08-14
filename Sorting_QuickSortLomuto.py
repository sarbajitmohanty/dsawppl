def lomutoPartition(arr: list[int], l: int, h: int) -> int:
    pivot = arr[h]
    i = l - 1
    for j in range(l, h):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return i+1


def qSort(arr: list[int], l: int, h: int) -> None:
    if l < h:
        p = lomutoPartition(arr, l, h)
        qSort(arr, l, p-1)
        qSort(arr, p+1, h)


arr = [10, 1, 23, 14, 17, 9, 4, 20]
qSort(arr, 0, len(arr)-1)
print(arr)
