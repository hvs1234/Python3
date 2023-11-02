def prime_no(num):
    if num<=1: return False
    for i in range(2,int(num//2)+1):
        if num%i==0:
            return False
    return True

num = int(input("Enter the number: "))
if prime_no(num):
    print(f"{num} is prime number")
else:
    print(f"{num} is not a prime number")