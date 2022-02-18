# define a function that takes one parameter and asks the user for input
# this function returns the sum or the parameter and the user's input
def deposit(current_balance):
  deposit_amount = float(input("Enter the amount to deposit"))
  current_balance = current_balance + deposit_amount
  print("Amount deposited: ", deposit_amount)
  print("Updated balance: ", current_balance)
  return current_balance

def withdraw(current_balance):
  withdraw_amount = float(input("Enter the amount to withdraw"))
  current_balance = current_balance - withdraw_amount
  print("Amount withdrawn: ", withdraw_amount)
  print("Updated balance: ", current_balance)
  return current_balance

def display_status(current_balance):
  print("Your balance is:", current_balance)
  if current_balance > 10:
    print("You are rich!")
  else:
    print("Work harder!")
