def mergeLists(a: list[int], b: list[int]) -> list[int]:
    res = []
    m = len(a)
    n = len(b)
    i, j = 0, 0
    while i < m and j < n:
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    while i < m:
        res.append(a[i])
        i += 1
    while j < n:
        res.append(b[j])
        j += 1
    return res
