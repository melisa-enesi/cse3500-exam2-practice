class MatrixGraph:
    def __init__(self, size):
        self.size = size
        self.matrix = [
            [0] * size
            for _ in range(size)
        ]
    
    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1
    
    def neighbors(self, v):
        result = []

        for i in range(self.size):
            if self.matrix[v][i] == 1:
                result.append(i)

        return result
    
# STATUS: good