def repeat_string(string, number):
    ans_string = (string + '\n')*number
    print(ans_string, end='')


s = input("Enter your String")
n = int(input("Enter a number by which the string should be repeated"))
repeat_string(s, n)
