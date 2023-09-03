import random
#1
# num=10
# for i in range(1,num+1):
#     print(i)

#2
# for i in range(10,0,-1):
#     print(i)

#3
# l=[10,11,20,21,30,31,40,41]
# for i in range(1,len(l),2):
#     print(l[i])

#4
# random_nums=random.sample(range(100), 5)
# sum=0
# avg=0.0
# for i in random_nums:
#     sum+=i
# print("sum is:%d"%sum)
# print("average is:%d"%(sum/5))

#5
# def print_chars(string):
#     for char in string:
#         print(char,end=",")
# print_chars("Irfan")

#6
# def print_ascii_values(string):
#     for char in string:
#         print(ord(char),end=",")
# print_ascii_values("Irfan@")

#7
# def store_ascii_values(string):
#     ascii_list=[]
#     for char in string:
#         ascii_list.append(ord(char))
#     return tuple(ascii_list)
# print(store_ascii_values("Irfan@"))

#8
# def sum_of_odds(nums_list):
#     odd_sum=0
#     for num in nums_list:
#         odd_sum+=(num%2)*num
#     print(odd_sum)
# sum_of_odds([int(num) for num in input().strip().split()])

#9
# def get_index_of(num,num_tuple):
#     return num_tuple.index(num) if num in num_tuple else "NOT FOUND"
# num_tuple=tuple([int(number) for number in input().strip().split()])
# num=int(input("Enter your number"))
# print(get_index_of(num,num_tuple))

#10
# nums=[]
# for i in range(21,31):
#     nums.append(i)
# print(nums)
#
# #11
# print(sum(nums))

#12
#num=int(input("Enter a number greater then 0: "))
# for i in range(1,num+1):
#     print(i,end=" ")

#13
def get_factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
print(get_factorial(int(input("Enter a number to get factorial : "))))




