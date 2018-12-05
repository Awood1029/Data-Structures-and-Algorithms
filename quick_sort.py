# ------------ Quick Sort ---------------- #

"""
Quick sort uses two different functions to operate.
Firstly, a partition function will need to be created,
which will be passed an unsorted list, a low index, and a high index.
The function will find a pivot point, put all numbers lower than
the pivot point before it, and all numbers higher after it.
The function then returns the last index of the lower part.

Next, a function called quick_sort will be called,
which will use the partition function to determine the low and high
partitions. The function will then recursively call itself using
the partitions passed in.
"""

import random

def partition(numbers, low_index, high_index):
    midpoint = low_index + (high_index - low_index) // 2
    pivot_value = numbers[midpoint]

    done = False
    while not done:
        while numbers[low_index] < pivot_value:
            low_index += 1

        while numbers[high_index] > pivot_value:
            high_index -= 1

        if low_index >= high_index:
            done = True
        else:
            temp = numbers[low_index]
            numbers[low_index] = numbers[high_index]
            numbers[high_index] = temp
            low_index += 1
            high_index -= 1

    return high_index

def quick_sort(numbers, low_index, high_index):
    if high_index <= low_index:
        return

    high = partition(numbers, low_index, high_index)

    quick_sort(numbers, low_index, high)
    quick_sort(numbers, high+1, high_index)



# Main program to test the quicksort algorithm.
"""num_list = []
for i in range(0, 300):
    x = random.randint(0, 800)
    num_list.append(x)"""

numbers = [12, 18, 3, 7, 32, 14, 91, 16, 8, 57]
print('UNSORTED:', numbers)

quick_sort(numbers, 0, len(numbers)-1)
print('SORTED:', numbers)