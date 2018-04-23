#!/usr/bin/env python
# -*- coding: utf-8 -*-

# secret = 3
# guess = 0

# while guess != secret:
#     guess=int(raw_input("Guess the number: "))
#     if guess != secret:
#         print "You entered the wrong number. Guess the number again: "
#     else:
#         print "You guessed the number"  + str (guess) + " Congratulation! "

# while guess != secret:
#     guess=int(raw_input("Guess the number: "))
#     if guess != secret:
#         print "You entered the wrong number. The secret number is not {0}. Guess the number again: ".format(guess)
#     else:
#         print "You guessed the number %s! Congratulation! " % secret

secret = 3
ponovi = True

while ponovi:
    guess = int(raw_input("Guess the number: "))

    if guess == secret:
        print "You guessed the number %s! Congratulation! " % secret
        # ponovi = False
        break

    else:
        print "You entered the wrong number. The secret number is not {0}. Guess the number again: ".format(guess)

    nadaljuj = raw_input("Ponovi? (DA/NE)")

    if nadaljuj.lower().strip() != 'da':
        ponovi = False
        print "Ne bom ponovil"