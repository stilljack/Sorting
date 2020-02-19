# TO-DO: complete the helpe function below to merge 2 sorted arrays

import random
import math
from src.BenchMarker import *





def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    i= j= k = 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1
        else:
            merged_arr[k] = arrB[j]
            j += 1
        k += 1

    # check for remainers
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # if we're not at the last element:
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]  # left side
        right = arr[mid:]  # right side
        left = merge_sort(left)  # do over til we at a single element and dont get here no more
        right = merge_sort(right)
        return list(merge(left, right))
    # if we are, return
    else:
        return arr

print (merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))


#quick sort as per guided

def partition(data):
    left =[]
    pivot = data[0]
    right = []

    for item in data[1:]:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)

    return left,pivot,right

def quicksort(data):
    if data == []:
        return data
    left,pivot,right = partition(data)
    return quicksort(left) + [pivot] + quicksort(right)



def quicksortAlt(arr):
    if arr:
        pivot = random.choice(arr)
        low = [n for n in arr if n < pivot]
        middle = [n for n in arr if n == pivot]
        high = [n for n in arr if n > pivot]
        return [*quicksort(low), *middle, *quicksort(high)]
    else:
        return []

# STRETCH: implement an in-place merge sort algorithm

def merge_in_place(arr, start, mid, end):
    right = mid + 1
    if (arr[mid] <= arr[right]):
        return

    while (start <= mid and right <= end):

        # If element 1 is in right place
        if (arr[start] <= arr[right]):
            start += 1
        else:
            tmp = arr[right]
            index = right

            while (index != start):
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = tmp

            start += 1
            mid += 1
            right += 1

    return arr

def mergeSortInPlace(list, l, r):

    if (l < r):

        # Same as (l + r) / 2, but avoids overflow
        # for large l and r
        m = l + (r - l) // 2;

        # Sort first and second halves
        mergeSortInPlace(list, l, m);
        mergeSortInPlace(list, m + 1, r);

        merge_in_place(list, l, m, r);


#
# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort(arr):
#     return arr
##impl stolen from an article, https://www.codespeedy.com/timsort-algorithm-implementation-in-python/
#good stuff here
minrun = 32
def InsSort(arr,start,end):
    for i in range(start+1,end+1):
        elem = arr[i]
        j = i-1
        while j>=start and elem<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = elem
    return arr
def mergeTS(arr,start,mid,end):
    if mid==end:
        return arr
    first = arr[start:mid+1]
    last = arr[mid+1:end+1]
    len1 = mid-start+1
    len2 = end-mid
    ind1 = 0
    ind2 = 0
    ind  = start

    while ind1<len1 and ind2<len2:
        if first[ind1]<last[ind2]:
            arr[ind] = first[ind1]
            ind1 += 1
        else:
            arr[ind] = last[ind2]
            ind2 += 1
        ind += 1

    while ind1<len1:
        arr[ind] = first[ind1]
        ind1 += 1
        ind += 1

    while ind2<len2:
        arr[ind] = last[ind2]
        ind2 += 1
        ind += 1

    return arr

def TimSort(arr):
    n = len(arr)

    for start in range(0,n,minrun):
        end = min(start+minrun-1,n-1)
        arr = InsSort(arr,start,end)

    curr_size = minrun
    while curr_size<n:
        for start in range(0,n,curr_size*2):
            mid = min(n-1,start+curr_size-1)
            end = min(n-1,mid+curr_size)
            arr = mergeTS(arr,start,mid,end)
        curr_size *= 2
    return arr


