from src.BenchMarker import *
from src.SearchBenchMarker import *
from src.recursive_sorting.recursive_sorting import *
from src.searching.searching import *


sortTester= BenchMarker(5, 10000, 0, 10000)

#?#$#$#$#$#$###test Config##$$#$#$#$#$
defRangeLow=-100000000
defRangeHigh=100000000
defListTotal=1000000
defNumberTests=10
defFloat=True
#?#$#$#$#$#$###test Config##$$#$#$#$#$
searchTester =SearchBenchMarker(
    rangeLow=defRangeLow,
    rangeHigh=defRangeHigh,
    listTotal=defListTotal,
    numberTests=defNumberTests,
    float=defFloat
    )

searchTester.multiTests(
    searchFunc=JumpSearch
)
searchTester.multiTests(
    searchFunc=binary_search,

)
searchTester.multiTests(
    searchFunc=linear_search,
)
#multiTests(linear_search,10)
#multiTests(JumpSearch,10)
searchTester.printResults()






# tstr.doTestsWith(TimSort,True)
# tstr.printResults()
# tstr.doTestsWith(count_sort)
# tstr.printResults()
# tstr.doTestsWith(selection_sort)
# tstr.printResults()
# tstr.doTestsWith(insertion_sort)
# tstr.printResults()
# tstr.doTestsWith(bubble_sort)
# tstr.printResults()
# tstr.doTestsWith(merge_sort)
# tstr.printResults()
# tstr.doTestsWith(quicksort)
# tstr.printResults()
# tstr.doTestsWith(quicksortAlt)
# tstr.printResults()


#for those stubborn ones we can shove into the tstr framework as easily
# stubList =tstr._newRand_(1000, 0, 1000)
# mArgs =[stubList, 0, len(stubList) - 1]
# wrapped = tstr._wrapper_(mergeSortInPlace, *mArgs)
# tstr.finalResult["mergesort in place"] = timeit.timeit(wrapped, number=1)
# tstr.printResults()


