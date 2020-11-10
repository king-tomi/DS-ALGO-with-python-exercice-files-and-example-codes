class Empty(Exception): pass

class _DoublyLinkedBase:
    """A private implementation providing a base class for the Doubly linked list representation"""

    class Node:

        __slots__ = "_element","_prev","_next"

        def __init__(self,element,prev,next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """initializes an empty list to hold the header node and trailer node"""
        self._header = self.Node(None,None,None)
        self._trailer = self.Node(None,None,None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self,e,predecessor,successor) -> Node:
        newest = self.Node(e,predecessor,successor) #creates a new node with the corresponding neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self,node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None #ensuring node is empty
        return element