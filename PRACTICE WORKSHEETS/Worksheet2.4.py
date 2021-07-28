print("Name :Mrinal Mayank")
print("UID :19BCS1605")
#changing values of tuples  
#first convert the tuple in list
#It is called type conversion 
# After converting Tuple in List it can be modified 
# As list is changable but tuple is not changable 
# Convert back again modified List in tuple 

t = (20,30,55,66,77)
print("ORIGINAL TUPLE :" ,t)
List= list(t)
i = int(input("Enter the position to modify : "))
j = int(input("Enter the element to replace : "))
List[i]=j

print("MODIFIED TUPLE :" ,tuple(List))


#FUNCTION 
#Here it will check if i is present in Tuple of Tuples 
#any is the sequence of OR operations 
#if in any TUPLES in TUPLE contain i then it will return true 

def CHECK(Numbers, i):
    OUT = any(i in Tuple for Tuple in Numbers)
    return OUT

Numbers = (('One', 'Two', 'Three'), ('Four', 'Five', 'Six'), ('Seven', 'Eight', 'Nine'))
print("ORIGINAL LIST :" ,Numbers)
i=str(input("ENTER THE ELEMENT TO CHEK IT IS IN THE ORIGINAL LIST :"))
if CHECK(Numbers, i)==True :
    print(i , " is present in said tuple of tuples")
else :
    print(i , " is NOT present in said tuple of tuples")
