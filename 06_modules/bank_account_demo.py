import bank_account

# Ask the user to input the starting balance
current_balance = float(input("Enter your starting balance"))

# Ask the user the amount to deposit
balance = bank_account.deposit(current_balance)

# Ask the user the amount to withdraw
balance = bank_account.withdraw(balance)

# Print "You are rich!" if balance > 10, otherwise print "Work harder!"
bank_account.display_status(balance)

# Ask the user the amount to deposit
balance = bank_account.deposit(balance)

# Ask the user the amount to withdraw
balance = bank_account.withdraw(balance)

# Print "You are rich!" if balance > 10, otherwise print "Work harder!"
bank_account.display_status(balance)
