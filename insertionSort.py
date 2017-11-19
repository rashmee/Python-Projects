"""In this, the second element is compared with the first
element and is swapped if it is not in order. Similarly, we
take the third element in the next iteration and place it at
the right place in the subarray of the first and second elements
(as the subarray containing the first and second elements is
already sorted). We repeat this step with the fourth element of
the array in the next iteration and place it at the right
position in the subarray containing the first, second and the
third elements. We repeat this process until our array gets sorted."""

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue


aList = [54,26,93,17,77,31,44,55,20]
insertionSort(aList)
print aList