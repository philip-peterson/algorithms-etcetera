def _swapElements(A, i, j):
   temp = A[i]
   A[i] = A[j]
   A[j] = temp

def selection_sort_recursive(A):
   """Sorts the elements of the array in place."""
   selection_sort_recursive_helper(A, len(A))

def selection_sort_recursive_helper(A, maxBound):
   """Sorts the elements numbered [0, maxBound) of the array in place."""
   if maxBound <= 1:
      return

   maxIndex = 0
   maxValue = A[0]
   for i in range(1, maxBound):
      x = A[i]
      if x > maxValue:
         maxValue = x
         maxIndex = i

   _swapElements(A, maxBound-1, maxIndex)
   selection_sort_recursive_helper(A, maxBound-1)
