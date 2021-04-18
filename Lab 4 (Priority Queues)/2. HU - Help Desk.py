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


issues = [('AC Not working in Tariq Rafi', 5), ('Password Change Issue', 4),
          ('Need Installation on laptop', 3), ('Need license', 1), ('Lab PCs Setup', 3), ('Login Issue', 4)]

helpdesk = PriorityQueue()

for issue in issues:
    helpdesk.enqueue(issue[0], issue[1])

while not(helpdesk.is_empty()):
    print(helpdesk.dequeue())
