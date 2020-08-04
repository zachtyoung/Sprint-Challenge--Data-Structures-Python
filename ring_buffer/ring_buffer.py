from doubly_linked_list import DoublyLinkedList

#Like a normal queue but when the queue is full we can add to the front of the queue if space is available

#Is empty if head = tail
#add to tail

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_oldest = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #Is the queue empty?
        #Is the queue full?
        # If we reach the capacity of the buffer set the current pointer back to the beginning

        #Is there anything in our list yet? If not add the first item and 
        #capacity full case
        if self.storage.length == self.capacity: #Yes?
            if self.current_oldest.next is not None:
                self.current_oldest.value = item # set value
                self.current_oldest = self.current_oldest.next #move current_oldest
            else:
                self.current_oldest.value = item #set value
                self.current_oldest = self.storage.head #set current oldnest 

        #capacity not full case
        #insert item and intialize current oldest value
        else: #No?
            self.storage.add_to_tail(item)
            self.current_oldest = self.storage.head    


    def get(self):
        # Note:  This is the only [] allowed
        # Loop through each item in the list and append that value to list_buffer_contents
        list_buffer_contents = []

        # Start off at the beginning of the list
        # check if node exists
        # append value of node to list
        # reassign node and move to next node

        node = self.storage.head
        #Is there a node?
        while node is not None:
            #apend to list
            list_buffer_contents.append(node.value)
            #move node
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
