# ---------------- Merge Sort ----------------- #

"""
Merge sort is a sorting algorithm that divides a list into two halves,
recursively sorts each half, and then merges the sorted halves to produce
a sorted list. Merge sort uses 2 functions: merge() and merge_sort().
The merge() function merges 2 sequential, sorted partitions within a list and has 4 parameters:

1. The list of numbers containing the 2 sorted partitions to merge
2. The start index of the first sorted partition
3. The end index of the first sorted partition
4. The end index of the second sorted partition

The merge_sort() function sorts a partition in a list and has 3 parameters:

1. The list containing the partition to sort
2. The start index of the partition to sort
3. The end index of the partition to sort
"""

def merge(nums, left_start, left_end, right_end):
    merged_size = right_end - left_start + 1
    merged_nums = [0] * merged_size                  # Dynamically allocates temp array for merged numbers

    merge_pos = 0                                    # Index in which to insert merged number
    left_pos = left_start
    right_pos = left_end + 1

    # Add smallest element from left or right partition to merged_nums
    while (left_pos <= left_end and right_pos <= right_end):
        if (nums[left_pos] <= nums[right_pos]):
            merged_nums[merge_pos] = nums[left_pos]
            left_pos += 1
        else:
            merged_nums[merge_pos] = nums[right_pos]
            right_pos += 1
        merge_pos += 1

    while (left_pos <= left_end):
        merged_nums[merge_pos] = nums[left_pos]
        left_pos += 1
        merge_pos += 1

    while (right_pos <= right_end):
        merged_nums[merge_pos] = nums[right_pos]
        right_pos += 1
        merge_pos += 1

    for merge_pos in range(merged_size):
        nums[left_start + merge_pos] = merged_nums[merge_pos]


def merge_sort(nums, start, end):
    mid = 0

    if start < end:
        mid = start + (end - start) // 2
        merge_sort(nums, start, mid)
        merge_sort(nums, mid + 1, end)

        merge(nums, start, mid, end)



# Create a list of unsorted values
numbers = [61, 76, 19, 4, 94, 32, 27, 83, 58]

# Print unsorted list
print('UNSORTED:', numbers)

# Initial call to merge_sort
merge_sort(numbers, 0, len(numbers) - 1)

# Print sorted list
print('SORTED:', numbers)

