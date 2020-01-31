from doubly_linked_list import DoublyLinkedList

#Like a normal queue but when the queue is full we can add to the front of the queue if space is available

#Is empty if head = tail
#add to tail

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #Is the queue empty?
        #Is the queue full?

        #Is there anything in our list yet? If not add the first item
        if self.storage.length == self.capacity:

        else: self.storage.add_to_head(item)            
    def get(self):
        # Note:  This is the only [] allowed
        # Loop through each item in the list and append that value to list_buffer_contents
        list_buffer_contents = []

        # Start off at the beginning of the list
        # check if node exists
        # append value of node to list
        # reassign node and move to next node

        return list_buffer_contents

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
