List1 = ["YELLOW","RED","BLACK","RED","RED"]

#counting the occurences using inbuilt function count()
print("COUNTING OF OCCURENCES OF RED USING count() :",List1.count("RED"))

#counting the occurences withouut using count()
count=0
for i in List1:
    if i=="RED":
        count= count +1
print("COUNTING OF OCCURENCES OF RED WITHOUT USING count() :",count)




M1= [[5,6],[2,2]] #Matrix1 = 2 X 2
M2 =[[5,6,7],[2,3,4]] #Matrix2 = 2 X 3
      
MULT = [[0, 0, 0],[0, 0, 0]]
    

for i in range(len(M1)): #ROW ITERATION OF M1
    for j in range(len(M2[0])): #COL ITERATION OF M2
        for k in range(len(M2)): #ROW ITERATION OF M2
            MULT[i][j] += M1[i][k] * M2[k][j] 

print("M1 X M2 : ") 
for n in MULT:
    print(n)   #printing the result



List1 = [33,22,10,5,6,44,60,80,90]

def MAXI(arg): #FUNCTION FOR MAXIMUM
  max=0
  for i in arg:
     if i>max:
       max=i
  return max 

def MINI(arg): #FUNCTION FOR MINIMUM 
  min=1e3
  for i in arg:
     if i<min:
       min=i
  return min

def MEAN(arg): #FUNCTION FOR MEAN
  avg=0
  for i in arg:
     avg= avg+i
  avg=int(avg/len(arg))
  return avg

def MEDI(arg): #FUNCTION FOR MEDIAN 
 arg.sort() #sorting before finding median 
 med= arg[int(len(arg)/2)]
 return med

def MODE(arg): #FUNCTION FOR MODE
    dictonary = {}
    for i in arg:
        if not i in dictonary:
            dictonary[i]=1
        else:
            dictonary[i]+=1
    return [k for k,j in dictonary.items() if j==max(dictonary.values())] 



#CALLING THE FUNCTIONS 
print("MAXIMUM  :" ,MAXI(List1))
print("MINIMUM  :" ,MINI(List1))
print("MEAN /AVG:" ,MEAN(List1))
print("MEDIAN   :" ,MEDI(List1))
print("MODE     :" ,MODE(List1))