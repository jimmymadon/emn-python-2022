# Define and call functions for each of the operations (add, subtract, multiply and divide)

def add(num1, num2):
  addition_result = num1 + num2
  print("Addition Result: " + str(addition_result))

def subtract(num1, num2):
  subtract_result = num1 - num2
  print("Subtract Result: " + str(subtract_result))

def multiply(num1, num2):
  multiplication_result = num1 * num2
  print("Multiplication Result: " + str(multiplication_result))

def divide(num1, num2):
  division_result = num1 / num2
  print("Division Result: " + str(division_result))

# All the above functions are of void / none type
result = add(10, 12)
print("Return type of the add function:", type(result))

print("""
Menu:
1: Addition
2: Subtraction
3: Multiplication
4: Division
""")

while True:
  chosen_operation = int(input("Enter a number from the above menu: "))
  if (chosen_operation < 1 or chosen_operation > 4):
    print("Invalid Option. Please retry!")
  else:
    break

# Taking string input and casting (converting) them to int
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if chosen_operation == 1:
    add(number1, number2)
elif chosen_operation == 2:
    subtract(number1, number2)
elif chosen_operation == 3:
    multiply(number1, number2)
elif chosen_operation == 4:
    divide(number1, number2)
