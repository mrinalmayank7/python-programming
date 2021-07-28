class pizza :
    def veg(self):
        print("veg pizza")
    def nonveg(self) :
        print("non veg pizza")

class size(pizza):               #single level inheritance
    def regular(self):
        print("regular pizza")
    def medium(self) :
        print("medium pizza")

class addon(size):               #multilevel inheritance 
    def vegaddon(self):
        print("Addon veg")
    def nonvegaddon(self):
        print("Addon nonveg")

class mania(addon,size,pizza):    #multiple inheritance (call in reverse order)
    def tomato(self):
        print("TOMATO PIZZA")
    def CORN(self):
        print("CORN PIZZA")

o1 = pizza()
o1.veg()
o1.nonveg()

o2 = size()
o2.veg()
o2.regular()

o3 = addon()
o3.veg()
o3.regular()
o3.vegaddon()

o4 = mania()
o4.veg()
o4.regular()
o4.vegaddon()
o4.tomato()