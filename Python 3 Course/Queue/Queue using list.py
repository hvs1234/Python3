queue = []
def enqueue():
    ele = input("Enter the element: ")
    queue.append(ele)
    print(queue,end=" ")

def dequeue():
    if not queue:
        print("\nQueue is empty!")
    else:
        e = queue.pop(0)
        print(f"Element removed: {e}")
        print(queue,end=" ")

while True:
    print("\nSelect your choice - 1.enqueue 2.dequeue 3.exit")
    ch = int(input('Enter your choice: '))
    match ch:
        case 1: enqueue()
        case 2: dequeue()
        case 3: break
        case _: print("Invalid choice!")
        