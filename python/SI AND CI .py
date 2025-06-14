#Simple Interest 

def si(p,t,r):
    return (p*t*r)/100
p,t,r = 4016.25,5,9

si_value = si(p,t,r)
print(si_value)

#compound intrest

def ci(p,t,r)