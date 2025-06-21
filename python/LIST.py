
playlist = ["swatika",'pathikuchu','gbu mammey']
fav_food = ['noodles','biriyani','dosa','chappati','omelete']

print("my play list : ",playlist)
print("my fav foods : ",fav_food)


#list methods

playlist.append("puli")
print("after append",playlist)

playlist.insert(2,"og sambavam")
print("after insert",playlist)

playlist.remove("puli")
print("after remove",playlist)

playlist.pop()
print("after pop",playlist)

playlist.reverse()
print("after reverse",playlist)

print("after count",playlist.count('og sambavam'))

#list slicing

print("top 2 fav dish",fav_food[0:2])

print("last 2 in fav dish",fav_food[-2:])

print("middle fav dish",fav_food[1:3])

#list iterations

for food in fav_food:
    print("orderd food",food)

#concatenate

for songs in playlist:
    print(songs +" for Ajith")

# check if

if 'dosa' in fav_food:
    print("yes")

#update        

playlist[2] = "swadeka"
print(playlist)

#mixed data types

mixed = ["joan",20,1.68]
for a in mixed:
    print(a)

# enumerate

recent_locations = ["home",'college','busstop','bakery']

for i,location in enumerate(recent_locations):
    print(f"location {i} : {location}")
           