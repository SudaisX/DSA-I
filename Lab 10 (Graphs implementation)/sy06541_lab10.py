from pprint import pprint
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
        reference = {node:num for num, node in enumerate(self.graph)} #for possible non-integer nodes

        matrix = [[0 for i in range(v)] for j in range(v)]
        for node in self.graph:
            for edges in self.graph[node]:
                matrix[reference[node]][reference[edges[0]]] = edges[-1]
        return matrix

#Exercise 1
print('\n' + '-'*30 + 'Exercise 1' + '-'*30, end='\n'*2)
G1 = Graph()

#Part a)
nodes1 = [1, 2, 3, 4, 5]
edges1 = [(1,2,1), (1,5,1), (2,5,1), (2,4,1), (2,3,1), (3,4,1), (4,5,1)] #Unweighted graph hence weight = 1 for all edges
G1.addNodes(nodes1)
G1.addEdges(edges1) #Since the graph is undirected, directed=False by default 

#Part b)
print(G1.listOfNodes(), end='\n'*2)

#Part c)
print(G1.listOfEdges(), end='\n'*2) #Since the graph is undirected, directed=False by default

#Part d)
pprint(G1.display_adj_matrix())
print()

#Part e)
pprint(G1.displayGraph())
print()

#Part f)
print('Degree of each node: ')
G1.printDegree()
print()
for node in G1.listOfNodes():
    print(f'Neighbour(s) of {node} =  {G1.getNeighbours(node)}')

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#Exercise 2
print('\n' + '-'*30 + 'Exercise 2' + '-'*30, end='\n'*2)
G2 = Graph()

#Part a)
nodes2 = [1, 2, 3, 4]
edges2 = [(1, 2, 1), (2, 4, 1), (3, 1, 1), (3, 2, 1), (4, 3, 1), (4, 4, 1)]
G2.addNodes(nodes2)
G2.addEdges(edges2, True)

#Part b)
pprint(G2.displayGraph())
print()

#Part c)
G2.printIn_OutDegree()
print()

#Part d)
for node in G2.listOfNodes():
    print(f'Neighbour(s) of {node} =  {G2.getNeighbours(node)}')
print()

#Part e)
in_sum = sum([len(G2.getInNeighbours(n)) for n in G2.listOfNodes()])
out_sum = sum([len(G2.getOutNeighbours(n)) for n in G2.listOfNodes()])

print(in_sum == out_sum == len(G2.listOfEdges()))

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#Exercise 3
print('\n' + '-'*30 + 'Exercise 3' + '-'*30, end='\n'*2)
G3 = Graph()

#Part a)
nodes3 = ['Austin', 'Atlanta', 'Chicago', 'Dallas', 'Denver', 'Houston', 'Washington']
edges3 = [('Austin', 'Dallas', 200), ('Austin', 'Houston', 160), ('Atlanta', 'Washington', 600), ('Atlanta', 'Houston', 800), ('Chicago', 'Denver', 1000), ('Dallas', 'Austin', 200), ('Dallas', 'Denver', 780), ('Dallas', 'Chicago', 900), ('Denver', 'Chicago', 1000), ('Denver', 'Atlanta', 1400), ('Houston', 'Atlanta', 800), ('Washington', 'Atlanta', 600), ('Washington', 'Dallas', 1300)]

G3.addNodes(nodes3)
G3.addEdges(edges3, True)

pprint(G3.displayGraph())
print()

#Part b)
def max_inbound(graph):
    max_in = 0
    for node in graph.listOfNodes():
        if len(graph.getInNeighbours(node)) > max_in:
            max_in = len(graph.getInNeighbours(node))

    for node in graph.listOfNodes():
        if len(graph.getInNeighbours(node)) == max_in:
            print(f'{node} airport has the maximum number of inbound flights')

def max_outbound(graph):
    max_out = 0
    for node in graph.listOfNodes():
        if len(graph.getOutNeighbours(node)) > max_out:
            max_out = len(graph.getOutNeighbours(node))

    for node in graph.listOfNodes():
        if len(graph.getOutNeighbours(node)) == max_out:
            print(f'{node} airport has the maximum number of outbound flights')

max_inbound(G3)
max_outbound(G3)
print()

#Part c)
def isOneWay(graph):
    oneway = []
    for node1 in graph.listOfNodes():
        for node2 in graph.listOfNodes():
            if node1 != node2:
                if node2 in graph.getInNeighbours(node1) and node1 not in graph.getInNeighbours(node2):
                    oneway.append((node2, node1))
    return oneway

print(isOneWay(G3), end='\n'*2)

#Part d)
#couldve just used G3.getNearestNeighbour(airport) but ok whatever the question requires
def nearestAirport(graph, airport): 
    return graph.getNearestNeighbour(airport) 

for airport in G3.listOfNodes(): 
    print(f'Nearest airport from {airport} airport is:   {nearestAirport(G3, airport)} airport.')

#Part e)
def connectedAirports(graph, airport):
    connected = graph.getInNeighbours(airport)
    for i in range(len(connected)):
        connected += graph.getInNeighbours(connected[i])
    return [n for n in connected if n != airport]

print()
print(connectedAirports(G3, 'Dallas'))
