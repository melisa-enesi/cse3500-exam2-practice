class UndirectedEdgeSetGraph:
    def __init__(self):
        self.vertices = set()
        self.edges = set()

    def add_vertex(self, v):
        self.vertices.add(v)

    def add_edge(self, u, v):
        self.vertices.add(u)
        self.vertices.add(v)

        edge = frozenset({u, v})
        self.edges.add(edge)

    def remove_edge(self, u, v):
        edge = frozenset({u, v})
        self.edges.discard(edge)

    def remove_vertex(self, v):
        self.vertices.discard(v)

        self.edges = {
            e for e in self.edges
            if v not in e
        }

    def neighbors(self, v):
        result = set()

        for edge in self.edges:
            if v in edge:
                result.update(edge - {v})
        return result
    
# STATUS: all good