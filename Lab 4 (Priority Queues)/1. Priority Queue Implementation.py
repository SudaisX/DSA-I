import ast
queue = input()
queue = ast.literal_eval(queue)

def Enqueue(queue, item, priority):
    new = (item, priority)
    for p in range(len(queue)):
        if queue[p][1] < priority:
            queue.insert(p, new)
            return
    queue.append(new)

def Dequeue(queue):
    return queue.pop(0)[0]

#for unsorted
#def Dequeue(queue):
    #vip = 0
    #vip_index = 0
    #if not(is_empty(queue)):
    #    for p in range(len(queue)):
    #        if queue[p][1] > vip:
    #            vip = queue[p][1]
    #            vip_index = p
    #return queue.pop(vip_index)[0]
        
def is_empty(queue):
    return len(queue) == []
    
operation = input()

if operation == "Enqueue":
    item = input()
    priority = int(input())
    Enqueue(queue, item, priority)
    print(queue)
elif operation == "Dequeue":
    print(Dequeue(queue))
    print(queue)