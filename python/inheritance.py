#inheritence or single level inheritance

class mom:  # parent
    def house(self):
        print("mom's house")
class son(mom): #child
    def bike(self):
        print("My Bike")

s = son()
s.bike()
s.house()      

#that's why this is called parents child relation and it is single level inheritance

#overwrite

class app1:

    def version1(self):
        print("order")

class app1_1(app1):

    def version2(self):
        print("refund")
        
    def version1(self):
        print("cart")
       
a=app1_1()
a.version2()
a.version1()
b=app1()
b.version1()
