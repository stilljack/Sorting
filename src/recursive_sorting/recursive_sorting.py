# TO-DO: complete the helpe function below to merge 2 sorted arrays


from src.Tester import *


tstr= Tester(2,1000,0,10000)


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
tstr.doTestsWith(merge_sort)
tstr.printResults()

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    return arr
