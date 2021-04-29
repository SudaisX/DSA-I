import ast
M = input()
M = ast.literal_eval(M)

def convertToAdjacencyList(M):
    G = {}
    for i in range(len(M)):
        G[i] = []
        
    for i in range(len(M)):
        for j in range(len(M)):
            if i != j and M[i][j] == 1:
                G[i].append(j)
    
    return G

def BFS(G, node):
    from queue import Queue
    queue = Queue()
    queue.put(node)
    visited = []
    while not queue.empty():
        vertex = queue.get()
        visited.append(vertex)
        for i in G[vertex]:
            if i not in visited:
                queue.put(i)
    return visited

def DFS(G, node, visit=[], visited_bool=[]):
    visit.append(node)
    visited_bool[node] = True
    for edge in G[node]:
        if edge not in visit:
            DFS(G, edge, visit, visited_bool)
    return visit
    
def extractFriendCircles(M):
    G = convertToAdjacencyList(M)
    # G = {0:[(1, 1)], 1:[(0, 1)], 2:[], 3:[]}
    visited_bool = [False for i in range(len(G))]
    friends = []
    
    for node in range(len(G)):
        if visited_bool[node] == False:
            friends.append(DFS(G, node, [], visited_bool))
    
    # print(G)
    return friends
    
friendCircles = extractFriendCircles(M)
print(sorted(friendCircles, key=lambda x: x[0]))