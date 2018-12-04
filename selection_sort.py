# --------- Selection Sort --------------- #

"""
Selection sort treats input as two parts, a sorted part and unsorted part.
Variables i and j keep track of the two parts.
Selection sort searches the unsorted part of the array for the smallest element.
indexSmallest stores the index of the smallest element found.
Elements at i and smallestIndex are swapped.
Indices are updated and process is repeated until list is sorted.

Runtime is O(n^2).
"""

def selection_sort(numbers):
    # We do len(numbers) - 1 because the last number will have to be
    # in ordder by the time i iterates through the second to last number
    for i in range(len(numbers)-1):

        # Assume that starting point is the smallest, then iterate through to find
        # the true smallest number in list.
        index_smallest = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[index_smallest]:
                index_smallest = j

        # Once we find the smallest number for the iteration,
        # we must swap it with first unsorted number, represented by index of i
        temp = numbers[i]
        numbers[i] = numbers[index_smallest]
        numbers[index_smallest] = temp


numbers = [10, 3, 8, 5, 14, 22, 2, 74, 54, 1]

print("Unsorted numbers: ", numbers)

selection_sort(numbers)

print("Sorted: ", numbers)
        
            

