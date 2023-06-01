#!/usr/bin/env python3

import random

print("Select option: \n[ 1 ] rock \n[ 2 ] paper \n[ 3 ] scissors\n")

option = input("Your option: ")

lista = ["rock", "paper", "scissors"]

pc = random.choice(lista)

def obracun():
    if int(option) == 1 and pc == lista[0]:
        print("\nPc option is: ", pc)
        print('draw')

    if int(option) == 1 and pc == lista[1]:
        print("\nPc option is: ", pc)
        print('u lost')

    if int(option) == 1 and pc == lista[2]:
        print("\nPc option is: ", pc)
        print('u win')

    if int(option) == 2 and pc == lista[0]:
        print("\nPc option is: ", pc)
        print('u win')

    if int(option) == 2 and pc == lista[1]:
        print("\nPc option is: ", pc)
        print('draw')

    if int(option) == 2 and pc == lista[2]:
        print("\nPc option is: ", pc)
        print('u lost')

    if int(option) == 3 and pc == lista[0]:
        print("\nPc option is: ", pc)
        print('u lost')

    if int(option) == 3 and pc == lista[1]:
        print("\nPc option is: ", pc)
        print('u win')

    if int(option) == 3 and pc == lista[2]:
        print("\nPc option is: ", pc)
        print('draw')

if __name__ == '__main__':
    obracun()
