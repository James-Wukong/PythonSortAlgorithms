class SelectionSort:
    """
    A class representing a selection sorting algorithm
    """
    def __init__(self, elements: list = None):
        self.elements = elements

    def selection_sort(self, elements: list = None) -> list:
        if elements is None and self.elements is not None:
            elements = self.elements

        # if the list contains less than 2 elements, dont sort
        if elements is None or len(elements) <= 1:
            return

        size = len(elements)

        for step in range(size):
          min_idx = step

          for i in range(step + 1, size):
              # to sort in descending order, change > to < in this line
              # select the minimum element in each loop
              if elements[i] < elements[min_idx]:
                  min_idx = i
            
          # put min at the correct position
          elements[step], elements[min_idx] = elements[min_idx], elements[step]