import operations

# operations.print_menu()
print(operations.menu)

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
    result = operations.add(number1, number2)
    print("Addition result:", result)
elif chosen_operation == 2:
    print("Subtraction result:", operations.subtract(number1, number2))
elif chosen_operation == 3:
    print("Multiplication result:", operations.multiply(number1, number2))
elif chosen_operation == 4:
    print("Division result:", operations.divide(number1, number2))
