def merge(a: list[int], low: int, mid: int, high: int) -> None:
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
