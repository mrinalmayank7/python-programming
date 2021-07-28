print("Name :Mrinal Mayank")
print("UID :19BCS1605")

Item_code =[12,13,14,15]
Item_name =["Apple","Kiwi","Orange","Banana"]
qty =[13,11,33,21]
price =[200,150,300,250]
ITEM = {"Item_code" :Item_code,"Item_name":Item_name ,"qty":qty,"price": price}

def BUBBLE(List ,n):  

    for i in range(0,n-1):  
        for j in range(0,n-i-1):  
            if(List[j]>List[j+1]):  
                temp = List[j]  
                List[j] = List[j+1]  
                List[j+1] = temp  
    return List  
  
BUBBLE(qty,len(qty)) 
print("Ascending order of qty using Bubble sort :\n",ITEM)


def INSERTION(List ,n):
    for i in range(1,n):  
        temp = List[i]   
        j = i-1  
        while j>=0 and temp >=List[j]:  
            List[j+1]=List[j]  
            j = j-1  
        List[j+1] = temp
    return List
INSERTION(price,len(price)) 
print("In descending order of price using Insertion sort. :\n",ITEM)
