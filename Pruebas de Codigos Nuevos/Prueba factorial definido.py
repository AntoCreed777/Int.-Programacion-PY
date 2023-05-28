def factorial(n):
    a=1
    while n>0:
        a=a*n
        n=n-1
    return a
n=int(input())
print (factorial (n))

#O se puede hacer asi

def factorial(n):
    a=1
    while n>0:
        a=a*n
        n=n-1
    print(a)
n=int(input())
factorial (n)

#Otra forma de sumar

d=1
d+=1
print (d)