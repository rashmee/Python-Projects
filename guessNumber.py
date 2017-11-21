# coding=utf-8
# The Goal: Similar to the first project, this project also uses the random module in
# Python. The program will first randomly generate a number unknown to the user.
# The user needs to guess what that number is. In other words, the user needs to be
# able to input information. If the user’s guess is wrong, the program should return
# some sort of indication as to how wrong (e.g. The number is too high or too low).
# If the user guesses correctly, a positive indication should appear. You’ll need
# functions to check if the user input is an actual number, to see the difference
# between the inputted number and the randomly generated numbers, and to then compare
# the numbers.


from random import randint

guessesTaken = 0

print("Hi! What is your name?")
myName = input()

_randNum_ = randint(1, 10)

print('Hi, ' + myName + ', I am ready with my number. Your turn!')

while guessesTaken<5:
    print("Guess?")
    theGuess = input()
    theGuess = int(theGuess)

    guessesTaken = guessesTaken+1

    if theGuess < _randNum_:
        print('Your guess is too low!')
    elif theGuess > _randNum_:
        print('Your guess it too high!')
    else:
        break

if theGuess == _randNum_:
    guessesTaken = str(guessesTaken)
    print('Awesome! ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if theGuess != _randNum_:
    _randNum_ = str(_randNum_)
    print('Nope! The number I was thinking of was ' + _randNum_)


