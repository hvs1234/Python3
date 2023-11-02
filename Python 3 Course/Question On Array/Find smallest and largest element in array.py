def find_smallest_largest(arr):
    if not arr:
        return None,None
    min = max = arr[0]
    for i in arr:
        if i<min:
            min = i
        if i>max:
            max = i
    return min,max

n = int(input("Enter size of array: "))
arr = []
print(f"Enter {n} elements in array: ")
for i in range(n):
    x = int(input(f"arr[{i}] = "))
    arr.append(x)
min,max = find_smallest_largest(arr)
print(f"Smallest element in {arr} is: {min}")
print(f"Largest element in {arr} is: {max}")