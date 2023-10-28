class Graph:
    def __init__(self, V):
        self.V = V
        self.adjList = [[] for _ in range(V)]

    def addEdge(self, v, w):
        self.adjList[v].append(w)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for i in self.adjList[v]:
            if not visited[i]:
                self.DFSUtil(i, visited)

    def DFS(self, v):
        visited = [False] * self.V
        self.DFSUtil(v, visited)

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("DFS starting from vertex 2: ", end='')
g.DFS(2)
