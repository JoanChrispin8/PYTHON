#set 
a=[1,2,3]
b=set(a)
print(b)

# no duplicates

rapido_cities = {'chennai','coimbatore','karur','chennai','karur'}
print(rapido_cities)

#union,intersection,difference

rapido_cities1 = {'coimbatore', 'chennai', 'karur'}
rapido_cities2 = {'coimbatore','hyd','benguluru'}

print(rapido_cities1.union(rapido_cities2))
print(rapido_cities1.intersection(rapido_cities2))
print(rapido_cities1.difference(rapido_cities2))
print(rapido_cities2.difference(rapido_cities1))

#add and remove

rapido_cities.add("salem")
print(rapido_cities)

rapido_cities.remove("karur")
print(rapido_cities)

#discard

my_set = {1,2,3}
print(my_set)
my_set.discard(8)