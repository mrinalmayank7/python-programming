
def Binary(List, low, high, ele):
    if high >= low:
        mid = (high + low) // 2
 
        if List[mid] == ele:
            return mid
        elif List[mid] > ele:
            return Binary(List, low, mid - 1, ele)
        else:
            return Binary(List, mid + 1, high, ele)
    else:
        return -1
 
n=int(input("ENTER THE SIZE OF THE LIST :"))
List=[]
for i in range(n):
    item = int(input("ENTER ELEMENT "))
    List.append(item)
print(List )
ele=int(input("ENTER THE ELEMENT TO SEARCH :"))
CALL= Binary(List, 0, len(List)-1, ele)
 
if CALL != -1:
    print("ELEMENT FOUND AT INDEX ", CALL)
else:
    print("ELEMENT NOT FOUND")