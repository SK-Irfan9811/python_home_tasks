s1="'single' in double"
s2="'''multi''' in double"
s3='"double" in single'
s4='''"double" in multi"'''
s5=''''single' in multi'''
s6=""" 'multi' "with" '''double''' quotes"""
#not possible cases
#double in double
#single in single
#multi in multi
#multi in single
#for all these need to use escape characters to get work done
print(s1,s2,s3,s4,s5,s6)

print(int("387"))

print(str('gh')+"hj")

print(int(23.56))

print(float("23"))



