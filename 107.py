#!/usr/bin/python3

#  listas ...

if __name__ == "__main__" :

 
    # comprehension (math concept: c. vs extension) 
    n1 = [0 for i in range(15)]
    n2 = [0] * 15

    print(n1)
    print(n2)

    n1[0:10] = [10] * 10

    print(n1)

    