def selection_sort(arr):
    for i in range (0,len(arr)-1):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i] , arr[min_index] = arr[min_index] , arr[i]
    return arr
 
input_array = input('Enter elements in array: ')
arr = list(map(int,input_array.split()))
print(f"Original Array is: {arr}")
print(f"Array after selection sort: {selection_sort(arr)}")