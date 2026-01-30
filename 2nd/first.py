# name=input("enter your name")
# age=int(input("ente you age"))
# print(f"The name is {name} and the age is {age}")
# age=int(input("enter your age"))

# if(age>18):
#     print("you are over age and your are able to drive the car")
# elif age==18:
#     print("your are just became an adult")
# else:
#     print("tum kuch bhi ke layak nahi ho")
# day=input("enter the starting letter of day so you get full day name")
# match day:
#     case 'm':
#         print("the day is monday")
#     case 't':
#         print("the day is tuesday")
#     case 'w':
#         print("the day is wednsday")

#     case 't':
#         print("the day is thursday")
#     case _:
#         print("you are enter wrong credential")

# fruits=["apple","banana","guava","grapes","orange"]
# for i in fruits:
#     print(i)
# for i in range(5):
#
#      print(i)
# n=int(input("enter the number you want multiplication table"))
# for i in range(10,0,-1):
#     print(f"{n}X{i}={n*i}")
# i=0;
# while(i<5):
#     print(i)
#     i+=1;
# for i in range(10):
#     if(i==5):
#         break
#     print(i)
# for i in range(10):
#     if(i==5):
#         continue
#     print(i)
# num=int(input("enter the number"))
# if(num<0):
#     print("the is negaive number")
# elif (num>0):
#     print("this is positive number")
# else:
#     print("this is equl to zero")
# num=int(input("enter the number"))
# if(num%2==0):
#     print("this is even number")
# else:
#     print("this is odd number")
# num1=int(input("enter the number1"))
# operation=input("enter the operation you want to perform")
# num2=int(input("enter the second number"))
# match operation:
#     case '+':
#         print(num1+num2)
#     case '-':
#         print(num1-num2)
#     case '*':
#         print(num1*num2)
#     case '/':
#         print(num1/num1)
#     case _:
#         print("enter valid operations")
# num=int(input("enter the number you want to sum"))
# sum=0;
# for i in range(num+1):
#     sum+=i
# print(sum)
# for i in range(5):
#     print('*'*i)
# password=input("enter the password")
# corr_pass="govind"
# while password!=corr_pass:
#     password=input("enter the correct password")
# print("login successful")

# num=123
# rev=0;
# while(num>0):
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# print(rev)

# name="python  developer"
# # print(name[::2])
# # name=" hello govind "
# # print(name)
# # print(name.strip())
# # print(name.rstrip())
# govind=name.split()
# print(govind[0])
# # print(name.title())
# text="apple,banana,mango"
# fruits=text.split(",")
# print(fruits);
# name="govind kumar"
# print(name[0])
# print(name[-1])
# print(len(name))
# firstname="govind"
# lastname="kumar"
# fullname=firstname+" "+lastname
# print(fullname)
# name=input("enter the name")
# count=0;
# for ch in name:
#     if ch in "aeiouAEIOU":
#         count+=1
# print(count)
# name="jahaj"
# same=name[::-1]
# if(name==same):
#     print("this is palidrone")
# else:
#     print("this is not a palidrone")/
# def name(name):
#     return f"hello,{name}"
# print(name("govind"))
# def sum(a,b):
#     return a+b
# print(sum(4,5))
# def greet(name="govind"):
#     return f"hello,{name}"
# print(greet())
# def students(name,age):
#     print( f"the name is {name}and the age is {age}")
# students(name="govind",age=44)
# square=lambda x:x*x
# print(square(4))
# sum=lambda x,y,z:x+y+z
# print(sum(1,2,3))
# number=[1,2,3,4,5]
# square=list(map(lambda x:x*x,number))
# print(square)
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return factorial(n-1)*n
# print(factorial(5))
