import sys
sys.path.append('/home/duke/lambda/Python/Data-Structures/singly_linked_list/singly_linked_list.py')
from dll import DoublyLinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
    
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