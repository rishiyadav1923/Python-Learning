# Assigning Multiple Values to multiple Multiple Variables

x,y,z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

# One value to multiple Variables

a = b = c = "Orange"

print(a)
print(b)
print(c)

# Unpack a Collection -> If you have a collection ofbof values in a list, tuple etc. Python allows you to extract the values
# into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]

x,y,z = fruits

print(x)
print(y)
print(z)