'''
write a function that checks whether a graph contains a cycle by performing
a DFS traversal and tracking visited vertices and their parent nodes.
'''
def has_cycle(graph):
    visited = set()
    for v in graph.vertices:
        if v not in visited:
            if dfs_cycle(graph, v, visited, None):
                return True
    return False

def dfs_cycle(graph, v, visited, parent):
    visited.add(v)
    for n in graph.neighbors(v):
        if n not in visited:
            if dfs_cycle(graph, n, visited, v):
                return True
            elif n != parent:
                return True
    return False

# STATUS: all good