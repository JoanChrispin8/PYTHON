#grandfather to dad,grandfatherand dad to son

class grandfather():
    def car(self):
        print("red")

class dad(grandfather):
    def house(self):
        print("blue")

class son(dad):
    def bike(self):
        print("black")

s =son()
s.car()
s.house()
s.bike()

#hirarachy

class father:
    def theatre(self):
        print("sundrapuram")
class son_1(father):
    def factory(self):
        print("podanur")
class son_2(father):
    def supermarket(self):
        print("gdtank")

s1 = son_1()
s1.factory()
s1.theatre()

s2 = son_2()
s2.supermarket()
s2.theatre()