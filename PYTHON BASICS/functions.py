def name():
    print("Mrinal") #function block end
name()

def pizza(x):
    print(x+ " crust")  #function block end
pizza("fresh pan")
pizza("Wheat thin")
pizza("classic")

def multiply(b,c):
    print(b*c)  #function block end
multiply(2,3)

 
def meal(type1 ,time =8):  #time is default ,so if we missed it no error will be created 
    print(type1 ," Time is ", time)   #function block end
meal(type1="dinner")
meal(time = 3 ,type1="lunch")
meal("brunch",11) #order matters

def yourname(firstname , lastname = " mayank"):
    print(firstname + lastname)     #function block end

yourname(firstname = "Mrinal")
yourname(lastname = "bhagat ",firstname = " Mrinal ") #order does not matters 

def multiply(b,c):
    return b*c   #function block end
b=int(input("Var 1:"))
c=int(input("Var 2:"))
print(multiply(b,c))