# Source for this Assignment 
# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-binary-search-tree-exercise-1.php

class TreeNode(object):
    # Initiating Data
    def __init__(self, data) -> None:
        self.val = data
        self.left = None
        self.right = None
        pass

# sorting numbers in node
def sorted_array_to_bst(nums):
    # return nothing if Not a number
    if not nums:
        return None
    # Gathers the middle value of the list
    mid_val = len(nums)//2
    # setting node at the middle value
    node = TreeNode(nums[mid_val])
    # setting left and right node numbers
    node.left = sorted_array_to_bst(nums[:mid_val])
    node.right = sorted_array_to_bst(nums[mid_val+1:])
    return node

# Order numbers in node
def preOrder(node): 
    if not node: 
        return      
    print(node.val)

    # setting Left and right of node 
    preOrder(node.left) 
    preOrder(node.right)   

# calling function and giving numbers as parameters
result = sorted_array_to_bst([1, 2, 3, 4, 5, 6, 7])

# Sorting the results
preOrder(result)
