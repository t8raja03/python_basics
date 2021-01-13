## Basics of Python programming, spring 2021
## Jarno Rankinen TVT19KMO
## Exercise 2

num = input("Please enter a number, I will check if it's smaller or larger than 10: ")

# Check that the user entered an integer or a float:
try:
    num = int(num)    # try if it's possible to parse an integer from the input
except Exception:
    try:
        num = float(num)  # if not, try parsing a float
    except Exception:
        # If neither is possible
        print("Please enter either a floating point number or an integer.")
        exit

# Generate the output string:
if num < 10:
    rel = 'less than '
elif num == 10:
    rel = ''
else:
    rel = 'greater than '
    
print(str(num) + " is " + rel + "10")