from collections import deque


def method1(l, d):
    l = l[d:] + l[:d]


def method2(l, d):
    dq = deque(l)

    # to left rotate d times ->
    dq.rotate(-d)
    # to right rotate d times ->
    dq.rotate(d)

    l = list(dq)


def method3(l, d):
    for i in range(d):
        l.append(l.pop(0))


def reverse(l, b, e):
    while b < e:
        l[b], l[e] = l[e], b[b]
        b += 1
        e -= 1


def method4(l, d):
    n = len(l)
    reverse(l, 0, d-1)
    reverse(l, d, n-1)
    reverse(l, 0, n-1)
