class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def Enqueue(item, priority):
        new = (item, priority)
        for p in range(len(self.queue)):
            if self.queue[p][1] < priority:
                self.queue.insert(p, new)
                return
        self.queue.append(new)