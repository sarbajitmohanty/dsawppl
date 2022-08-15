class TreeNode:
    def __init__(self, K: int) -> None:
        self.right = None
        self.left = None
        self.key = K


def inorder(root: TreeNode) -> None:
    if root != None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


def searchBST(root: TreeNode, key: int) -> bool:
    if root == None:
        return False
    elif root.key == key:
        return True
    elif key > root.key:
        return searchBST(root.right, key)
    else:
        return searchBST(root.left, key)


def searchBSTIterative(root: TreeNode, key: int) -> bool:
    while root != None:
        if root.key == key:
            return True
        elif key > root.key:
            root = root.right
        else:
            root = root.left
    return False


def insert(root: TreeNode, key: int) -> TreeNode:
    if root == None:
        return TreeNode(key)
    elif root.key == key:
        return root
    elif root.key > key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def insertIterative(root: TreeNode, key: int) -> TreeNode:
    parent = None
    curr = root
    while curr != None:
        parent = curr
        if curr.key == key:
            return root
        elif curr.key > key:
            curr = curr.left
        else:
            curr = curr.right
    if parent == None:
        return TreeNode(key)
    if parent.key > key:
        parent.left = TreeNode(key)
    else:
        parent.right = TreeNode(key)
    return root


def getSuccessor(curr: TreeNode, key: int) -> int:
    while curr.left != None:
        curr = curr.left
    return curr.key


def deleteNode(root: TreeNode, key: int) -> TreeNode:
    if root == None:
        return
    if root.key > key:
        root.left = deleteNode(root.left, key)
    elif root.key < key:
        root.right = deleteNode(root.right, key)
    else:
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            succ = getSuccessor(root.right, key)
            root.key = succ
            root.right = deleteNode(root.right, succ)
    return root


def getFloor(root: TreeNode, x: int) -> int:
    res = None
    while root != None:
        if root.key == x:
            return root
        elif root.key > x:
            root = root.left
        else:
            res = root
            root = root.right
    return res


def getCeil(root: TreeNode, x: int) -> int:
    res = None
    while root != None:
        if root.key == x:
            return root
        elif root.key < x:
            root = root.right
        else:
            res = root
            root = root.left
    return res


root = TreeNode(40)
root.left = TreeNode(20)
root.right = TreeNode(80)
root.left.left = TreeNode(8)
root.left.right = TreeNode(30)
root.right.left = TreeNode(60)
root.right.right = TreeNode(100)
root.right.right.right = TreeNode(120)

# print(searchBST(root, 100))
# print(searchBSTIterative(root, 100))
insert(root, 13)
insert(root, 65)
insertIterative(root, 25)
insertIterative(root, 105)
deleteNode(root, 65)
deleteNode(root, 80)
deleteNode(root, 40)
inorder(root)
print()
print(getCeil(root, 35).key)
print(getFloor(root, 35).key)
