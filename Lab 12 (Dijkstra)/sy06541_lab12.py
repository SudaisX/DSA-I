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
            self.reference = {node: num for num,
                              node in enumerate(self.listOfNodes())}

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

    def dijkstra(self, start):
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
        distance, previous = self.dijkstra(start)

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
        return self.dijkstra(start)[0][self.reference[end]]


# Dijkstra
print('----------------------Exercise 1a-----------------------')
#
G1 = Graph()

nodes = [chr(i) for i in range(65, 72)]
edges = [('A', 'B', 5), ('A', 'D', 3), ('A', 'E', 6), ('B', 'C', 6),
         ('C', 'D', 10), ('C', 'G', 2), ('D', 'F', 8), ('E', 'F', 9), ('F', 'G', 10)]

G1.addNodes(nodes)
G1.addEdges(edges)

print(G1.getShortestPath('A', 'G'))
print()
#
print('----------------------Exercise 1b-----------------------')
#
#i.
cities = Graph()
data = []
nodes = []
edges = []

import csv
with open('Lab 12 (Dijkstra)/connections.csv') as connections:
    data_csv = csv.reader(connections)
    counter = 0
    for row in data_csv:
        if counter == 0:
            nodes = row
            counter += 1
        else:
            data.append(row)

for node in data:
    city = node[0]
    for edge in range(1, len(node)):
        if int(node[edge]) != -1 and int(node[edge]) != 0:
            edges.append((city, nodes[edge], int(node[edge])))

cities.addNodes(nodes[1::])
cities.addEdges(edges, True)

#ii.
start = 'Islamabad'
end = 'Kaghan'

print(f'Shortest path from {start} to {end} is: \n{cities.getShortestPath(start, end)}')
print()
print(f'Shortest distance from {start} to {end} is: \n{cities.getShortestDistance(start, end)}km.')

#
print('----------------------Exercise 2-----------------------')
#
G2 = Graph()

nodes = [chr(i) for i in range(65, 72)]
edges = [('A', 'B', 7), ('A', 'D', 2), ('A', 'E', 6), ('B', 'C', 3),
         ('C', 'D', 2), ('C', 'G', 2), ('D', 'F', 8), ('E', 'F', 9), ('F', 'G', 4)]

G2.addNodes(nodes)
G2.addEdges(edges)

print(f'Shortest path from A to F is: \n{G2.getShortestPath("A", "F")}')
print(f'Shortest path from A to B is: \n{G2.getShortestPath("A", "B")}')