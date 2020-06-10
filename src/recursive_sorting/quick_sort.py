def partition(arr):
    left = []
    right = []
    pivot = arr[0]

    # iterate over the rest of the array 
    for num in arr[1:]:
        # if the element is greater than pivot, in the right
        if num > pivot:
            right.append(num)
        # else, in the left
        else:
            left.append(num)

    return left, pivot, right


def quicksort(arr):
    if len(arr) == 0:
        return arr

    # partition here into left, pivot, and right
    left, pivot, right = partition(arr)

    return quicksort(left) + [pivot] + quicksort(right)


def quicksort_in_place(arr):
    pass



items = [3, 6, 1, 5, 4, 2]
result = quicksort(items)
print(result)
