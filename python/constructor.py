# student name and age

class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def displays(self):
        print(f"My Name is {self.name} and My Age is {self.age}")

s1 = student("Joan Chrispin",20)
s1.displays()        

#name and aadhar use

class employee:
    def __init__(self,name_1,aadhar):
        self.name_1 = name_1
        self.aadhar = aadhar

    def for_office(self):
        print(f"{self.name_1} and aadhar number is {self.aadhar}") 

    def bank_account(self):
        print(f"Bank account opened for {self.name_1} and aadhar number is {self.aadhar}")

emp1 = employee("joan chrispin",12345678)
emp1.for_office()
emp1.bank_account()        
   
#without constructor        

class mathtool:
    def square(self,n):
        return n*n
    def cube(self,n):
        return n*n*n
    
num = mathtool()
print(num.square(4))
print(num.cube(4))
