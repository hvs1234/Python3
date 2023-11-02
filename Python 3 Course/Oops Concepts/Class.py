class Num:
    def add(self):
        return self.a + self.b
    def fact(self,n):
        if n == 0 or n == 1: return 1
        return n*self.fact(n-1) 
    def fibo(self,term):
        self.a = 0; self.b = 1
        for i in range(1,term+1):
            self.c = self.a+self.b
            self.a,self.b = self.b,self.c
            print(self.c,end=" ")
    def prime(self,prime_no):
        self.flag = 0
        if prime_no<0: return -1
        for i in range(2,int(prime_no//2)+1):
            if prime_no%i==0: self.flag=1
        if self.flag == 0: print(f"{prime_no} is prime number")
        else: print(f"{prime_no} is not a prime number")

class A:
    a = 3

    def print(self):
        print(f"{self.a+3}")
        
    @staticmethod
    def print1():
        print(f"Hello world in python")

class constructor:
    def __init__(self,name,salary,gender):
        self.name = name
        self.salary = salary
        self.gender = gender
    
    def get(self):
        print(f"Name is: {self.name}")
        print(f"Salary is: {self.salary}")
        print(f"Gender is: {self.gender}")

# obj = A()
# # obj.print()
# obj.print1()

        
# num = Num()
# num.a = int(input("Enter first number: "))
# num.b = int(input("Enter second number: "))
# print(f"The sum of {num.a} and {num.b} is: {num.add()}")

# n = int(input("Enter number: "))
# print(f"Factorial of {n} is: {num.fact(n)}")

# n = int(input("Enter the number: "))
# num.prime(n)

name = str(input("Enter the name: "))
salary = int(input("Enter the salary: "))
gender = str(input("Enter the gender: "))
obj = constructor(name,salary,gender)
obj.get()
