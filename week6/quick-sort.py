# Simple Sorted Array Method
print('\n')

array = [8, 2, 6, 4, 5]

def sortedArr(array):
    sorted(array)

sortedArr(array)
print(f'Using Sorted array method: {array}')

# --------------------
print(3*'\n*', '\n')


# Source: https://www.geeksforgeeks.org/python-program-for-quicksort/

# Partitioning Array
def partition(array, low_index, high_index) :

    # Setting the 'first' element in the array
    # and the pivot point of the array
    low = (low_index-1)
    pivot_index = array[high_index]

    # for loop of range between low and high indexes
    for j in range(low_index, high_index):
        if array[j] <= pivot_index: 

            # incrementing smaller elements index 
            low = low+1
            array[low], array[j] = array[j], array[low+1]
    array[low+1], array[high_index] = array[high_index], array[low+1]
    return(low+1)


# Quick Sort Array with Partition index

def quickSort(array, low_index, high_index):
    if len(array) == 1:
        return array
    if low_index < high_index:
        
        # This is the partition index
        partition_index = partition(array, low_index, high_index)

        # Calling sort Elements before partition and after
        quickSort(array, low_index, partition_index-1)
        quickSort(array, partition_index+1, high_index)

# Running Code
array = [10, 7, 8, 9, 1, 5]
n = len(array)
quickSort(array, 0, n-1)
print(f'Using first element as pivot Sorted arrray:')
for i in range(n):
    print('%d' % array[i]),

# -------------------------

print(3*'\n*', '\n')


# Source: https://www.geeksforgeeks.org/quicksort-using-random-pivoting/
import random

'''
The function which implements randomised
QuickSort, using Haore's partition scheme.
arr :- array to be sorted.
start :- starting index of the array.
stop :- ending index of the array.
'''
def quicksort(arr, start, stop):
    if(start < stop):
        
        # pivotindex is the index where
        # the pivot lies in the array
        pivotindex = partitionrand(arr,\
                              start, stop)

        # At this stage the array is
        # partially sorted around the pivot.
        # separately sorting the left half of
        # the array and the right
        # half of the array.
        quicksort(arr , start , pivotindex)
        quicksort(arr, pivotindex + 1, stop)
 
# This function generates random pivot,
# swaps the first element with the pivot
# and calls the partition function.
def partitionrand(arr , start, stop):
 
    # Generating a random number between
    # the starting index of the array and
    # the ending index of the array.
    randpivot = random.randrange(start, stop)
 
    # Swapping the starting element of
    # the array and the pivot
    arr[start], arr[randpivot] =\
        arr[randpivot], arr[start]
    return partition(arr, start, stop)
 
'''
This function takes the first element
as pivot, places the pivot element at
the correct position in the sorted array.
All the elements are re-arranged according
to the pivot, the elements smaller than
the pivot is places on the left and
the elements greater than the pivot is
placed to the right of pivot.
'''
def partition(arr,start,stop):
    pivot = start # pivot
    i = start - 1
    j = stop + 1
    while True:
        while True:
            i = i + 1
            if arr[i] >= arr[pivot]:
                break
        while True:
            j = j - 1
            if arr[j] <= arr[pivot]:
                break
        if i >= j:
            return j
        arr[i] , arr[j] = arr[j] , arr[i]
 
# Driver Code
if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    quicksort(array, 0, len(array) - 1)
    print(f'Sorted array using random pivot {array}')

# -------------------------

print(3 * '\n*', '\n')


# Source: https://realpython.com/sorting-algorithms-python/
from random import randint
from timeit import repeat


def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Execution time is: {min(times)}")

ARRAY_LENGTH = 10000

if __name__ == "__main__":
    # Generate an array of `ARRAY_LENGTH` items consisting
    # of random integer values between 0 and 999
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    # Call the function using the name of the sorting algorithm
    # and the array you just created
    run_sorting_algorithm(algorithm="sorted", array=array)