# # #dictionary: unordered collections with key value pair. key should be unique.

# dic = {
#     "name":"Agalya",
#     "course":"python",
#     "age":20,
#     "isActive":True,
#     "skills":["Power bi","Sql","python"]

# }


# print(dic["name"])
# dic["mail"] = "agal@gmail.com"
# dic["course"] = "Django"


# print(type(dic))

# # #methods:

# print(dic.get("name"))
# print(dic.keys())
# print(dic.values())
# print(dic.items())
# print(dic.pop("age"))
# print(dic.popitem())
# print(dic.update({"isActive":False}))
# print(dic.setdefault("course","fullstack"))


# print(dic)
# print(dic.keys())
# for i in dic.keys():
#     print(i,dic[i])

# print(dic.items())
# for key,values in dic.items():
#     print(key,values)





# d={"Name":"Anu","age":20,"course":"python"}
# print(d["course"])
# print(d.update({"age":19}))
# d["city"]="coimbatore"
# print(d)

# student={"name":"priya","age":25,"course":"python"}
# print(student.keys())
# print(student.values())
# for i in student:
#     print(i,":",student[i])


# if "age" in student:
#     print("age is available")
# else:
#     print("!")

# print(student.__len__())

# colours=["red","blue","red","green","blue","red"]
# count={}
# for dict2 in colours:
#     if  dict2 not in count.keys():
#         count[dict2]=1
#     else:
#         count[dict2]+=1
# print(count)



# d1={"a":10,"b":20}
# d2={"c":30,"d":40}
# print(d1.update(d2))
# print(d1)
# print(d2)

# marks={"maths":85,"science":92,"english":78}
# max=0
# sub=""
# for n in marks.keys():
#     print(n)
#     if marks[n] > max:
#         max=marks[n]
#         sub=n
# print(sub,max)
# max=0
# sub=""
# for subs,mark in marks.items():
#     if mark>max:
#         max=mark
#         sub=subs
# print(sub,max)


# print(marks.popitem())
# print(marks)

# students={"101":{"name":"asha","marks":90},
#           "102":{"name":"ravi","marks":85}}
# for h in students.keys():
#     print(students[h]["name"])
#     print(students["101"]["marks"])

# keys=["name","age","city"]
# values=["priya",25,"chennai"]
# dic={}
# for i in range(len(keys)):
#     dic.update({keys[i]:values[i]})
# print(dic)

# scores={"ravi":78,"asha":92,"kumar":85}
# for s in sorted(scores.keys()):
#     print(s,scores[s])
# maxi={}
# for m,n in sorted(scores.items()):
#     print(m,n)



d={1:"apple",2:"mango",3:"orange"}
print(d[2])
d[4]="grapes"
print(d)
d[3]="book"
print(d)
print(d.pop(3))
print(d)
print(d.keys())
print(d.values())
for i in d.items():
    print(i)
for j in d:
    if j in d.keys():
        print(j,"- key exists")
    else:
        print("no")
print(d.__len__())
print(d.copy())
print(d.clear())
print(d)

# d1=dict("enter value:")


d2={1:"book",2:"paper"}
d2[2]="stone"
print(d2)
d2[3]="paper"
d2[4]="pen"
d2[5]="pencil"
print(d2)
for n in d2.items():
    print(n)
print(d2.keys())
print(d2.values())
for m in d2:
    print(m,":",d2[m])

d3={}
x=True
while x:

    key=input("enter key")
    val =input("enter value")
    d3.update({key:val})
    y=input("enter STOP to finish")
    if(y=="STOP"):
        x=False
    else:
        x=True
print(d3)



