"""
To list out the fibonacci series, condition is
  f(n)=f(n-1)+f(n-2)
"""
n=int(input("Enter number: "))
x,y=0,1
for i in range(n):
    print(x,end=" ")
    x,y=y,x+y


    

