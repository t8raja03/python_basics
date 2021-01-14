## Basics of Python programming, spring 2021
## Jarno Rankinen TVT19KMO
## Exercise 3

# First get the amount of numbers
amount = int(input("How many numbers are you going to input? "))

numbers = [] # Initialise an empty array 

# Do this AMOUNT number of times
for i in range(0,amount):
    # append number to numbers-list
    numbers.append(int(input("Please input a number (" + str(amount - i -1) + " remaining): ")))

sum = 0 # initialize variable for sum

# Calculate the sum of numbers
for j in range(0,len(numbers)):
    sum += numbers[j]

avg = sum / len(numbers) # Calculate the average of the numbers

print("The average of the given numbers is " + str(avg) + ".")
