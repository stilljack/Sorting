# STRETCH: implement Linear Search
import math

def JumpSearch (lys, val):
  length = len(lys)
  jump = int(math.sqrt(length))
  left, right = 0, 0
  while left < length and lys[left] <= val:
    right = min(length - 1, left + jump)
    if lys[left] <= val and lys[right] >= val:
      break
    left += jump
  if left >= length or lys[left] > val:
    return -1
  right = min(length - 1, right)
  i = left
  while i <= right and lys[i] <= val:
    if lys[i] == val:
      return i
    i += 1
  return -1


def linear_search(arr, target):
  for i in range(len(arr)):
    if arr[i] == target:
      return i
  return -1



# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
  if len(arr) == 0:
    return -1 # array empty

  low = 0
  high = len(arr)-1

  while low <= high:

    mid = low + (high - low)//2
    print(f"target = {target}")
    print(f"low={low} high ={high} mid = {mid} arr[mid] = {arr[mid]}")

    # Check if x is present at mid
    if arr[mid] == target:
      return mid

    # If x is greater, ignore left half
    elif arr[mid] < target:
      low = mid + 1

    # If x is smaller, ignore right half
    else:
      high = mid - 1

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):


  mid = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
    # Check base case
  if low <= high:
    print(f"target = {target}")
    print(f"low={low} high ={high} mid = {mid} arr[mid] = {arr[mid]}")
    mid = low + (high - low)//2

    # If element is present at the middle itself
    if arr[mid] == target:
      return mid

    # If element is smaller than mid, then it can only
    # be present in left subarray
    elif arr[mid] > target:
      return binary_search_recursive(arr, target, low, mid-1)

    # Else the element can only be present in right subarray
    else:
      return binary_search_recursive(arr, target, mid+1, high)

  else:
    # Element is not present in the array
    return -1
  # TO-DO: add missing if/else statements, recursive calls
