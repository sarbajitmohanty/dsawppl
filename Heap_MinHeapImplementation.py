class Heap:
    def __init__(self, l: list = []) -> None:
        self.arr = l
        i = (len(l) - 2) // 2
        while i >= 0:
            self.minHeapify(i)
            i -= 1

    def parent(self, i: int) -> int:
        return (i - 1) // 2

    def leftChild(self, i: int) -> int:
        return (2 * i + 1)

    def rightChild(self, i: int) -> int:
        return (2 * i + 2)

    def insert(self, x: int) -> None:
        arr = self.arr
        arr.append(x)
        i = len(arr) - 1
        while i > 0 and arr[self.parent(i)] > arr[i]:
            p = self.parent(i)
            arr[i], arr[p] = arr[p], arr[i]
            i = p

    def minHeapify(self, i: int) -> None:
        arr = self.arr
        lt = self.leftChild(i)
        rt = self.rightChild(i)
        smallest = i
        n = len(arr)
        if lt < n and arr[lt] < arr[smallest]:
            smallest = lt
        if rt < n and arr[rt] < arr[smallest]:
            smallest = rt
        if smallest != i:
            arr[smallest], arr[i] = arr[i], arr[smallest]
            self.minHeapify(smallest)

    def extractMin(self) -> int:
        arr = self.arr
        n = len(arr)
        if n == 0:
            return float("inf")
        res = arr[0]
        arr[0] = arr[n-1]
        arr.pop()
        self.minHeapify(0)
        return res

    def decreaseKey(self, i: int, x: int) -> None:
        arr = self.arr
        arr[i] = x
        while i != 0 and arr[self.parent(i)] > arr[i]:
            p = self.parent(i)
            arr[i], arr[p] = arr[p], arr[i]
            i = p

    def delete(self, i: int) -> None:
        n = len(self.arr)
        if i >= n:
            return
        else:
            self.decreaseKey(i, float("-inf"))
            self.extractMin()


heap = Heap([12, 10, 3, 4, 15, 20])
print(heap.arr)
print(heap.extractMin())
print(heap.extractMin())
print(heap.extractMin())
print(heap.extractMin())
print(heap.extractMin())
