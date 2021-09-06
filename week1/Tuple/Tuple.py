from collections import defaultdict

# Setting up Tuple of Tuples 
classes = (
    ('V', 1),
    ('VI', 1),
    ('V', 2),
    ('VI', 2),
    ('VI', 3),
    ('VII', 1),
)

# Calling for a defaultdict list
rollno = defaultdict(list)

# For loop to append name with 'id' numbers
for name, id in classes:
    rollno[name].append(id)
    
# printing List 
print(rollno)


# Output: 
# defaultdict(<class 'list'>, {'V': [1, 2], 'VI': [1, 2, 3], 'VII': [1]})