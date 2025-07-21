
#Take user input and print it with different data types
# to find the type use type(variable name)

#string
name = input("Enter your name:")
print("Name:",name)

#integer
age = int(input("Enter your age:"))
print("Age:",age)

#float
weight = float(input("Enter your weight:"))
print("Weight:",weight)

#boolean
bool_input = input("Are you a student (Yes/No): ").lower()
is_student = True if bool_input == "yes" else False
print("Is Student:", is_student)

#list
hobbies = input("Enter your hobbies seprated by commas (list):").split(",")
print("Hobbies",hobbies)

#tuple
tuple_input = input("Enter tuple values:").split(",")
tuple_values = tuple(map(int,tuple_input))
print(tuple_values)

#set
set_input = input("Enter set values:").split(",")
set_values = set((map(float,set_input)))
print(set_values)

#complex
comp = complex(input("Enter complex input:"))
print("Complex:",comp)                 

#dict
print("---Enter dict values---")
dict_input = input("Enter dict:").split(",")
user_dict = {}
for item in dict_input:
    key,value = item.split(":")
    user_dict[key.strip()] = value.strip()
for key,value in user_dict.items():
    print(f"{key} : {value}")  