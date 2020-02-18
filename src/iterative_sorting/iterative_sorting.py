# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
    for smallest_index in range(cur_index + 1, len(arr)):
        if arr[smallest_index] < arr[cur_index]:
        # TO-DO: swap
            arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for sort in range(0, i):
           if arr[sort] > arr[sort+1]:
                # swap
                arr[sort], arr[sort+1] = arr[sort+1], arr[sort] 
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr