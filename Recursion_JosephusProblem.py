def josephusProblem(n, k) -> int:
    if n == 1:
        return 0
    else:
        return (josephusProblem(n - 1, k) + k) % n


def josephusBeginWithOne(n, k) -> int:
    return josephusProblem(n, k) + 1


print(josephusProblem(5, 3))