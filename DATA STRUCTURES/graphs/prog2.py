# directed weighted graph

'''class Edge:
    def __init__(self,dest,w):
        self.dest = dest
        self.w = w
    def __repr__(self):
        return f"({self.dest}, weight={self.w})"
'''
class graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self,src,dest):
        if src not in self.adjacency_list:
            self.adjacency_list[src] = []
        self.adjacency_list[src].append(dest)
    def display(self):
        for vertex, edges in self.adjacency_list.items():
            print(f"{vertex} -> {edges}")

graph1 = graph()
graph1.add_edge(0,1,)

graph1.add_edge(0,2,)

graph1.add_edge(2,3,)

graph1.add_edge(3,1,)

graph1.display()

print(graph1.adjacency_list[0])