def selectIdx(A, leftBound, rightBound, index):
   """Returns the index of the (index+1)'th largest element in A[leftBound <= i <= rightBound]"""
   n = rightBound-leftBound+1
   B = [None for i in range(n)] # initialize to empty array of length len(A)
   for i in range(n):
      B[i] = (A[leftBound+i], i) # two-tuple of element from A and its index
   B.sort(key=lambda x: x[0]) # sort B using the first index of the each tuple.
                              # You can use any algorithm you want that doesn't call this function in its base case
   return leftBound + B[index][1]

# TODO use this as test case
# x = [2,1,3,-2]
# assert selectIdx(x, 0, len(x)-1, 0) == 3

#x = [2, 1, 3, -2, -99]
#print selectIdx(x, 0, len(x)-1, 0) 
