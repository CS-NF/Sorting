# TO-DO: complete the helpe function below to merge 2 sorted arrays
# pseudocode 
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    
    a = 0
    b = 0

    for i in range(0, elements):
        # if arrA is done
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        # if arrB is done
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        # if arrA is smaller then arrB    
        elif arrA[a] <= arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        # if arrA is bigger then arrB
        else:
            merged_arr[i] = arrB[b]
            b += 1
    

    return merged_arr


        # if arrA[a] < arrB[b]:
        #     merged_arr[i] = arrA[a]
        #     a += 1
        # # if arrA is bigger then arrB
        # else:
        #     merged_arr[i] = arrB[b]
        #     b += 1


# TO-DO: implement the Merge Sort function below USING RECURSION
# pseudocode 
# create an if statment getting the length of the arr if it's greater the 1
# take the legnth of the arr and divided it by two 
# create a variable for the first half of the list 
# create a variable for the second half of the list 
# do recursion by calling merge_sort with the argumanet of the first half of the list 
# do recursion by calling merge_sort with the argumenet of the second half of the list 
# FINAL SETP: create a variable called arr that's equal to the recursive function and return the variable  

def merge_sort(arr):
    # TO-DO
  if len(arr) <= 1:
      return arr
  else:
      middle = len(arr) // 2
      first = arr[0: middle]
      second = arr[middle:]

      arrA = merge_sort(first)
      arrB = merge_sort(second)

      arr = merge(arrA, arrB)
    
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
