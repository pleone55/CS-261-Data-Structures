# hash_map.py
# ===================================================
# Implement a hash map with chaining
# ===================================================

class SLNode:
    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value

    def __str__(self):
        return '(' + str(self.key) + ', ' + str(self.value) + ')'


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_front(self, key, value):
        """Create a new node and inserts it at the front of the linked list
        Args:
            key: the key for the new node
            value: the value for the new node"""
        new_node = SLNode(key, value)
        new_node.next = self.head
        self.head = new_node
        self.size = self.size + 1

    def remove(self, key):
        """Removes node from linked list
        Args:
            key: key of the node to remove """
        if self.head is None:
            return False
        if self.head.key == key:
            self.head = self.head.next
            self.size = self.size - 1
            return True
        cur = self.head.next
        prev = self.head
        while cur is not None:
            if cur.key == key:
                prev.next = cur.next
                self.size = self.size - 1
                return True
            prev = cur
            cur = cur.next
        return False

    def contains(self, key):
        """Searches linked list for a node with a given key
        Args:
            key: key of node
        Return:
            node with matching key, otherwise None"""
        if self.head is not None:
            cur = self.head
            while cur is not None:
                if cur.key == key:
                    return cur
                cur = cur.next
        return None

    def __str__(self):
        out = '['
        if self.head != None:
            cur = self.head
            out = out + str(self.head)
            cur = cur.next
            while cur != None:
                out = out + ' -> ' + str(cur)
                cur = cur.next
        out = out + ']'
        return out


def hash_function_1(key):
    hash = 0
    for i in key:
        hash = hash + ord(i)
    return hash


def hash_function_2(key):
    hash = 0
    index = 0
    for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
    return hash


class HashMap:
    """
    Creates a new hash map with the specified number of buckets.
    Args:
        capacity: the total number of buckets to be created in the hash table
        function: the hash function to use for hashing values
    """

    def __init__(self, capacity, function):
        self._buckets = []
        for i in range(capacity):
            self._buckets.append(LinkedList())
        self.capacity = capacity
        self._hash_function = function
        self.size = 0

    def clear(self):
        """
        Empties out the hash table deleting all links in the hash table.
        """
        #loop thru the hashmap and check if the size is greater than 0
        #if greater than zero set the head to none and decrease the size to 0
        #to clear the hashmap
        for b in self._buckets:
            if b.size > 0:
                b.head = None
                b.size = 0
        self.size = 0
        return

    def get(self, key):
        """
        Returns the value with the given key.
        Args:
            key: the value of the key to look for
        Return:
            The value associated to the key. None if the link isn't found.
        """
        #similar to put however we return the value instead of updating
        #compute the index
        index = self._hash_function(key) % self.capacity
        #temp variable to hold the value of the key
        temp = self._buckets[index]
        #return the value if the key is not none
        if temp.contains(key) is not None:
            linked_node = temp.contains(key)
            return linked_node.value 
        else:
            return None

    def resize_table(self, capacity):
        """
        Resizes the hash table to have a number of buckets equal to the given
        capacity. All links need to be rehashed in this function after resizing
        Args:
            capacity: the new number of buckets.
        """
        #create a new bucket to resize the table
        new_bucket = []
        #insert new linked lists until new capacity is reached
        for c in range(capacity):
            new_bucket.append(LinkedList())
        #resize the hashmap capacity
        self.capacity = capacity
        #loop thru the bucket and check if the head is not None to rehash the links and its key-values
        for b in self._buckets:
            while b.head is not None:
                index = self._hash_function(b.head.key) % self.capacity
                #temp variable to hold the values of the new bucket
                temp = new_bucket[index]
                #add key-values to front in the new hashmap
                temp.add_front(b.head.key, b.head.value)
                b.head = b.head.next
        #set the old hashmap to the new hashmap
        self._buckets = new_bucket
        return

    def put(self, key, value):
        """
        Updates the given key-value pair in the hash table. If a link with the given
        key already exists, this will just update the value and skip traversing. Otherwise,
        it will create a new link with the given key and value and add it to the table
        bucket's linked list.

        Args:
            key: they key to use to has the entry
            value: the value associated with the entry
        """
        #compute the index
        index = self._hash_function(key) % self.capacity
        #temp variable to hold the value
        temp = self._buckets[index]
        #check if key is not None and set that value to the value being passed
        if temp.contains(key) is not None:
            linked_node = temp.contains(key)
            linked_node.value = value
            return
        #if the key is none then add the value to the front and increase the size
        else:
            temp.add_front(key, value)
            self.size = self.size + 1
            return

    def remove(self, key):
        """
        Removes and frees the link with the given key from the table. If no such link
        exists, this does nothing. Remember to search the entire linked list at the
        bucket.
        Args:
            key: they key to search for and remove along with its value
        """
        #compute the index
        index = self._hash_function(key) % self.capacity
        #temp variable to hold the key value
        temp = self._buckets[index]
        #check if key is not in hashmap
        if temp.remove(key) is False:
            return
        else:
            #decrease the size
            self.size = self.size - 1
            return

    def contains_key(self, key):
        """
        Searches to see if a key exists within the hash table

        Returns:
            True if the key is found False otherwise

        """
        #calculate the hash index
        index = self._hash_function(key) % self.capacity
        #get the value
        temp = self._buckets[index]
        #return True if the key is found
        if temp.contains(key) is not None:
            return True
        else:
            return False

    def empty_buckets(self):
        """
        Returns:
            The number of empty buckets in the table
        """
        #keep track of the number of empty buckets in the table
        count = 0
        #loop thru the buckets to determine if the size is zero
        #if size is zero increment count to track number of empty buckets
        for b in self._buckets:
            if b.size == 0:
                count += 1
        return count

    def table_load(self):
        """
        Returns:
            the ratio of (number of links) / (number of buckets) in the table as a float.

        """
        return float(self.size / self.capacity)

    def __str__(self):
        """
        Prints all the links in each of the buckets in the table.
        """

        out = ""
        index = 0
        for bucket in self._buckets:
            out = out + str(index) + ': ' + str(bucket) + '\n'
            index = index + 1
        return out
