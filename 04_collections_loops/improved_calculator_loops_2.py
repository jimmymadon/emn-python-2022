print("""
Menu:
add: Addition
sub: Subtraction
mul: Multiplication
div: Division
quit: Quit the program
""")

valid_operations = ["add","sub","mul","div","quit"]

# When there is a loop within a loop, the break statement takes you
# out of the 'nearest' loop that you are in.
while True:
  chosen_operation = input("Enter an operation from the above menu: ")

  isMatchFound = False
  for valid_operation in valid_operations:
    if (chosen_operation == valid_operation):
      isMatchFound = True
      break

  if (isMatchFound):
    break
  else:
    print("Invalid Operation! Please try again!")

# Taking string input and casting (converting) them to int
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if chosen_operation == 1:
    addition_result = number1 + number2
    print("Addition Result: " + str(addition_result))
elif chosen_operation == 2:
    subtraction_result = number1 - number2
    print("Subtraction Result: " + str(subtraction_result))
elif chosen_operation == 3:
    multiplication_result = number1 * number2
    print("Multiplication Result: ", multiplication_result)
elif chosen_operation == 4:
    division_result = number1 / number2
    print("Division Result: ", division_result)
