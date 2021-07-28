print("Name :Mrinal Mayank")
print("UID :19BCS1605")
  
def fibonacci():
    a,b,c=0,1,0 
    n=int(input("enter the limit: "))
    while c <= n:
        print(c," ")
        a=b
        b=c
        c=a+b
		
fibonacci()

lis=[1,4,5,6,7,90,23,45,66,88,34,56,70,98,80,10,20]
x=list(filter(lambda div :(div%5==0),lis))  
print(x)      

def divisor(x,y):
    if y == 0:
        return x
    else:
        return divisor(y, x%y)

print(divisor(56,divisor(34,64)))


#without recursion
def factorial(num):
    fact=1
    while(num>0):
        fact=fact*num
        num=num-1
    print("Factorial is " ,fact)

n=int(input("Enter number to find factorial : "))
factorial(n)

#with recursion
def fact(x):
   if x == 1:
       return x
   else:
       return x*fact(x-1)

n=int(input("Enter number to find factorial : "))


if n< 0 :
   print("Not exist")
elif n == 0:
   print("The factorial is 1")
else:
   print("The factorial is ",fact(n))