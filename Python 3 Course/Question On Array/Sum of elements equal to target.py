def sum_of_target(arr,k):
    pairs = []
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]+arr[j]==k):
                pairs.append([arr[i],arr[j]])
    return pairs

def sum_of_array(arr):
    sum = 0
    for i in arr:
        sum+=i
    return sum

input_array = input("Enter elements in array: ")
arr = list(map(int,input_array.split()))
k = int(input("Enter the target element in array: "))
result = sum_of_target(arr,k)
if result:
    print(f"Pairs found for {k} is: {result}")
else:
    print(f"No Pairs found for {k}")
print("Sum of elements in array is: ",sum_of_array(arr))
