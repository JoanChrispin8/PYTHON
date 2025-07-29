#leap year or not
#for _ in range(1): ( for loop)
''' i = 0
while i < 1:(while loop)'''

year=int(input("Enter a year:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not leap year")

#i += 1(while loop)

#recursion
def is_leap_year(yr):
    if (yr % 4 ==0 and yr % 100 != 0) or (yr % 400 == 0):
        return "leap year"
    return "not leap year"
yr = float(input("Enter a year:"))
print("year:",is_leap_year(year))
