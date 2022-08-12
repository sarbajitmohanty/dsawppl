def josephusProblem(n, k):
    if n == 1:
        return 0
    else:
        return (josephusProblem(n - 1, k) + k) % n


def josephusBeginWithOne(n, k):
    return josephusProblem(n, k) + 1


print(josephusProblem(5, 3))
