#get student name,mark,and total
class student:
    def __init__(self):
        self.name = ""
        self.marks = []
        self.total = 0

    def get_data(self):
        self.name = input("Enter your Name:")
        print(f"Enter Marks for {self.name}:")
        for i in range(5):
            marks = int(input(f"Subject {i+1} Mark: "))
            self.marks.append(marks)
            self.total = sum(self.marks)

    def display(self):
        print("\n Name: ",self.name)
        print("Marks: ",self.marks)
        print("Total: ",self.total)        

s=student()
s.get_data()
s.display() 
