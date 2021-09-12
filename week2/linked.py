# Initialize single node
class Node:
    def __init__(self, data = None, next = None) -> None:
        self.data = data
        self.next = next
        pass
    
# Linked List Class
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        pass

    # Inserting a new Node
    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    # Print Function 
    def printList(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

# Running The Functions in the Class
LinkedL = LinkedList()
LinkedL.insert('PHP')
LinkedL.insert('Python')
LinkedL.insert('C#')
LinkedL.insert('C++')
LinkedL.insert('Java')
LinkedL.printList()
