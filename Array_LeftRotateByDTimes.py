from collections import deque


def method1(l, d) -> None:
    l = l[d:] + l[:d]


def method2(l, d) -> None:
    dq = deque(l)

    # to left rotate d times ->
    dq.rotate(-d)
    # to right rotate d times ->
    dq.rotate(d)

    l = list(dq)


def method3(l, d) -> None:
    for i in range(d):
        l.append(l.pop(0))


def reverse(l, b, e) -> None:
    while b < e:
        l[b], l[e] = l[e], b[b]
        b += 1
        e -= 1


def method4(l, d) -> None:
    n = len(l)
    reverse(l, 0, d-1)
    reverse(l, d, n-1)
    reverse(l, 0, n-1)
