## Basics of Python programming, spring 2021
## Jarno Rankinen TVT19KMO
## Exercise 5
## Files: main.py, Binomi.py

class Binomi:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        

    def factorial(self, a):
        ## Calculate the factorial of an integer
        try:
            int(a) # Test if a is an integer, exit otherwise
        except:
            return False
        if a > 0:
            factorial_a = 1
            for i in range(1,a+1): # e.g. when a=3, loop from 1 to 3
                factorial_a = factorial_a * i
                # e.g. when a=3:
                #    1 * 1 = 1
                # => 1 * 2 = 2
                # => 2 * 3 = 6
            return factorial_a
        else:
            return False

    def calculate_binomi(self):
        # First check that 0<k<n
        if  self.n < 0:
            return False
        elif self.k >= self.n:
            return False
        elif self.k <= 0:
            return False
        else:
            # calculate n choose k
            b = self.factorial(self.n) / (self.factorial(self.k) * self.factorial(self.n - self.k))
            return b