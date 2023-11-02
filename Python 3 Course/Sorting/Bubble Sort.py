# Bubble sort in python
import numpy as np
def bubblesort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
    return arr

input = input("Enter elements in array: ")
try:
    arr = list(map(int,input.split()))
    print(bubblesort(arr))
except ValueError:
    print("Invalid input. Please write correct integers")