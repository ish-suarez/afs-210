# Source where I found the inspiration 
# https://www.w3resource.com/python-exercises/heap-queue-algorithm/python-heapq-exercise-1.php

# Importing heapq and setting variable
import heapq as HeapQ

# numbers that will be used
numbers = [25, 35, 22, 85, 14, 65, 75, 22, 58]
print(f'Original List: {numbers}')

# using heapq to find three largest numbers
three_large_nums = HeapQ.nlargest(3, numbers)
print(f'The three largest numbers are: {three_large_nums}')