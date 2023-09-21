l=[1,2,3]
s="Irfan"
# print("".join(list(reversed(s))))
# l=list(map(int,input().split()))
# print(l)

#set
# s={1,2,3,4}
# s.update((1,2,5))#with tuple
# s.update([0,-1,2])#with list
# s.update({1,2,3,9})#with set also
# s.add(100)#only one element
# s.remove((2))#gives key error if not found in set,tuple with single element is expected
# s.discard((4))#doesnt give error if ele is not  found
# s.pop()#key error if set is empty
# print(s)

#subset and superset


#list
# l=[1,2,3]
# l.append(4)
# l.extend([1,2,3])#list
# l.extend((200,900))#tuple
# l.extend({500,500,99})#set
# l.remove(900)#takes value and Value error if not present in list
# l.pop(2)#Index error if index is not found default is to remove the last ele
# l.insert(2,"one")#if index is greater than the length then it adds to the last one,no error
# reversed(l)#returns the list pointer
# l.reverse()#reverses the exiisting list
# print(l)

#ord and ch
# print(ord('2'))
# print(chr(12345645))

#dictionary
d={1:"one",2:"two"}
print((d.items()))#list of tuples
print(d.values())#list
print(d.keys())#list
print("1" in d)#only keys can be searched
d.update({3:"three",4:"four"})#any items can be added.
d.pop(3)
d.popitem()
print(d)
