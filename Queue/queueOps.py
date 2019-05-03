# Queue Operations

class Queue():
    def __init__(self):
        self.queue = list()

    def addtoqueue(self, dataval):
        if dataval not in self.queue:
            self.queue.insert(0, dataval)
            return True
        else:
            return False

    def removefromqueue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        else:
            return("No element in the queue")

queue = Queue()

print("Add element to the queue")
queue.addtoqueue("Monday")
queue.addtoqueue("Tuesday")
queue.addtoqueue("Wednesday")
print("Remove element from the queue")
print(queue.removefromqueue())
