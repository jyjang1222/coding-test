

class ListQueue():
    def __init__(self):
        self.queue = []


    def dequeue(self):
        if len(self.queue) == 0:
            return -1

        return self.queue.pop(0)

    def enqueue(self , n):
        self.queue.append(n)
        pass

    def printQueue(self):
        print(self.queue)


lq = ListQueue()
lq.enqueue(10)
lq.enqueue(20)
lq.enqueue(30)
lq.enqueue(40)
lq.enqueue(50)

lq.printQueue()

lq.dequeue()
lq.dequeue()

lq.printQueue()
