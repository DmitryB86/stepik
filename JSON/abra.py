import json

def convertString(line):
    with open('Alphabet.json', 'r') as keyjs:
        alpha_alpa  = keyjs.readline()
    # alpha = {"A": "N", "B": "O", "C": "P", "D": "Q", "E": "R", "F": "S", "G": "T", "H": "U", "I": "V", "J": "W",
    #          "K": "X", "L": "Y", "M": "Z", "N": "A", "O": "B", "P": "C", "Q": "D", "R": "E", "S": "F", "T": "G",
    #          "U": "H", "V": "I", "W": "J", "X": "K", "Y": "L", "Z": "M", "a": "n", "b": "o", "c": "p", "d": "q",
    #          "e": "r", "f": "s", "g": "t", "h": "u", "i": "v", "j": "w", "k": "x", "l": "y", "m": "z", "n": "a",
    #          "o": "b", "p": "c", "q": "d", "r": "e", "s": "f", "t": "g", "u": "h", "v": "i", "w": "j", "x": "k",
    #          "y": "l", "z": "m"}
        dic_json = json.loads(alpha_alpa)
        newtext = ''
        for i in line:
            for key, value in dic_json.items():
                if i == key:
                    newtext += value
                # elif i == ' ':
                #     newtext += ' '
                #     break
                elif i.isalpha()==False:
                    newtext += i
                    break
        newtext2 = ''
        for string1 in newtext:
            if string1 == '\n':
                break
            else:
                newtext2 += string1
    return newtext2



with open('Abracadabra__1_.txt', 'r') as f:
    fultext = f.readlines()
    for rows in fultext:
        print(convertString(rows))


