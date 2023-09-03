from problem_01 import *

def map_multiple(func_list,sequence):
    for lambda_func in func_list:
        sequence=map(lambda_func,sequence)
    return sequence

nums_list=[int(num) for num in input().strip().split()]
lambda_list=[do_square,do_inverse,negate_a_number]

print(list(map_multiple(lambda_list,nums_list)))

