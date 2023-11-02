def odd_even(n):
    if n%2 == 0:
        print(f"{n} is even number")
    else:
        print(f"{n} is odd number")

num = int(input("Enter the number: "))
odd_even(num)