class student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    def display(self):
        print(f"{self.name} is in grade {self.grade}")

s1 = student("nishanth",25)
s2 = student("midhun",32)
s3 = student("vanaraj",63)

s1.display()
s2.display()
s3.display()