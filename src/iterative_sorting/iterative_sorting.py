# TO-DO: Complete the selection_sort() function below

import math
import time
import random
import timeit

# timeit integration via https://www.pythoncentral.io/time-a-python-function/
# use: >>> wrapped = wrapper(costly_func, short_list)
# >>> timeit.timeit(wrapped, number=1000)

#this is the number of times to execute the timer checks
executeConst = 10000

#variables of use later (lol great docs jack)
finalResult = {str:float}
myRange = 100
size = 100
myRandoms = random.sample(range(myRange),size)
sortList1 = [random.randint(0,myRange) for i in range(size)]
sortList2 = [9,105,200,325,8,7,6,5,2,3,4]

print(f"myRandoms len = {len(myRandoms)}")
print(f"sortlist1 len = {len(sortList1)}")
print(f"sortlist2 = {sortList2}")
print("\n")

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


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
    return answer


wrapped = wrapper(selection_sort,sortList1)
print(f"time for selectionsort of sortlist1 executed x {executeConst}")
finalResult[f"selection_sort.sortlist1"] = timeit.timeit(wrapped, number=executeConst)
print(finalResult[f"selection_sort.sortlist1"])
wrapped = wrapper(selection_sort,myRandoms)
print(f"time for selectionsort of myrand executed x {executeConst}")
finalResult[f"selection_sort.myRandoms"] = timeit.timeit(wrapped, number=executeConst)
print(finalResult[f"selection_sort.sortlist1"])


print(
    f"sort list 1 {selection_sort(sortList1)}"
)
print(
    f"myRandoms {selection_sort(myRandoms)}"
)

print("\n")

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    length=len(arr)
    answer = arr
    for i in range(0,length):
        for j in range(0, length-i-1): #the last x-i-1 will already be assigned
            if answer[j] > answer[j+1] :
                answer[j], answer[j+1] = answer[j+1], answer[j]
    return answer

wrapped = wrapper(bubble_sort,sortList1)
print(f"time for bubblesort of sortlist1 executed x {executeConst}")
finalResult[f"bubble_sort.sortlist1"] = timeit.timeit(wrapped, number=executeConst)
print(finalResult[f"bubble_sort.sortlist1"])
wrapped = wrapper(bubble_sort,myRandoms)
print(f"time for bubble_sort of myrand executed x {executeConst}")
finalResult[f"bubble_sort.myRandoms"] = timeit.timeit(wrapped, number=executeConst)
print(finalResult[f"bubble_sort.myRandoms"])
print(
    f"sort list 1{bubble_sort(sortList1)}"
)
print(
    f"myRandoms {bubble_sort(myRandoms)}"
)


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr


for k,v in finalResult.items():
    print(f"k = {k} v = {v}")
