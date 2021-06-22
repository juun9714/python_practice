from hello import *

a=safeFourCal(1, 2)
b=safeFourCal(5, 0)

print(a.lastname)
print(b.lastname)

print(id(a.lastname))
print(id(b.lastname))

a.lastname='june'
print(id(a.lastname))
print(id(b.lastname))

print(a.lastname)
print(b.lastname)

safeFourCal.lastname='hee'

print(id(a.lastname))
print(id(b.lastname))

print(a.lastname)
print(b.lastname)