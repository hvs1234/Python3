def reverse_array(arr,n):
    n = len(arr)
    for i in range(n // 2):
        arr[i] , arr[n-i-1] = arr[n-i-1] , arr[i]
    return arr

n = input("Enter length of array: ")
print("Enter ",n," elements in array: ")
input = input("")
arr = list(map(int,input.split()))
print("Reverse elements in array: ",reverse_array(arr,n))