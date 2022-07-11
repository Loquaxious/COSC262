def product(data):
    """returns the product of the elements in the list"""
    
    the_product = 0
    
    if len(data) == 0:
        return 1
    else:
        return data[0] * product(data[1:])
    
print(product([1, 13, 9, -11]))
