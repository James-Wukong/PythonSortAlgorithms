class MergeSort:
    """
    A class representing a merge sorting algorithm
    """
    # MergeSort in Python
    def merge_sort(self, array: list = None) -> list:
        '''
        Args:
            array: The array to be sorted.

        Returns:
          A sorted array.
        '''
        if len(array) > 1:
            #  r is the point where the array is divided into two subarrays
            r = len(array)//2
            left = array[:r]
            right = array[r:]

            # Sort the two halves
            self.merge_sort(left)
            self.merge_sort(right)

            # i is the pointer in left, j is the pointer in right
            # k is the pointer in sorted array
            i = j = k = 0

            # Until we reach either end of either left or right, pick larger among
            # elements left and right and place them in the correct position at A[p..r]
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                k += 1

            # When we run out of elements in either left or right,
            # pick up the remaining elements and put in A[p..r]
            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1
    
array = [6, 5, 12, 10, 9, 1]
ms = MergeSort()
ms.merge_sort(array)

print(array)