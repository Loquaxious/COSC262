def find(data, value):
    """Returns the subscript of the first occurence of value or -1 if not 
    found"""
    
    subscript = 0
    
    if len(data) == 0:
        return -1
    else:
        if data[0] == value:
            return 0
        subscript = find(data[1:], value)
        if subscript < 0:
            return subscript
        return subscript + 1        
    
print(find(["hi", "there", "you", "there"], "there"))
print(find([10, 20, 30], 0))            