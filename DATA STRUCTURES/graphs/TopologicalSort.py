from collections import deque
class graph:
    def __init__(self):
        self.adjacency_list = {}
    def add_edge(self,src,dest):
        if src not in self.adjacency_list:
            self.adjacency_list[src] = []
        self.adjacency_list[src].append(dest)
    def display(self):
        for vertex, neighbors in self.adjacency_list.items():
            print(f"{vertex} -> {neighbors}")
graph1 = graph()
graph1.add_edge(5,0)
graph1.add_edge(5,2)
graph1.add_edge(2,3)
graph1.add_edge(3,1)
graph1.add_edge(4,0)
graph1.add_edge(4,1)

def topo(graph1,vis,curr,s):
    vis[curr] = True
    for i in graph1.adjacency_list.get(curr,[]):
        if not vis[i]:
            topo(graph1,vis,i,s)
    s.append(curr)

s = []
vis = [False]*6
for i in range(0,6):
    if not vis[i]:
        topo(graph1,vis,i,s)

while s:
    print(s.pop())