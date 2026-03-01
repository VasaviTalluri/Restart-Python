n=int(input("Enter Number:"))
fact=1
if n<0:
    print("Factorial not defined")
elif n==0 or n==1:
    print("Factorial for given number is 1")
else:
    for i in range(1,n+1):
        fact=fact*i
print("Factorial for given number is ",fact)
    
        