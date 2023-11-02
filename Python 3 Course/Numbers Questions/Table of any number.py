def table(n,j):
    if j<=0:
        print(f"Upto number should be greater than 0")
    for i in range(1,j+1):
        print(f"{n} x {i} = {n*i}")

n = int(input("Enter number: "))
j = int(input("Enter number upto table: "))
print(f"Table of {n}")
{table(n,j)}