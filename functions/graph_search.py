from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.visited_vertexes=[]

    def BFS(self, start_vertex):
        frontier_queues = []
        # find and add starting vertex to frontier queue and visited vertex
        frontier_queues.append(start_vertex)
        self.visited_vertexes.append(start_vertex)

        while frontier_queues:
            # go to the found vertex, which is the first in the frontier queues
            current_vertex = frontier_queues.pop(0)
            for adjacent_vertex in self.graph[current_vertex]:
                if adjacent_vertex not in self.visited_vertexes:
                    # find and add the adjacent vertex to frontier queue and visited vertex
                    frontier_queues.append(adjacent_vertex)
                    self.visited_vertexes.append(adjacent_vertex)

        for i in range(len(self.visited_vertexes)):
            if self.visited_vertexes[i] == len(self.visited_vertexes)-1:
                print(self.visited_vertexes[i])
            else:
                print(self.visited_vertexes[i],end='->')

    def DFS_util(self, vertex, visited_vertexes):
        visited_vertexes[vertex] = True
        print(vertex, end='->')
        # traverse as much of unvisited vertexes as possible
        for i in self.graph[vertex]:
            if visited_vertexes[i] == False:
                self.DFS_util(i, visited_vertexes)

    def DFS(self):
        total_vertexes = len(self.graph)
        visited_vertexes = [False]*total_vertexes
        print(self.graph)
        for i in range(total_vertexes):
            if visited_vertexes[i] == False:
                self.DFS_util(i, visited_vertexes)

g = Graph()
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,0)
g.add_edge(2,3)
g.add_edge(3,3)

g.DFS()