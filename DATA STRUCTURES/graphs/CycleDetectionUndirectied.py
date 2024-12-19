class graph:
    def __init__(self):
        self.adjacency_list = {}
    def add_edge(self,src,dest):
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
'''
graph1.add_edge(0,1)
graph1.add_edge(0,4)

graph1.add_edge(1,2)
graph1.add_edge(1,0)
graph1.add_edge(1,4)

graph1.add_edge(2,1)
graph1.add_edge(2,3)

graph1.add_edge(3,2)

graph1.add_edge(4,0)
graph1.add_edge(4,1)
graph1.add_edge(4,5)
graph1.add_edge(5,4)
'''
graph1.add_edge(0, 1)
graph1.add_edge(1, 2)
graph1.add_edge(3, 4)

def detCycle(graph1,vis,curr,parent):
    vis[curr] = True
    for i in graph1.adjacency_list.get(curr,[]):
        if vis[i] and parent != i:
            return True
        elif not vis[i]:
            if(detCycle(graph1,vis,i,curr)):
                return True
    return False

vis =[False]*6
print(detCycle(graph1,vis,0,-1))