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
def cycle(graph1,curr,vis,rec,ans):
    vis[curr] = True
    rec[curr] = True
    for i in graph1.adjacency_list.get(curr,[]):
        if rec[i]:
            return True
        elif( vis[i] == False):
            cycle(graph1,i,vis,rec,ans)
    rec[curr] = False
    return False

graph1 = graph()
graph1.add_edge(0,1)
graph1.add_edge(2,0)
graph1.add_edge(2,3)
graph1.add_edge(3,4)
graph1.add_edge(4,2)

#graph1.add_edge(3,0)
vis = [False]*5
rec = [False]*5
ans  = [False]*1

for i in range(0,5):
    ans = cycle(graph1,i,vis,rec,ans)
    if ans:
        print(ans)
        break
if not ans:
    print(False)

