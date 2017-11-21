# coding=utf-8
# Reverse string

def strReverse(theString):
    revStr = ''
    theIndex = len(theString)
    while theIndex>0:
        revStr += theString[theIndex-1]
        theIndex = theIndex - 1
    return revStr

theString = input("Enter String! ")
print(strReverse(theString))