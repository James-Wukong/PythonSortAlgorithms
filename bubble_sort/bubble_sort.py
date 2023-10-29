class BubbleSort:
    """
    A class representing a bubble sorting algorithm
    """

    def __init__(self, elements: list = None):
        # instance attribute elements: the target list to be sorted
        self.elements = elements

    def bubble_sort(self, elements: list = None) -> list:
        """
        Returns the sorted (ascending) elements 
        
        Args elements: the original unsorted list
        """
        if elements is None and self.elements is not None:
            elements = self.elements

        # if the list contains less than 2 elements, dont sort
        if elements is None or len(elements) <= 1:
            return

        swapped = False
        # looping through the size of the list: from last element[-1] to the first element[0]
        for n in range(len(elements)-1, 0, -1):
            for i in range(n):
                # place the large element at the end
                if elements[i] > elements[i + 1]:
                    elements[i], elements[i + 1] = elements[i + 1], elements[i]
                    swapped = True

            if swapped is False:
                return

        return