class Graph:
    def __init__(self, numberofVertices ):
        self.numberofVertices = numberofVertices
        self.graph = defaultdict(list)
    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)
    def topologicalSortHelper(self, n, visited, stack):
        visited.append(n)
        
        for i in self.graph[n]:
            if i not in visited:
                self.topologicalSortHelper(i, visited, stack)
        stack.insert(0, n)
    def topologicalSort(self):
        self.visited = []
        self.stack = []
        for k in list(self.graph):
            if k not in self.visited:
                self.topologicalSortHelper(k, self.visited, self.stack)
        print(self.stack)
