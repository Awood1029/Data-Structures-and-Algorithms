# -------------- Insertion Sort --------------- #

"""
Insertion sort is a sorting algorithm that treats the input as two parts,
a sorted part and an unsorted part, and repeatedly inserts the next value
from the unsorted part into the correct location in the sorted part.

Initially we assume the first number is sorted, so we start i at 1.

Average runtime is O(n^2)
"""

def insertion_sort(num_list):
    for i in range(1, len(num_list)):
        j = i

        while (j > 0 and num_list[j] < num_list[j - 1]):
            # Swap num_list[j] and num_list[j - 1]
            temp = num_list[j]
            num_list[j] = num_list[j - 1]
            num_list[j - 1] = temp
            j -= 1



numbers = [12, 34, 2, 1, 6, 47, 11, 22, 9]

print("Unsorted: ", numbers)

insertion_sort(numbers)

print("Sorted: ", numbers)
