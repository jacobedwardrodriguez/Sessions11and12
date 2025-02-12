# finding types

print(type(2+3))
print(type(6/2))
print(type(2!=3))
print(type(5 or 6))

print(type("abc".find))
print(type("abc"))


# What will each print display?
a = 2
b = 3
c = "abc"
print(a, b, c)
print(a, b, c, sep=",")
a += 2
a == 5
print(a)
print(c*(a-b))
d = c.find("b")
print(d)
print(d and b)
print(d == True)
e = str(a) + str(b) + str(c) + str(d)
print(e)
print(e[1::2])
print(e+e[::-1])