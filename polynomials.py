class Polynomials:
    """A Program to model a polynomial and calculates it's first derivative then output it
       in standard algebraic notation.

       degree: The degree of the polynomial

       coefficient: The literal variable i.e the variable of the polynomial.
       Date Modified: 29 - 06 - 2019
       Author: Ayodabo Tomisin Kolawole"""

    def __init__(self,degree: int,coefficient):
        self.degree = int(degree)
        self.coefficient = coefficient
        self.co_efficient = []
        self.n = self.degree - 1


    def get_degree(self):
        return self.degree

    def get_coefficient(self):
        return self.coefficient

    def _get_co_efficient(self):
        count = 0
        while count <= self.degree :
            co_efficient = int(input("enter co-efficients: "))
            self.co_efficient.append(co_efficient)
            count += 1

    def __str__(self):
        self._get_co_efficient()
        equation = ""
        for i in range(len(self.co_efficient)):
            equation = equation + str(self.co_efficient[i]) + str(self.coefficient) +  "^" + str(self.degree) + " + "
            self.degree -= 1
            if self.degree == -1:
                break
        return equation

    def derivative(self):
        """This calculates the first derivative and output it standard form."""
        new_derivative = " "
        new_coefficient = []
        for index in range(len(self.co_efficient)):
            new_coefficient.append(self.degree * self.co_efficient[index])    #appends the product of the coefficients
            self.degree -= 1                                                  # and the degree. reduces the degree by one
            if self.degree == 0:
                break

        new = self.degree + self.n

        for element in range(len(new_coefficient)):
            new_derivative =  new_derivative + str(new_coefficient[element]) + str(self.coefficient) +  "^" + str(new) + " + " #sets out the polynomial.
            new  -= 1
            if new == -1:
                break
        return new_derivative