print("Name :Mrinal Mayank")
print("UID :1605")

name="MRINAL MAYANK"
count = 0
for i in name: 
    count+= 1
print("LENGTH OF Name IS :" ,count) #print length of name

mid =int(len(name)/2)
if(name[mid]==" "):
    print("MIDDLE CHARACTER IS SPACE") #print message if middle character is space
else:
    print("MIDDLE CHARACTER IS :" ,name[mid]) #print middle character

print("STRING AFTER REPLACEMENT :" ,name.replace(name[mid],"1605"))#replace middle character

print("Name :Mrinal Mayank")
print("UID :1605")
def exchange(arg):
      return arg[-1:] + arg[1:-1] + arg[:1]

#the above function will first append the last character
#then it will add middle values leaving first and last character
#then it will add the first character at the end 
#this method is called slicing
	  
print("STRING AFTER EXCHANGING FIRST AND LAST LETTER :",exchange('MRINAL'))