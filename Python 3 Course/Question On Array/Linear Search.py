def linear_search(arr,target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices

input_array = input("Enter the elements in array: ")
arr = list(map(int,input_array.split()))
target = int(input("Enter the target element in array: "))
result = linear_search(arr,target)
if result:
    print(f"Element {target} found at index: {result}")
else:
    print(f"Element {target} not found in array")
