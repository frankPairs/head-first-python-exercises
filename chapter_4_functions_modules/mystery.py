def double(arg):
    print('Before: ', arg)
    arg = arg * 2
    print('After: ', arg)


def change(arg):
    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)


""" Call by value example"""
num = 10
double(10)
print(num)

""" Call by reference example"""
num_list = [1, 2, 3, 4]
change(num_list)
print(num_list)
