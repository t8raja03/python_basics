## Basics of Python programming, spring 2021
## Jarno Rankinen TVT19KMO
## Exercise 4
## Files: main.py, student.py

class Student:
    def __init__(self, fname, lname, stGroup):
        self.fname = fname
        self.lname = lname
        self.stGroup = stGroup

    def info(self):
        print("Student " + self.fname + " " + self.lname +
        " is a member of group " + self.stGroup)
    