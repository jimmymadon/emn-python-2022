# When you create a parameter, python creates a new separate temporary variable
def deposit(balance):
  balance = balance + 100
  print("balance inside the function:", balance)
  return balance

balance = 500
deposit(balance)

print("balance outside the function:", balance)
