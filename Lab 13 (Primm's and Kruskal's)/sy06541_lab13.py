from pprint import pprint

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        for p in range(len(self.queue)):
            if self.queue[p][1] < priority:
                self.queue.insert(p, (item, priority))
                return
        self.queue.append((item, priority))

    def dequeue(self):
        return self.queue.pop()[0]

    def is_empty(self):
        return self.queue == []


class Graph:
    def __init__(self):
        self.graph = {}

    def addNodes(self, nodes):
        for node in nodes:
            self.graph[node] = []
        self.reference = {node: num for num,node in enumerate(self.listOfNodes())}

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

    def getNeighbours(self, node):  # for undirected graphs
        neighbours = []
        for edges in self.graph[node]:
            neighbours.append(edges)
        return neighbours

    def displayGraph(self):
        return self.graph

    def MST(self, start):
        distance = [float('inf') for node in self.listOfNodes()]
        visited = [False for node in self.listOfNodes()]
        previous = [None for node in self.listOfNodes()]
        pq = PriorityQueue()

        distance[self.reference[start]] = 0
        previous[self.reference[start]] = 'START'
        pq.enqueue(start, 0)

        while not(pq.is_empty()):
            current = pq.dequeue()
            for neighbour in self.getNeighbours(current):
                d = distance[self.reference[current]] + neighbour[-1]
                if d < distance[self.reference[neighbour[0]]] and not(visited[self.reference[neighbour[0]]]):
                    distance[self.reference[neighbour[0]]] = d
                    previous[self.reference[neighbour[0]]] = current
                    pq.enqueue(neighbour[0], d)
            visited[self.reference[neighbour[0]]] = True

        return distance, previous


    def getShortestPath(self, start, end):
        path = []
        distance, previous = self.MST(start)

        if distance[self.reference[end]] == float('inf'):
            return path

        temp = end
        while True:
            if previous[self.reference[temp]] != 'START':
                path.append((previous[self.reference[temp]], temp))
                temp = previous[self.reference[temp]]
            else:
                break

        path.reverse()
        return path

    def getShortestDistance(self, start, end):
        return self.MST(start)[0][self.reference[end]]



print('----------------------Exercise 1-----------------------')
#
G1 = Graph()

nodes = [chr(i) for i in range(65, 72)]
edges = [('A', 'B', 5), ('A', 'D', 3), ('A', 'E', 6), ('B', 'C', 6),
         ('C', 'D', 10), ('C', 'G', 2), ('D', 'F', 8), ('E', 'F', 9), ('F', 'G', 10)]

G1.addNodes(nodes)
G1.addEdges(edges)

pprint(G1.MST('A'))
print(G1.getShortestPath('A', 'G'))