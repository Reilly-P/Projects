New_Alphabet = {
    "A": "@",
    "B": "8",
    "C": "(",
    "D": "|)",
    "E": "3",
    "F": "#",
    "G": "6",
    "H": "[-]",
    "I": "|",
    "J": "_|",
    "K": "|<",
    "L": "1",
    "M": "[]\\/[]",
    "N": "[]\\[]",
    "O": "0",
    "P": "|D",
    "Q": "(,)",
    "R": "|Z",
    "S": "$",
    "T": "']['",
    "U": "|_|",
    "V": "\\/",
    "W": "\\/\\/",
    "X": "}{",
    "Y": "`/",
    "Z": "2"
}
new_alphabet = {
    "a": "@",
    "b": "8",
    "c": "(",
    "d": "|)",
    "e": "3",
    "f": "#",
    "g": "6",
    "h": "[-]",
    "i": "|",
    "j": "_|",
    "k": "|<",
    "l": "1",
    "m": "[]\\/[]",
    "n": "[]\\[]",
    "o": "0",
    "p": "|D",
    "q": "(,)",
    "r": "|Z",
    "s": "$",
    "t": "']['",
    "u": "|_|",
    "v": "\\/",
    "w": "\\/\\/",
    "x": "}{",
    "y": "`/",
    "z": "2"
}

words = input()
def Convert():
    conv = ""
    for i in words:
        if i in New_Alphabet.keys():
            conv += New_Alphabet[i]
        elif i in new_alphabet.keys():
            conv += new_alphabet[i]
        else:
            conv += i
    print(conv)
    return(conv)

Convert()


print("Test cases")
words = "Sphinx of black quartz judge my vow"
print(words)
assert(Convert() == "$|D[-]|[]\[]}{ 0# 81@(|< (,)|_|@|Z']['2 _||_||)63 []\/[]`/ \/0\/\/")

words = "Yikes! #38's helmet, it's broken"
print(words)
assert(Convert() == "`/||<3$! #38'$ [-]31[]\/[]3'][', |'][''$ 8|Z0|<3[]\[]")

words = "Here we go again"
print(words)
assert(Convert() == "[-]3|Z3 \/\/3 60 @6@|[]\[]")