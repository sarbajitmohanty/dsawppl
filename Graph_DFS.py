from ast import Add


def DFS_Recursive(adj, s, visited):
    visited[s] = True
    print(s, end=" ")
    for u in adj[s]:
        if visited[u] == False:
            DFS_Recursive(adj, u, visited)


def DFS(adj, s):
    visited = [False] * len(adj)
    DFS_Recursive(adj, s, visited)


def DFS_Disconnected(adj):
    visited = [False] * len(adj)
    for u in range(len(adj)):
        if visited[u] == False:
            DFS_Recursive(adj, u, visited)


def addEdge(adj: list[list], u: int, v: int) -> None:
    adj[u].append(v)
    adj[v].append(u)


v = 4
adj = [[] for i in range(v)]
addEdge(adj, 0, 1)
addEdge(adj, 0, 2)
addEdge(adj, 1, 2)
addEdge(adj, 1, 3)

DFS(adj, 0)
