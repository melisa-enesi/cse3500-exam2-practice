'''
create a graph class using an edge set representation that stores vertices in
a set and edges as pairs of connected vertices, with methods to add vertices 
and edges to the graph
'''
class EdgeSetGraph:

    def __init__(self):
        self.vertices = set()
        self.edges = set()

    def add_vertex(self, v):
        self.vertices.add(v)

    def add_edge(self, u, v):
        self.vertices.add(u)
        self.vertices.add(v)
        self.edges.add((u, v))

    def remove_edge(self, u, v):
        self.edges.discard((u, v))

    def remove_vertex(self, v):
        self.vertices.discard(v)

        self.edges = {
            e for e in self.edges
            if e[0] != v and e[v] != v
        }

    def neighbors(self, v):
        result = set()

        for u, w in self.edges:
            if u == v:
                result.add(w)
        return result
    
# STATUS: all good