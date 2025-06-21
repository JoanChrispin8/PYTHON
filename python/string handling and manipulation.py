#upper
car_driver="joan chrispin"
print(car_driver.upper())

#lower
name= "JOAN CHRISPIN"
print(name.lower())

#capitalized
name_1="joan chrispin"
print(name_1.capitalize())

#mobile number masked
mobile = "8927389282"
masked=mobile[:2] + "******" + mobile[-2:]
print(masked)

#title to the sentence
song = "sahpe OF you"
artist = "joan chrispin"
formatted = f"{song.title()} - {artist.title()}"
print(formatted)

#replace
location = "chennai"
fixed_location = location.replace("chennai","coimbatore")
print(fixed_location)

#taking the id using split and strip
message=("your uber booking id id : uber12345 . please do not share")
booking_id = message.split(":")[1].split(".")[0].strip()
print(booking_id) 

# using if to find the offer code
promo_msg="use zomato100 to get 100 off on your first order"
if "zomato100" in promo_msg:
    print("offer applied")

#using find to find  the position number
feedback="the driver was polite and the ride was smooth"
print("position is:", feedback.find("polite"))    

#using len to count the words
word1= "i am joan chrispin , from coimbatore"
word_count=len(word1.split(","))
print(word_count)

#strip to remove spaces from both sides
a="    joan chrispin   "
b=a.strip()
print(b)

#word to make initials 
name_3="joan chrispin"
initials= "".join([word[0].upper() for word in name_3.split()])
print(initials)