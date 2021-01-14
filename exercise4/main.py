## Basics of Python programming, spring 2021
## Jarno Rankinen TVT19KMO
## Exercise 4
## Files: main.py, student.py

from student import Student

print("This program creates a list of Student class objects\nand prints them on the screen")
studentList = []

studentList.append(Student("Tupu", "Ankka", "5A"))
studentList.append(Student("Hupu", "Ankka", "5B"))
studentList.append(Student("Lupu", "Ankka", "5C"))

print("\nFirst print the first student in the list:")
studentList[0].info()

print("\nThen print the info of all the students in the list:")
for st in studentList:
    st.info()