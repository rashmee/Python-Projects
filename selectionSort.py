"""It is also a sorting algorithm in which first step is to
find the smallest element in the array. This smallest element
is swapped with the first element. After this, search for the
smallest element in the subarray formed by excluding the first
element and compare it with the first element of the subarray.
Repeat it till the array gets sorted."""

def selectionSort(lst):
    for i in range(len(lst)):
        minElement = min(lst[i:])
        min_Index = lst[i:].index(minElement)
        lst[i + min_Index] = lst[i]
        lst[i] = minElement

lst = [54,26,93,17,77,31,44,55,20]
selectionSort(lst)
print lst