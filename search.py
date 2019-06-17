#!python
"""STARTER CODE FROM NEPTUNIUS"""
def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    """Best case: O(1)
    Worst case: O(n)"""
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    """Best case: O(1)
    Worst case: O(n)"""
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
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # if item == array[0]:
    #     return array[0]
    # iteration = True
    # while iteration:
    #     if len(array) == 0:
    #         return None
    #     if item > array[len(array) // 2]:
    #         array = array[(len(array)//2):len(array)]
    #     elif item < array[len(array) // 2]:
    #         array = array[0:(len(array)//2)]
    #     elif item == array[len(array) // 2]:
    #         return array[len(array) // 2]
    #     else:
    #         return None
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    """Version above was used when I was returning items, not indexs
    Best Case: O(1)
    Worst Case: O(log)n"""
    left = 0
    right = len(array) - 1
    mid = (right - left) // 2
    while left <= right:
        if array[mid] == item:
            return mid
        elif array[mid] > item:
            right = mid - 1
        else:
            left = mid + 1
        mid = (left + right) // 2
    return None


def binary_search_recursive(array, item, left=None,right=None):
    # TODO: implement binary search recursively here
    # if tracker is None:
    #     tracker=len(array)//2
    # print(tracker)
    # if len(array) == 0:
    #     return None
    # if item == array[0]:
    #     return 0
    # if item > array[len(array) // 2]:
    #     print("up")
    #     half = (len(array)//2)//2
    #     return binary_search_recursive(array[(len(array)//2):len(array)], item, tracker=tracker + half)
    # elif item < array[len(array) // 2]:
    #     print("down")
    #     return binary_search_recursive(array[0:(len(array)//2)], item,tracker=tracker - (len(array)//2))
    # elif item == array[len(array) // 2]:
    #     return tracker
    # return None

    """I give up on doing it my super special way (shown above). Here's the normy version. *sigh*"""
    """Best case: O(1)
    Worst case: O(log)n"""
    if left == None:
        left = 0
        right = len(array) - 1

    if left <= right:
        mid = (left + right) // 2
        if array[mid] == item:
            return mid
        elif array[mid] > item:
            new_right = mid - 1
            return binary_search_recursive(array, item, left=left, right=new_right)
        else:
            new_left = mid + 1
            return binary_search_recursive(array, item, left=new_left, right=right)
    return None
print(binary_search_recursive([0,1,2,3,4,5,6,7,8,9], 6))
#print(binary_search_iterative([1,2,3,4,5], 5))
#print(binary_search_iterative(["Alpha","Bear","Cockey","Dat","Winnie"], "Winnie"))
# names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
# print(binary_search_recursive(names, 'Nick'))
