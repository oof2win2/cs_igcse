#!bin/bash/env python
import random

words = ["potato", "couch", "basic", "Monday", "hammer"]
# word = random.choice(words).lower()
word = "hammer"
found_word = ["_"] * len(word)
tot_guesses = int(input("amount of guesses: "))
guesses = 0
while True:
    print("Wrong guess", guesses, "of", tot_guesses)
    print("Current word is", "".join(found_word))
    letter = input("Letter: ").lower()
    if letter not in word:
        guesses += 1
        print(
            f"Letter '{letter}' is not in the word. You have {tot_guesses - guesses} remaining guesses"
        )
    else:
        lastIndex = 0
        for _ in word:
            found_word[word.index(letter, lastIndex)] = letter
            lastIndex = word.index(letter)
        print("Current found word is", "".join(found_word))
    if guesses == tot_guesses:
        print("Game lost.")
        break
