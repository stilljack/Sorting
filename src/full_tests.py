
import random
from src.BenchMarker import *
from src.iterative_sorting.iterative_sorting import *
from src.recursive_sorting.recursive_sorting import *
from src.searching.searching import *
tstr= BenchMarker(5, 10000, 0, 10000)

def newRandList():
    list = [1,2,3,4,6,7,12,3412,3421,5,14,1245,2154,5,123,1234,1234] #[random.randint(0,100000) for i in range(100000)]
    for i in range(random.randint(0,100000)):
        list.append(random.randint(0,100000))
    list.sort()
    return list

def randRandToSearchFor(list):
    size=len(list)
    return random.randint(0,size)

def makeTestForSearch(searchFunc):
    list =newRandList()
    targetID = randRandToSearchFor(list)
    mArgs =[list,list[targetID]]
    wrapped = tstr._wrapper_(searchFunc, *mArgs)
    str = searchFunc.__name__
    print(f"str{str} targetid ={targetID} target ={list[targetID]}")
    print(list)
    tstr.finalResult[str] = timeit.timeit(wrapped, number=1)



makeTestForSearch(linear_search)
makeTestForSearch(linear_search)
makeTestForSearch(linear_search)
makeTestForSearch(linear_search)
tstr.printResults()


list =newRandList()
# print(binary_search(list,5))
#print(binary_search_recursive(list,5,0,len(list)))
print(JumpSearch(list,5))
print(list[JumpSearch(list,5)])
print(list)








tstr.doTestsWith(TimSort,True)
tstr.printResults()
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


#for those stubborn ones we can shove into the tstr framework as easily
stubList =tstr._newRand_(1000, 0, 1000)
mArgs =[stubList, 0, len(stubList) - 1]
wrapped = tstr._wrapper_(mergeSortInPlace, *mArgs)
tstr.finalResult["mergesort in place"] = timeit.timeit(wrapped, number=1)
tstr.printResults()


