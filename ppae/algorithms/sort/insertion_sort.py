def _shiftRightByOne(C, a, b):
   """Shifts all elements in the range [a, b) to the right by one.
   Causes out-of-bounds error if range is nonempty (a < b) and b >= len(C)."""
   i = b-1
   while i >= a:
      x = C[i]
      C[i+1] = x
      i -= 1

def insertion_sort(A):
   """Sorts the list A in place"""
   i = 1
   n = len(A)
   while i < n:
      x = A[i]
      j = i-1

      # This is a half-open bound, [lowerBound, upperBound)
      lowerBound = i
      upperBound = i
      while j >= 0:
         if A[j] > x:
            lowerBound -= 1
         else:
            # We don't have to break here, but doing so skips
            # a bunch of unnecessary comparisons
            break 
         j -= 1
      _shiftRightByOne(A, lowerBound, upperBound)
      A[lowerBound] = x

      i += 1
   return A
