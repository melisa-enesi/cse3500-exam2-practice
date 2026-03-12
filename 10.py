class AdjacencySetGraph:
    def __init__(self):
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = set()
    
    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)

        self.adj[u].add(v)
        self.adj[v].add(u)
    
    def remove_edge(self, u, v):
        if u in self.adj:
            self.adj[u].discard(v)
        if v in self.adj:
            self.adj[v].discard(u)

    def remove_vertex(self, v):
        if v not in self.adj:
            return
        
        for neighbor in self.adj[v]:
            self.adj[neighbor].discard(v)
        
        del self.adj[v]
    
    def neighbors(self, v):
        return self.adj.get(v, set())
    
# STATUS: all good
    
'''
write functions that perform DFS on a graph, check whether the graph
is strongly connected using DFS, and create a reversed version of 
the graph by reversing all edges
'''
def dfs(graph, v, visited):
    visited.add(v)
    print(v)
    for neighbor in graph.neighbors(v):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def strongly_connected(graph):
    start = next(iter(graph.vertices))
    visited = set()
    dfs(graph, start, visited)
    if len(visited) != len(graph.vertices):
        return False
    reversed_graph = reverse_graph(graph)
    visited = set()
    dfs(reversed_graph, start, visited)
    return len(visited) == len(graph.vertices)

def reverse_graph(graph):
    rev = AdjacencySetGraph()
    for u in graph.adj:
        for v in graph.adj[u]:
            rev.add_edge(v, u)
    return rev

# STATUS: all good