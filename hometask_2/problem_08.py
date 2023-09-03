def my_map(lamb_func,seq):
    ans=[]
    for i in seq:
        ans.append(lamb_func(i))
    return ans

num_list=[1,2,4,5]
sqr_list=map((lambda x:x**2),num_list)
print(list(sqr_list))
