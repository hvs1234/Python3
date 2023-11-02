class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_last(self,data):
        new_node = Node(data)
        if self.head is None: 
            self.head = new_node 
        else:
            node = self.head
            while node.ref is not None:
                node = node.ref
            node.ref = new_node

    def add_after_node(self,data,x):
        node = self.head
        while node is not None:
            if x==node.data: break
            node = node.ref
        if node is None: print("Node is not present in linkedlist")
        else:
            new_node = Node(data)
            new_node.ref=node.ref
            node.ref=new_node

    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty. At least head is present")

    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty! You can't delete the first node.")
            return
        else:
            self.head = self.head.ref
    
    def delete_last(self):
        if self.head is None:
            print("Linked list is empty!. You can't delete the last node.")
        else:
            node = self.head
            while node.ref.ref is not None:
                node = node.ref
            node.ref = None

    def print_list(self):
        if self.head is None: print("Linked list is empty")
        else:
            node = self.head
            while node is not None:
                print(node.data,end="-> ")
                node = node.ref

l = Linkedlist()
while True:
    print("\nSelect choice - 1.add data in begin 2.add data in last 3.add data after the given node 4.insert data in empty linkedlist 5.delete at first node in linked list 6.delete last node in linked list 7.exit")
    ch = int(input("Enter your choice: "))
    match ch:
        case 1:
            data = int(input("Enter the data in beginning of linked list: "))
            l.add_begin(data)
            l.print_list()
        case 2:
            data = int(input("Enter the data in last of linked list: "))
            l.add_last(data)
            l.print_list()
        case 3:
            data = int(input("Enter the data you want to insert: "))
            x = int(input("Enter the value for which you want to insert data after it: "))
            l.add_after_node(data,x)
            l.print_list()
        case 4:
            data = int(input("Enter element or head in empty linked list: "))
            l.insert_empty(data)
        case 5:
            l.delete_begin()
            l.print_list()
        case 6:
            l.delete_last()
            l.print_list()
        case 7: break
        case _: print("Invalid choice!")