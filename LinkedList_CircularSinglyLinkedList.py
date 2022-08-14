class Node:
    def __init__(self, key: int) -> None:
        self.key = key
        self.next = None


def printCircular(head: Node) -> None:
    if head == None:
        return
    print(head.key, end=" ")
    curr = head.next
    while curr != head:
        print(curr.key, end=" ")
        curr = curr.next


def insertBegLinear(head: Node, x: int) -> Node:
    temp = Node(x)
    if head == None:
        temp.next = temp
        return temp
    curr = head
    while curr.next != head:
        curr = curr.next
    curr.next = temp
    temp.next = head
    return temp


def insertBeg(head: Node, x: int) -> Node:
    temp = Node(x)
    if head == None:
        temp.next = temp
        return temp
    else:
        temp.next = head.next
        head.next = temp
        head.key, temp.key = temp.key, head.key  # swap
        return head


def insertEndLinear(head: Node, x: int) -> Node:
    temp = Node(x)
    if head == None:
        temp.next = temp
        return temp
    curr = head
    while curr.next != head:
        curr = curr.next
    curr.next = temp
    temp.next = head
    return head


def insertEnd(head: Node, x: int) -> Node:
    temp = Node(x)
    if head == None:
        temp.next = temp
        return temp
    else:
        temp.next = head.next
        head.next = temp
        head.key, temp.key = temp.key, head.key  # swap
        return temp


def deleteHeadLinear(head: Node) -> Node:
    if head == None:
        return None
    elif head.next == head:
        return None
    curr = head
    while curr.next != head:
        curr = curr.next
    curr.next = head.next
    return curr.next


def deleteHead(head: Node) -> Node:
    if head == None:
        return None
    elif head.next == None:
        return None
    else:
        head.data = head.next.data
        head.next = head.next.next
        return head


def deleteKthNode(head: Node, K: int) -> Node:
    if head == None:
        return head
    elif K == 1:
        return deleteHead(head)
    else:
        curr = head
        for i in range(K - 2):
            curr = curr.next
        curr.next = curr.next.next
        return head


head = Node(10)
head.next = Node(20)
head.next.next = Node(15)
head.next.next.next = Node(30)
head.next.next.next.next = head
printCircular(head)
