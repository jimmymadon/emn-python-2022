# Define and call functions for each of the operations (add, subtract, multiply and divide)
def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  return num1 / num2

# All the above functions are of int / float type
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
    result = add(number1, number2)
    print("Addition result:", result)
elif chosen_operation == 2:
    print("Subtraction result:", subtract(number1, number2))
elif chosen_operation == 3:
    print("Multiplication result:", multiply(number1, number2))
elif chosen_operation == 4:
    print("Division result:", divide(number1, number2))

