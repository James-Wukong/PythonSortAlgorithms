## Quick Sort

Quicksort is a sorting algorithm based on the divide and conquer approach where

1. An array is divided into subarrays by selecting a pivot element (element selected from the array).

While dividing the array, the pivot element should be positioned in such a way that elements less than pivot are kept on the left side and elements greater than pivot are on the right side of the pivot.
1. The left and right subarrays are also divided using the same approach. This process continues until each subarray contains a single element.
1. At this point, elements are already sorted. Finally, elements are combined to form a sorted array.

**Time Complexity**: Best Case = Ω(nk), Worst Case = O(nk), Average Case = Θ(nk)

**Space Complexity**: Worst Case = O(n + k)