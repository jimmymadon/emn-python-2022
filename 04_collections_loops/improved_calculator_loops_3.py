# Example of using continue and break within a while loop to control flow
while True:
  print("""
  Menu:
  add: Addition
  sub: Subtraction
  mul: Multiplication
  div: Division
  quit: Quit the program
  """)

  valid_operations = ["add","sub","mul","div","quit"]
  chosen_operation = input("Enter an operation from the above menu: ")

  if (chosen_operation not in valid_operations):
    print("Invalid Operation! Please try again!")
    continue

  if (chosen_operation == "quit"):
      print("Goodbye!")
      exit()

  # Taking string input and casting (converting) them to int
  number1 = int(input("Enter the first number: "))
  number2 = int(input("Enter the second number: "))

  if chosen_operation == "add":
      addition_result = number1 + number2
      print("Addition Result: " + str(addition_result))
      break
  elif chosen_operation == "sub":
      subtraction_result = number1 - number2
      print("Subtraction Result: " + str(subtraction_result))
      break
  elif chosen_operation == "mul":
      multiplication_result = number1 * number2
      print("Multiplication Result: ", multiplication_result)
      break
  elif chosen_operation == "div":
      division_result = number1 / number2
      print("Division Result: ", division_result)
      break
