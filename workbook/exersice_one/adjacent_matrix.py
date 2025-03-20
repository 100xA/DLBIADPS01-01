from collections import deque

class AdjacentMatrix:
    def __init__(self, vertices):
        self.vertices = vertices
        self.matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        self.matrix[u][v] = 1
    
    def remove_edge(self, u, v):
        self.matrix[u][v] = 0
    
    def has_path (self, start, end):
        if start == end:
            return True
        visited = [False] * self.vertices
        queue = deque([start])
        while queue:
            current = queue.popleft()
            if current == end:
                return True
            for neighbour in range(self.vertices):
                if(self.matrix[current][neighbour] == 1 and not visited[neighbour]):
                    queue.append(neighbour)
                    visited[neighbour] = True
        return False

    def print_matrix(self):
        for row in self.matrix:
            print(row)


if __name__ == "__main__":

    graph = AdjacentMatrix(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 3)
    graph.print_matrix()
    print(graph.has_path(2, 3))
    print(graph.has_path(0, 3))
