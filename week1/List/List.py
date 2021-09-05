
# Class for list
class List():

    #  Init list of numbers
    def __init__(self) -> None:
        self.numbers = []
        pass
    
    # Add a series of numbers into list, and sort them.
    def add_num(self):
        for i in range(10): 
            num = int(input(f'Enter a number into the list: '))
            self.numbers.append(num)
            self.numbers.sort()
        
        
# Setting list variable and calling input function
list = List()
list.add_num()

# Printing the sorted list
print(f'This is your sorted list from lowest to highest: {list.numbers}')
