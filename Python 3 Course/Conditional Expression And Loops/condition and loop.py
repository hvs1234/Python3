# if-else condition. 
ch = int(input("Enter your choice: [1,2,3,4]: "))
match ch:
    case 0:
        print("Please enter valid choice!")
    case 1:
        # if, elif and else
        age = int(input("Enter your age: "))
        name = str(input("Enter your name: "))
        if age<18:
            print(f"{name}, your age: {age}. You are below 18. Not applicable for driving license.")
        elif age>=18 and age<=50:
            print(f"{name}, your age: {age}. You are applicable for driving license.")
        else:
            print(f"{name}, your age is above 50, please update your driving license.")
    case 2:
        # nested condition
        n = int(input("Enter the number: "))
        if n<0:
            print(f"{n}<0. Please enter postive number")
        elif n>0:
            if n%2==0:
                print(f"{n} is even number")
            else:
                print(f"{n} is odd number")
        
    case 3:
        # for loop condition
        n = int(input("Enter number: "))
        flag=0
        for i in range(2,int(n//2)+1):
            if n%i==0:
                flag = 1
        if flag==0:
            print(f"{n} is prime number")
        else:
            print(f"{n} is not a prime number")

    case 4:
        # while loop condition
        n = int(input("Enter the number: "))
        rev = 0
        print(f"Reverse of {n} is: ",end="")
        while(n>0):
            rev = rev*10+n%10
            n=n//10
        print(f"{rev}")

    
    