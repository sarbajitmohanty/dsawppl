def merge(a, low, mid, high) -> None:
    left = a[low: mid+1]
    right = a[mid+1: high+1]
    i, j = 0, 0
    k = low
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            k += 1
            i += 1
        else:
            a[k] = right[j]
            k += 1
            j += 1
    while i < len(left):
        a[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        a[k] = right[j]
        k += 1
        j += 1


def mergeSort(arr, l, r) -> None:
    if r > l:
        m = (l + r) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


arr = [10, 1, 23, 14, 17, 9, 4, 20]
mergeSort(arr, 0, len(arr)-1)
print(arr)
