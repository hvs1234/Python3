class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None

class DoublyList:
    def __init__(self):
        self.head = None

    def insert_begin_doublylist(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
            
    
    def print_doubly_list(self):
        if self.head is None: print("Linked list is empty!")
        else:
            node = self.head
            while node is not None:
                print(node.data,end="->")
                node = node.nref
    
    def print_doubly_list_reverse(self):
        if self.head is None: print("Linked list is empty!")
        else:
            node = self.head
            while node.nref is not None:
                node = node.nref
            while node is not None:
                print(node.data,end="->")
                node = node.pref

while True:
    print("\nSelect your choice from 1.insert at begin, 2.exit")
    dl = DoublyList()
    ch = int(input("Enter your choice: "))
    match ch:
        case 1:
            data = int(input("Enter the data: "))
            dl.insert_begin_doublylist(data)
            dl.print_doubly_list()00
        case 2: break
        case _: print("Invalid Choice!")