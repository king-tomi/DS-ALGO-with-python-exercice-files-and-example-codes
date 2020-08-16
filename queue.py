author = """AYODABO TOMISIN KOLAWOLE"""
date_created = """16 August 2020"""

"""This code is an example from the Data Structures and Algorithms with Python book.

   You can copy and edit this code as you wish but remember, try not to 'modify' but 'extend'
   
   Have a good read and a nice time."""


class Empty(Exception):
    pass

class Queue:

    DEFAULT_CAPACITY  = 10

    def __init__(self):
        self._data = [None] * Queue.DEFAULT_CAPACITY
        self._front = 0
        self._size = 0

    def last(self):
        if self.isempty():
            raise Empty("Queue is empty")
        return self._data[-1]

    def first(self):
        if self.isempty():
            raise Empty("Queue is empty")
        return self._data[self._front]

    def isempty(self) -> bool:
        return self._size == 0

    def __len__(self) -> int:
        return self._size

    def dequeue(self):
        """removes an element at the beginning of the queue"""
        if self.isempty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self,e):
        """attempts to add an element at the beginning by checking if it is full. if it is,
        it resizes the array and then perform the operation"""
        if len(self._data) == self._size:
            self.resize(2*len(self._data))
        avail = (self._front + self._size) % (len(self._data))
        self._data[avail] = e
        self._size += 1

    def resize(self,cap):
        """resizes the queue to the specified amount of capacity"""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0