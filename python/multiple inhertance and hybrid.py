# multiple inheritance
class dad():
    def factory(self):
        print("blue")
class mom():
    def shop(self):
        print("pink")
class son(dad,mom):
    def theatre(self):
        print("black")

s = son()
s.factory()
s.theatre()
s.shop()

#if any two types of inheritance occured that called hybrid