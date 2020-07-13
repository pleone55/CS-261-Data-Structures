########################################################################################################
#Name: Paul Leone
#CS 261
#student_list.py
#4/15/2020
########################################################################################################


import numpy as np

# StudentList class is our implementation of Python's List
class StudentList:
    def __init__(self):
        # creates an empty array of length 4, change the [4] to another value to make an
        # array of different length.
        self._list = np.empty([4], np.int16)
        self._capacity = 4
        self._size = 0
    
    def __str__(self):
        return str(self._list[:self._size])
    
    # You may want an internal function that handles resizing the array.
    # Dont modify get_list or get_capacity, they are for testing
    
    def get_list(self):
        return self._list[:self._size]
    
    def get_capacity(self):
        return self._capacity
    
    #method to resize the array to be double in size
    def resize_array(self):
        """double the capacity of the list"""
        self._capacity = self._capacity * 2
        """reset the list with the new capacity value"""
        arr_list = np.empty([self._capacity], np.int16)
        """copy all data from old list to new list"""
        for i in range(self._size):
            arr_list[i] = self._list[i]
        self._list = arr_list
    
    #method to append items to the array
    def append(self, val):
        """if there is nothing in the array"""
        if self._size == 0:
            self.__init__()
        """check if the array size is full in order to resize or not"""
        if self._capacity == self._size:
            self.resize_array()
        """add the item to the list"""
        self._list[self._size] = val
        self._size = self._size + 1
    
    #method to remove the last item from the list
    def pop(self):
        """if there is no element in the list"""
        if self._size == 0:
            return print("There is no element to pop")
        val = self._list[self._size - 1]
        self.rearrange_array()
        return val
    
    #grabs the last element of the array
    def rearrange_array(self):
        """grab the last element"""
        self._size = self._size - 1
        """decrease array size"""
        arr_list = np.empty([self._size], np.int16)
        for i in range(self._size):
            arr_list[i] = self._size[i]
        self._list = arr_list
    
    #method to insert an item at index location
    def insert(self, index, val):
        """check if array size is full before inserting new item"""
        if self._capacity == self._size:
            self.resize_array()
        """insert new element"""
        self._list = np.insert(self._list, index, val)
        self._size = self._size + 1
    
    #method to remove item from array
    def remove(self, val):
        """set a counter to ensure the element in the list exists"""
        i = 0
        """loop thru the list to find the element"""
        for j in range(self._size):
            if self._list[j] == val:
                """find the first occurence of the value"""
                arr_list = np.delete(self._list, j)
                self.rearrange_array()
                i = 1
                break
        if i == 0:
            return print("No element to remove that is ", val)
    
    #method to clear the array content
    def clear(self):
        self._size = 0
        return print("The list is cleared")
    
    #method for counting the occurences of an item in the array
    def count(self, val):
        count = np.count_nonzero(self._list == val)
        print("There are a total of ", self._size, " elements")
        return count
    
    #method for returning a specified value in the array
    def get(self, index):
        print("the value of the element is ", self._list[index])
        return self._list[index]