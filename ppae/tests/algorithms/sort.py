import random

from ppae.algorithms.sort.insertion_sort import insertion_sort
from ppae.algorithms.sort.selection_sort_iterative import selection_sort_iterative
from ppae.algorithms.sort.selection_sort_recursive import selection_sort_recursive

algos = ["insertion_sort", "selection_sort_iterative", "selection_sort_recursive"]

test_arr = range(100) + range(100)
correct = sorted(test_arr)

def run_tests():
   for algo in algos:
      print "Testing", algo
      a = list(test_arr)
      random.shuffle(a)
      globals()[algo](a)
      assert a == correct
