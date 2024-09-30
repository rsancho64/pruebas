#!/usr/bin/python3

#  poo mi primera clase

class Amigo:

    def __init__(self, unNombre=None) -> None:
        self.nombre = unNombre
    

if __name__ == "__main__" :


    m = Amigo()
    print(m.nombre)

    a = Amigo("ramon")
    print(a.nombre)

    