'''
write a function that performs BFS on a graph starting
from a given vertex, using a queue to visit nodes level 
by level while tracking visited vertices
'''
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        v = queue.popleft()
        if v in visited:
            continue
        visited.add(v)
        print(v)
        for n in graph.neighbors(v):
            queue.append(n)

# STATUS: all good