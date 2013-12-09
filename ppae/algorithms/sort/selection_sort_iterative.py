def _swapElements(A, i, j):
   temp = A[i]
   A[i] = A[j]
   A[j] = temp

def selection_sort_iterative(A):
   n = len(A)
   i = 0
   while i < n-1:
      j = i
      minSoFar = A[j]
      minIndex = j
      while j < n:
         x = A[j]
         if x < minSoFar:
            minSoFar = x
            minIndex = j
         j += 1
      _swapElements(A, i, minIndex)

      i += 1
