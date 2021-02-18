class Empty(Exception): pass

class LinkedQueue:

    class Node:

        __slots__ = "_element","_next"

        def __init__(self,element,next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._head._element

    def enqueue(self,e):
        newest = self.Node(e,None)
        if self.is_empty():
            self._head = newest  #case of queue is empty
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._head._element
        self._head = self._head._next #new head is the next of old head
        self._size -= 1
        if self.is_empty():   #special case of empty queue
            self._tail = None
        return answer