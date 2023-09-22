# 1
# l=[10,20,30,40]
# itr=iter(l)
# print(next(itr),next(itr))
# itr=iter(l)#re assigning of itr identifier(overrides existing content)
# print(next(itr),next(itr))

# output
# 10 20
# 10 20

# itr1 = iter(range(10,20))
# itr2 = iter(range(1,10,4))
# print(next(itr1))
# print(next(itr2))
# itr3 = itr1
# print(next(itr3))
# print(next(itr2))
# print(next(itr1))

# output
# range function does not return a iterator instead returns a range object
# so we need to convert it explicitly
# 10
# 1
# 11
# 5
# 12


# itr=[10,20,30,40].__iter__()#list has to be converted into iterable explicitly
# print(itr.__next__(),itr.__next__())
# itr=reversed([10,20,30,40])#reversed() function itself returns a iterator
# print(itr.__next__(),itr.__next__())

# output
# 10 20
# 40 30

# def num_gen(start, end, diff=1):
#     while start < end:
#         yield start
#         start = start + diff
#
# g1=num_gen(10,20)
# g2=num_gen(1,10,4)
# print(next(g1))
# print(next(g2))
# g3=iter(g1)#no mandatory to explicitly convert to iterable as g3 can be dynamically assigned
# print(next(g3))
# print(next(g2))
# print(next(g1))

# output
# 10
# 1
# 11
# 5
# 12

# 2
# Which exception is raised upon reaching the last element of on iterable via its iterator.
# ans:when any sequence is exhausted during iteration "StopIteration" exception is raised

# 3
# __iter__() and __next__()

# 4
# def is_iterable(in_type):
#     if '__iter__' in dir(in_type):
#         return True
#     return False
# print(is_iterable(list))
# print(is_iterable(int))

# output
# True
# False

# 5
# def fibo(num):
#     a,b=0,1
#     while num>=a:
#         yield a
#         a,b=b,a+b
#
# fibo_gen=fibo(20)
# for i in fibo_gen:
#     print(i)


# 6
# def filter_list(lst,predicate):
#     for i in lst:
#         if(predicate(i)):
#             yield i
#
# lst=[1,2,3,4,5,6,7,8,9]
# even_odd=lambda x:(x%2==0)
# filtered_gen=filter_list(lst,even_odd)
# for i in filtered_gen:
#     print(i)


# next() is preferred over __next__() because next() has a flexibility to tackle the StopIteraion exception
