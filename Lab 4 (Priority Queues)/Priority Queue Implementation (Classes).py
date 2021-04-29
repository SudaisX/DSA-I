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
        return self.queue.pop(0)[0]

    def is_empty(self):
        return self.queue == []