# would insert instead of swapping like bubble and selection_sort
# The idea is to make a sorted list from the unsorted list
# O(n^2)

import time

class InsertionSort:
    def sort(self, _list:list):
        start_time = time.time()
        counter, counter2 = 0, 0
        for i in range(1, len(_list)):
            value = _list[i]
            j = i - 1
            while j >= 0 and value < _list[j]:
                _list[j + 1] = _list[j]
                j -= 1
            _list[j + 1] = value
        print("The time taken by the algorithm is:", time.time() - start_time)
        return _list


if __name__ == '__main__':
    insertion_sort = InsertionSort()
    # import numpy as np
    # _list = [np.random.randint(10000) for i in range(1000)]
    _list = [10,5,2,6,2]
    sorted_list = insertion_sort.sort(_list)
    print("The Sorted list is", sorted_list)