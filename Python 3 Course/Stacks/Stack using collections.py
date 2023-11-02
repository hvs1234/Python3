import collections
stack = collections.deque()
def push():
    ele = input("Enter the element: ")
    stack.append(ele)
    print(stack,end=" ")

def pop():
    if not stack:
        print("\nStack is empty!")
    else:
        e = stack.pop()
        print(f"\nElement removed: {e}")
        print(stack,end=" ")

while True:
    print("\nSelect your choice - 1.push 2.pop 3.quit")
    ch = int(input("Enter your choice: "))
    match ch:
        case 1: push()
        case 2: pop()
        case 3: break
        case _: print("\nInvalid Choice!")