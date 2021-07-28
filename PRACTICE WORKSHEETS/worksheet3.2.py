
print("Name :Mrinal Mayank")
print("UID :19BCS1605")

class MAGIC:
    def __init__(self,o):
        self.o = o
 
    def __ge__(self,operator1):       #for greater than and equal to 
        return self.o > operator1.o
    def __mul__(self,operator1):      #for multiplication 
        return self.o * operator1.o
    def __lt__(self,operator1):       #for less than 
        return self.o < operator1.o
 

object1 = MAGIC(11)
object2 = MAGIC(10)

print (object1 >=object2) #magic method __ge__ 
print (object1 * object2) #magic method __mul__
print (object1 < object2) #magic method __lt__






class CU_STUDENT:
    def __init__(self,name ,UID):
        self.name = name
        self.UID = UID

    def view(self ,dept ,sec , group):
        print("NAME       :", self.name)
        print("UID        :", self.UID)
        print("DEPARTMENT :", dept)
        print("CLASS      :", sec)
        print("GROUP      :", group)
    
    def Age(self,age) :
        print("AGE        :", age)
    def Mark(self):
        sum= 0
        n=int(input("ENTER TOTAL NUMBER OF SUBJECTS :"))
        marks=[]
        for i in range(n):
            item = int(input("ENTER MARKS : "))
            marks.append(item)
        for i in range(0, len(marks)):
            sum = sum + marks[i]
        print("TOTAL MARKS :", sum)
o1 = CU_STUDENT("MRINAL MAYANK" , "19BCS1605")
o1.view("CSE","CSE 8","C")
o1.Age(20)
o1.Mark()
