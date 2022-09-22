from collections import deque


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


def inorderIterative(root: TreeNode) -> None:
    if root == None:
        return
    stack = []
    curr = root
    while curr is not None:
        stack.append(curr)
        curr = curr.left
    while len(stack) > 0:
        curr = stack.pop()
        print(curr.key, end=" ")
        curr = curr.right
        while curr is not None:
            stack.append(curr)
            curr = curr.left


def preorder(root: TreeNode) -> None:
    if root != None:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)


def preorderIterative(root: TreeNode) -> None:
    if root is None:
        return
    stack = [root]
    while len(stack) > 0:
        curr = stack.pop()
        print(curr.key, end=" ")
        if curr.right is not None:
            stack.append(curr.right)
        if curr.left is not None:
            stack.append(curr.left)


def postorder(root: TreeNode) -> None:
    if root != None:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=" ")


def levelOrder(root: TreeNode) -> None:
    if root is None:
        return
    q = deque()
    q.append(root)
    while len(q) > 0:
        node = q.popleft()
        print(node.key, end=" ")
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)


def levelOrderList(root: TreeNode) -> list[list[int]]:
    if not root:
        return []
    ans, level = [], [root]
    while level:
        ans.append([node.key for node in level])
        temp = []
        for node in level:
            temp.extend([node.left, node.right])
        level = [leaf for leaf in temp if leaf]
    return ans


def treeSize(root: TreeNode) -> int:
    if root == None:
        return 0
    else:
        leftSubTreeSize = treeSize(root.left)
        rightSubTreeSize = treeSize(root.right)
        return leftSubTreeSize + rightSubTreeSize + 1


def treeHeight(root: TreeNode) -> int:
    if root == None:
        return 0
    else:
        leftSubTreeHeight = treeHeight(root.left)
        rightSubTreeHeight = treeHeight(root.right)
        return max(leftSubTreeHeight, rightSubTreeHeight) + 1


def getMax(root: TreeNode) -> int:
    if root == None:
        return float("-inf")
    else:
        leftMax = getMax(root.left)
        rightMax = getMax(root.right)
        return max(root.key, leftMax, rightMax)


def getMin(root: TreeNode) -> int:
    if root == None:
        return float("inf")
    else:
        leftMin = getMin(root.left)
        rightMin = getMin(root.right)
        return min(root.key, leftMin, rightMin)


def search(root, key: int) -> bool:
    if root == None:
        return False
    elif root.key == key:
        return True
    else:
        return search(root.left, key) or search(root.right, key)


root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.right.left = TreeNode(40)
root.right.right = TreeNode(50)
inorder(root)
print()
preorder(root)
print()
postorder(root)
print()
print(treeSize(root))
print(treeHeight(root))
print(getMax(root))
print(getMin(root))
print(search(root, 40))
inorderIterative(root)
print()
preorderIterative(root)
print()
levelOrder(root)
print()
print(levelOrderList(root))
