from helpers import dll

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = dll.DoublyLinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None

        self.size -= 1
        return self.storage.remove_from_head()