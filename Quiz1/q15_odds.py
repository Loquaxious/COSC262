def odds(data):
    """takes a list of ints and returns a new list of all odd ints"""
    odd_list = []
    
    if len(data) == 0:
        return odd_list
    else:
        if data[0] % 2 == 1:
            return [data[0]] + odds(data[1:])
        return odds(data[1:])
        
        
print(odds([0, 1, 12, 13, 14, 9, -11, -20]))