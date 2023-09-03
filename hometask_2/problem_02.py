from functools import reduce

num_list=[int(num) for num in input().strip().split()]
max_number=reduce((lambda num1,num2: num1 if num1>num2 else num2),num_list)

print(max_number)
