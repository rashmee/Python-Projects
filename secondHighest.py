nums = [1,27,3,4,5,6,7,99,77]

def highest(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max

maxNum = highest(nums)
nums.remove(maxNum)
print nums

def secondHighest(numbers):
    secMax = numbers[0]
    for number in numbers:
        if number > secMax:
            secMax = number
    return secMax

print "Second Highest Number: ", secondHighest(nums)