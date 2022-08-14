# not a stable sorting algorithm
def selectionSort(l: list[int]) -> None:
    n = len(l)
    for i in range(n - 1):
        min_indx = i
        for j in range(i + 1, n):
            if l[j] < l[min_indx]:
                min_indx = j
        l[min_indx], l[i] = l[i], l[min_indx]
