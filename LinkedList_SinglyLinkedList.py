class Node:
    def __init__(self, key: int) -> None:
        self.key = key
        self.next = None


def printList(head: Node) -> None:
    curr = head
    while curr != None:
        print(curr.key, end=" -> ")
        curr = curr.next
    print("None")


def search(head: Node, x: int) -> int:
    pos = 1
    curr = head
    while curr != None:
        if curr.key == x:
            return pos
        pos += 1
        curr = curr.next
    return -1


def insertBegin(head: Node, key: int) -> Node:
    temp = Node(key)
    temp.next = head
    return temp


def insertEnd(head: Node, key: int) -> Node:
    if head == None:
        return Node(key)
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = Node(key)
    return head


def insertPos(head: Node, key: int, pos: int) -> Node:
    temp = Node(key)
    if pos == 1:
        temp.next = head
        return temp
    curr = head
    for i in range(pos - 2):
        curr = curr.next
        if curr == None:
            return head
    temp.next = curr.next
    curr.next = temp
    return head


def sortedInsert(head: Node, key: int) -> Node:
    temp = Node(key)
    if head == None:
        return temp
    elif key < head.key:
        temp.next = head
        return temp
    else:
        curr = head
        while curr.next != None and curr.next.key < key:
            curr = curr.next
        temp.next = curr.next
        curr.next = temp
        return head


def delFirst(head: Node) -> Node:
    if head == None:
        return None
    else:
        return head.next


def delLast(head: Node) -> Node:
    if head == None:
        return None
    if head.next == None:
        return None
    curr = head
    while curr.next.next != None:
        curr = curr.next
    curr.next = None
    return head


def naiveReverseList(head: Node) -> Node:
    stack = []
    curr = head
    while curr is not None:
        stack.append(curr.key)
        curr = curr.next
    curr = head
    while curr is not None:
        curr.key = stack.pop()
        curr = curr.next
    return head


def reverseList(head: Node) -> Node:
    prev = None
    curr = head
    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


def recursiveReverseList(head: Node) -> Node:
    if head == None or head.next == None:
        return head
    restHead = recursiveReverseList(head.next)
    restTail = head.next
    restTail.next = head
    head.next = None
    return restHead


def recursiveReverseList2(curr: Node, prev: Node = None) -> Node:
    if curr == None:
        return prev
    next = curr.next
    curr.next = prev
    return recursiveReverseList2(next, curr)


# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(15)
# head.next.next.next = Node(30)
# printList(head)
# print(search(head, 40))


# head = None
# head = insertBegin(head, 10)
# head = insertBegin(head, 20)
# head = insertBegin(head, 30)
# printList(head)


head = None
head = insertEnd(head, 10)
head = insertEnd(head, 20)
head = insertEnd(head, 30)
head = insertPos(head, 15, 2)
# head = delFirst(head)
# head = delLast(head)
head = sortedInsert(head, 18)
head = recursiveReverseList2(head)
printList(head)
