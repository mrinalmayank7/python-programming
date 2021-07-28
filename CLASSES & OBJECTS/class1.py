class computer:
 def __init__(self,cpu,ram):
   self.cpu = cpu
   self.ram = ram
   print("My computer cong")

 def conf(self):
  print("CPU", self.cpu, "RAM",self.ram)
  
c1 = computer("i5",8)
c2 = computer("i7",32)

c1.conf()
c2.conf()
