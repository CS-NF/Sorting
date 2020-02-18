# TO-DO: complete the helpe function below to merge 2 sorted arrays
# pseudocode 
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
# pseudocode 
# create an if statment getting the length of the arr if it's greater the 1
# take the legnth of the arr and divided it by two 
# create a variable for the first half of the list 
# create a variable for the second half of the list 
# do recursion by calling merge_sort with the argumanet of the first half of the list 
# do recursion by calling merge_sort with the argumenet of the second half of the list 
# FINAL SETP: create a variable called arr that's equal to the recursive function and return the variable  

def merge_sort( arr ):
    # TO-DO
  if len(arr) > 1:
      middle = len(arr) // 2
      first = arr[0: middle]
      second = arr[middle:]

      arr_a = merge_sort(first)
      arr_b = merge_sort(second)

      arr = merge(arr_a, arr_b)
    
    return arr








# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
