# Recursion:- It is a property, when a function call itself.

# Using Iterative:-
def fact1(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact

# Using recursion:- 
def fact2(n):
    if n==0: return 1
    if n==1: return n
    return n*fact2(n-1)

n = int(input('Enter the number: '))
print(f"Using Iterative, Factorial of {n} is: {fact1(n)}")
print(f"Using Recursion, Factorial of {n} is: {fact2(n)}")

