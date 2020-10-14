import random


def binary_adder():
    print("-" * 20)
    a = random.randint(1, 5)
    b = random.randint(1, 5)
    choice = random.choice(["bin", "hex"])
    if choice == "bin":
        bin_sum = bin(a + b)[2:]  # bin() returns a string

        ans = input(f"What is {a} + {b} in binary?   ")

        if ans == bin_sum:  # bin mode
            print(f"CORRECT: {bin_sum}")
            return 1
        else:
            print(f"NOPE: it is {bin_sum}")
            return 0
    if choice == "hex":  # hex mode
        hex_sum = hex(a + b)[2:]
        ans = input(f"What is {a} + {b} in hex?    ")
        if ans == hex_sum:
            print(f"CORRECT: {hex_sum}")
            return 1
        else:
            print(f"NOPE: it is {hex_sum}")
            return 0


def game(questions):
    score = 0
    for i in range(questions):
        score += binary_adder()
        print(f"SCORE: {score}/{i+1}")


game(5)
