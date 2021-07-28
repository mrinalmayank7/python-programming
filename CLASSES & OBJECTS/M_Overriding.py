class India:
    def __init__(self):
        self.value="INSIDE COUNTRY"  
    def globe(self):
        print(self.value)

class Punjab(India):
    def __init__(self):
         self.value="INSIDE STATE"  
    def globe(self):
        print(self.value)

o1=India()
o2=Punjab()
o1.globe()
o2.globe()
        

