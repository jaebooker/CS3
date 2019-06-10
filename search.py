#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if index > len(array)-1:
        return None
    if item == array[index]:
        return index
    index += 1
    return linear_search_recursive(array, item, index)
    # TODO: implement linear search recursively here
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    iteration = True
    while iteration:
        if len(array) == 0:
            return None
        if item > array[len(array) // 2]:
            array = array[(len(array)//2):len(array)]
        elif item < array[len(array) // 2]:
            array = array[0:(len(array)//2)]
        elif item == array[len(array) // 2]:
            return array[len(array) // 2]
        else:
            return None
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item):
    # TODO: implement binary search recursively here
    if len(array) == 0:
        return None
    if item > array[len(array) // 2]:
        return binary_search_recursive(array[(len(array)//2):len(array)], item)
    elif item < array[len(array) // 2]:
        return binary_search_recursive(array[0:(len(array)//2)], item)
    elif item == array[len(array) // 2]:
        return array[len(array) // 2]
    return None
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
print(binary_search_recursive([1,2,3,4,5], 5))
print(binary_search_iterative([1,2,3,4,5], 5))
print(binary_search_iterative(["Alpha","Bear","Cockey","Dat","Winnie"], "Winnie"))
