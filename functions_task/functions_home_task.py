#1
# def swap_strings(s1,s2):
#     global str1,str2
#     str1,str2=s2,s1
# str1=input("Enter first string")
# str2=input("Enter second string")
# swap_strings(str1,str2)
# print(str1,str2)

#2
import random
import string

random.seed(10)
sum=0
for i in range(4):
    sum+=random.randint(0,26)
print(sum/4)

#3
capitals_list=list(string.ascii_uppercase)
print(random.choice(capitals_list))

#4
# def get_si(p,r,t):
#     return (p*t*r)/100
#
# #5
# def get_ci(p,r,t,n=1):
#     return round(p*((1+(r/(100*n)))**(n*t)),2)
#
# principle=eval(input("Enter priciple value"))
# rate=eval(input("Enter rate of interest"))
# time=eval(input("Enter tenure"))
#
# print(get_si(principle,rate,time))
# print(get_ci(principle,rate,time))

#6
# def get_q_r(num1,num2):
#     return ("quotient : %s"%(num1//num2),"remainder : %s"%(num1%num2))
# print(get_q_r(int(input()),int(input())))

#7
# import math
# def get_hypotenuse(height,base):
#     return math.sqrt(height**2+base**2)
# print(get_hypotenuse(3,4))

#8
# def get_info_in_detail():
#     global sec
#     print("days:",sec//86400)
#     sec=sec%86400
#     print("hours",sec//3600)
#     sec=sec%3600
#     print("minutes",sec//60)
#     sec=sec%60
#     print("seconds",sec)
#
# sec=int(input())
# get_info_in_detail()

#9
#python --version

#10
x=2
x*=3
x=x%4#remainder
y=-x
print(x,y)

#11
def fun():
    pass
print(fun())
