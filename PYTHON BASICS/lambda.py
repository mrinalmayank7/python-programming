x=lambda a,b : a+b
print(x(4,2))

lis=[1,4,5,6,7,90,23,45,66,88]
x=list(filter(lambda even :(even%2==0),lis)) #lis is input 
print(x)                               #filter

m=list(filter(lambda i :(i%3==0 or i%5==0),lis)) #lis is input 
print(m) 

def func(n):                          #function
    return lambda odd : odd%2 !=0
print(bool(func(5)))
     
pizza= ["Mexican","Indian","Italian"]         #map for moification
x=list(map(lambda y : (str.upper(y)),pizza))
print(x)

from functools import reduce #or directly import functools
z=reduce(lambda p ,q :p+q,lis) #lis is input 
print(z) 

day = ['Monday', 'Tuesday', 'Wednesday']
filter_len = filter(lambda x:len(x)==6,day)
for z in filter_len:
  print(z)

z=list(map(lambda num:num*5,lis)) #multiply with list
print(z)
