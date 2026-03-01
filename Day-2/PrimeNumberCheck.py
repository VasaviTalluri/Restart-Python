""" 
To check if the given number is prime or not,conditions are
 1) first it should not be 0 and 1 
 2) it should have only two factors 1 and itself i.e 1 and x.
 3) it should not divisible by any number from 2 to x-1.
"""
x=int(input("Enter number:"))
if x<=1:
    print(f"{x} is not a prime number")
k=0
for i in range(2,x):
    if x%i==0:
        k=1
if k==0:
    print(f"{x} is a prime number")
else:
    print(f"{x} is not a prime number")
    


