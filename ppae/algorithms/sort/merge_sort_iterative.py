def _merge(a, b):
   C = [0 for i in range(len(a)+len(b))] # may be uninitialized array
   m = len(a)
   n = len(b)

   if m > n:
      # Swap (the names for) m with n, a with b
      q = m
      m = n
      n = q

      r = a
      a = b
      b = r

   k = 0

   bStart = 0

   for i in range(m):
      x = a[i]

      for j, y in enumerate(b):
         if y > x:
            break
         C[k] = y
         k += 1
         print "k is ", k

      C[k] = x
      print "k is ", k
      k += 1

   return C

x = [1,3,4,7]
y = [-2,-2]

print _merge(x,y)

# def merge_sort(A):
#    
