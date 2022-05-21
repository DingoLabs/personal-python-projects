# queue

# FIFO first in first out
# checkout in any store
# computer waiting in queue to print

class Queue:

    def __init__(self):
        #create new queue
        self.items = []

    def is_empty(self):
        #check if queue is empty
        return not bool(self.items)

    def enqueue(self, num):
        self.items.insert(0, num)

    def dequeue(self):
         return self.items.pop()

    def get_size(self):
        return len(self.items)

def hot_potato(name_list, num):
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)
    
    while sim_queue.get_size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())

        sim_queue.dequeue()

    return sim_queue.dequeue()

print(hot_potato(["bill","emily","joe","ralph","phil","pop"], 13))
