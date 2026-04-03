

# variables:
#data types: primitive dt: int, float, string, boolean
#non-prmitive: list, tuples, sets, dictionary
list = [5,67,89]
tuple = (67,3,12)
set ={45,67,90}
dic = {
    "name":"Agalya",
    "age":20
}
#operators:
#arithmatic operators +,-,*,/,//,%,**
#comparison => >,<,>=,<=,==, !=
# logical operator : and, or, not 
#assignment operator => = , +=, -=, *=, /=, %=, //=

a=10
a+=5 # a=a+5

# membership operator : is, is not

a=10
b=10
b=20

li = [1,2,3]
li1 =[1,2,3]

print(a is b)
print(li is li1)
print(li == li1)

li[0]=10

#identity operator : in , not in

print( 10 in li)

# type : it will return data type of given variable 
print(type(li))

#conditional statements: 
# simple if:

if(20>132):
    print("yes")
    print("jshs")
else:
    print("no")
x=[8]

if x:
    print("it have a value")
else:
    print("no value")

# 0,None,"", [], => false

P=int(input("Enter the principal amount:"))
R=int(input("Enter the rate of interest:"))
T=int(input("Enter the time:"))
SI=(P*T*R)/100
print(SI)

r=int(input("enter the radius:"))
pi=3.14
Area= pi* (r**2)
print(Area)

bs=10000
da = (bs/100)*20
hra = (bs/100 )*30
tax = (bs/100) *10
final = (bs+da+hra)-tax
print("salary",final)

height=int(input("enter height in meters:"))
weight=int(input("enter weight in kg:"))
BMI=weight/(height**2)
print(BMI)

distance=int(input("enter the distance in km:"))
speed=int(input("enter the speed in km/hr:"))
time=distance/speed
print(time)

c=int(input("enter temperature in celsius:"))
f=(c*(9/5))+32
print(f)

a=int(input("enter a value:"))
if a % 3==0 and a % 5==0:
    print("a is divisible by both 3 and 5")
    print("is divisible")
else:
    print("none")

username=input("enter username:")
password=int(input("enter te password:"))
if username=="admin" and password==12345:
    print("login successfully")
else:
    print("invalid credentials") 

n=int(input("enter the mark:"))
if n>=90 and n<=100:
    print("grade A")
elif n>=80 and n<=89:
    print("grade B")
elif n>=70 and n<=79:
    print("grade C")
elif n>=60 and n<=69:
    print("grade D")
else:
    print("0-59:E")

height=int(input("enter height in meters:"))
weight=int(input("enter weight in kg:"))
BMI=weight/(height**2)
print(BMI)
if BMI<19:
    print("underweight")
elif BMI>=20 and BMI<=25:
    print("normalweight")
elif BMI>=26 and BMI<=30:
    print("overweight")
else:
    print("obese")

age=int(input("enter the age:"))
if age<15:
    print("Ticket Price = 80")
elif age>=16 and age<=50:    
    print("Ticket Price = 190")
else:
    print("Ticket Price for seniors=200")

vehicle_type=input("enter the type:car,bike,truck:")
if vehicle_type=="car":
    print("Charge=Rs. 100")
elif vehicle_type=="bike":
    print("Charge=Rs. 50")
elif vehicle_type=="truck":
    print("Charge=Rs. 200")
else:
    print("invalid type")

Amount=int(input("enter the value:"))
if Amount>=5000:
    print("price:",Amount-(Amount*(20/100)))
elif Amount>=2000 and Amount<=4999:
    print("price:",Amount-(Amount*(10/100)))
else:
    print("no discount")




