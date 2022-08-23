from collections import deque


def BFS(adj, s):
    visited = [False] * len(adj)
    q = deque()
    q.append(s)
    visited[s] = True
    while q:
        s = q.popleft()
        print(s, end=" ")
        for u in adj[s]:
            if visited[u] == False:
                q.append(u)
                visited[u] = True


def BFS_Disconnected(adj):
    visited = [False] * len(adj)
    for u in range(len(adj)):
        if visited[u] == False:
            BFS(adj, u, visited)


def addEdge(adj: list[list], u: int, v: int) -> None:
    adj[u].append(v)
    adj[v].append(u)


v = 4
adj = [[] for i in range(v)]
addEdge(adj, 0, 1)
addEdge(adj, 0, 2)
addEdge(adj, 1, 2)
addEdge(adj, 1, 3)

BFS(adj, 0)
