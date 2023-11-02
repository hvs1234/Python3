def binary_search(arr,target):
    indices = []
    low=0; high = len(arr)-1;
    while(low<=high):
        mid = (low+high) // 2;
        if(arr[mid] == target):
            left,right = mid,mid
            while left>0 and arr[left-1] == target:
                left-=1 
            while right<len(arr)-1 and arr[right+1] == target:
                right+=1
            indices.extend(range(left,right+1))
            break
        elif(arr[mid] < target):
            low = mid+1;
        else:
            high = mid-1;
    return indices

input_array = input("Enter the elements in array: ")
arr = list(map(int,input_array.split()))
arr1 = []
n = len(arr1)
target = int(input("Enter target element: "))
result = binary_search(arr,target)
if result:
    print(f"Element {target} found at index: {result}")
else:
    print(f"Element {target} not found in array")