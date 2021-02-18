class Vector:
    """a class that represents a vector

       This is an example code in the Data Structures and Algorithm book
       and which i performed extra exercices on it
    
       Author: Ayodabo Tomisin Kolawole
       
       E-mail: ayodabooluwatomisin@gmail.com

       github: https://github.com/king-tomi
    """

    def __init__(self,n: int=0,items=None):
        """creates a vector with either an integer or an iterable of numbers
        
           n: integer defaults to zero

           items: iterable of numbers defaults to None
        """
        if items is not None:
            for item in items:
                if not self._validate(item):
                    raise TypeError("only numbers are allowed")
            self._data = list(items)
        else:
            self._data = [0] * n
        self._k = -1

    def __len__(self) -> int:
        return len(self._data)

    def __getitem__(self,i: int) -> int:
        """returns item at index i. supports negative indices too"""
        if i < 0: #for negative indices
            i += len(self._data)

        if i > len(self._data):  #when i is greater than the length
            raise IndexError("Index is out of range")

        return self._data[i]

    def __setitem__(self,i: int,v: int):
        """sets an item v at an index i. supports negative indices"""
        if i < 0:
            i += len(self._data)

        if i > len(self._data):
            raise IndexError

        self._data[i] = v

    def __add__(self,other):
        """adds two vectors"""

        if len(self) != len(other):
            raise ValueError("vectors do not match")

        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self._data[i] + other[i]
        self._data = result._data
        return result

    def __sub__(self,other):
        """subtracts two vectors"""

        if len(self) != len(other):
            raise ValueError("Vectors do not match")

        result = Vector(len(self))
        for i,v in enumerate(self._data):
            result[i] = v - other[i]
        return result

    def __mul__(self,other: [int,any]):
        """multiplies the vector with either a number or another vector
        
            when other is an integer, it performs scalar multiplication

            when other is a list or vector, it performs dot multiplication
        """
        if isinstance(other,int):
            new = [0] * len(self._data)

            for i,v in enumerate(self._data):
                new[i] = v * other
            self._data = new
            return self
        else:
            if len(self) != len(other):
                raise ValueError("Vectors do not match")
            res = Vector(len(self))
            for i,v in enumerate(self._data):
                res[i] = v * other[i]
            return sum(res._data)

    def __neg__(self):
        """negates a vector"""
        result = Vector(len(self))
        for i,v in enumerate(self._data):
            result[i] = -v
        return result

    def __eq__(self,other) -> bool:
        return self._data == other._data

    def __ne__(self,other) -> bool:
        return not self == other

    def __str__(self) -> str:
        return f"<{str(self._data)[1:-1]}>"

    def __repr__(self) -> str:
        return f"Vector<{str(self._data)[1:-1]}>"

    def __iter__(self):
        return self

    def __next__(self):
        self._k += 1
        if self._k < len(self._data):
            return self._data[self._k]
        else:
            raise StopIteration

    def index(self,v) -> int:
        if v in self._data:
            return self._data.index(v)
        else:
            raise ValueError("Item not a vector coordinate")

    @staticmethod
    def _validate(x) -> bool:
        return isinstance(x,(int,float))



if __name__ == "__main__":
    vec = Vector(5)
    print(vec + [1,2,3,4,5])
    print(vec * [1,2,3,4,5])
    print(vec - [1,1,1,1,1])
    print(-vec)
    print(vec[-5])
    print(vec * 2)