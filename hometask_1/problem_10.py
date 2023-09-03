def get_average(*number):
    return sum(*number)/len(*number)


x=[float(x) for x in input().split()]
print(get_average(x))
