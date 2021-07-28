class CSE8C:
  def __init__(self):
    print("It will be exceuted automatically")
  
  def display(self):
    print("Its not executed automatically")

c1 = CSE8C()
c2 = CSE8C()
e1 = CSE8C()
c1.display()
print(c1)
print(c2)
print(e1)
