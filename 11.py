'''
write an iterative function that performs DFS on a graph
starting from a given vertex, using a stack to visit nodes 
and track which vertices have already been visited
'''
def dfs_iter(graph, start):
    visited = set()
    stack = [start]
    while stack:
        v = stack.pop()
        if v in visited:
            continue
        visited.add(v)
        print(v)
        for n in graph.neighbors(v):
            if n not in visited:
                stack.append(n)

# STATUS: ehh...