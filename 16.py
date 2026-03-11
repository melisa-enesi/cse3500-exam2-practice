'''
write a function that finds all connected components in a graph
by performing DFS and grouping together vertices that are reachable
from each other
'''
def connected_components(graph):
    visited = set()
    components = []
    for v in graph.adj:
        if v not in visited:
            stack = [v]
            component = []
            while stack:
                node = stack.pop()
                if node in visited:
                    continue
                visited.add(node)
                component.append(node)
                for n in graph.neighbors(node):
                    if n not in visited:
                        stack.append(n)
            components.append(component)
    return components