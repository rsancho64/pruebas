#! /usr/bin/python3

codeASM = [
    ["REA", "M[0]"],
    ["REA", "M[1]"],
    ["ADD", "M[0]", "M[1]"], # AC
    ["STO", "M[2]"],
    ["WRI", "M[3]"]
]

def printSentence(aSentence):
    if not type(aSentence) == type([]):
        return
    

if __name__ == "__main__" :

    # print(codeASM)

    # for sentence in codeASM:
    #     print(sentence)
    
    for sentence in codeASM:
        printSentence(sentence)
    
    