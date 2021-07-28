print("Name :Mrinal Mayank")
print("UID :19BCS1605")

def greatest(p,q,r):
    maxi = (p if (p > q and p > r) else (q if (q > p and q > r) else r))
    return maxi

p,q,r=int(input("Val 1: ")),int(input("Val 2: ")),int(input("Val 3: "))
print(greatest(p,q,r))



i=1
sum=0
n=int(input("Enter limit :"))
while i<=n:
    sum= sum+i
    i=i+1
print(sum)


print("Name :Mrinal Mayank")
print("UID :19BCS1605")

n=int(input("Enter limit :"))
for i in range(n):
    k =int((i*(i+1))/2)
    for j in range(i):
      print(k, end=' ')
      k-=1
    print(' ')
 
