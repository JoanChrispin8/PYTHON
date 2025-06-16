age = 18

if age >= 18:
    print("you're allowed to vote")
else:
    print("you're not allowed to vote")    

mark = 99

if mark >= 90:
    print("Grade A")
elif mark >= 70:
    print("Grade B")
elif mark >=50:
    print("Grade C")
else:
    print("Fail")            

age_driving = 45
has_licsense = 'yes'

if age >= 18:
    if has_licsense == "yes":
        print("you can drive a car")
    else:
        print("please take a licsense to drive a car")
else:
    print("you are too young to drive a car")            

mark_1 = 70
attendence = 60

if mark_1 >= 50 and attendence >=60 : 
    print("you can write exam")
else:
    print("youi can't ")    

recharge_amount = 200
data_balance = 1.5

if recharge_amount >= 399 or data_balance >= 1 :
    print("you're getting bonuous data")
else:
    print("you are not elligeable")

order_amount = 1000
days = 'mon' #sat or sun
membership = 'gold' #gold

if (order_amount >= 1000 and days in ['sat','sun']) or membership == 'gold':
    print("20% discount")
else:
    print("no discount")    