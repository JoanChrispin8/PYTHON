# args
def add(*args):
    total = 0
    for num in args:
        total += num
    return total
print(add(1,23,3)) 
    
#kwargs

def idcard_details(**kwargs):
    print("Identy Card")
    for key,value in kwargs.items():
        print(f"{key} : {value}")
idcard_details(Name="joan",Age=18,rollno="rcas2023bai016")            