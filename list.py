# #list: we can store collection of values using list. and it is odered collection. and it is mutable.

# li =[23,45,67,89,12]

# print(len(li))

# for i in li:
#     print(i)

# li[2]=100  # mutable

# print(li)

# sum=0

# for i in li:
#     sum=sum+i

# print(sum)

# fruits = ["appple","orange","grapes","mango"]

# for i in fruits:
#     print(i.upper())
#     for j in i:
#         print(j)



# list1=[1,2,3,4,5,6]
# for l in list1:
#     if l % 2 == 0:
#         print(l)


# l1=["agalyaa","ralisha","priya"]
# for i in l1:
#     if len(i)>5:
#         print(i)

# l=[-2,2,3,-4]
# for i in range(len(l)):
#     if l[i] < 0:
#         l[i]=0
# print(l)

# l1=[1,2,3,4,5,6]
# l2=[6,7,8,9,0]
# for i in l1:
#     for j in l2:
#         if i==j:
#             print("l1:",l1,":",i)
#             print("l2:",l2,":",j)

# l=[1,2,88,100,4,44,4]
# max=0
# sec_max=0
# for i in l:
#     if i > max:
#         max=i
#     elif i > sec_max and i != max:
#         sec_max=i
# print("max:",max)
# print("second largest:",sec_max)


# #remove duplicates

# li = [23,45,67,23,12,12]

# re =[]

# for i in li:
#     if(i not in re):
#         re.append(i)

# print(re)

# list methods:

# li =[12,23,34,45,56,55]
# li2=[90,900,234]

# print(li.index(23))
# print(li.append(89))
# print(li.insert(3,100))
# print(li.pop())
# print(li.pop(2))
# print(li.remove(56))
# print(li.extend(li2))
# print(li.count(23))
# print(li.reverse())
# print(li.sort(reverse=True))
# print(li.copy())
# print(li.clear())
# print(li)

# cart=["bread","butter","jam","apple","banana","apple"]
# print(cart.append("milk"))
# print(cart)
# cart2=["chocolate","cookies"]
# print(cart.extend(cart2))
# print(cart)
# print(cart.insert(0,"eggs"))
# print(cart)
# print(cart.remove("butter"))
# print(cart)
# print(cart.remove("jam"))
# print(cart)
# print(cart.clear())
# print(cart)

# cart=["bread","apple","butter","apple"]
# print(cart.index("apple"))
# print(cart.count("apple"))
# print(cart.sort())
# print(cart)
# print(cart.copy())



# l=[1,2,1,4,88,4,6,9,7]
# s=[]
# for i in l:
#     if(i not in s):
#         s.append(i)
# print(s)
# print(s.sort())
# print(s)

# li=[1,2,3,4,5,6,7,8,9,0]
# rem = li.pop(4)
# li.insert(5,rem)
# print(li)

# l1=[1,2,3]
# l2=[4,5,6]
# l3=[7,8,9]
# l4=[0,1,9]
# print(l1.extend(l2),l1.extend(l3),l1.extend(l4))
# print(l1)

# li=[1,2,3,4,5,6,7,8,9,0]
# li1=[]
# li2=[]
# for i in li:
#     if i < 6:
#         li1=i
#         print("list1:",li1)
#     else:
#         li2=i
#         print("list2:",li2)

# l=[27,3,4,5,6,7,8,9]
# max=0
# min=l[0]
# for i in l:
#     if i > max:
#         max=i
#     elif i < min:
#         min=i
# print(max)
# print(min)

# l=[1,2,3,3,2,1,"rzszw"]
# count=0
# for i in l:
#     count+=1
# print(count)

# l=[2,3,4,"apple","book"]
# for i in l:
#     if i == 2:
#         print("2 exists")





