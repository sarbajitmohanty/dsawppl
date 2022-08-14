class HashMap:
    def __init__(self, b: int) -> None:
        self.BUCKET = b
        self.table = [[] for x in range(b)]

    def insert(self, x: int) -> None:
        i = x % self.BUCKET
        self.table[i].append(x)

    def remove(self, x: int) -> None:
        i = x % self.BUCKET
        self.table[i].remove(x)

    def search(self, x: int) -> bool:
        i = x % self.BUCKET
        return x in self.table[i]


hs = HashMap(7)
hs.insert(10)
hs.insert(20)
hs.insert(49)
hs.insert(21)
print(hs.table)
print(hs.search(10))
print(hs.search(20))
hs.remove(10)
print(hs.search(10))
