def find_median(arr):
    sort_arr = sorted(arr)
    n = len(sort_arr)
    if n%2 == 0:
        mid_left = sort_arr[n // 2 - 1]
        mid_right = sort_arr[n // 2]
        median = (mid_left+mid_right)/2
    else:
        median = sort_arr[n // 2]
    return median

input_array = input("Enter the elements in array: ")
arr = list(map(int,input_array.split()))
print(f"Median of {arr} is: {find_median(arr)}")
