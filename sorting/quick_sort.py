# Pick a pivot element(first or last) such that smaller numbers are one left of it and larger on the right of it
# Worst case complexity is O(n^2) but only in extreme edge cases it would give good results usually in O(n log n) on average cases

# Python3 implementation of QuickSort

# This Function handles sorting part of quick sort
# start and end points to first and last element of
# an array respectively
def partition(start, end, array):
    # Initializing pivot's index to start
    pivot_index = start
    pivot = array[pivot_index]

    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:

        # Increment the start pointer till it finds an
        # element greater than  pivot
        while start < len(array) and array[start] <= pivot:
            start += 1

        # Decrement the end pointer till it finds an
        # element less than pivot
        while array[end] > pivot:
            end -= 1

        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if (start < end):
            array[start], array[end] = array[end], array[start]

    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]

    # Returning end pointer to divide the array into 2
    return end


# The main function that implements QuickSort
def quick_sort(start, end, array):
    if (start < end):
        # p is partitioning index, array[p]
        # is at right place
        p = partition(start, end, array)

        # Sort elements before partition
        # and after partition
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)


# Driver code
array = [10, 7, 8, 9, 1, 5]
quick_sort(0, len(array) - 1, array)

print(f'Sorted array: {array}')




if __name__ == '__main__':
    # bubble_sort = BubbleSort()
    # import numpy as np
    # _list = [np.random.randint(10000) for i in range(1000)]
    # sorted_list = bubble_sort.sort(_list)
    # print("The Sorted list is", sorted_list)
    print(pivot_sort([21,11,88,33,22,66,22]))




