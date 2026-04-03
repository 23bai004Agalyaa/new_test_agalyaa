# #functions: it is a block of code to execute certain task. we can reuse it n no of times

# def greet():
#     print("hi, welcome")

# greet()
# greet()

# # functions wih parameters

# def add(a,b):
#     # print(a+b)
#     return a+b

# add(78,90)
# add(100,200)
# add(20,56)

# def greet(name):
#     print("hi...", name)

# greet("agalya")
# greet("ramya")

# ans = add(90,12)
# print(ans)



# def temperature(f):
#     c=20
#     f=((c*(9/5))+32)
#     return(f)
# res=temperature(45)
# print(res)

# def grade():
#     mark=int(input("enter the marks:"))
#     if mark>=90:
#         print("grade=A")
#     elif mark>=80 and mark<=89:
#         print("grade=B")
#     elif mark>=70 and mark<=79:
#         print("grade=C")
#     elif mark>=60 and mark<=69:
#         print("grade=D")
#     else:
#         print("E")
# grade()

# # def BMI(W,H):
# #     H=H/100                          # cm to m conversion
# #     calc=W/(H**2)
# #     return(calc)



# # Wt=int(input("enter the value:"))
# # Ht=int(input("enter the value:"))

# # print(BMI(Ht,Wt))



# def BMI():
    
#     W=int(input("enter the value:"))
#     H=int(input("enter the value:"))
#     H=H/100                          # cm to m conversion
#     calc=W/(H**2)
#     return(calc)




# print(BMI())



# def prime(p):
#     if p <= 1:
#         return(p,"not prime")
#     for j in range(2,p):
#         if p % j == 0:
#             return(p," not prime")
        
#     return (p,"prime")
# val=prime(2)
# print(val)


# s=input("enter a sentence:")
# w=s.split()
# c=0
# def count():
#     # s=input("enter a sentence:")
#     # w=s.split()
#     # count=0
#     for a in s:
#         if a !=" ":
#         c+=1

# count()



# def f():
#     n=int(input("enter value"))
#     fact=1
#     for i in range(n,1,-1):
#         fact*=i
#         # print(fact)
#     return(fact)
# print(f())



# def sumofnum(*num):
#     # print(num) #it will recv the value in tuple form
#     sum=0
#     for i in num:
#         sum+=i
#     print(sum)
# sumofnum(1,2,4,5)
# sumofnum(1,2)


# def food_collection(*food):
#     print(food)
#     for i in food:
#         print(i)
# food_collection('maggi','dosa','idly')
# food_collection('biriyani')



# ____________________KEYWORD ARGUMENTS______________________________

# def hotel(**items):
#     for i in items:
#         print(f'{i}---->{items[i]}')

# hotel(name='maggi',price='50',type='spicy')


# def num(*args):
#     for i in args:
#         print(i) 
# num(1,2,3,4,5,6)

# def all(**kwargs):
#     for j in kwargs:
#         print(f'{j}:{kwargs[j]}')
# all(A='ID',B='NAME',C='AGE')

# def greet(*a):
#     for i in a:
#         print(f'hello {i}')
# greet("keerthi",'hello','jkkk')
# greet ("raj")

# # name=input('enter name:')
# # age=int(input("enter age:"))
# def student(**kw):
#     for k in kw:
#         print(f'{k}:{kw[k]}')
# # student()
# student(name='agalyaa',age='20',course='python')

def calc(*ar):
    for c in ar:
        print(f'{c}*{'2'}:{c*2}')
calc(2,4,6,8)

def order(*item,**kwargs):
    for i in kwargs:
        print(f'{i}:{kwargs[i]}')
    
    for i in item:
        print(f'order dishes, {i}')
    
order('chicken pizza', 'margarita',size='1 kg',cut='4')


