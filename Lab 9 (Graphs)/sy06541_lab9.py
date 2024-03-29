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
        reference = {node:num for num, node in enumerate(self.graph)} #for possible non0integer nodes

        matrix = [[0 for i in range(v)] for j in range(v)]
        for node in self.graph:
            for edges in self.graph[node]:
                matrix[reference[node]][reference[edges[0]]] = edges[-1]
        return matrix


# G = Graph()

# nodes = ['BOS', 'ORD', 'JFK', 'DFW', 'MIA', 'SFO', 'LAX']
# edges = [('BOS', 'JFK', 1) , ('BOS', 'MIA', 1), ('BOS', 'SFO', 1), ('JFK', 'BOS', 1), ('JFK', 'SFO', 1), ('JFK', 'MIA', 1), ('JFK', 'DFW', 1), ('ORD', 'MIA', 1), ('ORD', 'DFW', 1), ('MIA', 'DFW', 1), ('MIA', 'LAX', 1), ('DFW', 'ORD', 1), ('DFW', 'SFO', 1), ('DFW', 'LAX', 1), ('SFO', 'LAX', 1), ('LAX', 'ORD', 1)]

# G.addNodes(nodes)
# pprint(G.displayGraph())

# G.addEdges(edges, True)
# pprint(G.displayGraph())

# print(G.listOfNodes())
# print(G.listOfEdges())

# G.printIn_OutDegree()

# print(G.getInNeighbours('BOS'))
# print(G.getOutNeighbours('BOS'))

# print(G.isNeighbour('MIA', 'DFW'))

# print(G.isNeighbour('DFW', 'MIA'))

# pprint(G.display_adj_matrix())
