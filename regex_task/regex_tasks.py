import re
#1
# matcher=re.finditer('(?i)python',"Python is a interpreted language,python is powerful.PYTHON is open source")
# for i in matcher:
#     print(i.start(),i.group())

#2
# matcher=re.finditer("[^\n]*","This is first line\nThis is second line")
# for i in matcher:
#     print(i.start(),i.group())

#3
# matcher=re.finditer("\d{4}\D{4}","12344asa^s1233@$er4")
# for i in matcher:
#     print(i.start(),i.group())

#4
# matcher=re.finditer("[a-zA-Z]{2}\s{1}[a-zA-Z]{2}\s{1}\S{2}","sk SK e3")
# for i in matcher:
#     print(i.start(),i.group())
#5
# matcher=re.match("^[0-9]{3}.*","123SK2345fhggh%")
# print(matcher.group())
#6
# matcher=re.finditer("(?i)[^aeiou]","This contains both  A vowels and non vowels")
# for i in matcher:
#     print(i.start(),i.group())
#7
# matcher=re.finditer("\d{4}","This is a 1234 mike testing 4567")
# for i in matcher:
#     print(i.start(),i.group())

#8
# matcher=re.finditer("[0-9]{6,10}","12345067 034523 32334422 21234343432 1444 6566 333333")
# for i in matcher:
#     print(i.start(),i.group())

#9
# matcher=re.finditer("[a-z]","Python is interpreted")
# for i in matcher:
#     print(i.start(),i.group())

#10
# matcher=re.finditer("AB*","AB A ABBB AABBB")
# for i in matcher:
#     print(i.start(),i.group())

#11
# matcher=re.finditer(".*[.?!]$","This is a sentence. Another sentence? Yet another sentence!")
# for m in matcher:
#     print(m.group())
#12
# matcher=re.findall("\d{3}","There are 123 apples and 456 oranges in the basket. 789 is a number too")
# for m in matcher:
#     print(m)
#13
# matcher=re.search("(?:not|no)","No!,This is negative sentence",re.IGNORECASE)
# print(matcher)
#14
matcher=re.findall(r'<(\w*)(.*?)<\/|1>',"<book>Jarvis</book>",re.DOTALL)
for i in matcher:
    print("tag",i[0])
    print("content",i[1])


