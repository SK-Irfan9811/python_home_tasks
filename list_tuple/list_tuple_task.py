#1
t=(1,2,3,4,5)
print(list(t))

#2
L=[1,3,5,7]
T=(8,6,4,2)
LS=L+list(T)
print(LS)

#3
#list is mutable whereas tuple is immutable
#list by [],tuple by ()
#no manipulation methods for tuple

#4
l=['a','d','c','A','C']
print(l[::-1])

#5
l=[10,11,20,21,30,31,40,41]
print(l[1::2])

#6
#copy method
#copy module
#deepcopy
#list comprehension
#list() constr
#slicing


#7
# n_list=["Happy",[2,0,1,5]]
# print(n_list[0][1])
# print(n_list[1][3])

#8
# odd=[2,4,6,8]
# odd[0]=1
# print(odd)
# odd[1:4]=[3,5,7]
# print(odd)

#9
# string=input().lower()
# if(string==string[::-1]):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

#10
l=[]
for i in range(20,0,-5):
    l.append(i)
print(tuple(l))

#11
string=input()
print(list(string))
