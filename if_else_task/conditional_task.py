#1
import sys

# def calculate_bmi(weight,height):
#     bmi_score=round(weight/((height/100)**2),2)
#     if(bmi_score<18.5):
#         return 'underweight'
#     elif(bmi_score>=18.5 and bmi_score<25):
#         return 'normal'
#     elif(bmi_score>=25 and bmi_score<30):
#         return 'overweight'
#     else:
#         return 'obese'
#
# weight_in_kg=eval(input())
# height_in_cm=eval(input())
# print(calculate_bmi(weight_in_kg,height_in_cm))

#2
# def get_oldest_youngest(ages):
#     min_age=100;
#     max_age=0;
#     for i in ages:
#         if i>max_age:
#             max_age=i
#         if i<min_age:
#             min_age=i
#     return "oldest :%s and youngest is :%s"%(max_age,min_age)
# ages_list=[int(age) for age in input().strip().split()]
# print(get_oldest_youngest(ages_list))

#3
# def check_divisibility(a):
#     if(a%5==0 and a%7==0):
#         return True
#     return False
# print(check_divisibility(int(input())))

#4
# def is_alphabet(string):
#     for i in string:
#         if (ord(i)>=97 and  ord(i)<=122) or (ord(i)>=65 and  ord(i)<=90):
#             pass
#         else:
#             return False
#     return True
# print(is_alphabet("irfansk"))

#5
# def is_leap_year(y):
#     if (y%400==0) or (y%100!=0) and (y%4==0):
#         return True
#     return False
# #print(is_leap_year(int(input())))

#6
# def days_in_month(month,year):
#     if(len(month)>3):
#         month=month[:3]
#     month_days_dict={"JAN":31,"FEB":28,"MAR":31,"APR":30,"MAY":31,"JUN":30,"JUL":31,
#         "AUG":31,"SEP":30,"OCT":31,"NOV":30,"DEC":31}
#     #update dict rather
#     if(month=='FEB' and is_leap_year(year)):
#         return month_days_dict[month]+1
#     else:
#         return month_days_dict[month]
#
# print(days_in_month("MAY",2028))

#8
def common_words(str1,str2):
    set1=set(str1.split())
    set2=set(str2.split())
    return set1.intersection(set2)
print(common_words("This is python","Training is started"))



