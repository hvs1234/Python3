def find_odd_and_even(arr):
    odd = []
    even = []
    for i in arr:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return odd,even

input_array = input("Enter elements in array: ")
arr = list(map(int,input_array.split()))
odd, even = find_odd_and_even(arr)
print(f"Odd elements in array is: {odd}")
print(f"Even elements in array is: {even}")

        