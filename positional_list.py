from doubly_base import _DoublyLinkedBase

class PositionalList(_DoublyLinkedBase):
    """
        A Sequential data structure that allows the access of its elements using positions

        Author: Ayodabo Tomisin Kolawole
       
        E-mail: ayodabooluwatomisin@gmail.com

        github: https://github.com/king-tomi
    """

    #-----------Nested Position class----------------
    class Position:
        """
            An abstraction representing a specific location of an element in the Positional list
        """

        __slots__ = "_container","_node"

        def __init__(self,container,node):
            self._container = container
            self._node = node

        @property
        def element(self):
            """returns the element stored at this position"""
            return self._node._element

        def __eq__(self,other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self,other):
            return not (self == other)

        def __str__(self):
            return f"<{self._node}>"


    #----------------Utility methods------------------
    def _validate(self,p):
        """
            a non-public method to validate a postion. returns the node at that position
            if it is a valid position
        """
        if not isinstance(p,self.Position):
            raise TypeError("p is not a position")

        if p._container is not self:
            raise ValueError("p does not belong to this container")

        if p._node._next is None:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self,node):
        """returns position instance for a given node(or None if sentinel)"""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self,node)
    #-----------------accessors-------------------
    def first(self):
        """returns the position of the first element"""
        return self._make_position(self._header._next)

    def last(self):
        """returns the position of the last element"""
        return self._make_position(self._trailer._prev)

    def after(self,p):
        """returns the position of element just after p"""
        node = self._validate(p)
        return self._make_position(node._next)

    def before(self,p):
        """returns the position of the element just before p"""
        node = self._validate(p)
        return self._make_position(node._prev)

    def __iter__(self):
        return self

    def __next__(self):
        """returns a forward iterator of the elements in the list"""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
    #---------------------mutators---------------------
    #override inherited _insert_between of the parent class to return position instead of node
    def _insert_between(self,e,predecessor,successor):
        """adds an element between existing nodes and returns the position"""
        node = super()._insert_between(e,predecessor,successor)
        return self._make_position(node)

    def add_first(self,e):
        """adds an element at the beginning of the list and returns the position"""
        return self._insert_between(e,self._header,self._header._next)

    def add_last(self,e):
        """adds an element at the end of the list and returns the position"""
        return self._insert_between(e,self._trailer._prev,self._trailer)

    def add_before(self,p,e):
        """adds an element e before position p and returns its position"""
        original = self._validate(p)
        self._insert_between(e,original._prev,original)

    def add_after(self,p,e):
        """adds an element e after position p and returns its position"""
        original = self._validate(p)
        return self._insert_between(e,original,original._next)

    def delete(self,p):
        """deletes node at position p and returns the element"""
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self,p,e):
        """replaces element at position p with node e and returns the replaced element"""
        original = self._validate(p)
        old,original._element = original._element,e
        return old