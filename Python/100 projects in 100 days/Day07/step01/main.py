word_list =["aardvark","baboon", "camel"]
import random
chosen_word=random.choice(word_list)
print(chosen_word)

placeholder =""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder+="_"
print(placeholder)

guess= input("guess a letter:").lower()
print(guess)

display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display)