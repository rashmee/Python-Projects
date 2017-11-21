#Program simulating the dice roll

from random import randint

repeat = True
dice1 = randint(1,6)
dice2 = randint(1,6)

while repeat:
    print "You rolled ",dice1, "&",dice2
    print "Your total is ",dice1+dice2
    if(dice1==dice2):
        print "DOUBLES! Great going!!!"
    elif(dice1==6 & dice2==6):
        print "DOUBLE SIXES!!! Way to go!"
    print("Do you want to roll again?")
    repeat = ("y" or "yes") in input().lower()

print("Thank you for playing!")
