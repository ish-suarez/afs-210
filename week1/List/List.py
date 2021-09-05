class List():
    def __init__(self) -> None:
        self.numbers = []
        pass

    def add_num(self):
        for i in range(10): 
            num = int(input(f'Enter a number into the list: '))
            self.numbers.append(num)
            self.numbers.sort()
        

list = List()
list.add_num()
print(f'This is your sorted list from lowest to highest: {list.numbers}')
