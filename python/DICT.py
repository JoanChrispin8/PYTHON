trip = {
    "Name" : "Joan Chrispin",
    "Age" : 20,
    "course" : "BSC",
    "Roll num" : "RCAS2023BAI016"    
}

#basic access
print(trip["Name"])
print(trip.get(20))
print(trip.get("Age"))
print(trip.keys())
print(trip.values())

#iterations

for key,values in trip.items():
    print(key,":",values)

#update
trip.update({"specialization" : "AIDS"})
print(trip)    

#upset
trip.update({"Age" : 21})
print(trip) 

#pop
trip.pop("specialization")
print(trip)

#duplicate 

trip_1 = {
    "Name" : "Joan Chrispin",
    "Age" : 20,
    "course" : "BSC",
    "Age" : 20,
    "Name" : "Joan Chrispin k",
    "Roll num" : "RCAS2023BAI016"    
}
for k,v in trip_1.items():
    print(k,":",v)

#multiple values

trip_2 = {
    "Name" : "Joan Chrispin",
    "Age" : 20,
    "course" : "BSC",
    "Roll num" : "RCAS2023BAI016",
    "place" : ['coimbatore','chennai','madurai']    
}

    
print(trip_2["place"][0])

for locations in trip_2["place"]:
    print(locations)

#multiple records

'''
trips = [
    {"trip_id" : "ub001","pickup" : "chennai","drop" : "airport","fare" : 350},
    {"trip_id" : "ub002","pickup" : "ukkadam","drop" : "manikondu","fare" : 250},
    {"trip_id" : "ub003","pickup" : "gdtank","drop" : "sundrapuram","fare" : 400} 
]  
'''
    
trips = {
    "ub001" : {"trip_id" : "ub001","pickup" : "chennai","drop" : "airport","fare" : 350},
    "ub002" : {"trip_id" : "ub002","pickup" : "ukkadam","drop" : "manikondu","fare" : 250},
    "ub003" : {"trip_id" : "ub003","pickup" : "gdtank","drop" : "sundrapuram","fare" : 400} 
}   

print("ub001 fare", trips["ub001"]["fare"])

for trip_id,detail in trips.items():
    print(trip_id)
    print(detail["pickup"],"-->",detail["drop"])