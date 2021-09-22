# Use divide and concur
# O(n*log(n))

class MergeSort():
    def sort(self, _list):
        if len(_list) > 1:
            mid = len(_list)//2
            L = _list[:mid]
            R = _list[mid:]
            L = self.sort(L)
            R = self.sort(R)
            sorted_array = self.merge(L,R)
            return sorted_array
        else:
            return _list


    def merge(self, A:list, B:list):
        A, B = list(A), list(B)
        # merge two sorted list
        self.merged_list = []
        while len(A+B) > 0:
            if len(A) == 0 and len(B)>0:
                B = self.update_list(B)
            elif len(B) == 0 and len(A)>0:
                A = self.update_list(A)
            else:
                if A[0] < B[0]:
                    A = self.update_list(A)
                else:
                    B = self.update_list(B)
        return self.merged_list

    def update_list(self,x_arr):
        """
        :param x_arr: any array
        :return: removes the first element from that array
        """
        self.merged_list.append(x_arr[0])
        x_arr.remove(x_arr[0])
        return x_arr






if __name__ == '__main__':
    merge_sort = MergeSort()
    import numpy as np
    _list = [np.random.randint(10000) for i in range(1000)]
    sorted_list = merge_sort.sort(_list)
    print(sorted_list)
    print(all(sorted_list == np.sort(_list)) == True)