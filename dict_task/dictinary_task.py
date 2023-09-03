# 1
# d={}
# for i in range(1,6):
#     d[i]=-i
# print(d)
#
# nums=[1,2,3,4,5]
# neg_nums=[-1,-2,-3,-4,-5]
# d=dict(zip(nums,neg_nums))
# print(d)

# 2
# d={1=2,2=3} won't work
d = {1: 2, 2: 3}
# d={1,2;2,3} won't work
d = {(1, 2), (2, 3)}  # works but it's a set
# d={'a':'A','b':1,c:[1234]}won't work
d = {'a': 'A', 'b': 1, 'c': [1234]}
d = dict([(1, 2), (2, 3)])
d = dict(((1, 2), (2, 3)))
d = dict([[10, 2], [1, 4]])
d = dict(x=2, y=3)
# d=dict('x'=2,'y'=3) won't work

# 3
# l1=[1,2,3,4]
# l2=[10,20,30,40]
# d=dict(zip(l1,l2))
# print(d)

# 4
# d={}
# for i in range(65,91):
#     d[chr(i)]=i
# print(d)

# 5
alpha_dict = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    0: 'zero'
}


# num=int(input("Enter number(0-9) : "))
# print(alpha_dict[num])
# print(alpha_dict.keys())
# print(alpha_dict.values())
# print(alpha_dict.items())

# 6
# l1=['A','B','C','D']
# l2=['Apple','Ball','Cat','Dog']
# d1=dict(zip(l1,l2))
# d2=dict(list(d1.items())[1::2])
# print(d2)

# 7
def frequency_of_words(string):
    d = {}
    for word in string.split():
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    return d


print(frequency_of_words(input()))
