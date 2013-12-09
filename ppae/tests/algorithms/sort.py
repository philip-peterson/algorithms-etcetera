import random
from ppae.algorithms.sort.insertion_sort import insertion_sort
from ppae.algorithms.sort.selection_sort import selection_sort

algos = [insertion_sort, selection_sort]

test_arr = range(100) + range(100)
correct = sorted(test_arr)

def run_tests():
   for algo in algos:
      a = list(test_arr)
      random.shuffle(a)
      algo(a)
      assert a == correct
