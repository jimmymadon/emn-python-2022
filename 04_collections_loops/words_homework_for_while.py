# Create a list of words from the below list that are greater than 4 characters
words = ["hello", "but", "merci", "and", "oxford", "goodbye", "salut"]
print("*** Using for loop ***")
filtered_words = []
for word in words:
  if (len(word) > 4):
    filtered_words.append(word)
print("List with less than 4 letter words using for:", filtered_words)
print()

print("*** Using while loop with normal condition ***")
filtered_words2 = []
index = 0
while index < len(words):
  if (len(words[index]) > 4):
    filtered_words2.append(words[index])
  index = index + 1
print("List with less than 4 letter words using while:", filtered_words2)
print()

print("*** Using infinite true while loop with break ***")
filtered_words3 = []
index = 0
while True:
  if (index < len(words)):
    break
  if (len(words[index]) > 4):
    filtered_words3.append(words[index])
  index = index + 1
print("List with less than 4 letter words using infinite while:", filtered_words2)

# Create a list by asking the user to enter some words.
# If the user enters quit, print the list and break.
words = []
while True:
  chosen_word = input("Please enter a word: ")
  if (chosen_word == "quit"):
    print(words)
    break
  words.append(chosen_word)
print("Your chosen words were:", words)
