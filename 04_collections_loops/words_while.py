words = []
while True:
  chosen_word = input("Please enter a word: ")
  words.append(chosen_word)
  if (len(words) < 4):
    continue
  else:
    break

print("Your chosen words were:", words)
