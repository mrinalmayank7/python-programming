class CSE8:
    def __init__(self,o1,o2):
        self.o1=o1
        self.o2=o2
    def arithmetic(self , a=None,b=None,c=None):
        add,mul=0,0
        if a!=None and b!=None and c!=None:
            add = a+b+c
            mul = a*b*c
        elif a!=None and b!=None:
            add = a+b
            mul = a*b
        else:
            add = a
            mul = a
        return add , mul

s1 = CSE8(58,60)
print(s1.arithmetic(2,3,4))


