class HashMap:
    def __init__(self, c) -> None:
        self.cap = c
        self.table = [-1] * c
        self.size = 0

    def hash(self, x) -> int:
        return x % self.cap

    def insert(self, x) -> bool:
        if self.size == self.cap:
            return False
        if self.search(x) == True:
            return False
        i = self.hash(x)
        t = self.table
        while t[i] not in (-1, -2):
            i = (i + 1) % self.cap
        t[i] = x
        self.size = self.size + 1
        return True

    def search(self, x) -> bool:
        h = self.hash(x)
        t = self.table
        i = h
        while t[i] != -1:
            if t[i] == x:
                return True
            i = (i + 1) % self.cap
            if i == h:
                return False
        return False

    def remove(self, x) -> bool:
        h = self.hash(x)
        t = self.table
        i = h
        while t[i] != -1:
            if t[i] == x:
                t[i] = -2
                return True
            i = (i + 1) % self.cap
            if i == h:
                return False
        return False


hs = HashMap(13)
hs.insert(20)
hs.insert(10)
hs.insert(30)
hs.insert(26)
hs.insert(13)
print(hs.table)
print(hs.search(20))
hs.remove(20)
print(hs.search(20))
print(hs.table)
