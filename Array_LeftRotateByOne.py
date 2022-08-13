def method1(l) -> None:
    l = l[1:] + l[0:1]


def method2(l) -> None:
    l.append(l.pop(0))


def method3(l) -> None:
    n = len(l)
    x = l[0]
    for i in range(1, n):
        l[i-1] = l[i]
    l[n-1] = x
