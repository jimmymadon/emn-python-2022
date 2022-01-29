marks = int(float(input("Enter your marks: ")))

# Example of the "number-line" that I drew in my head for this program
# -infinity, 0, 40, 60, 70, 100, +infinity
# In such cases, always check that the WHOLE number line is taken care by your program.

# Method 1: The below code uses ONE if-elif-else block
# if marks > 100 or marks < 0:
#     print("Invalid Marks!")
# elif marks >= 70:
#     print("Distinction!")
# elif marks >= 40:
#     print("Pass!")
# else:
#     print("Fail!")



# Method 2: Similar to above but remove elif - else and use exit() instead.
# This method will not execute further if it reaches any exit() function.
# if marks > 100 or marks < 0:
#   print("Invalid Marks!")
#   exit()
# if marks >= 70:
#   print("Distinction!")
#   exit()
# if marks >= 60:
#   print("First Class!")
#   exit()
# if marks >= 40:
#   print("Pass")
# else:
#   print("Fail!")

# print("This is out of the if-elif-else block")



# Method 3: (Without elif-else) The below code uses 5 separate if blocks
# ALL the if statements below WILL RUN as we don't exit()
if marks > 100 or marks < 0:
    print("Invalid Marks!")
if marks >= 70:
    print("Distinction!")
if marks >= 60:
    print("First Class!")
if marks >= 40:
    print("Pass!")
if marks >= 0:
    print("Fail!")
