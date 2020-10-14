#!bin/bash/env python
import random, time #import

# word = random.choice(words).lower()
def hangman(word, totGuesses): #define function with parameters
    word = word.lower() #make word lowercase so case is not an issue
    foundWord = ["_"] * len(word) #make an array of _ of the length of the word
    guesses = 0 #initialise variables
    points = 0	#initialise variables
    # print("\n"*100)
    while True: #iterate forever
        # time.sleep(0.2) #sleep for 2s
        print("Wrong guesses:", guesses, "of", totGuesses) #print amount of guesses
        print("Current word is", "".join(foundWord))  # make the array into a str
        letter = input("Letter: ").lower() #input of letter, lowercase so its 
        if letter not in word:  # if the letter is not in the word
            guesses += 1 #add a guess to the guesses (failed attempt)
            print(f"Letter '{letter}' is not in the word. You have {totGuesses - guesses} remaining guesses") #print guesses remaining
            # print("\n")
        else:  # if the letter is in the word
            for i in range(len(word)): #iterate over the found word
                if word[i] == letter:  #if the letter iterated is the letter found
                    foundWord[i] = letter #set the _ at $i to the letter
            print("Current found word is", "".join(foundWord)) #print the current word by joining the list as it is much easier to work with if it is a list
        print("\n") #print a new line
        if "_" not in foundWord:  # underscore is letters not found
            print("Game won!") #print game won
            points += 10 #add points
            return [True, totGuesses - guesses]  # winning, return the data
        if guesses == totGuesses: #if your number of guesses is the total number of allowed gueses
            print("Game lost.") #print game lost
            return [False, tot - guesses]  # losing, returns data


# easyWords = ["potato", "couch", "sleep", "running", "hammer"]
# mediWords = ["English", "Busstop", "McDonalds", "Textbook"]
# hardWords = ["Chemistry", "Ubiquitous", "Basement", "Machinegun"]

with open("ten_thousand_words.txt") as f:
    words = f.readlines() #read all of the lines
    words = [w.rstrip() for w in words if 5<len(w)<11] #list comprehension so words are between 5 and 11 letters


pts = 0
while True:
    word = random.choice(words) #choose a random word
    # print(f"word: {word}")  # debug
    res = hangman(word, 10) #run hangman function
    # print(res)
    pts += res[1]  # points are the amount of total guesses - wrong guesses. add points
    print("Your points are:", str(pts) + ". New game has started") #print points
