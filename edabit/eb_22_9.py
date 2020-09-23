def encode_morse(str_to_enc: "str") -> "str":
    char_to_dots = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        " ": " ",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "&": ".-...",
        "'": ".----.",
        "@": ".--.-.",
        ")": "-.--.-",
        "(": "-.--.",
        ":": "---...",
        ",": "--..--",
        "=": "-...-",
        "!": "-.-.--",
        ".": ".-.-.-",
        "-": "-....-",
        "+": ".-.-.",
        '"': ".-..-.",
        "?": "..--..",
        "/": "-..-.",
    }
    res = ""
    for i in str_to_enc:
        currchar = char_to_dots[i.upper()]
        currchar += " "
        res += currchar
    return res[:-1]


def how_many_seconds(time: "int") -> "int":
    return time * 3600


def relation_to_luke(person: "str") -> "str":
    rel = {
        "Darth Vader": "father",
        "Leia": "sister",
        "Han": "brother in law",
        "R2D2": "droid",
    }
    return "Luke, I am your " + rel[person] + '.'


def id_mtrx(size) -> "arr":
    if not isinstance(size, int):
        return "Error"
    ret = []
    if size >= 0:
        for i in range(size):
            a = []
            for j in range(size):
                if i == j:
                    a.append(1)
                else:
                    a.append(0)
            ret.append(a)
    else:
        size *= -1
        for i in range(size):
            a = []
            for j in range(size):
                if i == j:
                    a.append(1)
                else:
                    a.append(0)
            ret.append(a[::-1])

    return ret

def paths(num: "int") -> "int":
    res = 1
    if num != 1:
        res = num * paths(num - 1)
    return res
