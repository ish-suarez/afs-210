# This is the source of my work: https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-1.php

# Binary Search
def ordered_binary_search(num_list, num):
    # setting the first, last indexes and if the number is found.
    first = 0 
    last = len(num_list)-1
    found = False

    # Running a while loop to
    while(first <= last and not found):
        # Setting mid number
        mid = (first + last)//2

        # If else statements to run though the separete half
        if num_list[mid] == num:
            found = True
        else:
            if num < num_list[mid]:
                last = mid - 1
            else: 
                first = mid + 1
    return found

print(ordered_binary_search([0, 1, 3, 8, 14, 18, 19, 34, 52], 3))
print(ordered_binary_search([0, 1, 3, 8, 14, 18, 19, 34, 52], 17))