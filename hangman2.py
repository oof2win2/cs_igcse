import random

with open("/Users/honza/randomFiles/data/words/words_alpha.txt") as f:
    words = f.readlines()
    words = [w.rstrip() for w in words if 5<len(w)<11]

def hangman():
    word = random.choice(words)
    word = list(word)
    blanks = [" _ "]*len(word)
    lives = 1000
    while lives > 0:
        correct = False
        print(''.join(blanks))
        guess = input("Guess a letter:  ")
        for i in range(len(word)):
            if guess == word[i]:
                blanks[i] = guess
                correct = True
                print("Yes!")
        if not correct:
            lives -= 1
            print(f"Nope. You have {lives} lives left.")

        if blanks == word:
            print(''.join(word))
            print(f"The word is \"{''.join(word)}\". YOU WIN!")

            break
    if blanks != word:
        print("you lost  :(")
        print(f"The word was \"{''.join(word)}\".")

if __name__ == "__main__":
    hangman()
