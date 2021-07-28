def BUBBLE(List ,n):  

    for i in range(0,n-1):  
        for j in range(0,n-i-1):  
            if(List[j]>List[j+1]):  
                temp = List[j]  
                List[j] = List[j+1]  
                List[j+1] = temp  
    return List  
  
n=int(input("ENTER THE SIZE OF THE LIST :"))

List=[]
for i in range(n):
    item = int(input("ENTER ELEMENT "))
    List.append(item)
print("UNSORTED : ", List)   
print("SORTED : ", BUBBLE(List,n))