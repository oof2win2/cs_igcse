#!bin/bash/env python
import random, time

# word = random.choice(words).lower()
def hangman(word, totGuesses):
    word = word.lower()
    foundWord = ["_"] * len(word)
    guesses = 0
    points = 0
    # print("\n"*100)
    while True:
        time.sleep(0.2)
        print("Wrong guesses:", guesses, "of", totGuesses)
        print("Current word is", "".join(foundWord))  # make the array into a str
        letter = input("Letter: ").lower()
        if letter not in word:  # if the letter is not in the word
            guesses += 1
            print(f"Letter '{letter}' is not in the word. You have {totGuesses - guesses} remaining guesses")
            # print("\n")
        else:  # if the letter is in the word
            for i in range(len(word)):
                if word[i] == letter:
                    foundWord[i] = letter
            print("Current found word is", "".join(foundWord))
        print("\n")
        if "_" not in foundWord:  # underscore is letters not found
            print("Game won!")
            points += 10
            return [True, totGuesses - guesses]  # winning
        if guesses == totGuesses:
            print("Game lost.")
            return [False, tot - guesses]  # losing


easyWords = ["potato", "couch", "sleep", "running", "hammer"]
mediWords = ["English", "Busstop", "McDonalds", "Textbook"]
hardWords = ["Chemistry", "Ubiquitous", "Basement", "Machinegun"]

pts = 0
while True:
    if pts < 10:
        word = random.choice(easyWords)
    elif pts > 10 and pts < 30:
        word = random.choice(mediWords)
    else:
        word = random.choice(hardWords)
    print(f"word: {word}")  # debug
    res = hangman(word, 10)
    # print(res)
    pts += res[1]  # points are the amount of total guesses - wrong guesses
    print("Your points are:", str(pts) + ". New game has started")
