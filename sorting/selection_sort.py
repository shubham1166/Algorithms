# Inefficient, only taught because of educational purpose
# /ok at the adjecent and add a minimum every time
# O(n^2)
import time

class SelectionSort:
    def sort(self, _list:list):
        start_time = time.time()
        counter, counter2 = 0, 0
        for i in range(len(_list)):
            minimum = _list[i]
            for j in range(i+1, len(_list)):
                if _list[j] < minimum:
                    minimum = _list[j]
                    _list = self._swap_elements(_list, j, i)
                    counter2 +=1
            if counter2 <= counter:  # No need to continue
                break
            else:
                counter = counter2
        print("The time taken by the algorithm is:", time.time() - start_time)
        return _list

    @staticmethod
    def _swap_elements(_list:list, i:int, j:int):
        """
        :return: Swaps the elements i and j in the list _list
        """
        _list[i], _list[j] = _list[j], _list[i]
        return _list


if __name__ == '__main__':
    selection_sort = SelectionSort()
    import numpy as np
    # _list = [10,11,0,7]
    _list = [np.random.randint(10000) for i in range(1000)]
    sorted_list = selection_sort.sort(_list)
    print("The Sorted list is", sorted_list)