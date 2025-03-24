class AdjacentList:
    def __init__(self, vertices):
        self.vertices = vertices
        self.list = [[] for _ in range(vertices)]
        
    def add_edge(self, u, v):
        self.list[u].append(v)
        
    def remove_edge(self, u, v):
        if v in self.list[u]:
            self.list[u].remove(v)
    
    def has_path(self, start, end):
        if start == end:
            return True
        
        visited = [False] * self.vertices
        visited[start] = True
        
        queue = [start]
        front = 0
        
        while front < len(queue):
            current = queue[front]
            front += 1
            
            if current == end:
                return True
    
            for neighbour in self.list[current]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)
        
        return False


if __name__ == "__main__":
    g = AdjacentList(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 3)
    print(g.has_path(0, 3))  
    print(g.has_path(2, 1))  