class Node:
    def __init__(self, K: int) -> None:
        self.key = K
        self.next = None
        self.prev = None


class Deque:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.sz = 0

    def size(self) -> int:
        return self.sz

    def isEmpty(self) -> bool:
        return self.sz == 0

    def insertRear(self, x: int) -> None:
        temp = Node(x)
        if self.rear == None:
            self.front = temp
        else:
            self.rear.next = temp
            temp.prev = self.rear
        self.rear = temp
        self.sz += 1

    def deleteFront(self) -> int:
        if self.front == None:
            return None
        else:
            res = self.front.key
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None
            self.sz -= 1
            return res


dq = Deque()
dq.insertRear(10)
dq.insertRear(20)
dq.insertRear(30)
print(dq.size())
print(dq.deleteFront())
print(dq.deleteFront())
print(dq.size())
