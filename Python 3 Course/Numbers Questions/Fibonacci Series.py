ch = int(input('Enter your choice: '))
match ch:
    case 1:
        # Using Iterative:-
        def fibo1(n):
            a = 0; b = 1
            for i in range(1,n+1):
                c = a+b
                a,b = b,c
                print(c,end=" ")
                
        n = int(input("Enter last term of series: "))
        fibo1(n)

    case 2:
        # Using Recursion:-
        def fibo2(n):
            if n<=0: return -1
            elif n==1: return 0
            elif n==2: return 1
            return fibo2(n-1)+fibo2(n-2)
        
        n = int(input("Enter last term of series: "))
        for i in range(1,n+1):
            print(fibo2(i),end=" ")