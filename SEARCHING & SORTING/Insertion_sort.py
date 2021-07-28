
def INSERTION(List ,n):
    for i in range(1,n):  
        temp = List[i]   
        j = i-1  
        while j>=0 and temp <=List[j]:  
            List[j+1]=List[j]  
            j = j-1  
        List[j+1] = temp
    return List
	

n=int(input("ENTER THE SIZE OF THE LIST :"))
List=[]
for i in range(n):
    item = int(input("ENTER ELEMENT "))
    List.append(item)

print("UNSORTED : ", List)  
print("SORTED : ", INSERTION(List,n))
