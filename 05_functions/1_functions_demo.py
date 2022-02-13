# # This is an example of copy-pasting or repeating groups of lines of code 3 times
# print("Hi, the class of M2 students!")
# print("Hope you are having fun learning Python!")
# print()

# print("Hi, the class of M2 students!")
# print("Hope you are having fun learning Python!")
# print()

# print("Hi, the class of M2 students!")
# print("Hope you are having fun learning Python!")
# print()

# # Loop and print something 3 times
# counter = 0
while (counter < 3):
  print("Hi, the class of M2 students!")
  print("Hope you are having fun learning Python!")
  print()
  counter = counter + 1

# # Loop using for and range() 3 times
print("Loop using for and range(3) - 3 times")
for x in range(3):
  print("Hi, the class of M2 students!")
  print("Hope you are having fun learning Python!")
  print()

# DEFINE (or creating) a function which is a group of lines of code
# Example of a function with no input (paramaters) and no output (return value)
def greeting():
  print("Hi, the class of M2 students!")
  print("Hope you are having fun learning Python!")
  print()

# # CALLING or (= running) the function
greeting()

print("Loop inside a function using for and range(3) - 3 times")
for x in range(3):
  greeting()

# Example of a function with a output or "return value" of string
def greeting_with_return():
  return "Hello everyone!"

print()
print("greeting_with_return() returns a String")
value = greeting_with_return()
print("value:", value)
print("Type of value:", type(value))
print()

print ("greeting() does NOT return anything but prints the greeting!")
value2 = greeting()
print("value2:", value2)
print("Type of value2:", type(value2))

# Example of a function that returns an int
def large_number():
  return 9834543

# We can use the return value directly (not put it inside a variable)
print("Use the large_number() function directly")
print("Return of large_number():", large_number())
print(type(large_number()))
print(large_number() + 1)

# Example of a function that has INPUT = PARAMETERS and OUTPUT = RETURN VALUE
def add(number1, number2):
  if (type(number1) != int or type(number2) != int):
    return "Error! Numbers should be an int"
  return number1 + number2

result1 = add(5, 10)
print("result1: ", result1)

result2 = add(12, 8)
print("result2: ", result2)

print("4 + 7 = ", add(4, 7))

print("4.5 + 5.5 = ", add(4.5, 5.5))

print(add("hello", "world"))
