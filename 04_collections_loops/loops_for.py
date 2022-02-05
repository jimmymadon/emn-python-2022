bank_balances = [10.00, 503.87, 11001.90, 1000.00]

# The below way to print all items of a list is very repetitive
# and it requires duplicate code!
print(bank_balances[0])
print(bank_balances[1])
print(bank_balances[2])
print(bank_balances[3])
print() # Print an empty line

print("***Printing all items in a list***")
for bank_balance in bank_balances:
  print(bank_balance)

print()

print("***Sum of all balances***")
sum_result = 0
for bank_balance in bank_balances:
  sum_result = sum_result + bank_balance
  print(sum_result)
print("Final sum of all balances:", sum_result)
print()

average = sum_result / len(bank_balances)
print("Average of all bank balances:", average)
print()

largest_item = bank_balances[0]
for bank_balance in bank_balances:
  if (largest_item < bank_balance):
    largest_item = bank_balance
print("Largest balance of all bank balances:", largest_item)
print()

smallest_item = bank_balances[0]
for bank_balance in bank_balances:
  if (smallest_item > bank_balance):
    smallest_item = bank_balance
print("Smallest balance of all bank balances:", smallest_item)
print()

# Find the position of an item in a list
print("Position of 10.00:", bank_balances.index(11001.90))
print()
