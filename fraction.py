class Fraction:
    """
    Class representation of fractions

    Attributes:
        _top (int):
        _bottom (int):

    Args:
        top (int):
        bottom (int):

    """
    
    def __init__(self,top: int, bottom: int):
        if self._validate(top) and self._validate(bottom):
            if bottom < 0:
                gcd = self.gcd(abs(top),abs(bottom))
                self._top = -top // gcd
                self._bottom = -bottom // gcd
            else:
                gcd = self.gcd(abs(top),abs(bottom))
                self._top = top // gcd
                self._bottom = bottom // gcd
        else:
            raise ValueError("numerator and denominator must be integers")

    #---------------helper methods-----------------
    @staticmethod
    def _validate(x) -> bool:
        return isinstance(x,int)

    @staticmethod
    def gcd(x,y):
        while x % y != 0:
            old_x = x
            old_y = y

            x = old_y
            y = old_x % old_y
        return y

    @property
    def top(self):
        return self._top

    @top.setter
    def top(self,x):
        self._top = x

    @property
    def bottom(self):
        return self._bottom

    @bottom.setter
    def bottom(self,x):
        self._bottom = x

    #----------------main methods-----------------------
    def __str__(self) -> str:
        return f"{self._top}/{self._bottom}"

    def __repr__(self):
        return f"Fraction<{self.top}/{self.bottom}>"

    def __add__(self,other):
        top = self.top * other.bottom + self.bottom * other.top
        bottom = self.bottom * other.bottom
        if top == 0:
            return 0
        return Fraction(top,bottom)

    def __sub__(self,other):
        top = self.top * other.bottom - self.bottom * other.top
        bottom = self.bottom * other.bottom
        if top == 0:
            return 0
        return Fraction(top,bottom)

    def __truediv__(self,other):
        top = self.top * other.bottom
        bottom = self.bottom * other.top
        if bottom == 1:
            return top
        return Fraction(top,bottom)

    def __mul__(self,other):
        top = self.top * other.top
        bottom = self.bottom * other.bottom
        return Fraction(top,bottom)

    def __eq__(self,other) -> bool:
        top = self.top * other.bottom
        o_top = self.bottom * other.top
        return top == o_top

    def __ne__(self,other) -> bool:
        top = self.top * other.bottom
        o_top = self.bottom * other.top
        return top != o_top

    def __lt__(self,other) -> bool:
        top = self.top * other.bottom
        o_top = self.bottom * other.top
        return top < o_top

    def __le__(self,other) -> bool:
        top = self.top * other.bottom
        o_top = self.bottom * other.top
        return top <= o_top

    def __gt__(self,other) -> bool:
        top = self.top * other.bottom
        o_top = self.bottom * other.top
        return top > o_top

    def __ge__(self,other) -> bool:
        top = self.top * other.bottom
        o_top = self.bottom * other.top
        return top >= o_top




if __name__ == "__main__":
    first = Fraction(2,3)
    second = Fraction(2,-3)
    print(first / second)