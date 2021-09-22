# Inefficient, only taught because of educational purpose
# Filtering out the largest element and putting it to the last each time
# O(n^2)
import time

class BubbleSort:
    def sort(self, _list:list):
        start_time = time.time()
        counter, counter2 = 0, 0
        for i in range(len(_list)):
            for j in range(len(_list) - i - 1):
                if _list[j] > _list[j+1]:
                    _list = self._swap_elements(_list, j, j+1)
                    counter2+=1
            if counter2 <= counter: # No need to continue
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
    bubble_sort = BubbleSort()
    import numpy as np
    _list = [np.random.randint(10000) for i in range(1000)]
    sorted_list = bubble_sort.sort(_list)
    print("The Sorted list is", sorted_list)