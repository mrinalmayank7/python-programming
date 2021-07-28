def Linear_Search(List , n ,ele):
    
    for i in range(n):
        if (List[i] == ele):
            return i
    return -1

n=int(input("ENTER THE SIZE OF THE LIST :"))

List=[]
for i in range(n):
    item = int(input("ENTER ELEMENT "))
    List.append(item)
print(List )
ele=int(input("ENTER THE ELEMENT TO SEARCH :"))
CALL =Linear_Search(List , n ,ele)
if CALL==-1:
    print("ELEMENT NOT FOUND ")
else :
    print("ELEMENT  FOUND  AT INDEX  ",CALL)



