# Below four lines show 3 disconnected individual variables.
# Hence, for related data, we use Collections (Lists, Tuples, Sets, Dictionaries)
marks1 = 100
marks2 = 90
marks3 = 50
marks99 = 76
marks100 = 67
print("Variable marks2:", marks2)
print("Variable marks3:", marks3)

## Lists ##

# Below we create a list
print("*** Creating a list with 5 elements ***")
students_marks = [100, 90, 50, 76, 67]
print("Type of collection students_marks:", type(students_marks))

print("Printing the whole list")
print(students_marks)

# Accessing individual items of a list using their index
print("students_marks[1]:", students_marks[1])
print("students_marks[2]:", students_marks[2])

# List items can be changed
students_marks[1] = 40
print("Printing modified list:")
print(students_marks)

# Finding the size of a list
print("Length of students_marks:", len(students_marks))

# Inserting items to the END of the list using the append() function
print("*** Appending items the END of our list ***")
students_marks.append(45)
print("Length of students_marks after append:", len(students_marks))

# Inserting items in between the list using the insert() function
students_marks.insert(2,10)
print("students_marks[2]:",  students_marks[2])
print("Length of students_marks after insert:", len(students_marks))


## Tuples ##
