# #1a
# print([i+j for i in "abc" for j in "def"])
#
# #1b
# print([i.lower() for i in "HELLO"])
#
# #1c
# text="Zero One Two Three Four Five Six Seven Eight Nine"
# result=[word[0]+word[-1] for word in text.split()]
# print(result)
#
# #1d
# result=[word[0]+word[-1] for word in text.split() if word[0]>word[-1]]
# print(result,ord('Z'),ord('o'))
#
# #1e
# text="banglore : city with lakes and punctures"
# result=[word for word in text.split() if word.startswith(('a','e','i','o','u'))]
# print(result)
#
# #2a
# D=[(i/10) for i in [10,20,30,40]]
# print(D)
# #2b
# L=[x for x in range(10) if x%2==0]
# print(L)
# #2c
# vowels_list=[c for c in 'aLphaBEts' if c in 'aeiouAEIOU']
# print(len(vowels_list))
# #2d
# updated_list=[c.upper() if c.islower() else c.lower() for c in 'aLphaBEts']
# print(updated_list)
#
# #3
# #loop
# word_list=[]
# words=['Python','Object','Oriented','Language']
# for word in words:
#     word_list.append(word[0])
# print(word_list)
#
# #list comprehension
# word_list=[word[0] for word in words]
# print(word_list)

#4
# word_list=[word for word in input().split() if len(word)>5]
# print(word_list)

#5
# import sys
# def isPalindrome(string):
#     if(string==string[::-1]):
#         return True
#     return False
# print(isPalindrome(sys.argv[1]))

#6
# word='synonymous'
# g=['a','o','n']
# s=[ch if ch in g else '_' for ch in word]
# s=''.join(s)
# print('_' in s,s)

#7
# str="words"
# w_list=[str[:i+1] for i in range(len(str))]
# print(w_list)
#
# nested_list=["".join([str[j] for j in range(i)]) for i in range(1,len(str)+1)]
# print(nested_list)

#8
import sys
def get_common_words(str1,str2):
    return set(str1.split()) & set(str2.split())
print(get_common_words(sys.argv[1],sys.argv[2]))





