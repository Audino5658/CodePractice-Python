from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):

        visited.add(v)
        print(v, end=' ')

        for neighbor in self.graph[v]:
            if  not neighbor in visited:
                self.DFSUtil(neighbor, visited)

    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)


def main():
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    #print(g.graph)
    g.DFS(2)



if __name__ == "__main__":
    main()