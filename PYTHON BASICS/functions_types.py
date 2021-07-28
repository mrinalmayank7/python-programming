
def record(UID , Name , Department = "CSE"):
    print(Name ," UID is ",UID," and is in " ,Department ," Department")

record( Name ="Mrinal",UID =1605)#Keyword , here order does not matters 
record(1605 ,"Mrinal") #default department taken as CSE
record(1549 ,"Ukshit",Department=" ECE") #Name and UID are required argument and order matters

def fruits(*a): #can print till any number
    for i in a:
        print(i)

fr=["Apple","Banana"]
fruits(fr)

# record(Name="Mrinal",UID=1605,UID=1549)   #error as keyword arg repeated
#def pizza(y= 2,x): #shows error with non default arg followed by default arg
#    print(x,y )  


def fruit(x=5): #shows error with non default arg followed by default arg
    print(x)  

print(fruit("ann))


