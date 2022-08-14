def method1(l: list[int]) -> None:
    l = l[1:] + l[0:1]


def method2(l: list[int]) -> None:
    l.append(l.pop(0))


def method3(l: list[int]) -> None:
    n = len(l)
    x = l[0]
    for i in range(1, n):
        l[i-1] = l[i]
    l[n-1] = x
