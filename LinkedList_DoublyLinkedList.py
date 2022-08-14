class Node:
    def __init__(self, key: int) -> None:
        self.key = key
        self.prev = None
        self.next = None


def printList(head: Node) -> None:
    curr = head
    while curr != None:
        print(curr.key, end=" ")
        curr = curr.next


def insertBegin(head: None, x: int) -> Node:
    temp = Node(x)
    if head == None:
        return temp
    head.prev = temp
    temp.next = head
    return temp


def insertEnd(head: Node, x: int) -> Node:
    temp = Node(x)
    if head == None:
        return temp
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = temp
    temp.prev = curr
    return head


def deleteHead(head: Node) -> Node:
    if head == None:
        return None
    if head.next == None:
        return None
    head.next.prev = None
    newHead = head.next
    head.next = None
    return newHead


def deleteLast(head: Node) -> Node:
    if head == None:
        return None
    if head.next == None:
        return None
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.prev.next = curr.next
    curr.prev = None
    return head


def reverseDLL(head: Node) -> Node:
    if head == None:
        return None
    if head.next == None:
        return head
    curr = head
    prev = None
    while curr != None:
        prev = curr
        curr.next, curr.prev = curr.prev, curr.next  # swap
        curr = curr.prev
    return prev


head = None
head = insertBegin(head, 10)
head = insertBegin(head, 20)
head = insertBegin(head, 30)
head = insertEnd(head, 40)
head = deleteHead(head)
head = insertBegin(head, 25)
head = deleteLast(head)
head = insertEnd(head, 50)
head = reverseDLL(head)

printList(head)
