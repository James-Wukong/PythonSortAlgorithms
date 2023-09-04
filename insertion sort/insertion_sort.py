class InsertionSort:
    """
    A class representing a insertion sorting algorithm
    """
    def __init__(self, elements: list = None):
        self.elements = elements

    def insertion_sort(self, elements: list = None) -> list:
        if elements is None and self.elements is not None:
            elements = self.elements

        # if the list contains less than 2 elements, dont sort
        if elements is None or len(elements) <= 1:
            return

        for step in range(1, len(elements)):
          key = elements[step]
          j = step - 1
            
          # Compare key with each element on the left of it until an element smaller than it is found
          # For descending order, change key<elements[j] to key>elements[j].        
          while j >= 0 and key < elements[j]:
              elements[j + 1] = elements[j]
              j = j - 1
            
          # Place key at after the element just smaller than it.
          elements[j + 1] = key