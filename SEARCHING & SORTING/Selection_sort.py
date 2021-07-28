
def SELECTION(List , n):
    for i in range(0,n):
        small=List[i]
        pos=i
        for j in range(i+1 , n):
            if(List[j]<small):
                small=List[j]
                pos=j        
        tmp=List[i]
        List[i]=List[pos]
        List[pos]=tmp 
    return List

n=int(input("ENTER THE SIZE OF THE LIST :"))
List=[]
for i in range(n):
    item = int(input("ENTER ELEMENT "))
    List.append(item)

print("UNSORTED : ", List)  
print("SORTED : ", SELECTION(List,n))


# SET MIN to INDEX 0
#Search the MIN ELEMENT IN LIST
# Swap WITH MIN VALUE AT LOC 0
#Increment MIN 
#REPEAT TILL ELEMENTS ARE SORTED