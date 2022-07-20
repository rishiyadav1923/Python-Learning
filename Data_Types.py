"""
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

a = "Hello World"	# str	
b = 20	#int	
c = 20.5	#float	
d = 1j	#complex	
e = ["apple", "banana", "cherry"]	#list	
f = ("apple", "banana", "cherry")	#tuple	
g = range(6)	#range	
h = {"name" : "John", "age" : 36}	#dict	
i = {"apple", "banana", "cherry"}	#set	
j = frozenset({"apple", "banana", "cherry"})	#frozenset	
k = True	#bool	
l = "Hello"	#bytes	
m = bytearray(5)	#bytearray	
n = memoryview(bytes(5))	#memoryview	
o = None	#NoneType

print(a)
print(type(a))

print(b)
print(type(b))

print(c)
print(type(c))

print(d)
print(type(d))

print(e)
print(type(e))

print(f)
print(type(f))

print(g)
print(type(g))

print(h)
print(type(h))

print(i)
print(type(i))

print(j)
print(type(j))

print(k)
print(type(k))

print(l)
print(type(l))

print(m)
print(type(m))

print(n)
print(type(n))

print(o)
print(type(o))


# Setting the Specific Data Type

# If you want to specify the data type, you can use the following constructor functions:
# Example 	

p = str("Hello World") 	# str 	
q = int(20) 	# int 	
r = float(20.5) 	# float 	
s = complex(1j) 	# complex 	
t = list(("apple", "banana", "cherry")) 	# list 	
u = tuple(("apple", "banana", "cherry")) 	# tuple 	
v = range(6) 	# range 	
w = dict(name="John", age=36) 	# dict 	
x = set(("apple", "banana", "cherry")) 	# set 	
y = frozenset(("apple", "banana", "cherry")) 	# frozenset 	
z = bool(5) 	# bool 	
abc = bytes(5) 	# bytes 	
pqr = bytearray(5) 	# bytearray 	
xyz = memoryview(bytes(5)) 	# memoryview 	

# Print

print(p)
print(type(p))

print(q)
print(type(q))

print(r)
print(type(r))

print(s)
print(type(s))

print(t)
print(type(t))

print(u)
print(type(u))

print(v)
print(type(v))

print(w)
print(type(w))

print(x)
print(type(x))

print(y)
print(type(y))

print(z)
print(type(z))

print(abc)
print(type(abc))

print(pqr)
print(type(pqr))

print(xyz)
print(type(xyz))

