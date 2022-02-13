# Ask the user to input the starting balance
balance = float(input("Enter your starting balance"))

# Ask the user the amount to deposit
deposit_amount = float(input("Enter the amount to deposit"))
balance = balance + deposit_amount
print("Amount deposited: ", deposit_amount)
print("Updated balance: ", balance)

# Ask the user the amount to withdraw
withdraw_amount = float(input("Enter the amount to withdraw"))
balance = balance - withdraw_amount
print("Amount withdrawn: ", withdraw_amount)
print("Updated balance: ", balance)

# Print "You are rich!" if balance > 10, otherwise print "Work harder!"
print("Your balance is:", balance)
if balance > 10:
  print("You are rich!")
else:
  print("Work harder!")

# Ask the user the amount to deposit
deposit_amount = float(input("Enter the amount to deposit"))
balance = balance + deposit_amount
print("Amount deposited: ", deposit_amount)
print("Updated balance: ", balance)

# Ask the user the amount to withdraw
withdraw_amount = float(input("Enter the amount to withdraw"))
balance = balance - withdraw_amount
print("Amount withdrawn: ", withdraw_amount)
print("Updated balance: ", balance)

# Print "You are rich!" if balance > 10, otherwise print "Work harder!"
print("Your balance is:", balance)
if balance > 10:
  print("You are rich!")
else:
  print("Work harder!")
