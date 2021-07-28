pizza={"name":"Farmhouse" ,"Price":200,"size":"Regular"}
pizza2={"name":"Mexican" ,"Price":300,"size":"Regular","size":"medium"}
#replace size medium with regular as dict does not allow duplicate members
print(pizza2) 
print(pizza)
print(pizza.values()) #print only values
print(pizza.items())  #print keys with values in combination
print(pizza["name"]) #print value of name
print(len(pizza))
print(type(pizza))

for i in pizza:
    print(pizza[i]) #print the values not keys
    
for i in pizza:
    print(i) #print the keys not values

pizza["Offer"]="40%" #add new key and values
print(pizza)
print(pizza.keys()) #print only keys

dominos={"PIZZA" :{"Veg":11,"Non-Veg":11},"BEVERAGE":{"Coke":11,"Sprite":11}} #2 dict in one
print(dominos)


print(bool("PIZZA" in dominos))
print(bool("Veg" in dominos))
print(bool(11 in dominos))
print(bool(11 not in dominos))

print(bool("Farmhouse" in pizza.values()))

pizza.update({"name":"Chicken Dominator"})#update the values  
print(pizza)

pizza.pop("Offer") #pop specific value
print(pizza)


pizza.popitem() #pop last item
print(pizza)

del pizza2["name"] #delete key
print(pizza2)

# del pizza2  #delete whole dictonary
pizza2.clear()# delete all the items
print(pizza2)

pizza3=pizza.copy() #copy content of pizza in pizza3
print(pizza3)


#nested dictonary
A={"Name":"Mrinal"}
B={"Name":"Ukshit"}
Friends ={"F1":A,"F2":B}
print(Friends)
