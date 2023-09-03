#1
# s='Python is Object Oriented'
# print(s[-1])
# print(s[::-1])
# print(s[:-1])
# print(s[1:1])
# print(s[4:10])

#2
# s=''
#print(s[1])index out of range

#3
# s="Landry"
# print(s[1])

#4
#a
# s='a b cd'
# print(len(s))
# print(s[::2])
# print(len(s[::2]))
#b
# s='a#b#c#d#'
# print(s.split())
# print(s.split("#"))
# l=s.split("#")
# s='$'.join(l)
# print(s)

#c
# s='Landry'
# s=s[::-2][::-2]
# print(s)

#d
# print(1>2)

#e
# print(4%2,5%2,2%5,sep=", ")

#f
# s='abcba'
# # s=s.upper()
# s.upper()
# print(s.count('A'),end=" ,")
# print(s.count('A',2,4), end=" ,")
# print(s.count('a',2,5))

#5
# string=input().split()
# print("".join(string))

#6
#[]-->empty list

#7
meths=list(dir(str))

#8
# print(" ".join(meths))

#9
# print('rstrip' in meths)

#10
# string=input().replace(" ","\n")
# print(string)

#11
# full_name=input().split()
# print("First name is %s: "% full_name[0])
# print("Last name is %s: "% full_name[1])
#
# print(" ".join(full_name[::-1]))

#12
string=input()
S1=string[0:len(string)//2]
if(len(string)%2==0):
    S2=string[len(string)//2:]
else:
    S2=string[len(string)//2+1:]
print(S1,S2)
