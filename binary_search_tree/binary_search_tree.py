
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:#If value is less than root
            if self.left is None:#If left value none insert into node
                self.left = BSTNode(value)
            else:#If left value not none recursively check before inserting
                self.left.insert(value)
        else:#If the value is not less than root
            if self.right is None:#If right value is none insert into node
                self.right = BSTNode(value)
            else:#If right value not none recursively check before inserting
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:#Return True if target is value
            return True

        if target < self.value or target > self.value:
            if target is self.left.value or target is self.right.value:
                return True
            else:
                try:
                    self.right.contains(target)
                    self.left.contains(target)
                except:
                    return None
                
        else:
            return False
                


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()
            

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)#Add self.value to the callback
        if self.right != None: 
            self.right.for_each(fn)#Recursively add all values from the right
        if self.left != None:
            self.left.for_each(fn)#Recursively add all values from the left
        
        
        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
