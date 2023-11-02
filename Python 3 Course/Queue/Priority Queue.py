import queue
q = queue.PriorityQueue()
def enqueue():
    ele = input("Enter the element: ")
    q.put(ele)
    print(q,end=" ")

def dequeue():
    if not q:
        print("\nPriority queue is empty!")
    else:
        q.get()
        print(q,end=" ")

while True:
    print("Select your choice - 1. enqueue 2.dequeue 3.exit")
    ch = int(input("Enter your choice: "))
    match ch:
        case 1: enqueue()
        case 2: dequeue()
        case 3: break
        case _: print("Invalid choice!")