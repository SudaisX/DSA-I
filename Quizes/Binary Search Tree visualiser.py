def insert(BST, value):
    if BST == {}:
        BST['value'] = value
        BST['left'] = {}
        BST['right'] = {}
    elif value > BST['value']:
        insert(BST['right'], value)
    elif value < BST['value']:
        insert(BST['left'], value)
    return BST

def createBST(lst):
    BST = {}
    for n in lst:
        insert(BST, n)
    return BST
        
def TracingKey_to_LRpath(bst, query):
    def tracing(BST, query, path=''):
        if BST == {}:
            return None
        elif BST['value'] == query:
            return path
        elif query < BST['value']:
            path += 'L'
            return tracing(BST['left'], query, path)
        elif query > BST['value']:
            path += 'R'
            return tracing(BST['right'], query, path)  
    return tracing(bst, query)

lst = eval(input())
bst = createBST(lst)
print(bst)

N = int(input())

for i in range(N):
    query = int(input())
    print(TracingKey_to_LRpath(bst, query))