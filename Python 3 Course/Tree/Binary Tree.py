class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self,root):
        self.root = Node(root)
    
    def insert(self,data):
        self.insert_data(self.root,data)
    def insert_data(self,node,data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert_data(node.left,data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert_data(node.right,data)
    
    
    def search(self,data):
        return self.search_data(self.root,data)
    def search_data(self,node,data):
        if node is None: return False
        if data == node.data: return True
        if data < node.data:
            return self.search_data(node.left,data)
        return self.search_data(node.right,data)


    def inorder(self):
        return self.inorder_traversal(self.root)
    def inorder_traversal(self,node):
        result = []
        if node:
            result+= self.inorder_traversal(node.left)
            result.append(node.data)
            result+= self.inorder_traversal(node.right)
        return result
    

while True:
    bt = BinaryTree(10)
    print("Select your choice - 1.insert node in tree 2.search node 3.inorder traversal 4.exit")
    ch = int(input("Enter your choice: "))
    match ch:
        case 1:
            data = input("Enter the value to be inserted into the binary tree: ")
            bt.insert(data)
        case 2:
            data = input("Enter the data you want to search in binary tree: ")
            bt.search(data)
        case 3:
            print(bt.inorder())
        case 4: break
        case _: print("Invalid Choice!")