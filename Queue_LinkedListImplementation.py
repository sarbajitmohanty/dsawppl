class Node:
    def __init__(self, K: int) -> None:
        self.key = K
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.sz = 0

    def size(self) -> int:
        return self.sz

    def isEmpty(self) -> bool:
        return self.sz == 0

    def getFront(self) -> int:
        return self.front.key

    def getReat(self) -> int:
        return self.rear.key

    def enqueue(self, x: int) -> None:
        temp = Node(x)
        if self.rear == None:
            self.front = temp
        else:
            self.rear.next = temp
        self.rear = temp
        self.sz += 1

    def dequeue(self) -> int:
        if self.front == None:
            return None
        else:
            res = self.front.key
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            self.sz -= 1
            return res


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.size())
print(q.dequeue())
print(q.dequeue())
print(q.size())
