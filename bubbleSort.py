#It is a sorting algorithm in which two adjacent elements of
# an array are checked and swapped if they are in wrong order
# and this process is repeated until we get a sorted array.

#In this first two elements of the array are checked and
# swapped if they are in wrong order. Then first and third
# elements are checked and swapped if they are in wrong order.
# This continues till the lat element is checked and swapped if
# necessary.

def bubble_sort(seq):
    changed = True
    while changed:
        changed = False
        for i in range(len(seq) - 1):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                changed = True
    return None

seq = [54,26,93,17,77,31,44,55,20]
bubble_sort(seq)
print seq