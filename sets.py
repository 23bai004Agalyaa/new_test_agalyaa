# # sets: unordered collection , allowed only unique values

# s={12,34,56,12,45,89,90,12}
# print(s)
# #methods:
# s1={56,78,90}

# print(s.add(349))
# print(s.remove(12))
# print(s.pop())
# print(s.union({34,67,90,12}))
# print(s.intersection({34,56,78}))
# print(s.difference({23,34,56,78}))
# print(s.issuperset(s1))
# print(s.update({45,67,899}))
# print(s)



n={1,2,3,3,4,5,3,4,6,7}
l={}
for i in n:
    if i != l:
        l=i
        print(l)

n1={1,2,3,4,5,6}
n2={5,6,7,8,9,1,2}
for i1 in n1:
    for j in n2:
        if i1==j:
            print(j)

n=input("enter a sentence:")
w=n.split()
words=set(w)
c=0
for i in n:
    if i !=" ":
        c+=1
print(c)

s1={1,2,3,4,5}
s2={4,5,6,7,8,9}
print(s1.union(s2))
print("In s1:",s1.difference(s2))
print("In s2:",s2.difference(s1))
print(s1.symmetric_difference_update(s2))

s1={1,2,3,4,5,6,7}
s2={1,2,3}
s3={6,7,8,9}
print(s1.issuperset(s2))
# print(s2.issuperset(s1))
# print(s1.issuperset(s3))
print(s2.issubset(s1))

s=set({56,90,34})
l=list(s)
print(l)

