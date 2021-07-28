pizza = "Dominos , khushiyon ki home delivery"
print("Dominos" in pizza)
print("SRT" not in pizza)
print("Dominos" not in pizza)

print(pizza[2:6])#slicing
print(pizza[:6])#slicing form start
print(pizza[2:])#slicing from end
print(pizza[-2:-1])#negative slicing
print(len(pizza))
print(pizza.upper())
print(pizza.lower())
print(pizza.replace("D","A"))#Replace

city = " In chandigarh"
print(pizza + city)
print(pizza.split())#split function
print(pizza.count("h"))
print(pizza[3:10].count("h"))

uid="MY UID IS {} AND MY FRIEND UID IS {}"
name="Number 2 is {1} and number 1 is {0}"
num = 1605
num2 = 1345
print(uid.format(num,num2))
print(name.format(num,num2))

#a="name"name"name" #shows error
print("name\"name\"name")

txt="My name "
print(max(txt))
print(min(txt))
print(txt[0:2]+" Year")

y="Heart"
print(y*3)
print(txt.count("a",1,16))
print(txt.index("name"))
print(txt.find("sss"))
print(txt.find("srt"))
#print(txt.index("srt"))# error as srt is not in the string
mid = int(len(txt)/2)
print(txt[mid])
print(txt[mid-1 :mid+2]) #print middle 3