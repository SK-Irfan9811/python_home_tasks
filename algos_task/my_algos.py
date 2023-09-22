# 1
def reverse_list(lst):
    rev_lst = []
    n = len(lst)
    for i in range(n):
        rev_lst.append(lst[n - i - 1])
    return rev_lst


print(reverse_list([1, 2, 3, 4, 5]))


# 2
def count_even_odd(lst):
    even_count = 0
    odd_count = 0
    for i in lst:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return f"even count is {even_count},odd count is {odd_count}"


print(count_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))


# 3
def maximum(lst):
    max_value = float('-inf')
    for i in lst:
        if i > max_value:
            max_value = i
    return f"max value is {max_value}"


print(maximum([-200, 200, 440, 0, 1234]))


# 4
def second_maximum(lst):
    max_value = second_max = float('-inf')
    for i in lst:
        if i > max_value:
            second_max = max_value
            max_value = i
        elif i > second_max and i != max_value:
            second_max = i
    return f"second maximum is {second_max}"


print(second_maximum([5, 4, 3, 7, 8, 9, 10]))


# 5
def mean(lst):
    sum = 0
    for i in lst:
        sum += i
    return f"mean is {sum / len(lst)}"


print(mean([1, 2, 3, 4, 5]))


# 6
def find_in_range(lst, start, end):
    res = []
    for i in lst:
        if start < i < end:
            res.append(i)
    return f"nums between {start} and {end} are {res}"


print(find_in_range([1, 3, 5, 8, 9, 3, 2, 5, 6, 10, 23, 45, 76], 10, 60))
