class Deque:
    def __init__(self, C: int) -> None:
        self.l = [None] * C
        self.cap = C
        self.size = 0
        self.front = 0

    def deleteFront(self) -> int:
        if self.size == 0:
            return None
        else:
            res = self.l[self.front]
            self.front = (self.front + 1) % self.cap
            self.size -= 1
            return res

    def deleteRear(self) -> int:
        if self.size == 0:
            return None
        else:
            rear = (self.front + self.size - 1) % self.cap
            res = self.l[rear]
            self.size -= 1
            return res

    def insertFront(self, x: int) -> None:
        if self.size == self.cap:
            return
        else:
            self.front = (self.front - 1) % self.cap
            self.l[self.front] = x
            self.size += 1

    def insertRear(self, x: int) -> None:
        if self.size == self.cap:
            return
        rear = (self.front + self.size - 1) % self.cap
        rear = (rear + 1) % self.cap
        self.l[rear] = x
        self.size += 1


dq = Deque(10)

dq.insertFront(1)
dq.insertRear(2)
dq.insertFront(3)
dq.insertRear(4)
print(dq.deleteFront())
print(dq.deleteRear())
