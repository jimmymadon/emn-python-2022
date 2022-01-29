# Use if-elif-else or if-else or if to ask user which operation to print

print("""
Type of operations:
1: Addition
2: Subtraction
3: Multiplication
4: Division
""")
operation_type = int(input("Select an operation (number): "))
if (operation_type < 1 or operation_type > 4):
  print("Invalid Operation - Please try again.")
  exit()

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

addition_result = number1 + number2
print("Addition Result: " + str(addition_result))

subtraction_result = number1 - number2
print("Subtraction Result: " + str(subtraction_result))

multiplication_result = number1 * number2
print("Multiplication Result:", multiplication_result)

division_result = number1 / number2
print("Division Result:", round(division_result, 2))
