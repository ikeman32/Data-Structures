import sys
sys.path.append('/home/duke/lambda/Python/Data-Structures/binary_search_tree/helpers/dll.py')
from dll import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None

        self.size -= 1
        return self.storage.remove_tail()