from queue import Queue
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

graph1.add_Edge(0,1)
graph1.add_Edge(0,2)
graph1.add_Edge(1,3)
graph1.add_Edge(2,4)
graph1.add_Edge(3,4)
graph1.add_Edge(3,5)
graph1.add_Edge(4,5)
graph1.add_Edge(5,6)


def bfs(graph1,node):
    vis = [False]*7
    q = Queue()
    q.put(node)
    vis[node] = True
    while(q.empty() == False):
        n = q.get()
        print(n)
        for i in graph1.adjacency_list[n]:
            if vis[i] == False:
                q.put(i)
                vis[i] = True

def dfs(graph1,node):
    vis = [False]*7
    def dfs_util(node):
        vis[node] = True
        print(node)
        for i in graph1.adjacency_list[node]:
            if vis[i] == False:
                dfs_util(i)
    dfs_util(node)
def print_all_paths(self, start, end):
        visited = {node: False for node in self.adjacency_list}  
        path = []  # To store the current path

        def helper(current):
            visited[current] = True  # Mark the current node as visited
            path.append(current)  # Add the current node to the path

            # If the destination is reached, print the path
            if current == end:
                print("Path:", path)
            else:
                # Recur for all unvisited neighbors
                for neighbor in self.adjacency_list[current]:
                    if not visited[neighbor]:
                        helper(neighbor)

            # Backtrack: Remove the current node from the path and mark it as unvisited
            path.pop()
            visited[current] = False

        # Start the DFS-based search from the start node
        helper(start)



bfs(graph1,0)
print("\n")
dfs(graph1,0)
print("\n")
print_all_paths(graph1,0,5)
