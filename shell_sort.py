# -------------- Shell Sort ------------------ #

"""
Shell sort is a sorting algorithm that treats the input as a collection
of interleaved lists, and sorts each list individually with a variant
of the insertion sort algorithm.

Shell sort uses gap values to determine the number of interleaved
lists. A gap value is a positive integer representing the distace
between elements in an interleaved list. For each interleaved list,
if an element is at index i, the next element is at index i +
gap value.
"""

