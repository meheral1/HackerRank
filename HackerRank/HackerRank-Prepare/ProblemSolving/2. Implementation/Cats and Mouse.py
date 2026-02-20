def catandmouse(x,y,z):
    catA = abs(x-z)
    catB = abs(y-z)
    if catA>catB:
        return "Cat B"
    elif catB>catA:
        return "Cat A"
    else:
        return "Mouse C"
#testcase:
x=1
y=2
z=3
print(catandmouse(x,y,z)) 
x,y,z = 1,3,2
print(catandmouse(x,y,z))   