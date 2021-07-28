class India:
    def __init__(self,PIN,name):
        self._PIN=PIN #protected with single underscore
        self.name=name #default PUBLIC with no underscore
    

class Punjab(India):
    def show(self):
        print("Address ABOVE")
     

o1=India(834001,"Main Road")
print("PIN : ", o1._PIN ," | Name : ",o1.name)
o2=Punjab(834002,"Green Park")
print("PIN : ", o2._PIN ," | Name : ",o2.name)
o2.show()


        

