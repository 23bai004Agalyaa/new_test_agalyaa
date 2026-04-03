
# #loops: 
# # while condn:
# # block of code
# # increment or decrement

# i=1
# s=0
# count=0
# while i<=50:
#     # print("hello")
#     if i%2==0:
#         # print(i)
#         count=count+1
#     i=i+1
#     # s=s+i
#     # print(s)
# # print(s)
# print(count)

# n=56
# if n%2==0:
#     print("even")
# else:
#     print("odd")


# i=1
# while i<=10:
#     print(i)
#     i=i+1

# i=0
# while i<=20:
#     if i%2==0:
#         print(i)
#         i=i+1
 
# i=0
# sum=0
# while i<=10:
#     i=i+1
#     sum=sum+i
#     print(sum)


# i=10
# while i>=1:
#     print(i)
#     i=i-1
  

# number=int(input("enter the number:"))
# i=1
# a=1
# while i <=10:
#     # a = a * i
#     print(f"{number} X {i} = {number * i}")

#     i+=1

    
# i=1
# factorial=1
# a=4
# while i<=a:
#     factorial=factorial*i
#     i=i+1
# print(factorial)

# n=123878787
# count=0
# while(n>0):
#     digit = n%10
#     count=count+1
#     n=n//10
# print(count)



# #for loop:

# for i in range(1,10,2):
#     print(i)

# for i in range(10,0,-1):
#     print(i)

# #string:
# s = "python"

# print(len(s))

# for i in s:
#     print(i)
# for i in range(len(s)):
#     print(i, s[i])

# n=int(input("guess a number:"))
# real_n=6
# a=True
# while a:
#     if n==real_n:
#         print(n)
#     else:
#         print("none")
#     break


# n=456
# rev=0
# while(n>0):
#     digit = n%10
#     rev= rev*10 +digit
#     print(rev)
#     n=n//10
#     print(digit)


# n=474
# m=n
# rev=0
# while(n>0):
#     digit = n%10
#     rev=rev*10+digit
#     n=n//10
# print(rev)
# if rev==m:
#     print("palindrome")
# else:
#     print("not")

# n=54
# sum=0
# while n>0:
#     d=n%10
#     sum=sum+d
#     n=n//10
# print(sum)

# n=12345
# count=0
# while n>0:
#     # d=n%10=digit//1
#     count=count+1
#     n=n//10
# print(count)

# for i in range(1,11):
#     n=i**2
#     # if n>10:
#     #     break
#     # else:
#     print(n)

# a=int(input("enter the value:"))
# for i in range(1,11):
#     n=i*a
#     print(i,"*",a,"=",n)
#     i=i+1

# # 1*2*3*4
# f=1
# i=1
# n=4
# for i in range(1,n+1):
#     f*=i
    
#     # i=i+1

# print(f)


# for i  in 'imstorng':
#     print(i)


# n=int(input("enter a value"))
# isprime=True
# for i in range(2,n):
#     if (n%i==0):
#        print(i)
#        isprime=False
#        break
#     else:
#         print('i',i)
# if(isprime):
#     print('this is prime number')
# else:
#     print('this is not a prime')

# for i in "apple":
#     print(i)

# a="apple"
# for i in a:
#     print(i)


# a="amhvhv"
# n=" "
# for x in a:
#     if x not in n:
#         i=a.count(x)
#         print(x,i)
#         n=n+x
        
# a="aaeewtryuuio"
# n=""
# for i in a:
#     if i in "aeiou" and i not in n:
#         v=a.count(i)
#         print(i,v)
#         n=n+i

# a="computer"
# for i in a:
#     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#         print(i,"vowels")
#     else:
#         print(i,"consonants")

# s="rali"
# rev=" "
# for str in s:
#     rev=str+rev
# print(rev)

# s="rali"
# for i in range(len(s)):
#     print(s[i],i)

s="rali sha"
n=""
for st in s:
    if st ==" ":
        continue
    else:
        n=n+st
print(n)

#loop controls: break, continue


#nested loops:

for i in range(5):
    s=""
    for j in range(i):
        s+=str("*")
    print(s)    
    # print("\n")



