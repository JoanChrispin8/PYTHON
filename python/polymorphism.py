# polymorphism will do overriding
class dad:

    def house(self):
        print("blue")

class son(dad):

    def bike(self):
        print("black")
        
    def house(self):
        print("black")
       
a=son()
a.bike()
a.house()

