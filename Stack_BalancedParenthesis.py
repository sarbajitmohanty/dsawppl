def isMatching(a: str, b: str) -> bool:
    if ((a == '(' and b == ')') or
        (a == '{' and b == '}') or
            (a == '[' and b == ']')):
        return True
    else:
        return False


def isBalanced(expr: str) -> bool:
    stack = []
    for x in expr:
        if x in ('(', '{', '['):
            stack.append(x)
        else:
            if not stack:
                return False
            elif isMatching(stack[-1], x) == False:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True


print(isBalanced("{[{{([])}}]}"))
