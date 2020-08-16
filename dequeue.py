author = """AYODABO TOMISIN KOLAWOLE"""
date_created = """16 August 2020"""

"""This code is an exercise code from the Data Structures and Algorithms with Python book

   The mesage remains the same, 'extend' not 'modify'"""




class Empty(Exception):
    pass

class Dequeue:

    MAX_CAPACITY = 10

    def __init__(self):
        self._data = [None] * Dequeue.MAX_CAPACITY
        self._size = 0
        self._front = 0
        self._last = -1
    
    def first(self):
        if self.isempty():
            raise Empty("Dequeue is empty")
        return self._data[self._front]

    def isempty(self) -> bool:
        return self._size == 0

    def last(self):
        if self.isempty():
            raise Empty("Dequeue is empty")
        return self._data[self._last]

    def __len__(self):
        return self._size

    def resize(self,cap):
        """resizes the dequeue to the specified amount of capacity"""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    def add_first(self,e):
        """adds an element at the beginning of the dequeue"""
        if len(self._data) == self._size:
            self.resize(2*len(self._data))
        avail = (self._front + self._size) % (len(self._data))
        self._data[avail] = e
        self._size += 1

    def add_last(self,e):
        """adds an element to the end of the dequeue"""
        if len(self._data) == Dequeue.MAX_CAPACITY:
            self.resize(2*len(self._data))
        prev, self._data[-1] = self._data[-1], e  #item swapping here
        past = (self._size + self._last - 2)  % len(self._data)
        self._data[past] = prev
        self._size += 1

    def delete_first(self):
        """deletes and returns the first element in the dequeue"""
        if self.isempty():
            raise Empty("Dequeue is empty")
        res, self._data[self._front] = self._data[self._front], None
        self._front = (self._front - 1) % len(self._data)
        self._size -= 1
        return res

    def delete_last(self):
        """deletes an element at the end of the dequeue"""
        if self.isempty():
            raise Empty("Dequeue is empty")
        res, self._data[self._last] = self._data[self._last], None
        self._last = (self._last + self._size - 1) % len(self._data)
        self._size -= 1
        return res