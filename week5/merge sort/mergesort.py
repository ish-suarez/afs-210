# Here is my source: https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheMergeSort.html


# Merge Sort Function that takes an Array of numbers
def mergeSort(alist):
    print(f'Splitting: {alist}')

    # if there list is populated run thins
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        # Split and sort the other half
        mergeSort(lefthalf)
        mergeSort(righthalf)

        # setting index variable for nums in half
        i, j, k = 0, 0, 0
        
        # running while loop when both halfs are populated
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    print(f'Merging: {alist}')

alist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
mergeSort(alist)
print(alist)