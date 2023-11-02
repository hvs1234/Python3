def remove_duplicate(arr):
    unique = []
    for i in arr:
        if i not in unique:
            unique.append(i);
    return unique

input = input("Enter elements: ")
arr = list(map(int,input.split()))
print('Original array: ',arr)  
print('Array after removing duplicates: ',remove_duplicate(arr))