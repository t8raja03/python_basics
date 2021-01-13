## Basics of Python programming, spring 2021
## Jarno Rankinen TVT19KMO
## Exercise 1

str_in = input("Please enter 3 numbers separated with a space, I will calculate their average: ")

numbers = str_in.split()    # Split the input string to an array

sum = 0
for i in range(0,len(numbers)):     # Calculate the sum of input numbers
    sum += int(numbers[i])

avg = sum / len(numbers)            # Count the average

print("The average value is " + str(avg) + ".")