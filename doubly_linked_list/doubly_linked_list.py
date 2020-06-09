"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # create a new node
        new_node = ListNode(value, prev=None, next=None)
        #check for head
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:#change the head
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        #check if there no head if no return None
        if not self.head:
            return None

        self.length -= 1

        #check if only one item in list
        if self.head == self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            return current_head.value
        else:
            current_head = self.head
            self.head = self.head.next
            self.head.prev = self.head.prev
            return current_head.value


    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value, prev=None, next=None)# create new node

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:#change the tail
            self.tail.prev = new_node
            new_node.next = self.tail
            self.tail = new_node

        self.length += 1


    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        #check if there is no tail if not return None
        if not self.tail:
            return None

        self.length -= 1

        if self.tail == self.head:#check if only one item
            current_tail = self.tail
            self.tail = None
            self.head = None
            return current_tail.value
        else:#change tail
            current_tail = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            return current_tail.value


    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node == self.head:#if the node equals head do nothing
            return
        if node == self.tail:#if the node equals tail remove from tail
            self.remove_from_tail()
        else:#otherwise delete node
            node.delete()
            self.length -= 1
        self.add_to_head(node.value)#add current node value to the head

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node == self.tail:#if the node equals tail do nothing
            return
        if node == self.head:# if the node equals head remove from head
            self.remove_from_head
        else:#otherwis delete node
            node.delete()
            self.length -= 1
        self.add_to_tail(node.value)#add current node to tail

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        pass
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        pass
