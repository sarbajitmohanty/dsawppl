def firstIndex(l, x):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] > x:
            high = mid - 1
        elif l[mid] < x:
            low = mid + 1
        else:
            if mid == 0 or l[mid - 1] != l[mid]:
                return mid
            else:
                high = mid - 1
    return -1


def lastIndex(l, x):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] > x:
            high = mid - 1
        elif l[mid] < x:
            low = mid + 1
        else:
            if mid == len(l) - 1 or l[mid] != l[mid + 1]:
                return mid
            else:
                low = mid + 1
    return -1


def countOcc(l, x):
    first = firstIndex(l, x)
    if first == -1:
        return 0
    else:
        return lastIndex(l, x) - first + 1


print(countOcc([5, 10, 10, 20, 20, 20, 40], 10))
