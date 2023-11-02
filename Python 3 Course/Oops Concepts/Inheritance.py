class A:
    def fact(self,n):
        if n==0 or n==1: return 1
        else: return self.fact(n-1)*n

class B(A):
    def prime(self,n):
        self.flag = 0
        if n<0: return -1
        for i in range(2,int(n//2)+1):
            if n%i == 0:
                self.flag = 1
        if self.flag == 0: return True
        else: return False

class C(B,A): pass

# Inheritance: - It is a way of creating new class from an existing class.
ch = int(input("Enter choice [1,2,3,4]: "))
match ch:
    case 1:
        # Single level inheritance:- It occurs when a derived or child class inherits only one parent class.
        n = int(input("Enter the number: "))
        obj1 = B(); print(f"Factorial of {n} is: {obj1.fact(n)}")

    case 2:
        # Multiple level inheritance:- It occurs when a derived or child class inherits more than one base or parent class.
        obj2 = C()
        n = int(input("Enter the number: "))
        print(f"Factorial of {n} is: {obj2.fact(n)}")
        num = int(input("Enter the number to check whether it's prime or not: "))
        result = obj2.prime(num)
        if result: print(f"{num} is prime number")
        else: print(f"{num} is not a prime number")

    case 3:
        # Multilevel inheritance:- It occurs when a derived class or child class becomes a parent of another child class.
        pass
    
    case 4:
        pass
    case _:
        print("Invalid choice!")
