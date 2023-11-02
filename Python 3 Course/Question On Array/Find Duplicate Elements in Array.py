def duplicate(arr):
    count=1;
    print("Duplicate Elements are: ")
    for i in range(0,len(arr)-1):
        if(arr[i] == arr[i-1]):
            count = count+1;
            print(arr[i],end=" ");
    return  count

input = input("Enter elements in array: ");
try:
    arr = list(map(int,input.split()))
    print("\nDuplicates Elements Count: ",duplicate(arr));
except ValueError:
    print("Invalid integers. Please Enter valid integers")
