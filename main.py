letters = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "w": ".--",
    "x": "-..-",
    "v": "...-",
    "w": ".--",
    "y": "-.--",
    "z": "--..",
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
}


def toMorse():
    phrase = input("What would you like to translate to morse code? ")
    result = []
    phrase = phrase.split()
    for i in phrase:
        for n in i:
            result.append(letters.get(n.lower()))
        result.append("/")

    print(*result[:-1:], sep=" ")
    # print(*result, sep="   ")
    to_con = input("Would you like to translate something else as well? ")
    if to_con == "yes":
        toMorse()
    else:
        pass


toMorse()
