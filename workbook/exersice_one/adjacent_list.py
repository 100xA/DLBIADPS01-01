class AdjacentList:
    def __init__(self, vertices):
        self.vertices = vertices
        self.list = [[] for _ in range(vertices)]
        
    def add_edge(self, u, v):
        self.list[u].append(v)
        
    def remove_edge(self, u, v):
        self.list[u].remove(v)
    
    def has_path(self, start, end):
        if start == end:
            return True
        visited = [False] * self.vertices
        queue = [start] * self.vertices
        front = 0
        visited[start] = True

        while front < len(queue):
            current = queue[front]
            front += 1
            for neighbour in self.list[current]:
                if neighbour == end:
                    return True
                if not visited[neighbour]:
                    queue.append(neighbour)
                    visited[neighbour] = True
        return False

    def print_list(self):
        for row in self.list:
            print(row)

if __name__ == "__main__":
    graph = AdjacentList(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 3)
    graph.remove_edge(0, 1)
    print(graph.has_path(0, 1))
    print(graph.has_path(0, 3))
    graph.print_list()
