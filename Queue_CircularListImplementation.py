class Queue:
    def __init__(self, C: int) -> None:
        self.l = [None] * C
        self.cap = C
        self.size = 0
        self.front = 0

    def getSize(self) -> int:
        return self.size

    def getFront(self) -> int:
        if self.size == 0:
            return None
        else:
            return self.l[self.front]

    def getRear(self) -> int:
        if self.size == 0:
            return None
        else:
            rear = (self.front + self.size - 1) % self.cap
            return self.l[rear]

    def enqueue(self, x: int) -> None:
        if self.size == self.cap:
            return
        else:
            rear = (self.front + self.size - 1) % self.cap
            rear = (rear + 1) % self.cap
            self.l[rear] = x
            self.size += 1

    def dequeue(self) -> int:
        if self.size == 0:
            return None
        else:
            res = self.l[self.front]
            self.front = (self.front + 1) % self.cap
            self.size -= 1
            return res


q = Queue(10)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.getSize())
print(q.dequeue())
print(q.dequeue())
print(q.getSize())
