# TO-DO: Complete the selection_sort() function below

import math
import time
import random
import timeit
import numpy
##+90 to -90 long +180 to -180
random_float_number = numpy.random.uniform(-90.0, 90.0)
import src.recursive_sorting.recursive_sorting
# timeit integration via https://www.pythoncentral.io/time-a-python-function/
# use: >>> wrapped = wrapper(costly_func, short_list)
# >>> timeit.timeit(wrapped, number=1000)

#this is the number of times to execute the timer checks
executeConst = 2

#variables of use later (lol great docs jack)
def newRand(amountToReturn,targetRange):
    new = [0 for i in range(amountToReturn)]
    for i in range(amountToReturn):
        new[i] =numpy.random.uniform(-90.0, 90.0)
    return new

finalResult = {}
maxRange = 10000000
sizeOfLists = 10001
myRandoms = newRand(sizeOfLists,maxRange)

finalResult["maxRange"] =maxRange
finalResult["sizeOfLists"]=sizeOfLists
print(f"max range = {maxRange}")
print(f"sizeOfLists = {sizeOfLists}")
print(f"myRandoms len = {len(myRandoms)}")
print("\n")




def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def doTestsWith(func):
    count = 0
    for i in range(executeConst):
        count+=1
        newRandom=newRand(sizeOfLists,maxRange)
        print(newRandom)
        wrapped = wrapper(func,newRandom)
        nameOfTest = f"{func.__name__} list {count}"
        print(f" execute count: {executeConst} Fun: {func.__name__} list: list{count}")
        finalResult[nameOfTest] = timeit.timeit(wrapped, number=1)

       # # print(f"final result k = {nameOfTest} v = {finalResult[nameOfTest]}")


def insertion_sort(list_to_sort):
    # Separate the first element from the rest of the array. Think about it as a sorted list of one element.
    # For all other indices, beginning with [1]:
    for i in range(1, len(list_to_sort)):
        #a. Copy the item at that index into a temp variable
        temp = list_to_sort[i]

        # b. Iterate to the left until you find the correct index in the "sorted" part of the array at which this element should be inserted
        j = i
        while j > 0 and temp < list_to_sort[j-1]:
            # Shift items over to the right as you iterate
            list_to_sort[j] = list_to_sort[j - 1]
            j -= 1
        # c. When the correct index is found, copy temp into this position
        list_to_sort[j] = temp
    print (list_to_sort)
    return list_to_sort

def selection_sort( arr ):
    # loop through n-1 elements
    answer =arr
    for i in range(0, len(arr)-1):
        #print(f"begin for i = {i} is {arr[i]}")
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i+1, len(arr)):
            if answer[smallest_index] > answer[j]:
                smallest_index = j
        answer[i], answer[smallest_index] = answer[smallest_index], answer[i]
    print(answer)
    return answer

print("\n")

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    length=len(arr)
    answer = arr
    for i in range(0,length):
        for j in range(0, length-i-1): #the last x-i-1 will already be assigned
            if answer[j] > answer[j+1] :
                answer[j], answer[j+1] = answer[j+1], answer[j]
    print(answer)
    return answer



# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=maxRange ):

    newval=arr
    m = maximum + 1
    count = [0 for i in range(m)]
    for a in newval:
    # count occurences
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            newval[i] = a
            i += 1
    print(newval)
    return newval

### HERE BE ENTRY POINT###
#doTestsWith(count_sort)
doTestsWith(insertion_sort)
doTestsWith(bubble_sort)
doTestsWith(selection_sort)

#####here be print out#####
for k,v in finalResult.items():
    print(f"k = {k} v = {v}")




# wrapped = wrapper(insertion_sort,sortList1)
# print(f"time for insertion_sort of sortlist1 executed x {executeConst}")
# finalResult[f"insertion_sort.sortlist1"] = timeit.timeit(wrapped, number=executeConst)
# print(finalResult[f"insertion_sort.sortlist1"])
# wrapped = wrapper(insertion_sort,myRandoms)
# print(f"time for insertion_sort of myrand executed x {executeConst}")
# finalResult[f"insertion_sort.myRandoms"] = timeit.timeit(wrapped, number=executeConst)
# print(finalResult[f"insertion_sort.myRandoms"])
# wrapped = wrapper(selection_sort,sortList1)
# print(f"time for selectionsort of sortlist1 executed x {executeConst}")
# finalResult[f"selection_sort.sortlist1"] = timeit.timeit(wrapped, number=executeConst)
# print(finalResult[f"selection_sort.sortlist1"])
# wrapped = wrapper(selection_sort,myRandoms)
# print(f"time for selectionsort of myrand executed x {executeConst}")
# finalResult[f"selection_sort.myRandoms"] = timeit.timeit(wrapped, number=executeConst)
# print(finalResult[f"selection_sort.sortlist1"])
#
# wrapped = wrapper(bubble_sort,sortList1)
# print(f"time for bubblesort of sortlist1 executed x {executeConst}")
# finalResult[f"bubble_sort.sortlist1"] = timeit.timeit(wrapped, number=executeConst)
# print(finalResult[f"bubble_sort.sortlist1"])
# wrapped = wrapper(bubble_sort,myRandoms)
# print(f"time for bubble_sort of myrand executed x {executeConst}")
# finalResult[f"bubble_sort.myRandoms"] = timeit.timeit(wrapped, number=executeConst)
# print(finalResult[f"bubble_sort.myRandoms"])
