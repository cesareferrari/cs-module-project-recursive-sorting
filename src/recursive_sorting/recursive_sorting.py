def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # array that holds the sorted elements from A and B
    # merged_arr = [0] * elements
    merged_arr = []

    # initialize the pointers that start at each array
    a = 0
    b = 0

    while a < len(arrA) and b < len(arrB):
        # compare the elements where a and b point to
        # and append the correct element from array A or B to merged_arr
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a += 1
        else:
            merged_arr.append(arrB[b])
            b += 1

    # one of the lists may have extra elements:
    # append all of them to merged_arr
    # only one of these loops is going to run
    while a < len(arrA):
        merged_arr.append(arrA[a])
        a += 1

    while b < len(arrB):
        merged_arr.append(arrB[b])
        b += 1

    return merged_arr


def merge_sort(arr):
    # break the array down recursively
    # base case: when list is length of 1
    if len(arr) > 1:
        # if length more than 1: keep recursing
        # break array down into left and right subarrays
        # split into 2 subarrays
        # left half contains elements from 0 to half
        left = merge_sort(arr[:len(arr) // 2])
        # right half contains elements from half to end
        right = merge_sort(arr[len(arr) // 2:])

        # merge them back up
        arr = merge(left, right)

    return arr



# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
