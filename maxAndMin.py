#Find the maximum and minimum of a list without using any built-ins

def theMax(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max

def theMin(numbers):
    min = numbers[0]
    for number in numbers:
        if number < min:
            min = number
    return min

print "Max: ", theMax([1,27,3,4,5,6,7])
print "Min: ", theMin([1,-27,3,4,5,6,7])





