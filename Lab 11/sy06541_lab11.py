from pprint import pprint
class Queue:
    def __init__(self):
        self.q = []   
    def enQueue(self, item):
        self.q.append(item) 
    def deQueue(self):
        return self.q.pop(0)
    def front(self):
        return self.q[0]
    def is_empty(self):
        return self.q == []

class Graph:
    def __init__(self):
        self.graph = {}
        self.directed = False

    def addNodes(self, nodes):
        for node in nodes:
            self.graph[node] = []

    def listOfNodes(self):
        return [node for node in self.graph]

    def addEdges(self, edges, directed=False):
        if directed:
            for edge in edges:
                self.graph[edge[0]].append((edge[1], edge[2]))
        else:
            for edge in edges:
                self.graph[edge[0]].append((edge[1], edge[2]))
                self.graph[edge[1]].append((edge[0], edge[2]))

    def listOfEdges(self, directed=False):
        self.edges = []
        if directed:
            for node in self.graph:
                for edge in self.graph[node]:
                    self.edges.append((node, edge[0], edge[1]))
        else:
            self.visited = []
            for node in self.graph:
                for edge in self.graph[node]:
                    if ((node, edge[0])) not in self.visited: #checks if the node has not been visited yet
                        self.edges.append((node, edge[0], edge[1])) 
                        self.visited.append((edge[0], node)) #appends reversed tuple of the current edge to indicate it has been visited       
        return self.edges

    def printIn_OutDegree(self):
        _in = {node:0 for node in self.graph}
        out = [len(self.graph[node]) for node in self.graph]

        for node in self.graph:
            for edges in self.graph[node]:
                _in[edges[0]] += 1

        i = 0
        for node in self.graph:
            print(f'{node} => In-Degree: {_in[node]}, Out-Degree: {out[i]}')
            i += 1

    def printDegree(self): #for undirected graph
        for node in self.graph:
            print(f'{node} => {len(self.graph[node])}')

    def getNeighbours(self, node): #for undirected graphs
        neighbours = []
        for edges in self.graph[node]:
            neighbours.append(edges[0])
        return neighbours

    def getInNeighbours(self, node): #for directed graph
        neighbours = []
        for nodes in self.graph:
            for edges in self.graph[nodes]:
                if node == edges[0]:
                    neighbours.append(nodes)
        return neighbours

    def getOutNeighbours(self, node):
        neighbours = []
        for edges in self.graph[node]:
            neighbours.append(edges[0])
        return neighbours

    def getNearestNeighbour(self, node):
        nearest_node = self.graph[node][0][0]
        nearest_weight = self.graph[node][0][1]
        for edges in self.graph[node]:
            if edges[1] < nearest_weight:
                nearest_node = edges[0]
                nearest_weight = edges[1]
        return nearest_node

    def isNeighbour(self, node1, node2):
        for edges in self.graph[node1]:
            if edges[0] == node2:
                return True
        return False

    def removeNode(self, node):
        self.graph.pop(node)
        for nodes in self.graph:
            for edges in self.graph[nodes]:
                if edges[0] == node:
                    self.graph[nodes].remove(edges)

    def removeNodes(self, nodes):
        for n in nodes:
            self.removeNode(n)

    def clearEdges(self):
        for edges in self.graph:
            self.graph[edges] = []
    
    def displayGraph(self):
        return self.graph

    def display_adj_matrix(self):
        v = len(self.graph)
        reference = {node:num for num, node in enumerate(self.graph)} #for possible non0integer nodes

        matrix = [[0 for i in range(v)] for j in range(v)]
        for node in self.graph:
            for edges in self.graph[node]:
                matrix[reference[node]][reference[edges[0]]] = edges[-1]
        return matrix

    def DFS(self, position):
        def DFS_helper(pos):
            if self.visited[self.reference[pos]]: return
            else:
                self.visited[self.reference[pos]] = True
                self.order.append(pos)
                for neighbour in self.getNeighbours(pos):
                    DFS_helper(neighbour)
        
        self.reference = {node:num for num, node in enumerate(self.graph)}
        self.visited = [False for i in self.listOfNodes()]
        self.order = []
        DFS_helper(position)
        return self.order

    def isCyclic(self, lst):
        for node in range(len(lst)):
            if lst[node] not in self.getOutNeighbours(lst[node-1]):
                return False
        return True

    def BFS(self, start, end):
        pass

print('----------------------Exercise 1-----------------------') #Depth First Search
#Algorithm is in the Graph Class
G1 = Graph()

G1.addNodes([0, 1, 2, 3, 4, 5])
G1.addEdges([(0,1,1), (0,2,1), (1,2,1), (1,3,1), (2,4,1), (3,4,1), (3,5,1), (4,5,1)], True)

for node in G1.listOfNodes():
    print(f'If Start Node = {node} : Order of Visited Vertices = {G1.DFS(node)}')
print()

print('----------------------Exercise 2-----------------------') #Detecing Cycles between list of N airports
#
airports = Graph()
airports.addNodes(['Austin', 'Atlanta', 'Chicago', 'Dallas', 'Denver', 'Houston', 'Washington'])
airports.addEdges([('Austin', 'Dallas', 200), ('Austin', 'Houston', 160), ('Atlanta', 'Washington', 600), ('Atlanta', 'Houston', 800), ('Chicago', 'Denver', 1000), ('Dallas', 'Austin', 200), ('Dallas', 'Denver', 780), ('Dallas', 'Chicago', 900), ('Denver', 'Chicago', 1000), ('Denver', 'Atlanta', 1400), ('Houston', 'Atlanta', 800), ('Washington', 'Atlanta', 600), ('Washington', 'Dallas', 1300)], True)

print(airports.isCyclic(['Austin','Houston','Atlanta','Washington','Dallas']))
print(airports.isCyclic(['Austin','Houston','Atlanta','Washington']))
print()

print('----------------------Exercise 3-----------------------') #Breadth First Search
#
G2 = Graph()
G2.addNodes(['S', 1, 2, 3, 4, 5, 6, 7])
G2.addEdges([('S',1,1), ('S',2,1), (1,3,1), (1,4,1), (1,5,1), (2,6,1), (6,7,1)], True)

pprint(G2.displayGraph())