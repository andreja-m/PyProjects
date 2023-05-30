#!/usr/bin/env python3

import random

guess = random.randint(1,100)

#print(guess)

def checker():
    user_input = input("Enter your guess: ")

    if int(user_input) == int(guess):
        print('You guessed correctly!')

    if int(user_input) < int(guess):
        print('Your guess ih lower then selected number')
        checker()

    if int(user_input) > int(guess):
        print('Your guess is higher then selected number')
        checker()

if __name__ == '__main__':
    checker()
