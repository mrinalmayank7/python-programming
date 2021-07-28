pizza = ("Veg","Non veg","Pizza Mania ","Pasta Pizza","Sides")

print(pizza)
print(len(pizza))
print(type(pizza))
tuple1=("apple",) #tuple are separated by commas , even if there is one element 
tuple2=("apple") #not a tuple 
print(type(tuple1))
print(type(tuple2))

tuple3 =tuple(("A","B","C")) #tuple  constructor 
print(tuple3)
print(tuple3[1]) #print item 
print(pizza[1:2]) #slicing with tuple
print(pizza[-1:]) # check last element 

#changing values of tuples  , first convert the tuple in list
#it is called type conversion and list is changable but tuple is not changable 
List = list(pizza)
print(List)
List.insert(0,"Drinks")
print(List)
tuple4 = tuple(List) #change modified list in tuple then print 
print(tuple4)


#PACKING AND UNPACKING TUPLE
# ONE TO ONE MAPPING  
tuple5=("Coke","Pepsi","Sprite","Mazza") #packing 
(A,B,C,D)=tuple5 #unpacking ...assigning values to A,B,C  
print(A)
print(B)
print(C)
print(D)

#ONE TO MANY MAPPING
(E,*F)=tuple5
print(E)
print(F)


for i in tuple5:
    print(i)

for i in range(len(tuple5)):
    print(tuple5[i])

tuple6=("a","b","c")
tuple7=("A","B","C")
tuple8 = tuple6 +tuple7
print(tuple8)

tuple9=(1,2,3,4,5,5,6)
print(tuple9*2)
print(tuple9.count(1))

print(tuple9.index(1))

    
 

