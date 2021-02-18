author = """AYODABO TOMISIN KOLAWOLE"""
date_created = """16 August 2020"""

"""This code is an exercise code from the Data Structures and Algorithms with Python book

   The mesage remains the same, 'extend' not 'modify'"""




class Empty(Exception):
    pass

class Dequeue:

    """
        This is a custom implementation to mimic python's standard collections.Dequeue class

        Args:
            max_length: sn integer indicating the maximum length the Dequeue can take

        Author:
            Ayodabo Tomisin

    """
    

    MAX_CAPACITY = 10

    def __init__(self,max_length: int=None):
        self._data = [None] * Dequeue.MAX_CAPACITY
        self._size = 0
        self._front = 0
        self._last = -1
        self._max_length = max_length
    
    def first(self):
        if self.is_empty():
            raise Empty("Dequeue is empty")
        return self._data[self._front]

    def is_empty(self) -> bool:
        return self._size == 0

    def last(self):
        if self.is_empty():
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
        if len(self._data) == self._max_length:  #checks if maximum length has been reached
            avail = (self._front + self._size) % (len(self._data))
            self._data[avail] = e
            self._data.pop()

        if len(self._data) == self._size:
            self.resize(2*len(self._data))
        avail = (self._front + self._size) % (len(self._data))
        self._data[avail] = e
        self._size += 1

    def add_last(self,e):
        """adds an element to the end of the dequeue"""
        if len(self._data) == self._max_length:  #checks if maximum length has been reached
            self._data.append(e)
            self._data.pop(0)

        if len(self._data) == self._size:
            self.resize(2*len(self._data))
        self._data.append(e)
        self._size += 1

    def delete_first(self):
        """deletes and returns the first element in the dequeue"""
        if self.is_empty():
            raise Empty("Dequeue is empty")
        res, self._data[self._front] = self._data[self._front], None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return res

    def delete_last(self):
        """deletes an element at the end of the dequeue"""
        if self.is_empty():
            raise Empty("Dequeue is empty")
        self._size -= 1
        self._data.pop()

    def __str__(self):
        return f"<{item for item in self._data}>"

    def __getitem__(self,j):
        if self.is_empty():
            raise Empty("Dequeue is Empty")

        if j < 0:    #accommodating indexes less than zero
            j += self._size
        return self._data[j]

    def __setitem__(self,j,value):
        if j > self._size:    #raises error if greater than the size
            raise IndexError("Index out of range")

        if j < 0:               #accepts negative index
            j += self._size  
        self._data[j] = value

    def clear(self):
        if self.is_empty():
            raise Empty("Dequeue is empty")
        self._data = [None for _ in range(Dequeue.MAX_CAPACITY)]  #clears the entire dequeue

    def count(self,e):
        """counts the occurence of e in self._data"""
        if self.is_empty():
            raise Empty("Dequeue is empty")
        return self._data.count(e)

    def remove(self,e):
        """removes the first matching element eqaul to e"""
        if self.is_empty():
            raise Empty("Dequeue is empty")
        for i,item in enumerate(self._data):
            if item == e:
                self._data[i] = None
                self._size -= 1
                break
            else:
                continue