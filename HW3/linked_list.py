# linked_list.py
# ===================================================
# Linked list exploration
# Part 1: implement the deque and bag ADT with a Linked List
# Part 2: implement the deque ADT with a CircularlyDoubly-
# Linked List
# ===================================================


'''
**********************************************************************************
Part1: Deque and Bag implemented with Linked List
**********************************************************************************
'''

class SLNode:
    def __init__(self):
        self.next = None
        self.data = None


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a linked list with a head and tail node with None data
        """
        self.head = SLNode()
        self.tail = SLNode()
        self.head.next = self.tail

        # populate list with initial set of nodes (if provided)
        if start_list is not None:
            for data in start_list:
                self.add_back(data)

    def __str__(self):
        """
        Returns a human readable string of the list content of the form
        [value1 -> value2 -> value3]

        An empty list should just return []

        Returns:
            The string of the human readable list representation
        """
        out = '['
        if self.head.next != self.tail:             
            cur = self.head.next.next
            out = out + str(self.head.next.data)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.data)
                cur = cur.next
        out = out + ']'
        return out


    def add_link_before(self, data, index):
        """
        Adds a new link containing data and inserts it before the link at index.
        If index is 0, it inserts at the beginning of the list.

        Args:
            data: The data the new node will contain
            index: The index of the node that will immediately follow the newly added node
        """
        #Check if index is within range
        if index < 0:
            print("Index out of range")
        
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        #place the node at the head if the list in empty
        if self.head.next == self.tail:
            new_link.next = self.tail
            self.head.next = new_link
            return self
        
        #if the index is 0 place the node at the head
        if index == 0:
            new_link.next = self.head.next
            self.head.next = new_link
            return self

        #insert node at specified index
        current_node = self.head
        prev = None
        #traverse thru the list
        for i in range(index + 1):
            #if current node becomes tail raise exception
            if current_node == self.tail:
                raise Exception('Out of bounds')
            prev = current_node
            current_node = current_node.next
        
        #insert node into list
        new_link.next = current_node
        prev.next = new_link
        return self

    def remove_link(self, index):
        """
        Removes the link at the location specified by index
        Args:
            Index: The index of the node that will be removed
        """
        #if index is out of range
        if index < 0:
            print("Index out of range")
        current_node = self.head
        prev = None
        
        #if index is 0 place at head of list
        if index == 0:
            self.head.next = current_node.next
        #traverse thru list to find index
        for i in range(index + 1):
            if current_node == self.tail:
                raise Exception("Out of range")
            prev = current_node
            current_node = current_node.next
        prev.next = current_node.next

    def add_front(self, data):
        """
        Adds a new node after the head that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        new_link.next = self.head.next
        self.head.next = new_link
        return self

    def add_back(self, data):
        """
        Adds a new node before the tail that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        if self.head == None:
            self.add_front(new_link)
            return self
        
        current_node = self.head
        prev = None
        
        while current_node != self.tail:
            prev = current_node
            current_node = current_node.next
        
        new_link.next = current_node
        prev.next = new_link

    def get_front(self):
        """
        Returns the data in the element at the front of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at index 0 or None if there is no such node
        """

        #if the list is empty
        if self.head.next == self.head:
            return None
        return self.head.next.data

    def get_back(self):
        """
        Returns the data in the element at the end of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at last index of the list or None if there is no such node
        """

        #if the list is empty
        if self.head.next == self.tail:
            return None
        
        current_head = self.head
        prev = None
        
        #while the current head does not equal to the tail set and return the last node
        while current_head != self.tail:
            prev = current_head
            current_head = current_head.next
        return prev.data

    def remove_front(self):
        """
        Removes the first element of the list. Will not remove the tail.
        """

        #if the list is empty
        if self.head.next == self.tail:
            return None
        current_node = self.head.next
        self.head.next = current_node.next
        return self

    def remove_back(self):
        """
        Removes the last element of the list. Will not remove the head.
        """

        current_head = self.head
        prev = None
        
        #find the last node and remove it
        while current_head.next != self.tail:
            prev = current_head
            current_head = current_head.next
        prev.next = self.tail
        return self

    def is_empty(self):
        """
        Checks if the list is empty

        Returns:
            True if the list has no data nodes, False otherwise
        """

        #return true if list is empty
        if self.head.next == self.tail:
            return True
        else:
            return False

    def contains(self, value):
        """
        Checks if any node contains value

        Args:
            value: The value to look for

        Returns:
            True if value is in the list, False otherwise
        """

        while self.head != self.tail:
            if self.head.data == value:
                return True
            self.head = self.head.next
        else:
            return False

    def remove(self, value):
        """
        Removes the first instance of an element from the list

        Args:
            value: the value to remove
        """

        current_head = self.head
        prev = None
        
        while current_head != self.tail:
            #check if each node contains the value we are looking for
            if current_head.data == value:
                prev.next = current_head.next
                return self
            prev = current_head
            current_head = current_head.next
        return self


'''
**********************************************************************************
Part 2: Deque implemented with CircularlyDoublyLinked List
**********************************************************************************
'''

class DLNode:
    def __init__(self):
        self.next = None
        self.prev = None
        self.data = None

class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a linked list with a single sentinel node containing None data
        """
        self.sentinel = DLNode()
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate list with initial set of nodes (if provided)
        if start_list is not None:
            for data in start_list:
                self.add_back(data)

    def __str__(self):
        """
        Returns a human readable string of the list content of the form
        [value1 <-> value2 <-> value3]

        An empty list should just print []

        Returns:
            The string of the human readable list representation
        """
        out = '['
        if self.sentinel.prev != self.sentinel:             
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.data)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.data)
                cur = cur.next
        out = out + ']'
        return out

    def add_link_before(self, data, index):
        """
        Adds a new link containing data and inserts it before the link at index.
        If index is 0, it inserts at the beginning of the list.

        Args:
            data: The data the new node will contain
            index: The index of the node that will immediately follow the newly added node
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        #if index is out of range
        if index < 0:
            print("Index out of range")
        
        #if index is 0 add to the head
        if index == 0:
            new_link.prev = self.sentinel
            new_link.next = self.sentinel.next
            self.sentinel.next.prev = new_link
            self.sentinel.next = new_link
            return True

        #if the head is not none
        current = self.sentinel.next
        for num in range(next):
            current = current.next
            if current == self.sentinel:
                #out of range
                print("Index out of range")
        
        new_link.prev = current.prev
        current.prev.next = new_link
        new_link.next = current
        current.prev = new_link

    def remove_link(self, index):
        """
        Removes the link at the location specified by index
        Args:
            Index: The index of the node that will be removed
        """

        #if index out of range
        if index < 0:
            raise Exception('Index out of range')
        
        current = self.sentinel.next
        for num in range(index):
            current = current.next
            if current == self.sentinel:
                raise Exception("index out of range")
        
        #if node being removed is not linked to the sentinel
        if current.prev != self.sentinel and current.next != self.sentinel:
            current.next.prev = current.prev
            current.prev.next = current.next
        
        #if the node is in front
        if current.prev == self.sentinel and current.next != self.sentinel:
            current.next.prev = current.prev
            current.prev.next = current.next 
        
        #if the node is in the back
        if current.prev != self.sentinel and current.next == self.sentinel:
            current.prev.next = self.sentinel
            self.sentinel.next = current.next 
        
        #if only one node is in the list
        if current.prev == self.sentinel and current.next == self.sentinel:
            self.sentinel.prev = self.sentinel
            self.sentinel.next = self.sentinel
        
        return True

    def add_front(self, data):
        """
        Adds a new node at the beginning of the list that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # if the list is empty next and prev on the sentinel
        if self.sentinel.prev == self.sentinel:
            new_link.prev = self.sentinel
            new_link.next = self.sentinel.next
            self.sentinel.prev = new_link
            self.sentinel.next = new_link

        # if the list isn't empty set next on the sentinel
        else:
            new_link.prev = self.sentinel
            new_link.next = self.sentinel.next
            self.sentinel.next.prev = new_link
            self.sentinel.next = new_link

        return

    def add_back(self, data):
        """
        Adds a new node at the end of the list that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # if the list is empty we set both next and prev on the sentinel
        if self.sentinel.prev == self.sentinel:
            new_link.prev = self.sentinel
            new_link.next = self.sentinel.next
            self.sentinel.prev = new_link
            self.sentinel.next = new_link

        # if the list isn't empty we just set next on the sentinel
        else:
            new_link.prev = self.sentinel.prev
            new_link.next = self.sentinel
            self.sentinel.prev.next = new_link
            self.sentinel.prev = new_link

        return

    def get_front(self):
        """
        Returns the data in the element at the front of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at index 0 or None if there is no such node
        """

        return self.sentinel.next.data


    def get_back(self):
        """
        Returns the data in the element at the end of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at last index of the list or None if there is no such node
        """

        return self.sentinel.prev.data


    def remove_front(self):
        """
        Removes the first element of the list. Will not remove the tail.
        """

        #if empty
        if self.sentinel.next == self.sentinel:
            return False
        else:
            #move the next element to the front and continue to move the link down
            self.sentinel.next.next.prev = self.sentinel
            self.sentinel.next = self.sentinel.next.next
            return True


    def remove_back(self):
        """
        Removes the last element of the list. Will not remove the head.
        """

        if self.sentinel.prev == self.sentinel:
            return False
        else:
            #remove the last element and move the prev node to be the last node
            self.sentinel.prev.prev.next = self.sentinel
            self.sentinel.prev = self.sentinel.prev.prev

    def is_empty(self):
        """
        Checks if the list is empty

        Returns:
            True if the list has no data nodes, False otherwise
        """

        #same as checking if their is a front
        if self.sentinel.next == self.sentinel:
            return True
        else:
            return False


    def contains(self, value):
        """
        Checks if any node contains value

        Args:
            value: The value to look for

        Returns:
            True if value is in the list, False otherwise
        """

        #check if list is empty
        if self.sentinel.next == self.sentinel:
            return False
        else:
            #set the current node to the next element after the sentinel
            current = self.sentinel.next
            #loop thru while the current doesnt equal the sentinel to check if the current node is the data we are looking for then stop
            while current != self.sentinel:
                if current.data == value:
                    return True
                #check the next value
                current = current.next
            return False

    def remove(self, value):
        """
        Removes the first instance of an element from the list

        Args:
            value: the value to remove
        """
        #check if list is empty
        if self.sentinel.next == self.sentinel:
            return False
        else:
            current = self.sentinel.next
            while current != self.sentinel:
                if current.data == value:
                    #no end value
                    if current.prev != self.sentinel and current.next != self.sentinel:
                        #set the prev node to link to the next and prev node
                        current.next.prev = current.prev
                        current.prev.next = current.next
                    #value in the front of the list
                    if current.prev == self.sentinel and current.next != self.sentinel:
                        self.sentinel.next = current.next
                        current.next.prev = self.sentinel
                    #value at the end of the list
                    if current.prev != self.sentinel and current.next == self.sentinel:
                        #set the previous node to link the previous and the sentinel and remove the last node
                        self.sentinel.prev = current.prev
                        current.prev.next = self.sentinel
                    return True
                current = current.next
            return False

    def circularListReverse(self):
        """
        Reverses the order of the links. It must not create any additional new links to do so.
        (e.g. you cannot call DLNode()). If the list printed by following next was 0, 1, 2, 3,
        after the call it will be 3,2,1,0
        """

        #look at the first and second node to compare and then switch
        current = self.sentinel.next
        node = current.next
        
        #switch the values
        while current != self.sentinel:
            current.next = current.prev
            current.prev = node
            current = node
            node = current.next
            
        #reset the current and previous values to close the loop
        pointer = current.prev
        current.prev = current.next
        current.next = pointer
        return
