from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph=defaultdict(list)


    def addEdge(self,v,u):
        self.graph[v].append(u)


    def printG(self):
        for key in self.graph.keys():
            print(self.graph[key])


    def DFS_work(self,v,visited):
        visited.add(v)
        print(v)

        for node in self.graph[v]:
            if node not in visited:
                self.DFS_work(node,visited)

    def DFS(self,v):

        visited=set()
        self.DFS_work(v,visited)

    def BFS(self, s):


        visited = [False] * (max(self.graph) + 1)


        queue = []


        queue.append(s)

        visited[s] = True

        while queue:

            s = queue.pop(0)
            print (s)


            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True



g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("DFS")

g.DFS(2)


print("BFS")

g.BFS(2)
