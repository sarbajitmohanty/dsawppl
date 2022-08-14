# stable sorting algorithm
def insertionSort(l: list[int]) -> None:
    for i in range(1, len(l)):
        x = l[i]
        j = i - 1
        while j >= 0 and x < l[j]:
            l[j+1] = l[j]
            j = j - 1
        l[j + 1] = x
