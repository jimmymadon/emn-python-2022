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
