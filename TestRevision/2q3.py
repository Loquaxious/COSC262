def recursive_divide(x,y):
    if x < y:
        return 0
    else:
        return 1 + recursive_divide(x-y,y)


print(recursive_divide(8, 3))