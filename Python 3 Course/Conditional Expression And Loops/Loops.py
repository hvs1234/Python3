ch = int(input("Enter your choice from [1,2]: "))
match ch:
    case 1:
        # for loop
        n = int(input("Enter last term of fibonacci series: "))
        a = 0; b = 1
        print("Fibonacci Series is: ",end="")
        for i in range(1,n+1):
            c = a+b
            a,b = b,c
            print(f"{c}",end=" ")
    case 2:
        # while loop
        n = int(input("Enterf the number: "))
        rev = 0
        print(f"Reverse of {n} is: ",end="")
        while n>0:
            rev = rev*10 + n%10
            n = n//10
        print(f"{rev}")
    case _:
        print("Invalid Choice")