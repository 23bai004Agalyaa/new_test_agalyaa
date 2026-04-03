#tuples; ordered collection, immutable

t=(34,56,78)
# t[0]=90 immutable

t=(45,67,89,100,200,400,78)
print(t)

t1=(45,)

print(type(t))


#methods:

print(t.index(67))
print(t.count(100))

print(len(t))


#slicing:

print(t[0:3])
print(t[2:])
print(t[:4])

print(t[-3:-1])
print(t[::-1])
# print(t[:4:-1])
print(t)