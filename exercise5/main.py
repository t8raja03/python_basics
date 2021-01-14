## Basics of Python programming, spring 2021
## Jarno Rankinen TVT19KMO
## Exercise 5
## Files: main.py, Binomi.py

from Binomi import Binomi

str_n = input("Input the numbers from which the binomial is to be calculated,\nseparated by space (0<k<n, 'n k', e.g. '4 2'): ")
numbers = str_n.split()

if len(numbers) > 2:
    print("Too many coefficients, exiting...")
    exit

else:
    b = Binomi(int(numbers[0]),int(numbers[1]))
    print("The value of " + numbers[0] + " choose " + numbers[1] + " is " + str(int(b.calculate_binomi())) + ".")