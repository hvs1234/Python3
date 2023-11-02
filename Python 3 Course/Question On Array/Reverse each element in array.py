def reverse_element_in_array(arr):
    reversed_array = []
    for i in arr:
        if isinstance(i,str):
            reverse = i[::-1]
        elif isinstance(i,list):
            i.reverse()
            reverse = i
        else:
            reverse = str(i)[::-1]
        reversed_array.append(reverse)
    return reversed_array

input_array = input("Enter elements in array: ")
arr = list(map(int,input_array.split()))
print(f"Original array: {arr}")  
print(f"Reverse each elements inside array: {reverse_element_in_array(arr)}")