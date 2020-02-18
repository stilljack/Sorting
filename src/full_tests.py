
import random
from src.BenchMarker import *
from src.iterative_sorting.iterative_sorting import *
from src.recursive_sorting.recursive_sorting import *



tstr= BenchMarker(5, 10000, 0, 10000)

tstr.doTestsWith(count_sort)
tstr.printResults()
tstr.doTestsWith(selection_sort)
tstr.printResults()
tstr.doTestsWith(insertion_sort)
tstr.printResults()
tstr.doTestsWith(bubble_sort)
tstr.printResults()
tstr.doTestsWith(merge_sort)
tstr.printResults()
tstr.doTestsWith(quicksort)
tstr.printResults()
tstr.doTestsWith(quicksortAlt)
tstr.printResults()





