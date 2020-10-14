import random


def convertQues(rng):
    # num = random.randint(0, rng)
    num = rng
    modes = ["hex", "bin"]
    mode = random.choice(modes)

    wrongAnswer = True
    if mode == "hex":
        while wrongAnswer:
            inp = input(f"What is hex {hex(num)[2:]} in decimal: ")
            if int(inp, 10) == num:
                wrongAnswer = False
            else:
                print("Wrong answer. Please try again")
    if mode == 'bin':
        while wrongAnswer:
            inp = input(f"What is binary {bin(num)[2:]} in decimal: ")
            if int(inp, 10) == num:
                wrongAnswer = False
            else:
                print("Wrong answer. Please try again")

while True:
    r = random.randint(0, 256)
    print(f"{r}, {bin(r)}, {hex(r)}")
    convertQues(r)
