#1
# class Student:
#     pass
# s=Student()
# s.name="Guido"
# s.age=62
# print(s.name)
# print(s.age)

# class Student:
#     pass
# s1=Student()
# s1.name="Guido"
# s1.age=62
# s2=Student()
# s2.name="Bjarne"
# s2.age=67
# print(s1.name,s1.age)
# print(s2.name,s2.age)

#2
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"name is {self.name}, age is {self.age}"
# s1=Student("SK",21)
# s2=Student("Johncena",22)
# print(s1,s2,sep="\n")

#3
# class Test:
#     def __init__(self):
#         print("Constructor")
#     def __del__(self):
#         print("Destructor")
#
# s1 = Test()
# s2 = Test ()

# class Test:
#     def __init__(self):
#         print("Constructor")
#     def __del__(self):
#         print("Destructor")
#
# s1 = Test()
# Test()
# s2 = Test()
# s3 = s1
# del(s1)
# s3.name="sk"

#4
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def set_marks(self,marks_list):
#         self.marks_list=marks_list
#
#     def print_details(self):
#         print(f"Name : {self.name}\nAge : {self.age}\naverage_marks : {sum(self.marks_list)/len(self.marks_list)}")
# if __name__ == '__main__':
#     s= Student('abc', 20)
#     s.set_marks([80,60,90,70,99])
#     s.print_details()

#5
import math
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#
#     def get_area(self):
#         return math.pi*(self.radius**2)
#
#     def get_perimeter(self):
#         return 2*math.pi*self.radius
# c1=Circle(5.0)
# print("%.2f"%(c1.get_area()))
# print("%.2f"%(c1.get_perimeter()))

#6
import gc
import sys
gc.disable()
class SelfManaged:
    object_count=0
    def __init__(self):
        SelfManaged.object_count+=1
    def __del__(self):
        print("gc invoked")
        SelfManaged.object_count-=1

    @classmethod
    def get_current_count(cls):
        return cls.object_count

# s1=SelfManaged()
# s2=SelfManaged()
# s3=s2
# s4=SelfManaged()
# print(SelfManaged.get_current_count())
# # del s1
# print(SelfManaged.get_current_count())

#7
# class BankAccount:
#     def __init__(self,name):
#         self.name=name
#         self.balance=0
#     def deposit(self,amount):
#         if(amount>0):
#             self.balance+=amount
#             print(f"{amount} is credited in your account")
#         else:
#             sys.exit("Invalid input")
#     def withdraw(self,amount):
#         if(self.balance>=amount):
#             self.balance-=amount
#             print("please collect your cash.\n"
#             "Would you like to display balance?\n"
#             "1.Yes\n"
#             "2.No")
#
#             print(f"balance is {self.balance}" if input()=='1' else "thank you")
#         else:
#             sys.exit("Insufficient funds")
#
#     def __str__(self):
#         print(f"name : {self.name}\n balance : {self.balance}")
#
# b1=BankAccount("Irfan")
# b1.deposit(1000)
# b1.withdraw(5000)











