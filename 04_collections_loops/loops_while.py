# Two ways to come out of a while loop

# Using the while condition statement
print("***While loop with condition statement***")
counter = 0
while counter < 10:
  print(counter)
  counter = counter + 1

print("***While loop with always True statement and break***")
# Using the break statement at the start of the loop
counter = 0
while True:
  if (counter >= 10):
    break
  print(counter)
  counter = counter + 1
