from collections import deque

class Graph:
    def __init__(self, V):
        self.V = V
        self.adjList = [[] for _ in range(V)]

    def addEdge(self, v, w):
        self.adjList[v].append(w)

    def BFS(self, s):
        visited = [False] * self.V
        queue = deque()
        visited[s] = True
        queue.append(s)

        while queue:
            s = queue.popleft()
            print(s, end=' ')

            for i in self.adjList[s]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("BFS starting from vertex 2: ", end='')
g.BFS(2)
