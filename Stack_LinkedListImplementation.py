import math


class Node:
    def __init__(self, d: int) -> None:
        self.data = d
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.head = None
        self.sz = 0

    def push(self, x: int) -> None:
        temp = Node(x)
        temp.next = self.head
        self.head = temp
        self.sz += 1

    def size(self) -> int:
        return self.sz

    def peek(self) -> int:
        if self.head == None:
            return math.inf
        return self.head.data

    def pop(self) -> int:
        if self.head == None:
            return math.inf
        res = self.head.data
        self.head = self.head.next
        self.sz -= 1
        return res


s = Stack()
s.push(10)
s.push(20)
print(s.size())
print(s.peek())
print(s.pop())
print(s.size())
print(s.pop())
print(s.pop())
print(s.pop())
