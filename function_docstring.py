def print_max(x, y):
    '''Prints the maximum of two numbers.

    The two values must be intehers.'''
    # convert to integer, if possible
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print()
print(print_max.__doc__)

help(print_max)