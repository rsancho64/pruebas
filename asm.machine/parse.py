#! /usr/bin/python3

codeASM = [
    ["REA", "M[0]"],
    ["REA", "M[1]"],
    ["ADD", "M[0]", "M[1]"], # -> AC
    ["STO", "M[2]"],         # AC -> 
    ["WRI", "M[2]"]
]

def printSentence(aSentence):
    if not type(aSentence) == type([]):
        return
    # assert: aSentence is a list
    for item in aSentence:
        print(item, end=' ')
    print()

if __name__ == "__main__" :

    # print(codeASM)

    for sentence in codeASM:
        print(sentence)
    
    for sentence in codeASM:
        printSentence(sentence)
    
    