def recursive_divide(x, y):
    """Recursively performs integer division"""
    
    if x < y:
        return 0
    else:
        return 1 + recursive_divide(x-y, y)
    
print(recursive_divide(3, 2))