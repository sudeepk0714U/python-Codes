class graph:
    def __init__(self):
        self.adjacency_list = {}
    def add_Edge(self,src,dest):
        if src not in self.adjacency_list:
            self.adjacency_list[src] = []
        if dest not in self.adjacency_list:
            self.adjacency_list[dest] = []

        self.adjacency_list[src].append(dest)
        self.adjacency_list[dest].append(src)
    def display(self):
        for vertex, neighbors in self.adjacency_list.items():
            print(f"{vertex} -> {neighbors}")

graph1 = graph()
graph1.add_Edge(0,2)
graph1.add_Edge(2,3)
graph1.add_Edge(2,1)
graph1.add_Edge(3,1)
graph1.display()
print(graph1.adjacency_list[2])

