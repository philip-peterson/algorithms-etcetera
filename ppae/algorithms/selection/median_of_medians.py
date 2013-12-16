from selectIdx import selectIdx
import math

def _swap(A, a, b):
   temp = A[a]
   A[a] = A[b]
   A[b] = temp

def _sort(A, leftBound, rightBound):
   """Sorts in place (using any algorithm that doesn't cause infinite recursion) 2-tuples
   stored as elements in list A. Only elements of index i : leftBound <= i <= rightBound are
   sorted.  The elements (which are 2-tuples) are sorted using the left part of the 2-tuple.
   Implemented here as a Python-ism for simplicity."""

   A[leftBound:rightBound+1] = sorted(A[leftBound:rightBound+1], key=lambda x: x[0])


def median_of_medians(A, leftBound, rightBound):
   """Returns the index of the median of medians of A[leftBound to rightBound inclusive]"""

   n = (rightBound - leftBound + 1)
   numMedians = int(math.ceil( n / 5. ))
   medians = [(-1, -1) for i in range(numMedians)] # allocate array

   for i in range(numMedians):
      subLeft = leftBound + i*5
      subRight = min(subLeft+4, rightBound)
      subLength = subRight - subLeft

      index = selectIdx(A, subLeft, subRight, subLength // 2)
      medians[i] = (A[index], index)

   _sort(medians, 0, numMedians - 1)
   return medians[(numMedians - 1) // 2][1]

# TODO test case
# x = [2,1,3,-2, -99, -1000]
# assert median_of_medians(x, 0, len(x)-1) == 5
